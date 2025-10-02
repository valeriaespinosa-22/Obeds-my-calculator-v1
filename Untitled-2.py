# Definimos una función para sumar dos números
def sumar(a, b):
    return a + b  # retorna la suma de a y b

# Definimos una función para restar dos números
def restar(a, b):
    return a - b  # retorna la resta de a y b

# Función principal del programa
def main():
    print("=== Calculadora Básica en Python ===")  # mensaje de bienvenida
    
    # Pedimos al usuario que ingrese el primer número
    a = float(input("Ingresa el primer número: "))  # usamos float para permitir decimales
    
    # Pedimos al usuario que ingrese el segundo número
    b = float(input("Ingresa el segundo número: "))
    
    # Pedimos al usuario que elija la operación
    op = input("Selecciona una operación (+ o -): ")
    
    # Condicional para decidir qué función usar
    if op == "+":  # si el usuario eligió "+"
        print("Resultado:", sumar(a, b))  # llama a la función sumar
    elif op == "-":  # si el usuario eligió "-"
        print("Resultado:", restar(a, b))  # llama a la función restar
    else:
        # Si el usuario escribió algo diferente a + o -
        print("Operación no válida")

# Este bloque asegura que el programa se ejecute solo si es el archivo principal
if _name_ == "_main_":
    main()  # llama a la función main para iniciar el programa

    
