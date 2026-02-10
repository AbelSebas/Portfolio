# Monitorización de Líneas Industriales

Proyecto enfocado en la **monitorización, análisis y optimización del consumo energético** en líneas de producción industriales mediante una arquitectura basada en la nube y modelos de análisis de datos.

## Objetivos

* Obtener visibilidad completa de máquinas y líneas de producción.
* Controlar y optimizar el consumo energético.
* Detectar anomalías de forma automática, rápida y eficaz.
* Facilitar la toma de decisiones mediante análisis y dashboards.

## Arquitectura del sistema

El sistema se apoya en servicios de **AWS** para garantizar escalabilidad, disponibilidad e integración:

* **Extracción de datos** desde APIs usando Python.
* **Automatización en tiempo real** mediante AWS Lambda.
* **Base de datos en AWS RDS (PostgreSQL)** con actualización cada pocos minutos.
* **Procesamiento y análisis de datos** con Pandas, NumPy y Scikit-learn.
* **Modelo de predicción de consumo** basado en XGBoost.
* **Visualización y monitorización** mediante dashboards en Grafana.

## Funcionalidades clave

* Consultas SQL orientadas a negocio: consumo por línea, métricas por máquina, detección de fallos y costes por lote.
* Forecasting de consumo para comparar valores reales vs. futuros.
* Detección de desviaciones y anomalías en producción.
* Posible integración de **Text-to-SQL con FastAPI** para consultas en lenguaje natural.

## Tecnologías utilizadas

Python · AWS (Lambda, RDS) · PostgreSQL · Pandas · NumPy · Scikit-learn · XGBoost · Grafana · SQL

## Resultados

El proyecto propone una **arquitectura escalable y eficiente** que permite monitorizar en tiempo real, optimizar el consumo energético y mejorar la toma de decisiones en entornos industriales.

---

Proyecto desarrollado como parte de una prueba tecnica para una entrevista con análisis de datos y soluciones cloud industriales.

