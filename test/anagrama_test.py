from anagrama import anagrama

def test_anagramas_validos():
    assert anagrama("roma", "amor") == True
    assert anagrama("listen", "silent") == True
    assert anagrama("elvis", "lives") == True

def test_anagramas_invalidos():
    assert anagrama("python", "java") == False
    assert anagrama("rat", "car") == False

def test_con_mayusculas_y_espacios():
    assert anagrama("Roma ", "Amor") == True
    assert anagrama("Dormitory", "Dirty room") == True

def test_cadenas_vacias():
    assert anagrama("", "") == True

def test_con_tildes_y_acentos():
    assert anagrama("canción", "nacción") == True
    assert anagrama("résumé", "sérumé") == True 