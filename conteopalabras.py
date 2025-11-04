# src/01_conteo_palabras.py

import collections
import matplotlib.pyplot as plt

def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto.
    """
    palabras = texto.split()
    frecuencias = collections.Counter(palabras)
    return frecuencias

def generar_grafico(frecuencias, top_n=20):
    """
    Genera un gráfico de barras con las palabras más frecuentes.
    """
    comunes = frecuencias.most_common(top_n)
    palabras, conteos = zip(*comunes)

    plt.figure(figsize=(10, 6))
    plt.bar(palabras, conteos, color='skyblue')
    plt.xticks(rotation=45)
    plt.title('Frecuencia de palabras')
    plt.tight_layout()
    plt.savefig('output/graficos/frecuencia_palabras.png')
    plt.close()
