# Natural Park Occupancy 🌍🌿
**Optimización del flujo de visitantes en parques naturales mediante modelos predictivos**

## 📖 Descripción
El crecimiento urbano y el auge de las **Smart Cities** han generado nuevos desafíos en la gestión de áreas naturales protegidas. La masificación en parques naturales puede afectar negativamente a los ecosistemas locales. Este proyecto busca mitigar estos efectos analizando los patrones de visitantes y optimizando la asistencia a parques mediante **modelos predictivos basados en datos abiertos y sensores IoT**.

Este estudio se centra en el **Parque Natural de Torrevieja**, utilizando múltiples fuentes de datos para desarrollar una herramienta en tiempo real que ayude a gestionar la afluencia de visitantes, promoviendo un **turismo sostenible**.

## 📊 Objetivos del Proyecto
✔ **Predecir la cantidad de visitantes** en función de variables como clima, hora del día y eventos.  
✔ **Optimizar la gestión del parque** mediante datos en tiempo real.  
✔ **Promover la conservación ecológica** evitando la sobreexplotación del entorno.  
✔ **Aplicar técnicas de Machine Learning** y análisis de datos en la gestión de espacios naturales. 

## 🏗️ Tecnologías Utilizadas
🚀 **Lenguajes y Herramientas**  
- Python 🐍  
- Jupyter Notebook 📒  
- Pandas y NumPy para el análisis de datos 📊  
- Sensores IoT para recopilación de datos en el parque 🌍

## 📝 Datos Utilizados
Este proyecto combina diversas fuentes de datos para generar predicciones precisas:

1. **Datos de Ocupación ([CHAN TWIN](https://smartcitycluster.org/project/sensing-tools-chan-twin/))** 📊  
   - Datos históricos sobre la cantidad de visitantes en el parque.

2. **Datos Meteorológicos ([Proyecto Mastral](https://www.eltiempoentorrevieja.es/))** 🌦️  
   - Registros de temperatura, humedad, velocidad del viento y precipitaciones.

3. **Datos de Fauna ([eBird](https://ebird.org))** 🐦  
   - Observaciones de aves en el parque registradas.  

## ▶️ Cómo funciona

Este proyecto está estructurado para facilitar la recolección, tratamiento y modelado de datos relacionados con la ocupación del Parque Natural de Torrevieja:

- En la carpeta `utils/` se encuentra el script **`data_downloader.py`**, encargado de **descargar los datos desde la API de Sensing Tools (CHAN TWIN)**, automatizando el acceso a información actualizada sobre la ocupación del parque.

- El archivo **`obtencion_y_tratamiento_de_datos.ipynb`** contiene el desarrollo completo del proceso de **preparación, limpieza de los datos además del entrenamiento de modelos**.

- En la carpeta **`data/`** se encuentran los **datos concretos descargados y utilizados** en este trabajo, listos para su análisis.

- Para poder ejecutar correctamente el código, es necesario crear un archivo **`.env`** con la variable de entorno **`TIMEGPT_API_KEY`**. Puedes usar el archivo **`.env_sample`** como referencia para conocer el formato y las claves requeridas.


