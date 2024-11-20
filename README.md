# Mutant API

Esta es una API para detectar si una secuencia de ADN pertenece a un mutante o no. La aplicación está desarrollada en Python usando Flask y se encuentra desplegada en **Azure App Service** con integración continua desde GitHub.

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Ejecución Local](#ejecución-local)
- [Pruebas Locales](#pruebas-locales)
- [Despliegue en Azure](#despliegue-en-azure)
- [Pruebas en el Entorno Desplegado](#pruebas-en-el-entorno-desplegado)
- [Endpoints de la API](#endpoints-de-la-api)

---

## Requisitos

Antes de comenzar, asegúrate de tener instalado:
- **Python 3.8 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **Pipenv** (opcional, para administrar dependencias): 
  ```bash
  pip install pipenv
  ```
## Ejecución Local
### Sigue los pasos para ejecutar el proyecto localmente:

#### 1. Clona el repositorio:

```bash
git clone https://github.com/mitu858/mutant-api.git
cd mutant-api
```
#### 2. Instala las dependencias: Si usas pip:

```bash
pip install -r requirements.txt
```
##### O si usas pipenv:

```bash
pipenv install
pipenv shell
```
#### 3. Configura las variables de entorno: Crea un archivo .env en la raíz del proyecto con las siguientes variables:

```env
FLASK_APP=app.py
FLASK_ENV=development
```
#### 4. Inicia la aplicación:

```bash
flask run
```
##### La aplicación estará disponible en http://127.0.0.1:5000.

## Pruebas Locales
Para probar la API localmente, usa una herramienta como Postman o cURL.

### Ejemplo de solicitud:
 #### Endpoint:
```HTTP
POST http://127.0.0.1:5000/mutant/
```
#### Cuerpo (JSON):
```json
{
  "dna": ["ATCGGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
}
```
#### Respuesta esperada:
- 200 OK: Si es mutante.
- 403 Forbidden: Si no es mutante.

## Despliegue en Azure
El proyecto está configurado para un despliegue continuo en Azure con el repositorio de GitHub. Los cambios en la rama principal (main) se reflejarán automáticamente en el servidor de Azure.

### Configuración en Azure
- Origen del código: https://github.com/mitu858/mutant-api
- Servicio de despliegue: Azure App Service
- URL desplegada: https://mutant-api.azurewebsites.net

## Pruebas en el Entorno Desplegado
 Prueba la API directamente en el entorno de Azure:

### Ejemplo de solicitud:
#### Endpoint:
POST https://mutant-api.azurewebsites.net/mutant/

#### Cuerpo (JSON):

```json

{
  "dna": ["ATCGGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
}
```
#### Respuesta esperada:

- 200 OK: Si es mutante.
- 403 Forbidden: Si no es mutante.
## Endpoints de la API
### 1. Verificar ADN mutante
#### Endpoint:
POST /mutant/

#### Cuerpo (JSON):

```json
{
  "dna": ["ATCGGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
}
```
#### Respuestas:

- 200 OK: Si es mutante.
- 403 Forbidden: Si no es mutante.
- 400 Bad Request: Si hay errores de validación.
### 2. Estadísticas de ADN
#### Endpoint:
GET /stats/
#### Respuesta esperada:

```json
{
  "count_mutant_dna": 40,
  "count_human_dna": 100,
  "ratio": 0.4
}
```
## Contribuciones
Si deseas contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios:
```bash

git checkout -b feature/nueva-funcionalidad
```
3. Realiza un pull request hacia la rama principal (main).
