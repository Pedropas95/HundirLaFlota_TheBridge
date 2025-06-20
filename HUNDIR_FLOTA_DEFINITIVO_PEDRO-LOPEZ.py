

print("""BIENVENIDO A HUNDIR LA FLOTA
          
          Hoy te enfrentarás al temible capitán Davy Jones en este juego por la supervivencia marítima. Adelante, demuestra que no eres un grumete. 

          REGLAS: 

          1) Los barcos aparecerán como 'O', el agua es '~'. 
          2) Introduce fila y columna para disparar
          3) Si aciertas, aparecerá una X. Si fallas, aparecerá una 'A' de agua. 
          4) Si terminas con sus barcos, pues ganas. Sino... Serás pasto de los peces
      

          
          SUERTE """)
    


import numpy as np
import time
import math
import random
tablero = np.full((10,10),"~")
print(tablero)



############# 1. CREAR TABLERO ############

def crea_tablero_jugador(lado = 10):
    tablero_jugador = np.full((lado,lado),"~")
    print("creando tu tablero, jugador")
    print(tablero_jugador)
    return tablero_jugador

def crea_tablero_ia(lado = 10):
    tablero_ia = np.full((lado,lado),"~")
    print("creando el tablero de Davy Jones")
    print(tablero_ia)
    return tablero_ia



# crea_tablero_jugador(lado=10)
tablero_ia = crea_tablero_ia()
tablero_jugador = crea_tablero_jugador()
def coloca_barco_plus(tablero, barco):
    tablero = tablero.copy()
    num_max_filas = 10
    num_max_columnas = 10
    for pieza in barco:
        fila, columna = pieza
        if fila < 0 or fila >= num_max_filas:
            print("No puedo poner el buque", pieza, "porque se sale del tablero")
            return None
        if columna < 0 or columna >= num_max_columnas:
            print("No puedo poner el buque", pieza, "porque se sale del tablero")
            return None
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            print("No puedo poner el buque", pieza,  "porque hay otro barco")
            return None
        tablero[pieza] = "O"
    return tablero

import random
import numpy as np

def coloca_barco(tablero):
    esloras = [2, 2, 2, 3, 3, 4]
    for eslora in esloras:
        colocado = False
        intentos = 0
        print("Intentando colocar barco de", eslora, "metros de eslora...")
        while not colocado and intentos < 1000:
            intentos = intentos + 1
            barco = []
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(["N", "S", "E", "O"])

            if orientacion == "N" and fila - (eslora - 1) < 0:
                continue
            if orientacion == "S" and fila + (eslora - 1) > 9:
                continue
            if orientacion == "E" and columna + (eslora - 1) > 9:
                continue
            if orientacion == "O" and columna - (eslora - 1) < 0:
                continue

            barco.append((fila, columna))
            for _ in range(eslora - 1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "E":
                    columna += 1
                elif orientacion == "O":
                    columna -= 1
                barco.append((fila, columna))

            resultado = coloca_barco_plus(tablero, barco)  

            if isinstance(resultado, np.ndarray):
                tablero = resultado
                colocado = True
                print("El barco de eslora", eslora, "metros ha sido colocado")

        if not colocado:
            print("No se pudo colocar el barco de", eslora, "metros tras", intentos, "intentos")

    print(tablero)
    return tablero


###### LLAMAAAAAAAAAAAAAAAADA A LA FUNCIÓNNN
print("TABLERO JUGADOR. Dale caña piratón...")
tablero_juego_jugador = coloca_barco(tablero_jugador)

print("TABLERO IA.")
tablero_juego_ia = coloca_barco(tablero_ia)

print("ESTOS SON TUS BARCOS... ")
print(tablero_juego_jugador)

print("Y ESTOS SON LOS DE LA IA")
print(tablero_juego_ia)



############    DISPARAR TÚ A LA MÁQUINA


def disparar(tablero_juego_ia):
    print("ahora te toca disparar...")
    fila = int(input("Introduce la coordenada de disparo (fila): "))
    col = int(input("Introduce la coordenada de disparo (columna): "))
    
    disparo = (fila, col)  
    
    if tablero_juego_ia[disparo] == "O":
        tablero_juego_ia[disparo] = "X"
        print("ENHORABUENA. Has tocado un barco enemigo. Sigue así piratón")
    elif tablero_juego_ia[disparo] == "X":
        print("Agonía... Ya habías disparado ahí. Cambia a otro sitio porque estás perdiendo el tiempo.")
    else:

        tablero_juego_ia[disparo] = "A"
        print("Agua. Afina tus disparos anda.")
        
    return tablero_juego_ia

disparar(tablero_juego_ia)


##########  RECIBIR DISPARO DE LA IAAAAAAAAAAAAAAAAAAAAAAA


def disparo_aleatorio(tablero_juego_jugador):
    filas = len(tablero_juego_jugador)
    columnas = len(tablero_juego_jugador[0])
    
    while True:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        disparo = (fila, columna)

       
        if tablero_juego_jugador[disparo] not in ["X", "A"]:
            break  

    if tablero_juego_jugador[disparo] == "O":
        tablero_juego_jugador[disparo] = "X"
        print("Tu enemigo te ha disparado en", fila, columna, ":TOCADOOOO. Cuidadín, cuidadín")
    else:
        tablero_juego_jugador[disparo] = "A"
        print("El enemigo te dispara al", fila, columna, " Suerte, no te ha dado... Agua")
    
    return tablero_juego_jugador

disparo_aleatorio(tablero_juego_jugador)




######## FUNCIÓN BUCLE PARA QUE EL JUEGO CONTINÚE


def fin_juego(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == "O":
                return False
    print("GAME OVER, has perdido")
    return True


while True:
    tablero_juego_ia = disparar(tablero_juego_ia)
    if fin_juego(tablero_juego_ia):
        print("¡Has ganado! Eres un máquina")
        break

    tablero_juego_jugador = disparo_aleatorio(tablero_juego_jugador)
    if fin_juego(tablero_juego_jugador):
        print("Has perdido... Dormirás con los peces.")
        break
