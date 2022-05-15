#importando los archivos
from matplotlib import pyplot as plt
import numpy as np
from numpy import loadtxt
import os
import random
import collections
import itertools 
import math
#import pygame 
#from pygame.locals import *

#############################################################################################################
#############################################################################################################
#############################################################################################################


#archivos

RUTA_ABSOLUTA=os.getcwd()

provLISTA_DE_PALABRAS = os.path.join(RUTA_ABSOLUTA, "provisionales.txt")
imagenes=os.path.join(RUTA_ABSOLUTA,"imagenes")


#hace un rastreo del archivo y lo convierte en una lista
def aLista(path):
    image = loadtxt(str(path),dtype=str, delimiter='","')
    provLISTA_VERTICAL=[]
    for element in image:
        provLISTA_VERTICAL.append(element)
    return provLISTA_VERTICAL

LiSTA_TRABAJABLE=aLista(provLISTA_DE_PALABRAS)

palabra_del_dia=random.choice(LiSTA_TRABAJABLE)
#palabra_del_dia="lumpy"
#############################################################################################################





#alguien ya hizo el trabajo ajajaj (https://www.abc.es/tecnologia/videojuegos/abci-letras-mas-probables-wordle-espanol-cada-posicion-202202111501_noticia.html)


#METODOS UTILES



def VER_PALABRAS(LiSTA_TRABAJABLE):
    for palabra in LiSTA_TRABAJABLE:
        print(palabra)


#############################################################################################################


def OBTENER_COLORES(palabra_del_dia,LiSTA_TRABAJABLE):
    COMPENDIO_COLORES=[]

    for palabra in LiSTA_TRABAJABLE:
        COLORES=list()
        for letter in range(5):
            if(palabra[letter]==palabra_del_dia[letter]):
                COLORES.append("v")            
            elif (palabra[letter] in palabra_del_dia):
                COLORES.append("a")
            else:
                COLORES.append("g")

        COMPENDIO_COLORES.append(COLORES)

    return COMPENDIO_COLORES



#############################################################################################################


def COLOR_SINGULAR(palabra_del_dia):
    palabra=input("INTRODUCE LA PALABRA: ")
    COLORES=[]
    LETRASVERDES=[]
    NARANJAS=[]
    GRISES=[]
    for letter in range(len(palabra)):
        if(palabra[letter]==palabra_del_dia[letter]):
            COLORES.append("v")
            LETRASVERDES.append(palabra[letter])

        elif (palabra[letter] in palabra_del_dia):
            COLORES.append("n")
            NARANJAS.append(palabra[letter])
                
        else:
            COLORES.append("g")
            GRISES.append(palabra[letter])
            
    
    print(COLORES)
    return LETRASVERDES,NARANJAS,GRISES,COLORES
  


#############################################################################################################


def VER_COMPENDIO(COMPENDIO_COLORES):
    for color in COMPENDIO_COLORES:


        print(color)



#############################################################################################################


       
#que me muestre la probabilidad
def _INDICE(tablero):
    INDICES=[]
    for i in range(len(tablero)):
        if tablero[i]=="v":
            INDICES.append(i)
    #print(INDICES)
    return INDICES


#############################################################################################################

#METODO PRINCIPAL PRACTICAMENTE


def REDUCIR_PROBABILIDADES(LiSTA_TRABAJABLE, INDICES, LETRASVERDES,NARANJAS,GRISES):
    NUEVAS_PALABRAS=[]
    #print(INDICES)#[3,1,4]
    #print(LETRASVERDES,'VERDES')
    #print(NARANJAS,'NARANJAS')
    #print(GRISES,'GRISES')
    LiSTA_TRABAJABLE.pop()


    preNUEVAS_PALABRAS=[]



#############################################################################################################

#PARTE NARANJAS


    for word in LiSTA_TRABAJABLE:
        if len(NARANJAS)>=1:
            if NARANJAS[0] in word:
                if len(NARANJAS)>=2:
                    if NARANJAS[1] in word:
                        if len(NARANJAS)>=3:
                            if(NARANJAS[2]) in word:
                                if len(NARANJAS)>=4:
                                    if NARANJAS[3] in word:
                                        if len(NARANJAS)==5:
                                            if NARANJAS[4] in word:
                                                preNUEVAS_PALABRAS.append(word)

                                        else:
                                            preNUEVAS_PALABRAS.append(word)

                                else:
                                    preNUEVAS_PALABRAS.append(word)

                        else:
                            preNUEVAS_PALABRAS.append(word)
                else:
                    preNUEVAS_PALABRAS.append(word)



#############################################################################################################

#PARTE VERDES

    if len(INDICES)>=1:
        for palabra in LiSTA_TRABAJABLE:
            if palabra[INDICES[0]]==LETRASVERDES[0]:
                if len(INDICES) >= 2:
                    if palabra[INDICES[1]]==LETRASVERDES[1]:
                        if len(INDICES) >= 3:
                            if palabra[INDICES[2]]==LETRASVERDES[2]:
                                if len(INDICES) >= 4:
                                    if palabra[INDICES[3]]==LETRASVERDES[3]:
                                        if len(INDICES) == 5:
                                            if palabra[INDICES[4]]==LETRASVERDES[4]:
                                                NUEVAS_PALABRAS.append(palabra)
                                        else:
                                            NUEVAS_PALABRAS.append(palabra)
                                else:
                                    NUEVAS_PALABRAS.append(palabra)                                                     
                        else:
                            NUEVAS_PALABRAS.append(palabra)
                else:
                    NUEVAS_PALABRAS.append(palabra)
    else:
        print("Todas las palabras")
    
#############################################################################################################


#PARTE GRISES


    lista_final=[]

    for word in LiSTA_TRABAJABLE:
        
        if len(GRISES)>=1:
            if GRISES[0] not in word:
                if len(GRISES)>=2:
                    if GRISES[1] not in word:
                        if len(GRISES)>=3:
                            if(GRISES[2]) not in word:
                                if len(GRISES)>=4:
                                    if GRISES[3] not in word:
                                        if len(GRISES)==5:
                                            if GRISES[4] not in word:
                                                lista_final.append(word)

                                        else:
                                            lista_final.append(word)

                                else:
                                    lista_final.append(word)

                        else:
                            lista_final.append(word)
                else:
                    lista_final.append(word)


#############################################################################################################

#lista_final(grises)
#preNUEVAS_PALABRAS(naranjas)
#NUEVAS_PALABRAS(verdes)

#CUALES SON CUALES (arriba)
#############################################################################################################

#TODOS LOS POSIBLES CASOS DONDE NO EXISTEN ALGUNOS 


    prelista_final=[]
    if(len(NUEVAS_PALABRAS)>=1):
        if(len(preNUEVAS_PALABRAS)>=1):
            if(len(lista_final)>=1):
                for w1 in NUEVAS_PALABRAS:
                    for w2 in preNUEVAS_PALABRAS:
                        for w3 in lista_final:
                            if w1==w2==w3:
                                prelista_final.append(w1)  #VNG
            else:
                for w1 in NUEVAS_PALABRAS:
                    for w2  in preNUEVAS_PALABRAS:
                        if w1==w2:
                            prelista_final.append(w1) #VN

        elif(len(lista_final)>=1): 
            for w1 in NUEVAS_PALABRAS:
                for w2 in lista_final:
                    if w1==w2:
                        prelista_final.append(w1) #VG
        else:
            print("GANASTEEE") #V
    
    elif(len(preNUEVAS_PALABRAS)>=1):
        if(len(lista_final)>=1):
            for w1 in preNUEVAS_PALABRAS:
                for w2 in lista_final:
                    if w1==w2:
                        prelista_final.append(w1)   #NG
        else:
            prelista_final=preNUEVAS_PALABRAS  #N

    else:
        prelista_final=lista_final  #G



#############################################################################################################

    probabilidad=len(prelista_final)/len(LiSTA_TRABAJABLE)

#############################################################################################################

#EJECUTABLE
    
    print ("\n".join([" ".join(prelista_final[i:i+15]) for i in range(0,len(prelista_final),15)]))
   # print(prelista_final)
    

    if len(prelista_final)>=1:    
        bits=-(math.log2(probabilidad)) 
        print("Hay ",len(prelista_final), " palabras posibles, dando una probabilidad de: " ,probabilidad,"para este patron de colores dada la palabra original")
        print("Ademas nos da",bits, "bits de informacion")
    else:
        print("La probabilidad de tu palabra es: 1/", str(len(LiSTA_TRABAJABLE)))
    #return NUEVAS_PALABRAS




#############################################################################################################
#############################################################################################################
#############################################################################################################




#poner que sea solo 6 intentos


def JUGAR_WORDLE(palabra_del_dia,LiSTA_TRABAJABLE):
    i=1
    GANASTE=['v','v','v','v','v']
    TABLERO=[]
    while TABLERO != GANASTE: #and i<=6:
        LETRASVERDES,NARANJAS,GRISES,TABLERO=COLOR_SINGULAR(palabra_del_dia)
        INDICES=_INDICE(TABLERO)    
        REDUCIR_PROBABILIDADES(LiSTA_TRABAJABLE,INDICES,LETRASVERDES,NARANJAS,GRISES)

    print("GANASTEEE")



#############################################################################################################


def frecuencias(COMPENDIO_COLORES,LiSTA_TRABAJABLE):
    NUEVO_COMPENDIO=[]
    for element in COMPENDIO_COLORES:
        nuevo_string=str(element).replace('"','')
        NUEVO_COMPENDIO.append(nuevo_string)

    counter=collections.Counter(NUEVO_COMPENDIO)
    diccionario2=dict(counter)
    diccionario=dict(sorted(diccionario2.items(), key=lambda item: item[1]))
    nueva_lista=[]
    for x in diccionario.keys():
        nueva_lista.append(diccionario[x]/len(LiSTA_TRABAJABLE))
        #print(x , " => " , diccionario[x])
    
   # print(nueva_lista)
    return nueva_lista



#############################################################################################################

def mejoresfrecuencias(COMPENDIO_COLORES,LiSTA_TRABAJABLE):
    NUEVO_COMPENDIO=[]
    for element in COMPENDIO_COLORES:
        nuevo_string=str(element).replace('"','')
        NUEVO_COMPENDIO.append(nuevo_string)

    counter=collections.Counter(NUEVO_COMPENDIO)
    diccionario2=dict(counter)
    diccionario=dict(sorted(diccionario2.items(), key=lambda item: item[1]))
    nueva_lista=[]
    for x in diccionario.keys():
        if ((int(list(diccionario.values())[-1]))-(int((list(diccionario.values())[-2]))))<100000:
            #print(x , " => " , diccionario[x])
            nueva_lista.append(diccionario[x]/len(LiSTA_TRABAJABLE))
        else:
            #print("Muy poca entriopia")
            exit 
   # print(nueva_lista)
    return nueva_lista


#############################################################################################################

def histograma(mydict,palabra_del_dia):
    numeros=[]
    for x in range(len(mydict)):
        numeros.append(x)
    fig, ax = plt.subplots()
    ax.bar(numeros,mydict)
    plt.title(palabra_del_dia)

    imagenes=str(palabra_del_dia)
    plt.savefig('imagenes2/'+palabra_del_dia)

#   plt.xlabel('Patron')
#   plt.ylabel('frecuencias')
 #   plt.show()


def auxiliarentropia(COMPENDIO_COLORES,LiSTA_TRABAJABLE):
    NUEVO_COMPENDIO=[]
    for element in COMPENDIO_COLORES:
        nuevo_string=str(element).replace('"','')
        NUEVO_COMPENDIO.append(nuevo_string)

    counter=collections.Counter(NUEVO_COMPENDIO)
    
    diccionario2=dict(counter)
    
    diccionario=dict(sorted(diccionario2.items(), key=lambda item: item[1]))
    
    nueva_lista=[]
    for x in diccionario2.keys():
        nueva_lista.append(diccionario[x]/len(LiSTA_TRABAJABLE))


    
    return nueva_lista,diccionario2

def guardarimagenes(LiSTA_TRABAJABLE):
    for palabra in LiSTA_TRABAJABLE:
        COMPENDIO_COLORES=OBTENER_COLORES(palabra,LiSTA_TRABAJABLE)
        lista=mejoresfrecuencias(COMPENDIO_COLORES,LiSTA_TRABAJABLE)
        if len(lista)>1:
            #print(lista)
            histograma(lista,palabra)

#dado una palabra, que recopile la probababilidad de los colores, y sume las probababilidades:
#mas plano mas entriopia

def entriopia(LiSTA_TRABAJABLE):
    promedios=[]
    mayor=0
    palabrafinal=''
    for palabra in LiSTA_TRABAJABLE:
        promedio=[]
        diccionariopromedios=dict()
        COMPENDIO_COLORES=OBTENER_COLORES(palabra,LiSTA_TRABAJABLE)
        lista,dicti=auxiliarentropia(COMPENDIO_COLORES,LiSTA_TRABAJABLE)
        if len(lista)>1:
            for element in lista:

                bits=-(math.log2(element))
                suma=len(lista)/243
                entriopia=bits*suma
                promedio.append(entriopia)
                

        else:
            print("Existo :)")
        
        palabraentriopia=sum(promedio)/len(lista)

        
        diccionariopromedios={ palabra  : [palabraentriopia] }
#############################################################################################################
#############################################################################################################

#MAIN POR DECIRLO ASI


#############################################################################################################
#############################################################################################################
#guardarimagenes(LiSTA_TRABAJABLE)
#entriopia(LiSTA_TRABAJABLE)
#print(palabra_del_dia)


JUGAR_WORDLE(palabra_del_dia,LiSTA_TRABAJABLE)

#COMPENDIO_COLORES=OBTENER_COLORES(palabra_del_dia,LiSTA_TRABAJABLE)

#frecuencias(COMPENDIO_COLORES,LiSTA_TRABAJABLE)

#lista=frecuencias(COMPENDIO_COLORES,LiSTA_TRABAJABLE)
#diccionario = {1: 27, 34: 1, 3: 72, 4: 62, 5: 33, 6: 36, 7: 20, 8: 12, 9: 9, 10: 6, 11: 5, 
    #          12: 8, 2: 74, 14: 4, 15: 3, 16: 1, 17: 1, 18: 1, 19: 1, 21: 1, 27: 2}

#histograma(lista,palabra_del_dia)




#VER_COMPENDIO(COMPENDIO_COLORES)
#VER_PALABRAS(LiSTA_TRABAJABLE)














#METODOS INUTILES
def enumerar_colores():
    cont=0
    colores="vag"
    estados=itertools.product(colores,colores,colores,colores,colores)
    PATRONES=[]
    for i in estados:
        PATRONES.append(i)
   
    for element in PATRONES:
        print(element)


    return PATRONES












