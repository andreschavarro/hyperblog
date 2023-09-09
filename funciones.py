# Definición de función: Para definir una función en Python, utilizamos la palabra clave def, seguida del nombre de la función y paréntesis que pueden contener argumentos. Por ejemplo

def saludar(nombre):
    print(f"Hola, {nombre}!")

def suma(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma(3, 5)


def suma(a, b):
    """
    Esta función suma dos números y devuelve el resultado.
    
    Args:
        a (int): El primer número.
        b (int): El segundo número.
    
    Returns:
        int: La suma de a y b.
    """
    resultado = a + b
    return resultado
