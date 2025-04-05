from esPrimo import esPrimo

def test_es_primo():
    assert esPrimo(3) == True
    assert esPrimo(5) == True
    assert esPrimo(7) == True
    assert esPrimo(11) == True
    assert esPrimo(13) == True
    assert esPrimo(2) == True
    assert esPrimo(17) == True
    assert esPrimo(983) == True

def test_no_es_primo():
    assert esPrimo(10) == False
    assert esPrimo(0) == False
    assert esPrimo(1) == False
    assert esPrimo(-7) == False 
    assert esPrimo(4) == False
    assert esPrimo(100) == False
    assert esPrimo(15) == False
    assert esPrimo(21) == False
