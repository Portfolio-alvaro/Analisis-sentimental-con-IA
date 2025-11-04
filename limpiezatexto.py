# src/02_limpieza_texto.py

import re

def cargar_stopwords(ruta):
    """
    Carga stopwords personalizadas desde un archivo.
    """
    with open(ruta, 'r', encoding='utf-8') as f:
        return set(f.read().split())

def procesar_texto(ruta_archivo, ruta_stopwords):
    """
    Limpia el texto eliminando puntuación, números y stopwords.
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        texto = f.read().lower()

    texto = re.sub(r'[^\w\s]', '', texto)
    texto = re.sub(r'\d+', '', texto)

    stopwords = cargar_stopwords(ruta_stopwords)
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p not in stopwords]

    return ' '.join(palabras_filtradas)
