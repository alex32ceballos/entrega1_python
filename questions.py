import random
lista1 = ["python","programa"]
    
lista2 = ["variable","funcion"]
    
lista3 = ["bucle","cadena"]
    
lista4 = ["entero","lista"]

categorias = {
    "categoria1":lista1,
    "categoria2":lista2,
    "categoria3":lista3,
    "categoria4":lista4
}


ok = True
while ok:
    seleccionar = input("seleccione una categoria del 1 al 4: ")
    if (len(seleccionar) == 1) and (seleccionar.isdigit()) and (int(seleccionar) in range(1,5)): # chequeo si es un numero del 1 al 4
        word = random.choice(categorias["categoria"+seleccionar])
        ok=False
    else:
        print("Vuelva a intentarlo, ingrese bien la categoria")


    
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
    
    letter = input("Ingresá una letra: ").lower() # de esta manera si se ingresa mayuscula lo pasa a minuscula
    
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
