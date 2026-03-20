tabla = { #agregue algunos equipos a la tabla
    "Platense":2,
    "Estudiantes":6,
    "Boca":8
}

def eliminarEquipo(equipo): #funcion para eliminar equipo
    if (equipo in tabla):
        del tabla[equipo]
        print(f"el equipo {equipo} fue eliminado")
    else:
        print("el equipo ingresado no se encuentra en la tabla")
        
        
def agregarEquipo(equipo): #agrego un equipo
    if (not equipo in tabla):
        tabla[equipo]=0
    else:
        print('No se puede agregar el equipo porque ya se encuentra')
        
        
def partidoRegistrar(local,visitante, golesLocal, golesVisitante):
    if (local in tabla) and (visitante in tabla):
        if (golesLocal > golesVisitante):
            tabla[local]+=3
        elif (golesVisitante > golesLocal):
            tabla[visitante]+=3
        else:
            tabla[local]+=1
            tabla[visitante]+=1
    else:
        print("No se puede registrar el partido. Uno o ambos equipos no se encuentran en la tabla")


def marcadorEsNumero(marcador,local,visitante):
    if (marcador[0].isdigit() and marcador[1].isdigit()):
        golesLocal=int(marcador[0])
        golesVisitante=int(marcador[1])
        partidoRegistrar(local,visitante,golesLocal,golesVisitante)
    else:
        print('formato de marcador invalido')
        

def partidoActualizar(): #actualiza la tabla segun el partido
    local = input("ingresar equipo local: ")
    visitante = input("ingresar equipo visitante: ")
    marcador = input("ingresar marcador: ")
    if marcador.count("-") == 1:
        marcador = marcador.split("-")
        marcadorEsNumero(marcador,local,visitante)
    else:
        print('formato de marcador invalido')
  
  
def ordenarTabla(): #creo una lista de listas 
    tablaOrdenada = []
    for clave,valor in tabla.items():
        datos = []
        datos.append(valor)
        datos.append(clave)
        tablaOrdenada.append(datos)
    tablaOrdenada.sort(reverse=True)
    return tablaOrdenada

def mostrarTabla():
    tablaOrdenada = ordenarTabla()
    print("--------------------------------------------------")
    print("posicion   |      equipo      |    puntaje")
    contador = 1
    for subLista in tablaOrdenada:
        print(f"{contador}          |      {subLista[1]}      |    {subLista[0]}")
        contador+=1
        

def menuOpciones():
    print("¡BIENVENIDO A LA TABLA DE POSICIONES!\nIngrese una de las siguientes opciones: \n")
    print("0. Agregar un equipo al torneo.")
    print("1. Registrar partido")
    print("2. Mostrar tabla de posiciones(menor a mayor)")
    print("3. Eliminar un equipo del torneo")
    print("4. Salir del programa")
    
menuOpciones()