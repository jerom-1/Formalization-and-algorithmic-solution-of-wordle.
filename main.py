#importando los archivos
import numpy as np
from numpy import loadtxt
import os
import random
from collections import Counter



RUTA_ABSOLUTA=os.getcwd()

provLISTA_DE_PALABRAS = os.path.join(RUTA_ABSOLUTA, "palabras.txt")

#hace un rastreo del archivo y lo convierte en una lista
def aLista(path):
    image = loadtxt(str(path),dtype=str, delimiter=' ')
    provLISTA_VERTICAL=[]
    for element in image:
        provLISTA_VERTICAL.append(element)
    return provLISTA_VERTICAL

LiSTA_TRABAJABLE=aLista(provLISTA_DE_PALABRAS)

palabra_del_dia=random.choice(LiSTA_TRABAJABLE)
print(palabra_del_dia)
#def CONTAR_FRECUENCIA(palabra):
#    contados=Counter(palabra)

#alguien ya hizo el trabajo ajajaj (https://www.abc.es/tecnologia/videojuegos/abci-letras-mas-probables-wordle-espanol-cada-posicion-202202111501_noticia.html)

#    print(contados)
#CONTAR_FRECUENCIA(palabra_del_dia)

#letras mas comunes = A O E S R
inicial_provisional="OSERA"
#2inicial_provisional='SALON'

def VER_PALABRAS(LiSTA_TRABAJABLE):
    for palabra in LiSTA_TRABAJABLE:
        print(palabra)


#VER_PALABRAS(LiSTA_TRABAJABLE)
def OBTENER_COLORES(palabra_del_dia,LiSTA_TRABAJABLE):
    COMPENDIO_COLORES=[]


    for palabra in LiSTA_TRABAJABLE:
        COLORES=[]
        for letter in range(len(palabra)):
            if(palabra[letter]==palabra_del_dia[letter]):
                COLORES.append("v")            
            elif (palabra[letter] in palabra_del_dia):
                COLORES.append("g")
            else:
                COLORES.append("b")

        COMPENDIO_COLORES.append(COLORES)

    return COMPENDIO_COLORES

def COLOR_SINGULAR(palabra_del_dia):
    palabra=input("INTRODUCE LA PALABRA")
    COLORES=[]
    for letter in range(len(palabra)):
        if(palabra[letter]==palabra_del_dia[letter]):
                COLORES.append("v")            
        elif (palabra[letter] in palabra_del_dia):
                COLORES.append("g")
        else:
            COLORES.append("b")
    
    print(COLORES)
    return COLORES





def VER_COMPENDIO(COMPENDIO_COLORES):
    for color in COMPENDIO_COLORES:
        print(color)


#COMPENDIO_COLORES=OBTENER_COLORES(palabra_del_dia,LiSTA_TRABAJABLE)

#VER_COMPENDIO(COMPENDIO_COLORES)
       
def JUGAR_WORDLE(palabra_del_dia):
    GANASTE=['v','v','v','v','v']
    TABLERO=[]
    while TABLERO != GANASTE:
        TABLERO=COLOR_SINGULAR(palabra_del_dia)


    print("GANASTEEE")


JUGAR_WORDLE(palabra_del_dia)








