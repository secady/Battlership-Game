# Importar todos los scripts
import py_clases as cls
import py_funciones as fun
import os



nombre = ""
genero = ""

while nombre == "" and genero == "":
    # cargar sonido de bienvenida
    fun.cargar_sonido_bienvenida()
    #cargar imagen
    # fun.cargar_imagen()
    # Mensaje de bienvenida
    nombre = input("Name: ").capitalize()
    nombre = nombre.strip()
    genero = input("Gender (M/F): ").capitalize()
    genero = genero.strip()
    fun.dar_bienvenida(nombre, genero)
    print("\n")

    # Instrucciones del juego
    fun.dar_instrucciones()
    print("\n")
    break


# Inicializar el juego
inicializar = ""
juego_iniciado = False
while not juego_iniciado:
    # cargar sonido de bienvenida
    inicializar = input("Are you ready to play (Y/N)? ").capitalize()
    if inicializar != "Y":
        print("What are you waiting for? It is gonna be so fun!")   
        fun.cargar_sonido_bienvenida()
    else:
        juego_iniciado = True



# Inicializar tableros
nombre = cls.Tablero(input("Input your user ID: "))
print("\n")
print("------------------------------------------------")  


os.system("cls")


# Colocar barcos aleatoriamente para la máquina SIN imprimir el tablero
nombre.tablero_maquina 
nombre.colocar_barcos_aleatorio()
print("\n")  



# Colocar barcos aleatoriamente para el usuario
nombre.tablero
nombre.colocar_barcos_aleatorio_usuario()
print("\n")
print("------------------------------------------------")


# El jugador empieza a disparar primero
nombre.disparar_alternativamente()
print("------------------------------------------------")

