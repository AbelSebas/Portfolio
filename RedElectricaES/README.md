# Proyecto Red Eléctrica - Demanda
## 00.Ree
En este archivo se hace un request de todos los datos disponibles a la API de REE - 31 diciembre 2013-. Pasos:
- Petición de Token a la API de REE
- Con este token sacamos la demanda de la Península por día, base url + id + params

## 01. Ree_indicators
Para saber que indicador teníamos que usar en el archivo anterior.

## 02. Extracion_load
Este archivo saca los datos y los lleva al bucket AWS S3 donde se guardan por año/mes/nombre_del_archivo_fecha.json

## 03. Merged_files
Este script busca todos los archivos en las carpetas donde se guardan los datos de demanda por día y los une en un único json para su carga en RDS.

## 04. BBDD_creation
Creación de base de datos donde se importa el archivo generado en el notebook anterior para guardarlo en la BBDD.

## 05. Model_training_funciones
Version de testeo para la FastAPI. En este notebook entrenamos los modelos XGBoost (forescasting) que predicirán t+1, t+2, t+3. 
Se ajustan features y se prueban para convertirlo en la función externa .py y generar los modelos plks.

## Text_to_SQL_hf
Versión de testeo para la FastAPI. En este notebook realizamos una traducción de frases coloquiales a consultas de SQL a través de un modelo HuggingFace "defog/llama-3-sqlcoder-8b":
- Introducción frase en español
- Se traduce mediante Google Translator
- Devuelve una consulta SQL mediante un prompt definido con instrucciones (limitaciones).


## S3-Trigger-RDS-versionfinal
Lambda que recoge nuevos datos de la API.
Lambda que identifica un evento en S3 de subida de un nuevo archivo –demanda del día anterior– y lo pasa a la base de datos en RDS.

## FastAPI-Energy
Estructura de FastAPI que está levantada en EC2. Archivos definitivos para hacer endpoint de /forecasting y /ask con los modelos anteriormente citados y el conversor de texto a SQL.
