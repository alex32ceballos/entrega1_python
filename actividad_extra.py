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
        
def agregarEquipo(equipo):
    if (not equipo in tabla):
        tabla[equipo]=0
    else:
        print('No se puede agregar el equipo porque ya se encuentra')
        

def menuOpciones():
    print("¡BIENVENIDO A LA TABLA DE POSICIONES!\nIngrese una de las siguientes opciones: \n")
    print("0. Agregar un equipo al torneo.")
    print("1. Registrar partido")
    print("2. Mostrar tabla de posiciones(menor a mayor)")
    print("3. Eliminar un equipo del torneo")
    print("4. Salir del programa")
    
menuOpciones()