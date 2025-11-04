# src/03_sentimiento_por_lexicon.py

import matplotlib.pyplot as plt

# Diccionario básico de sentimientos
LEXICON = {
    'feliz': 1, 'alegría': 1, 'bueno': 1, 'excelente': 2,
    'triste': -1, 'malo': -1, 'horrible': -2, 'odio': -2
}

def analizar_sentimiento(texto):
    """
    Analiza el sentimiento del texto usando un léxico simple.
    """
    palabras = texto.split()
    puntuacion = sum(LEXICON.get(p, 0) for p in palabras)
    resultado = 'Positivo' if puntuacion > 0 else 'Negativo' if puntuacion < 0 else 'Neutro'
    return {'puntuacion': puntuacion, 'resultado': resultado}

def generar_grafico(resultado):
    """
    Genera un gráfico circular del resultado de sentimiento.
    """
    etiquetas = ['Positivo', 'Negativo', 'Neutro']
    valores = [0, 0, 0]
    if resultado['resultado'] == 'Positivo':
        valores[0] = 1
    elif resultado['resultado'] == 'Negativo':
        valores[1] = 1
    else:
        valores[2] = 1

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', colors=['green', 'red', 'gray'])
    plt.title('Análisis de Sentimiento')
    plt.savefig('output/graficos/sentimiento.png')
    plt.close()
