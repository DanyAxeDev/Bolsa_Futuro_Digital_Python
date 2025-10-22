import unicodedata

def remove_acentos(texto):
    # Normaliza o texto para separar caracteres e seus diacríticos
    normalizado = unicodedata.normalize("NFKD", texto)
    # Filtra os caracteres que não são "combinantes" (acentos)
    sem_acentos = "".join([c for c in normalizado if not unicodedata.combining(c)])
    return sem_acentos