from palindromo_o_capicua import palindromo_o_capicua

def test_numeros_capicua():
    assert palindromo_o_capicua(121) == True
    assert palindromo_o_capicua(1221) == True
    assert palindromo_o_capicua(123) == False
    assert palindromo_o_capicua(10) == False
    assert palindromo_o_capicua(0) == True
    assert palindromo_o_capicua(999999) == True
    assert palindromo_o_capicua(-121) == False
    assert palindromo_o_capicua(-12321) == False

def test_palabras_palindromas():
    assert palindromo_o_capicua("oso") == True
    assert palindromo_o_capicua("radar") == True
    assert palindromo_o_capicua("civic") == True
    assert palindromo_o_capicua("madam") == True
    assert palindromo_o_capicua("level") == True
    assert palindromo_o_capicua("hello") == False
    assert palindromo_o_capicua("python") == False

def test_cadenas_vacias():
    assert palindromo_o_capicua("") == True

def test_palabras_mayusculas():
    assert palindromo_o_capicua("Racecar") == True
    assert palindromo_o_capicua("Madam") == True
    assert palindromo_o_capicua("Python") == False

def test_numeros_y_letras():
    assert palindromo_o_capicua("12321") == True
    assert palindromo_o_capicua("1a2b2a1") == True
    assert palindromo_o_capicua("abc123321cba") == True
    assert palindromo_o_capicua("abc123abc") == False

def test_palabras_con_espacios_signos_tildes_y_puntuacion():
    assert palindromo_o_capicua("anita lava la tina") == True
    assert palindromo_o_capicua("¿Acaso hubo búhos acá?") == False
    assert palindromo_o_capicua("Dábale arroz a la zorra el abad") == False
    assert palindromo_o_capicua("Yo dono rosas, oro no doy") == False
    assert palindromo_o_capicua("esto no es palindromo") == False
    assert palindromo_o_capicua("hola mundo!") == False
