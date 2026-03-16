import random
words = [ #lista de palabras
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

word = random.choice(words)
    
guessed = [] #adivina
    
attempts = 6 #intentos 
    
print("¡Bienvenido al Ahorcado!")
print()
    
puntaje = 6

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las quprogress = ""
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje = 6
        break
    
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ")
    
    if (letter.isalpha()) and (len(letter) == 1): #compruebo si es una letra, y si es solo una
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
    else:
        print("entrada no valida")
        
    print()
    
else:
    print(f"¡Perdiste! La palabra era: {word}")

print("tu puntaje es de: ", puntaje)
