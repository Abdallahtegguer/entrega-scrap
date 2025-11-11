Práctica 1: Web Scraping de Accidentes de Tráfico
Descripción

Este proyecto se enmarca en el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC).
El objetivo es aplicar técnicas de web scraping empleando el lenguaje de programación Python para extraer información relacionada con accidentes de tráfico desde :
https://open.canada.ca/data/en/dataset/1eb9eba7-71d1-4b30-9fb1-30cbdab7e63a

Autor

La actividad ha sido realizada de manera individual por Abdallah Tegguer.

Estructura del proyecto
scrap_accidents/
│
├── src/
│   ├── scraper.py            # Clase principal responsable de obtener y procesar los datos.
│
├── dataset/
│   └── accidents.csv         # datasets descargado desde el URL.
│
└── README.md                 # Documento descriptivo del proyecto.

Descripción de los archivos principales

src/main.py
Encargado de iniciar el proceso de scraping y guardar el dataset resultante.

src/scraper.py
Contiene la clase encargada de realizar las peticiones HTTP, extraer el datasets y estructurarla en el disk.

Dependencias

Para ejecutar el proyecto, instalar los módulos requeridos:

pip install -r requirements.txt

Ejecución

Desde la carpeta raíz del proyecto:

python src/scraper.py

Referencias

Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd.

Mitchell, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O’Reilly Media, Inc.

Documentación oficial de BeautifulSoup, Requests y Pandas.
