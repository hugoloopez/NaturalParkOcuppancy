import requests
import datetime
import time
import pandas as pd
import os
import argparse

def obtener_datos_api(base_url, sensor_type_names=None, from_date=None, to_date=None, location_ids=None, tipo=None):
    def convertir_a_milisegundos(fecha_str):
        dt = datetime.datetime.strptime(fecha_str, "%d-%m-%Y %H:%M")
        return int(time.mktime(dt.timetuple()) * 1000)

    def convertir_a_fecha(epoch_ms):
        return datetime.datetime.fromtimestamp(epoch_ms / 1000).strftime("%d-%m-%Y %H:%M")

    if from_date is None:
        from_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%d-%m-%Y %H:%M")
    if to_date is None:
        to_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    from_epoch = convertir_a_milisegundos(from_date)
    to_epoch = convertir_a_milisegundos(to_date)

    datos_consolidados = {}
    registros = []
    periodo = 30 * 24 * 60 * 60 * 1000

    while from_epoch < to_epoch:
        next_epoch = min(from_epoch + periodo, to_epoch)

        params = {
            "fromDate": from_epoch,
            "toDate": next_epoch
        }

        if sensor_type_names:
            params["sensorTypeNames"] = ",".join(sensor_type_names)
        if location_ids:
            params["locationIds"] = ",".join(map(str, location_ids))

        try:
            response = requests.get(base_url, params=params, verify=False)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            print(f"Error en la petición: {e}")
            from_epoch = next_epoch
            continue

        print(f"Procesando datos desde {convertir_a_fecha(from_epoch)} hasta {convertir_a_fecha(next_epoch)}")

        if tipo == "aves":
            fecha = convertir_a_fecha(from_epoch)
            if "count" in data and isinstance(data["count"], list):
                for ubicacion in data["count"]:
                    loc_id = ubicacion.get("location", "desconocido")
                    for especie, cantidad in ubicacion.get("count", []):
                        registros.append({
                            "timestamp": fecha,
                            "location": loc_id,
                            "species": especie,
                            "count": cantidad
                        })
            else:
                print("La respuesta no contiene la clave 'count' esperada para tipo='aves'.")

        else:
            if "series" in data:
                for variable, series_dict in data["series"].items():
                    for series_id, puntos in series_dict.items():
                        for timestamp, valor in puntos:
                            fecha = convertir_a_fecha(timestamp)
                            if fecha not in datos_consolidados:
                                datos_consolidados[fecha] = {}
                            datos_consolidados[fecha][variable] = valor
            else:
                print("La respuesta no contiene la clave 'series'.")

        from_epoch = next_epoch

    os.makedirs("data", exist_ok=True)

    if tipo == "aves":
        if not registros:
            print("No se obtuvieron datos de aves.")
            return None

        df_final = pd.DataFrame(registros)
        df_final = df_final.sort_values(["timestamp", "location", "species"])
        csv_filename = f"data/datos_aves_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df_final.to_csv(csv_filename, index=False)

    else:
        if not datos_consolidados:
            print("No se obtuvieron datos.")
            return None

        df_final = pd.DataFrame.from_dict(datos_consolidados, orient="index")
        df_final.index.name = "timestamp"
        df_final = df_final.reset_index()
        df_final = df_final.sort_values("timestamp")
        csv_filename = f"data/datos_series_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df_final.to_csv(csv_filename, index=False)

    print(f"Datos guardados en {csv_filename}")
    return df_final


parser = argparse.ArgumentParser(description="Extrae datos desde la API de ST en intervalos de un mes y los guarda en un CSV.")

parser.add_argument("base_url", help="URL base de la API")
parser.add_argument("--sensor_type_names", nargs="*", help="Lista de nombres de sensores (opcional)")
parser.add_argument("--from_date", help="Fecha de inicio (DD-MM-YYYY HH:MM)")
parser.add_argument("--to_date", help="Fecha de fin (DD-MM-YYYY HH:MM)")
parser.add_argument("--location_ids", nargs="*", type=int, help="Lista de IDs de ubicación (opcional)")
parser.add_argument("--tipo", choices=["aves", "series"], help="Tipo de datos: 'aves' o 'series'")

args = parser.parse_args()

obtener_datos_api(
    base_url=args.base_url,
    sensor_type_names=args.sensor_type_names,
    from_date=args.from_date,
    to_date=args.to_date,
    location_ids=args.location_ids,
    tipo=args.tipo
)


# fecha_inicio = "10-09-2024 00:01"
# fecha_fin = "11-12-2024 00:01"