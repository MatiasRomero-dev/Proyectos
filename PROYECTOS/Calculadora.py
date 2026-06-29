def Calculadora():

    print("Bienvenido a la Calculadora!")

    while True:
        num1 = input("\nPorfavor Ingrese el primer numero: ")
        try:
            num1 = float(num1)
            break
        except ValueError:
            print("(ERROR) Porfavor ingrese un numero valido")

    while True:

        num2 = input("\nPorfavor Ingrese el segundo numero: ")
        try:
            num2 = float(num2)
            break
        except ValueError:
            print("(ERROR) Porfavor ingrese un numero valido")
            print("-----MENU-----"
            "\n(1) Suma\n"
            "(2) Resta\n"
            "(3) Multiplicacion\n"
            "(4) Division\n"
            "(5) Potencia\n")
     
    while True:
        opcion = input("\nInserte la opcion: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("")
        match opcion:
            case 1:
                op = (num1 + num2)
                print(f"\nEl resultado es: {op}")
                break
            case 2:
                op = (num1 - num2)
                print(f"\nEl resultado es: {op}")
                break
            case 3:
                op = (num1 * num2)
                print(f"\nEl resultado es: {op}")
                break
            case 4:
                if num2 == 0:
                    print("(ERROR) No se puede dividir por cero")
                else:
                    op = (num1 / num2)
                    print(f"\nEl resultado es: {op}")
                break
            case 5:
                op = (num1 ** num2)
                print(f"\nEl resultado es: {op}")
                break
            case _:
                print("\n(ERROR) Porfavor ingrese una opcion valida")
             
Calculadora() 