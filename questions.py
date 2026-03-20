import random
programacion = ["python","programa","variable","bucle","cadena","entero","lista"]
    
musica = ["rock","metal","pop","jazz"]
    
comida = ["arroz","fideos","carne","huevo","pescado"]

categorias = {
    "programacion":programacion,
    "musica":musica,
    "comida":comida,
}

print("¡Bienvenido al Ahorcado!")
print()

#-------------------------- funciones -------------------------------

def seguirJugando(): #funcion que permite volver a jugar
    valido = False
    ingresar = input("Quiere jugar? s/n: ").lower()
    while not valido:
        if (len(ingresar) == 1) and (ingresar in ("s","n")):
            valido = True
            if (ingresar == "s"):
                print("Usted eligio jugar")
            elif (ingresar == "n"):
                print("Usted eligio no jugar")
        else:
            print("ingrese bien, elija entre s/n")
            ingresar = input("Quiere jugar? s/n: ").lower()
    return   ingresar == "s"


def mezclarCategorias(categorias): #mezclo las categorias
    mezcladas = {}
    for i in categorias:
        mezcladas[i] = random.sample(categorias[i],len(categorias[i]))
    return mezcladas

def elegirCategoria(mezcladas):
    ok = True
    print("categorias a elegir: ")
    for c in mezcladas:
        print("-", c)
    while ok:
        seleccionar = input("seleccione una categoria: ").lower()
        if seleccionar in mezcladas: # chequeo si se selecciono bien la categoria
            if (len(mezcladas[seleccionar]) > 0):
                word = mezcladas[seleccionar].pop()
                ok=False
            else:
                print(f'la categoria {seleccionar} no tiene mas palabras')
                if all(len(mezcladas[c]) == 0 for c in mezcladas): #verifico si hay palabras en todas las categorias
                    return None
        else:
            print("Vuelva a intentarlo, ingrese bien la categoria")
    return word
            
            
def esUnaLetra(letter, guessed, word, attempts, puntaje):
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
    return attempts, puntaje


def juegoAhorcado():
    mezcladas = mezclarCategorias(categorias)
    seguir = seguirJugando()
    while seguir:
        word = elegirCategoria(mezcladas)
        if (word is None):
            print("No quedan mas palabras por elegir de ninguna categoria, el juego se acabo")
            break
        
        guessed = [] #adivina
        attempts = 6 #intentos 
        puntaje = 0

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
                puntaje += 6
                break
            
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
            
            letter = input("Ingresá una letra: ").lower() # de esta manera si se ingresa mayuscula lo pasa a minuscula
            attempts, puntaje = esUnaLetra(letter, guessed, word, attempts, puntaje)
            print()
            
        else:
            print(f"¡Perdiste! La palabra era: {word}")
            puntaje = 0

        print("tu puntaje es de: ", puntaje)
        seguir = seguirJugando()
            
#------------------------------------------------------------------------            
# PPAL

juegoAhorcado()
