# Hackathon 3: Markdown, Embeddings, ChromaDB
## Mario Ventura

Objetivo: Usar archivos markdown para crear embeddings y usarlos como dataset con el que trabajar en ChromaDB

Pasos seguidos:
1. Obtener documentos Markdown con los que trabajar mediante la ejecución del script scrapper.py del repositorio https://github.com/junjielyu13/DGSI-UCPtoMarkdown


2. Seguir los pasos de https://docs.trychroma.com/docs/overview/getting-started para obtener ChromaDB. Código de todos los pasos en el archivo `chroma.py`


    2.1. Mientras los documentos se descargan, se instala chromadb con el comando `pip install chromadb` 


    2.2. Crear Chroma client

    2.3. Crear una collection


    2.4. Añadir documentos a la collection


    2.5. Consultar la collection


    2.6. Inspeccionar los resultados