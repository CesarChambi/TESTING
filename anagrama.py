def anagrama(palabra1: str, palabra2: str) -> bool:
    # Limpiar espacios y pasar a minusculas para evitar errores por mayusculas o espacios
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    # Compara las letras ordenadas
    return sorted(palabra1) == sorted(palabra2)