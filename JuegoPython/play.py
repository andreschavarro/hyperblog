import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "computadora", "juego", "ahorcado", "diversion"]
    return random.choice(palabras)

def jugar_ahorcado():
    palabra = seleccionar_palabra()
    palabra_oculta = ["_" for _ in palabra]
    intentos = 6  # Número de intentos antes de perder
    
    print("¡Bienvenido al Juego del Ahorcado!")
    
    while intentos > 0:
        letra = input(f"Palabra actual: {' '.join(palabra_oculta)}\nIntentos restantes: {intentos}\nIngresa una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa una letra válida.")
            continue
        
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
            if "_" not in palabra_oculta:
                print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                break
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            intentos -= 1
    
    if intentos == 0:
        print(f"¡Perdiste! La palabra era: {palabra}")

if __name__ == "__main__":
    jugar_ahorcado()
