import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        try:
            guess = int(input("¿Cuál es tu suposición? "))
            intentos += 1

            if guess < numero_secreto:
                print("El número es mayor. Intenta de nuevo.")
            elif guess > numero_secreto:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! ¡Adivinaste el número {numero_secreto} en {intentos} intentos!")
                break

        except ValueError:
            print("Ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()