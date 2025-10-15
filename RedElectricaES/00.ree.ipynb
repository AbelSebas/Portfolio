# Propuesta de Proyecto: Pipeline y API de Forecasting con REE

## 👥 Roles y Responsabilidades

### 🏗️ Data Architect
- **Responsable del Diseño en AWS:** Definir y configurar la arquitectura en la nube, incluyendo el bucket S3, la base de datos **PostgreSQL en RDS** y los permisos de los servicios.

### ⚙️ Data Engineer
- **Responsable del Pipeline de Datos:** Implementar las funciones AWS Lambda para la extracción masiva inicial y diaria de datos de la API de REE, y para la carga y transformación de estos datos desde S3 a la base de datos.

### 🔬 Data Scientist
- **Responsable del Análisis y Modelado:**
  - Diseñar la lógica para interpretar las preguntas en lenguaje natural del endpoint de Q&A.
  - Entrenar un modelo de forecasting utilizando arquitectura decoder-only de transformers para predecir la demanda elétrica.

### 🚀 ML Engineer
- **Responsable del Despliegue y la API:**
  - Envolver la lógica de consulta y el modelo de forecasting en una API robusta utilizando FastAPI.
  - Desplegar la aplicación FastAPI en una instancia de AWS EC2, asegurando que todos los endpoints sean funcionales.

---

## 📝 Fases del Proyecto

### **Fase 01: Infraestructura y Pipeline de Datos**
**Objetivo:** Construir un sistema automatizado que extraiga datos de demanda de la REE y los almacene de forma estructurada en una base de datos **PostgreSQL**.

**Tareas Clave:**
1.  **Extracción de Datos (Data Engineer, Architect):**
    - Obtener la API Key de REE.
    - Crear una pipeline para realizar una extracción masiva de datos históricos de demanda y guardarlos en un **bucket S3**.
    - Configurar una **AWS Lambda** con **EventBridge** para que se ejecute diariamente y obtenga las observaciones de las últimas 24 horas para almacenarlas en el bucket.

2.  **Procesamiento y Carga (Data Engineer, Architect):**
    - Desarrollar una segunda **AWS Lambda** que se active con un **trigger de S3** al recibir nuevos datos.
    - Esta función procesará los ficheros JSON y los cargará de forma estructurada y **limpia** en la base de datos **PostgreSQL**.

**Entregables de esta fase:**
- Infraestructura en AWS (S3, RDS) configurada.
- Pipelines de datos automáticos (masivo y diario) funcionando.
- Base de datos poblada y actualizada con los datos de la REE.

### **Fase 02: Modelado, API y Despliegue**
**Objetivo:** Desarrollar una API que permita consultar datos de demanda históricos y predecir demanda futura.

**Tareas Clave:**
1.  **Desarrollo del Modelo (Data Scientist):**
    - Utilizar los datos de demanda para entrenar un modelo de forecasting que prediga la demanda de la próxima franja horaria en base a las anteriores.

2.  **Desarrollo de la API (ML Engineer, Data Scientist):**
    - Crear una aplicación con **FastAPI** que incluya los siguientes endpoints:
      - `/ask`: Recibe una pregunta en texto (ej. *"Cuánta electricidad se generó la semana pasada"*), la interpreta, construye una consulta a la base de datos y devuelve la respuesta.
      - `/forecast`: Recibe un número de días, y devuelve la predicción de demanda generada por el modelo esa cantidad de días en el futuro.

3.  **Despliegue (ML Engineer):**
    - Desplegar la aplicación FastAPI completa en una instancia **AWS EC2** para que sea accesible públicamente.

**Entregables de esta fase:**
- Un modelo de forecasting entrenado.
- API funcional desplegada en EC2 con los dos endpoints implementados.
- Documentación de la API (generada por FastAPI).