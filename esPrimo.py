def esPrimo(num: int) -> bool:
    divisores = 0  # Contador de divisores

    for i in range(1, num + 1):  # Recorremos desde 1 hasta el número mismo
        if num % i == 0:
            divisores += 1  # Si es divisible, sumamos 1 al contador

    return divisores == 2  # Un numero primo solo tiene 2 divisores: 1 y el mismo

# Ejemplo
# numero = int(input("Ingresa un numero: "))
# if esPrimo(numero):
#     print(f"{numero} es primo.")
# else:
#     print(f"{numero} no es primo.")
