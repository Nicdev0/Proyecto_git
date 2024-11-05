# andres echeverria,coraima porta, carlos lopez, Juan Noguera, andierick fernandez

import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def porcentaje(a, b):
    return (a * b) / 100
def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return math.sqrt(a)

def mostrar_menu():
    print("\nSelecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Porcentaje")
    print("6. RAiz Cuadrada")
    print("0. Salir")

def main():
    print("Bienvenido a la calculadora sencilla")
    while True:
        mostrar_menu()
        opcion = input("Introduce el número de la operación: ")

        if opcion == '0':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        try:
            if opcion in ['1', '2', '3', '4', '5']:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
            elif opcion == '6':
                num1 = float(input("Introduce el número para la raíz cuadrada: "))
                num2 = None


            if opcion == '1':
                resultado = suma(num1, num2)
                operacion = "suma"
            elif opcion == '2':
                resultado = resta(num1, num2)
                operacion = "resta"
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
                operacion = "multiplicación"
            elif opcion == '4':
                resultado = division(num1, num2)
                operacion = "división"
            elif opcion == '5':
                resultado = porcentaje(num1, num2)
                operacion = "porcentaje"
            elif opcion == '6':
                resultado = raiz_cuadrada(num1)
                operacion = "raíz cuadrada"    
            else:
                print("Opción no válida. Por favor, selecciona de nuevo.")
                continue

            print(f"El resultado de la {operacion} de {num1} y {num2} es: {resultado}")

        except ValueError:
            print("Por favor, introduce números válidos.")

if __name__ == "__main__":
    main()
