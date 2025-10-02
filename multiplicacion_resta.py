# Definimos una función llamada "calcular" que toma tres argumentos: num1, num2 y operacion
def calcular(num1, num2, operacion):
    # Si la operación es "multiplicar", realizamos la multiplicación de num1 y num2
    if operacion == "multiplicar":
        return num1 * num2
    # Si la operación es "dividir", realizamos la división de num1 entre num2
    elif operacion == "dividir":
        # Antes de realizar la división, verificamos que num2 no sea cero
        if num2 == 0:
            # Si num2 es cero, lanzamos un error con un mensaje personalizado
            raise ValueError("No se puede dividir por cero")
        return num1 / num2
    # Si la operación no es "multiplicar" ni "dividir", lanzamos un error con un mensaje personalizado
    else:
        raise ValueError("Operación no válida")

# Definimos una función llamada "main" que será la entrada principal de nuestro programa
def main():
    # Solicitamos al usuario que ingrese el primer número
    num1 = float(input("Ingrese el primer número: "))
    # Solicitamos al usuario que ingrese el segundo número
    num2 = float(input("Ingrese el segundo número: "))
    # Solicitamos al usuario que ingrese la operación que desea realizar
    operacion = input("Ingrese la operación (multiplicar/dividir): ")

    # Intentamos realizar la operación solicitada por el usuario
    try:
        # Llamamos a la función "calcular" con los números y la operación ingresados por el usuario
        resultado = calcular(num1, num2, operacion)
        # Mostramos el resultado de la operación al usuario
        print(f"El resultado de la {operacion} es: {resultado}")
    # Capturamos cualquier error que pueda ocurrir durante la ejecución de la función "calcular"
    except ValueError as e:
        # Mostramos un mensaje de error al usuario con la descripción del error
        print(f"Error: {e}")

# Verificamos si este script es el principal (no es importado como módulo en otro script)
if _name_ == "_main_":
    # Llamamos a la función "main" para iniciar el programa
    main()