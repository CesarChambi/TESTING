def palindromo_o_capicua(dato: int | str):
    if isinstance(dato, int):  # Si es un numero
        dato_str = str(dato)  # Convertimos a string
    elif isinstance(dato, str):  # Si es una cadena
        dato_str = dato
    else:
        return False
    
    # Eliminamos los espacios y convertimos a minusculas
    dato_str = dato_str.replace(" ", "").lower()
    
    # Comparamos con su inverso
    return dato_str == dato_str[::-1]
