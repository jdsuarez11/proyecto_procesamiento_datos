import os
from readchar import readkey, key

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################..
"""

def mapa_laberinto(laberinto):
    for fila in laberinto.split("\n"):
        print(list(fila))
    return [list(fila) for fila in laberinto.split("\n")]


def limpiar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')
    
def mostrar_mapa(mapa):
    for fila in mapa:
        print(''.join(fila))

def main_loop(mapa, posicion_inicial, posicion_final):
    mostrar_mapa(mapa)
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        limpiar_pantalla()
        mapa[px][py] = 'P'
        mostrar_mapa(mapa)
        mapa[px][py] = '.'

        t = readkey()
        if t == key.UP and px > 0 and mapa[px - 1][py] != '#':
            px -= 1
        elif t == key.DOWN and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            px += 1
        elif t == key.LEFT and py > 0 and mapa[px][py - 1] != '#':
            py -= 1
        elif t == key.RIGHT and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            py += 1
        elif t == "Q" or t == "q":
            print("Saliste del juego")
            break

    print(posicion_final)


mapa = mapa_laberinto(laberinto)
posicion_inicial = (0, 0)
posicion_final = (20, 20)
main_loop(mapa, posicion_inicial, posicion_final)