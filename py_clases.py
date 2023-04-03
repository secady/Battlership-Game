import numpy as np
import os
import pygame as pg
from tabulate import tabulate

class Tablero:
    """
    los tableros tienen tamaño de 10x10 por defecto.
    tablero_barcos = este tablero es para colocar barcos del jugador.
    tablero_disparos = este tablero es para apuntar los disparos que lanza el jugador (nosotros) hacia los barcos del enemigo (maquina).
    """

    tablero_maquina = np.full((10,10), "  ")
    tablero_maquina_sin_barcos = tablero_maquina.copy()
    dimensiones_barcos_maquina = {"K ": 1,
                                "L ": 1,
                                "M ": 1,
                                "N ": 1,
                                "O ": 2,
                                "P ": 2,
                                "Q ": 2,
                                "R ": 3,
                                "S ": 3,
                                "T ": 4}
    coordenadas_barcos_maquina = {}
    barcos_vidas_maquina = dimensiones_barcos_maquina.copy()


    tablero = np.full((10,10), "  ")
    dimensiones_barcos = {"A ": 1,
                        "B ": 1,
                        "C ": 1,
                        "D ": 1,
                        "E ": 2,
                        "F ": 2,
                        "G ": 2,
                        "H ": 3,
                        "I ": 3,
                        "J ": 4}
    coordenadas_barcos = {}
    barcos_vidas = dimensiones_barcos.copy()


    def __init__(self, id_jugador):
        """
        id_jugador = alphanumeric. 
        barcos = dict (nombre de barcos y sus esloras).
        """
        self.id_jugador = id_jugador
        


    def colocar_barcos_aleatorio(self):
        """
        Es una función para colocar barcos aleatoriamente (para el tablero de la máquina)
        is_vertical = True = Vertical
        is_vertical = False = Horizontal
        """

        def comprobar_colision_maquina(coord, eslora, is_vertical):
            """
            Comprobar colisión con barcos existentes y si va fuera el rango del tablero
            """
            if is_vertical:
                if coord[0]+eslora > 10: # Comprobar si el barco va fuera el rango del tablero
                    return True
                for i in range(coord[0]-1, coord[0]+eslora+1):
                    if i < 0 or i > 9:
                        continue
                    for j in range(coord[1]-1, coord[1]+2):
                        if j < 0 or j > 9:
                            continue
                        if self.tablero_maquina[i][j] != "  ":
                            return True
            else:
                if coord[1]+eslora > 10: # Comprobar si el barco va fuera el rango del tablero
                    return True
                for i in range(coord[0]-1, coord[0]+2):
                    if i < 0 or i > 9:
                        continue
                    for j in range(coord[1]-1, coord[1]+eslora+1):
                        if j < 0 or j > 9:
                            continue
                        if self.tablero_maquina[i][j] != "  ":
                            return True
            return False

        for barco, eslora in self.dimensiones_barcos_maquina.items():
            while True:
                is_vertical = np.random.random() > 0.5
                coordenada_inicial = np.random.randint(0, 10, 2)
                if not comprobar_colision_maquina(coordenada_inicial, eslora, is_vertical):
                    break
            if eslora == 1:
                self.tablero_maquina[coordenada_inicial[0], coordenada_inicial[1]] = barco           
            elif eslora > 1:
                if is_vertical == True:
                    self.tablero_maquina[coordenada_inicial[0]:coordenada_inicial[0]+eslora, coordenada_inicial[1]] = barco
                else:
                    self.tablero_maquina[coordenada_inicial[0], coordenada_inicial[1]:coordenada_inicial[1]+eslora] = barco          
            fila = np.where(self.tablero_maquina == barco)[0]
            col = np.where(self.tablero_maquina == barco)[1]
            proa = (fila[0], col[0])
            popa = (fila[-1], col[-1])
            self.coordenadas_barcos_maquina[barco] = (is_vertical, proa, popa)
        

        os.system("cls")
        
        tabla_maquina_sin_barcos = tabulate(self.tablero_maquina_sin_barcos, range(0,10), showindex="always", tablefmt="fancy_grid")
        print("\nThe opponent's board (only shows the impacts of your shoots)\n", tabla_maquina_sin_barcos, "\n")


    def colocar_barcos_aleatorio_usuario(self):
        """
        Es una función para colocar barcos aleatoriamente (para el tablero de la máquina)
        is_vertical = True = Vertical
        is_vertical = False = Horizontal
        """

        def comprobar_colision(coord, eslora, is_vertical):
            """
            Comprobar colisión con barcos existentes y si va fuera el rango del tablero
            """
            if is_vertical:
                if coord[0]+eslora > 10: # Comprobar si el barco va fuera el rango del tablero
                    return True
                for i in range(coord[0]-1, coord[0]+eslora+1):
                    if i < 0 or i > 9:
                        continue
                    for j in range(coord[1]-1, coord[1]+2):
                        if j < 0 or j > 9:
                            continue
                        if self.tablero[i][j] != "  ":
                            return True
            else:
                if coord[1]+eslora > 10: # Comprobar si el barco va fuera el rango del tablero
                    return True
                for i in range(coord[0]-1, coord[0]+2):
                    if i < 0 or i > 9:
                        continue
                    for j in range(coord[1]-1, coord[1]+eslora+1):
                        if j < 0 or j > 9:
                            continue
                        if self.tablero[i][j] != "  ":
                            return True
            return False

        for barco, eslora in self.dimensiones_barcos.items():
            while True:
                is_vertical = np.random.random() > 0.5
                coordenada_inicial = np.random.randint(0, 10, 2)
                if not comprobar_colision(coordenada_inicial, eslora, is_vertical):
                    break
            if eslora == 1:
                self.tablero[coordenada_inicial[0], coordenada_inicial[1]] = barco           
            elif eslora > 1:
                if is_vertical == True:
                    self.tablero[coordenada_inicial[0]:coordenada_inicial[0]+eslora, coordenada_inicial[1]] = barco
                else:
                    self.tablero[coordenada_inicial[0], coordenada_inicial[1]:coordenada_inicial[1]+eslora] = barco          
            fila = np.where(self.tablero == barco)[0]
            col = np.where(self.tablero == barco)[1]
            proa = (fila[0], col[0])
            popa = (fila[-1], col[-1])
            self.coordenadas_barcos[barco] = (is_vertical, proa, popa)
        

        tabla = tabulate(self.tablero, range(0,10), showindex="always", tablefmt="fancy_grid")
        print("\nYour board\n", tabla, "\n")
    


    # FALTA poner condiciones para que no repita poner las mismas coordenadas o chocar otro barco
    def colocar_barcos_usuario(self):
        """
        Es una función para colocar barcos en base del input del jugador/usuario
        """

        print("Ahora vas a colocar 10 barcos en tu tablero\n")

        for barco, eslora in self.dimensiones_barcos.items():
            while True:
                is_vertical = input(f"Introduce 'Vertical' o 'Horizontal' para la posición del barco {barco}: ").capitalize()
                is_vertical = is_vertical.strip()
                if is_vertical == "Vertical" or is_vertical == "Horizontal":
                    self.coordenadas_barcos[barco] = [is_vertical]

                    coord_barco_x = int(input(f"Introduce un número de 0 a 9 para la coordenada X del barco {barco}: "))
                    if coord_barco_x >= 0 and coord_barco_x <= 9:
                        self.coordenadas_barcos[barco].append(coord_barco_x)

                        coord_barco_y = int(input(f"Introduce un número de 0 a 9 para la coordenada Y del barco {barco}: "))   
                        if coord_barco_y >= 0 and coord_barco_y <= 9:
                            self.coordenadas_barcos[barco].append(coord_barco_y)
                            break

                        else:
                            print("El número introducido está fuera del rango. Elige entre 0 y 9.")
                            continue
 
                    else:    
                        print("El número introducido está fuera del rango. Elige entre 0 y 9.")
                        continue

                else:
                    print("Por favor elige 'Vertical' o 'Horizontal'.")
                    continue
                
                                           
            if eslora == 1:
                self.tablero[coord_barco_x, coord_barco_y] = barco           
            elif eslora > 1:
                if is_vertical == "Vertical":
                    self.tablero[coord_barco_x:coord_barco_x+eslora, coord_barco_y] = barco
                elif is_vertical == "Horizontal":
                    self.tablero[coord_barco_x, coord_barco_y:coord_barco_y+eslora] = barco          
            fila = np.where(self.tablero == barco)[0]
            col = np.where(self.tablero == barco)[1]
            proa = (fila[0], col[0])
            popa = (fila[-1], col[-1])
            self.coordenadas_barcos[barco] = (is_vertical, proa, popa)

        print("\n")
        print("Tu tablero\n", self.tablero)
        print("\n")

        
            

    #El usuario dispara primero
    def disparar_alternativamente(self):
        """
        Esta función es para lanzar disparos alternos. 
        Empieza primero por el jugador donde tiene que introducir las coordenadas manualmente
        y seguido por el disparo aleatorios por la máquina.

        range de disparos = 0-9 porque jugamos en un tablero de 10x10.
        size de disparos = 2 porque las coordinadas consisten en 2 números.

        Condiciones:
        1. Si los números aleatorios tocan una eslora de barco, se marcará con "X" e se imprimirá "Tocado"
        2. Si los números aleatorios tocan todas las esloras de barco (la longitud del barco), cambia el nombre del barco con la "$" e imprime "Hundido"
        3. Si toca agua, el nombre del barco se cambiará a "@" e se imprimirá "Agua"!
        4. El juego seguirá en marcha hasta las vidas del jugador o de la máquina se agote. Quién alcanza 0 vida primero, perderá el juego.

        """

        total_vidas_usuario = sum(self.barcos_vidas.values())
        total_vidas_maquina = sum(self.barcos_vidas_maquina.values())

        total_intentos = 0
        while total_vidas_usuario != 0 or total_vidas_maquina != 0:

            total_intentos += 1
            print(f"\nAttempt {total_intentos}")

            disparos_x = int(input("\nInput X coordinate to shoot: "))
            disparos_y = int(input("Input Y coordinate to shoot: "))

            try:
                if (disparos_x >= 0 and disparos_x <= 9) and (disparos_y >= 0 and disparos_y <= 9):
                    if self.tablero_maquina[disparos_x, disparos_y]  != "  ":
                        self.tablero_maquina[disparos_x, disparos_y] = "💣"
                        print("\nHit!\n")
                        self.cargar_sonido_tocado()
                        # print("El tablero del oponente\n", self.tablero_maquina, "\n") # Deberiamos desactivar esta parte para esconder los barcos de la máquina
                        self.demostrar_impactos_maquina()
                        self.comprobar_vidas_maquina()
                        total_vidas_maquina -= 1
                        print(f"\nThe opponent's remaining lives: {total_vidas_maquina}")
                        print("------------------------------------------------")
                        if total_vidas_maquina == 0:
                            print("\nYou won! 🥳")
                            self.cargar_sonido_victoria()
                            break
                    else:
                        self.tablero_maquina[disparos_x, disparos_y] = "💧"
                        print("\nMiss\n")
                        self.cargar_sonido_agua()
                        # print("El tablero del oponente\n", self.tablero_maquina, "\n") # Deberiamos desactivar esta parte para esconder los barcos de la máquina
                        self.demostrar_impactos_maquina()
                        self.comprobar_vidas_maquina()
                        print(f"\nThe opponent's remaining lives: {total_vidas_maquina}")
                        print("------------------------------------------------")           

                    disparos = np.random.randint(0, 10, size=2)

                    if self.tablero[disparos[0], disparos[1]] != "  ":
                        self.tablero[disparos[0], disparos[1]] = "💣"
                        print("\nHit!\n")
                        # print("Your Board\n", self.tablero, "\n")
                        tabla = tabulate(self.tablero, range(0,10), showindex="always", tablefmt="fancy_grid")
                        print("Your Board\n", tabla, "\n")
                        self.comprobar_vidas_usuario()
                        total_vidas_usuario -= 1
                        print(f"\nYour remaining lives: {total_vidas_usuario}")
                        print("------------------------------------------------")  
                        if total_vidas_usuario == 0:
                            print("\nYou lost! 😰")
                            self.cargar_sonido_perdida()
                            break
                        
                    else:
                        self.tablero[disparos[0], disparos[1]] = "💧"
                        print("\nMiss\n")
                        # print("Your board\n", self.tablero, "\n")
                        tabla = tabulate(self.tablero, range(0,10), showindex="always", tablefmt="fancy_grid")
                        print("Your Board\n", tabla, "\n")
                        self.comprobar_vidas_usuario()
                        print(f"\nYour remaining lives: {total_vidas_usuario}")
                        print("------------------------------------------------")  
                
                else:
                    print("Please select between 0 y 9")
            except:
                print("Please select between 0 y 9")


    # FALTAN: Declarar barcos hundidos y contar bien las vidas
    def comprobar_vidas_usuario(self):
        """
        Esta función sirve para comprobar las vidas de los barcos del jugador.
        """

        for barco, vida in self.barcos_vidas.items():
            self.barcos_vidas[barco] = np.count_nonzero(self.tablero == barco)
            if vida == 0:
                print("A ship was just SUNK!")
            # print(f"\nEl barco {barco} tiene {vida} vidas")
        # print(f"\nYour remaining lives: {sum(self.barcos_vidas.values())}")


    def comprobar_vidas_maquina(self):
        """
        Esta función sirve para comprobar las vidas de los barcos de la máquina.
        """       

        for barco, vida in self.barcos_vidas_maquina.items():
            self.barcos_vidas_maquina[barco] = np.count_nonzero(self.tablero_maquina == barco)
            if vida == 0:
                print("A ship was just SUNK!")
            # print(f"\nEl barco {barco} tiene {vida} vidas")
        # print(f"\nThe opponent's remaining lives: {sum(self.barcos_vidas_maquina.values())}")
       



    def demostrar_impactos_maquina(self):
        """
        Esta función sirve para demostrar el impacto de disparos del jugador hacia los barcos en 
        el tablero de la máquina (SIN imprimir la ubicación de los barcos)
        """

        if "💣" in self.tablero_maquina or "💧" in self.tablero_maquina:
            condicion_1 = (self.tablero_maquina == "💣") # tocado
            # condicion_2 = (self.tablero_maquina == "$") # hundido
            condicion_3 = (self.tablero_maquina == "💧") # agua
            self.tablero_maquina_sin_barcos = np.where((condicion_1 | condicion_3), self.tablero_maquina, "  ")
            # print("The opponent's board (only shows the impacts of your shoots)\n", self.tablero_maquina_sin_barcos, "\n")
            tabla_maquina_sin_barcos = tabulate(self.tablero_maquina_sin_barcos, range(0,10), showindex="always", tablefmt="fancy_grid")
            print("\nThe opponent's board (only shows the impacts of your shoots)\n", tabla_maquina_sin_barcos, "\n")
        else:
            # print("The opponent's board (only shows the impacts of your shoots)\n", self.tablero_maquina_sin_barcos, "\n")
            tabla_maquina_sin_barcos = tabulate(self.tablero_maquina_sin_barcos, range(0,10), showindex="always", tablefmt="fancy_grid")
            print("\nThe opponent's board (only shows the impacts of your shoots)\n", tabla_maquina_sin_barcos, "\n")



    def cargar_sonido_tocado(self):
        pg.mixer.init()
        pg.mixer.music.load("Tocado.wav")
        pg.mixer.music.set_volume(1)
        return pg.mixer.music.play()

    
    def cargar_sonido_agua(self):
        pg.mixer.init()
        pg.mixer.music.load("Agua.mp3")
        pg.mixer.music.set_volume(2)
        return pg.mixer.music.play()
    

    def cargar_sonido_victoria(self):
        pg.mixer.init()
        pg.mixer.music.load("Victoria.mp3")
        pg.mixer.music.set_volume(1)
        return pg.mixer.music.play()

    
    def cargar_sonido_perdida(self):
        pg.mixer.init()
        pg.mixer.music.load("Perdida.wav")
        pg.mixer.music.set_volume(1)
        return pg.mixer.music.play()