from src import limpieza_texto, conteo_palabras, sentimiento_por_lexicon
import os

# PASO 1: Selección de archivo
archivo = 'data/textos/novela.txt'
stopwords_file = 'data/stopwords/stopwords.txt'

# PASO 2: Carga y preprocesamiento
texto_limpio = limpieza_texto.procesar_texto(archivo, stopwords_file)

# PASO 3: Análisis de frecuencias
frecuencias = conteo_palabras.contar_palabras(texto_limpio)

# PASO 4: Análisis de sentimiento
sentimientos = sentimiento_por_lexicon.analizar_sentimiento(texto_limpio)

# PASO 5: Resultados y gráficos
conteo_palabras.generar_grafico(frecuencias)
sentimiento_por_lexicon.generar_grafico(sentimientos)
