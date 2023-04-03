from time import sleep
import pygame as pg
from PIL import Image

# def cargar_imagen():
#     imagen = Image.open('Battleship.jpg');
#     imagen.show();

def cargar_sonido_bienvenida():
    pg.mixer.init()
    pg.mixer.music.load("Bienvenida.wav")
    pg.mixer.music.set_volume(2)
    return pg.mixer.music.play()


def dar_bienvenida(nombre, genero):
    if genero == "M":
        mensaje = f"\n{nombre}, welcome to the 'Battleship Game'!"
        for char in mensaje:
            sleep(0.1)
            print(char, end='', flush=True)

    elif genero == "F":
        mensaje = f"\n{nombre}, welcome to the 'Battleship Game'!"
        for char in mensaje:
            sleep(0.1)
            print(char, end='', flush=True)

    else:
        mensaje = f"\nPlease select 'F' (Female) or 'M' (Male)"
        for char in mensaje:
            sleep(0.1)
            print(char, end='', flush=True)


def dar_instrucciones():
    instrucciones = """Battleship is a two-player guessing game that involves trying to sink your opponent's fleet of ships. Here are the basic steps to play the game:

1. Each player has their own game board that consists of a grid of squares. The size of the board is 10x10. 

2. Place your ships: Before the game begins, each player secretly places their ships on their own game board. Usually players can place their ships horizontally or vertically on the board, but not diagonally, and the ships cannot overlap.
In this game, all the ships will be placed randomly and you will play against the bot! The number of ships and their sizes per player is as follows: 

1 carrier (4 spaces)
2 battleships (3 spaces)
3 submarines (2 spaces)
4 destroyers (1 spaces)

3. Take turns guessing: The first player chooses a square on their opponent's grid to guess if there is a ship there or not. 
They call out the coordinates of the square, such as "3,4". The coordinates are ranged between 0 and 9. If there is a ship in that square, the opponent says "hit." If there is no ship, the opponent says "miss." 

4. Continue guessing: Players take turns guessing until one player sinks all of their opponent's ships. A ship is considered sunk when every space it occupies has been hit.

5. Declare a winner: The player who sinks all of their opponent's ships first wins the game!

I hope these instructions help you understand how to play Battleship. Have fun playing!\n
"""
    print(instrucciones)
    # for char in instrucciones:
    #     sleep(0.1)
    #     print(char, end='', flush=True)





