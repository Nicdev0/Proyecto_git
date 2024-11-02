def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    pass

def division(a, b):
    pass

def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    print("Bienvenido a la calculadora sencilla")
    while True:
        mostrar_menu()
        opcion = input("Introduce el número de la operación: ")

        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if opcion == '1':
                resultado = suma(num1, num2)
                operacion = "suma"
            elif opcion == '2':
                resultado = resta(num1, num2)
                operacion = "resta"    
            else:
                print("Opción no válida. Por favor, selecciona de nuevo.")
                continue

            print(f"El resultado de la {operacion} de {num1} y {num2} es: {resultado}")

        except ValueError:
            print("Por favor, introduce números válidos.")

if __name__ == "__main__":
    main()