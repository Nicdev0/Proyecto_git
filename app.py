def suma(a, b):
    return a + b

def resta(a, b):
    pass

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def porcentaje(a, b):
    return (a * b) / 100

def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Porcentaje")
    print("6. Salir")

def main():
    print("Bienvenido a la calculadora sencilla")
    while True:
        mostrar_menu()
        opcion = input("Introduce el número de la operación: ")

        if opcion == '6':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if opcion == '1':
                resultado = suma(num1, num2)
                operacion = "suma"
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
                operacion = "multiplicación"
            elif opcion == '4':
                resultado = division(num1, num2)
                operacion = "división"
            elif opcion == '5':
                resultado = porcentaje(num1, num2)
                operacion = "porcentaje"
            else:
                print("Opción no válida. Por favor, selecciona de nuevo.")
                continue

            print(f"El resultado de la {operacion} de {num1} y {num2} es: {resultado}")

        except ValueError:
            print("Por favor, introduce números válidos.")

if __name__ == "__main__":
    main()
