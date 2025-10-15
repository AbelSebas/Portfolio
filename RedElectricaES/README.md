📊 Sistema Automatizado de Extracción y Carga de Datos de Demanda REE

Este proyecto implementa una arquitectura automatizada y escalable para la extracción, procesamiento y almacenamiento de datos de demanda eléctrica provenientes de la Red Eléctrica de España (REE).

El sistema permite obtener datos históricos y actualizados de demanda, almacenarlos en AWS S3 y cargarlos de forma estructurada en una base de datos PostgreSQL para su posterior análisis.

🚀 Objetivo

Construir una pipeline de datos automatizada que extraiga información de la API de la REE, la almacene en un entorno seguro en la nube y la procese para su análisis eficiente en una base de datos relacional.

⚙️ Arquitectura General

Extracción de Datos (Data Engineering & Architecture):

Obtención de la API Key de REE.

Desarrollo de una pipeline de extracción masiva para recopilar datos históricos de demanda y almacenarlos en un bucket S3.

Configuración de una AWS Lambda programada mediante EventBridge para ejecutar la extracción diaria de las últimas 24 horas y guardar las observaciones en el bucket.

Procesamiento y Carga (ETL - Data Engineering):

Implementación de una segunda AWS Lambda con trigger de S3, que se activa al detectar nuevos ficheros JSON.

Esta función procesa y limpia los datos antes de cargarlos en una base de datos PostgreSQL, asegurando integridad y consistencia en el almacenamiento.

🧩 Tecnologías Utilizadas

AWS Lambda

Amazon S3

Amazon EventBridge

PostgreSQL

Python (boto3, psycopg2, pandas)

API REE (Red Eléctrica de España)

📈 Beneficios

Pipeline completamente automatizada y sin servidor (serverless).

Almacenamiento de datos histórico y actualizado.

Estructura escalable y mantenible.

Datos limpios y listos para análisis o visualización.

FICHEROS CON LAS DIFERENTES PARTES DEL PROYECTO
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
