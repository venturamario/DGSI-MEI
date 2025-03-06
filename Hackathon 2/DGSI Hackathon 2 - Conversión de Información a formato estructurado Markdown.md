
Se usan varias herramientas, las cuales se detallan a continuación

# MarkDownload

Instrucciones ofrecias por CHatGPT:

- Extrae el contenido principal de una página web y lo convierte en Markdown.
- Descarga imágenes o las deja referenciadas en línea.
- Permite copiar al portapapeles o guardar el archivo `.md`.

**Resultado obtenido:**

[![](https://www.fib.upc.edu/sites/fib/files/images/practiquesstockphoto.png)](https://www.fib.upc.edu/es/empresa/practicas-en-empresa)

  

[**Prácticas en empresa**](https://www.fib.upc.edu/es/empresa/practicas-en-empresa)

  

¿Quieres realizar prácticas en empresa? Consulta las diferentes modalidades, requisitis y condiciones para realizar prácticas.

  

## Noticias

  

### [Convocatoria Unite! Seed Fund 2025](https://www.fib.upc.edu/es/noticias/convocatoria-unite-seed-fund-2025 " Convocatoria Unite! Seed Fund 2025")

  

Dirigida a proyectos de estudiantes, docentes y personal investigador, la fecha tope para la presentación de propuestas es el 20 de marzo de 2025.

  

### [ICFO Summer Fellows 2025](https://www.fib.upc.edu/es/noticias/icfo-summer-fellows-2025 "ICFO Summer Fellows 2025")

  

El ICFO - Instituto de Ciencias Fotónicas ofrece becas de verano dirigidas a estudiantes interesados en participar en proyectos de investigación.

  

### [Unite! Programa de Profesorado Visitante 2025](https://www.fib.upc.edu/es/noticias/unite-programa-de-profesorado-visitante-2025 "Unite! Programa de Profesorado Visitante 2025")

  

TU Darmstadt invita a postdoctorales, profesores y catedráticos experimentados de las universidades socias de Unite! a postularse para las plazas de profesorado visitante financiadas

  

### [Convocatoria Unite! Seed Fund 2025](https://www.fib.upc.edu/es/noticias/convocatoria-unite-seed-fund-2025 " Convocatoria Unite! Seed Fund 2025")

  

Dirigida a proyectos de estudiantes, docentes y personal investigador, la fecha tope para la presentación de propuestas es el 20 de marzo de 2025.

  

### [ICFO Summer Fellows 2025](https://www.fib.upc.edu/es/noticias/icfo-summer-fellows-2025 "ICFO Summer Fellows 2025")

  

El ICFO - Instituto de Ciencias Fotónicas ofrece becas de verano dirigidas a estudiantes interesados en participar en proyectos de investigación.

  

### [Unite! Programa de Profesorado Visitante 2025](https://www.fib.upc.edu/es/noticias/unite-programa-de-profesorado-visitante-2025 "Unite! Programa de Profesorado Visitante 2025")

  

TU Darmstadt invita a postdoctorales, profesores y catedráticos experimentados de las universidades socias de Unite! a postularse para las plazas de profesorado visitante financiadas

  

## Agenda

  

Mié 05 Mar

  

 12:00 - 13:30

  

  Sala d'actes Manuel Martí Recober

  

Mié 12 Mar

  

 16:00 - 17:30

  

  online

  

## Pide cita previa

  

___

  

Si necesitas realizar algun trámite presencial tanto de grado, máster, prácticas en empresa, institucional o hablar con algun vicedegano, i/o jefe de estudios, etc.  

Si has de venir presencialmente a la administración de la FIB, pide cita previa



[Cita previa](https://www.fib.upc.edu/ca/cita-previa)


## Premios y reconocimientos


## Haz un recorrido por la historia de la informática

  

___

  

La colección de la Facultat d'Informàtica recoge y presenta la historia de la informática y de los instrumentos de cálculo más utilizados a lo largo de la historia.

  

[Conoce el "Museo" de la FIB](https://www.fib.upc.edu/es/museo)

  

## Acreditaciones de calidad

  

### Sellos AQU

  

**GEI**

  

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-gei-excelent-es.png)

  

**GCED**

  

![](https://www.fib.upc.edu/sites/fib/files/segell-qualitat-gced-excellent-en.png)

  

**GIA**

  

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-gia-verificat-es.png)

  

**MEI**

  

**![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-mei-excellent-es.png)**

  

**MIRI**

  

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-miri-excelent-es.png)

  

**MAI**

  

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-mai-excelent-es.png)

  

**MFPS**

  

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-mfps-favorable-es.png)

  

**MDS**

  

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-mds-verificat-es.png)

  

### Sellos Euro-inf

  

**GEI**

  

![](https://www.fib.upc.edu/sites/fib/files/images/fib/fib-euro-inf-bachelor.png)

  

**MEI y MIRI**

  

![](https://www.fib.upc.edu/sites/fib/files/images/fib/fib-euro-inf-master.png)

  

## La FIB es miembro de



# Pandoc
Se llega a la conclusión de que no es una buena herramienta por los problemas y complicaciones que da al necesitar modificaciones de variables de entorno del sistema.

# Script Python
The results can be found in website_content.md and the script in md_test.py.

## Setup and Initialization:

The script uses Selenium WebDriver to open the main website (https://www.fib.upc.edu/) in a Chrome browser.
It runs with headless mode disabled, meaning the browser window will be visible during scraping.

## Extracting Links:

The script scrapes all links (<a> tags with href attributes) from the main page of the website using BeautifulSoup.
It resolves these links into absolute URLs using the urljoin function, so it can scrape them properly.

## Scraping Content:

For the main page and each link found, the script uses the requests library to fetch the HTML content.
It then converts the fetched HTML into Markdown format using the markdownify library.

## Retry Mechanism:

In case of timeouts or connection errors, the script retries up to 3 times with a 5-second delay between each attempt.
If a URL cannot be fetched after all retries, the script returns an error message for that URL.

## Saving the Data:

All Markdown-converted content (from the main page and the links) is saved into a file named website_content.md.

# urltomarkdown.com

## Facultad de Informática de Barcelona |
[![](https://www.fib.upc.edu/sites/fib/files/images/practiquesstockphoto.png)](/es/empresa/practicas-en-empresa)

[**Prácticas en empresa**](https://www.fib.upc.edu/es/empresa/practicas-en-empresa)

¿Quieres realizar prácticas en empresa? Consulta las diferentes modalidades, requisitis y condiciones para realizar prácticas.

Noticias
--------

### [Unite! Programa de Profesorado Visitante 2025](https://www.fib.upc.edu/es/noticias/unite-programa-de-profesorado-visitante-2025 "Unite! Programa de Profesorado Visitante 2025")

TU Darmstadt invita a postdoctorales, profesores y catedráticos experimentados de las universidades socias de Unite! a postularse para las plazas de profesorado visitante financiadas

### [Convocatoria Unite! Seed Fund 2025](https://www.fib.upc.edu/es/noticias/convocatoria-unite-seed-fund-2025 " Convocatoria Unite! Seed Fund 2025")

Dirigida a proyectos de estudiantes, docentes y personal investigador, la fecha tope para la presentación de propuestas es el 20 de marzo de 2025.

### [ICFO Summer Fellows 2025](https://www.fib.upc.edu/es/noticias/icfo-summer-fellows-2025 "ICFO Summer Fellows 2025")

El ICFO - Instituto de Ciencias Fotónicas ofrece becas de verano dirigidas a estudiantes interesados en participar en proyectos de investigación.

Agenda
------

Mié 05 Mar

 12:00 - 13:30

  Sala d'actes Manuel Martí Recober

Mié 12 Mar

 16:00 - 17:30

  online

Pide cita previa
----------------

* * *

Si necesitas realizar algun trámite presencial tanto de grado, máster, prácticas en empresa, institucional o hablar con algun vicedegano, i/o jefe de estudios, etc.  
Si has de venir presencialmente a la administración de la FIB, pide cita previa

[Cita previa](https://www.fib.upc.edu/ca/cita-previa)

Premios y reconocimientos
-------------------------

Haz un recorrido por la historia de la informática
--------------------------------------------------

* * *

La colección de la Facultat d'Informàtica recoge y presenta la historia de la informática y de los instrumentos de cálculo más utilizados a lo largo de la historia.

[Conoce el "Museo" de la FIB](https://www.fib.upc.edu/es/museo)

Acreditaciones de calidad
-------------------------

### Sellos AQU

**GEI**

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-gei-excelent-es.png)

**GCED**

![](https://www.fib.upc.edu/sites/fib/files/segell-qualitat-gced-excellent-en.png)

**GIA**

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-gia-verificat-es.png)

**MEI**

**![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-mei-excellent-es.png)**

**MIRI**

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-miri-excelent-es.png)

**MAI**

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-mai-excelent-es.png)

**MFPS**

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-mfps-favorable-es.png)

**MDS**

![](https://www.fib.upc.edu/sites/fib/files/images/fib/segell-qualitat-mds-verificat-es.png)

### Sellos Euro-inf

**GEI**

![](https://www.fib.upc.edu/sites/fib/files/images/fib/fib-euro-inf-bachelor.png)

**MEI y MIRI**

![](https://www.fib.upc.edu/sites/fib/files/images/fib/fib-euro-inf-master.png)

La FIB es miembro de
--------------------
