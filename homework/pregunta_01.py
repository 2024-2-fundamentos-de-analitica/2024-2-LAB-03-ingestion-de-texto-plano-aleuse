"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def clean_keywords(text):
    """Limpia y formatea las palabras clave"""
    cleaned_words = [word.strip().rstrip('.') for word in text.replace('\n', ' ').split(',')]
    return ', '.join(' '.join(word.split()) for word in cleaned_words)

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    # Lee el archivo
    with open('files/input/clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Inicializa listas para datos
    clusters = []
    quantities = []
    percentages = []
    keywords = []
    
    current_cluster = None
    current_keywords = []
    
    # Procesa el contenido
    for line in lines[4:]:  # Skip header lines
        if line.strip() and not line.startswith('----'):
            parts = line.strip().split()
            if parts[0].isdigit():
                # Si hay un cluster anterior, guardarlo
                if current_cluster is not None:
                    keywords.append(clean_keywords(' '.join(current_keywords)))
                
                current_cluster = int(parts[0])
                clusters.append(current_cluster)
                quantities.append(int(parts[1]))
                percentages.append(float(parts[2].replace(',', '.')))
                current_keywords = parts[4:]
            else:
                current_keywords.extend(parts)
    
    # Agrega el último conjunto de keywords
    if current_keywords:
        keywords.append(clean_keywords(' '.join(current_keywords)))
    
    # Crea el DataFrame
    df = pd.DataFrame({
        "cluster": clusters,
        "cantidad_de_palabras_clave": quantities,
        "porcentaje_de_palabras_clave": percentages,
        "principales_palabras_clave": keywords
    })
    
    print(df.columns)
    return df

print(pregunta_01())