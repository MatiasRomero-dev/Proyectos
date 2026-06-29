import random

MINIMO = 1
MAXIMO = 100
intentos = 0
 
numero_azar = random.randint(MINIMO, MAXIMO)

while True:
    intento_usuario = int(input("Introduce un numero: "))
    intentos += 1
    if intento_usuario > numero_azar:
        print(f"\nTe pasaste! El numero es mas pequeño que {intento_usuario}\n" )
    elif intento_usuario < numero_azar:
        print(f"\nTe quedaste corto! El numero es mas alto que {intento_usuario}\n")
    else:
        break

print(f"\nBien hecho! el numero era: {numero_azar}")
print(f"Te costo {intentos} intentos.")