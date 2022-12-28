#Corra el algoritmo anterior “desordena” (del ejercicio 1) muchas veces para 
# la misma sucesión de entrada. ¿Como puede analizarse la salida para determinar
#  si es  verdaderamente “aleatorio”?


import random
def desordenar(lista):
 #iteracion para la cantidad de valores que tendra la lista creada posteriormente
    for i in range(len(lista)):
        aleatorio = random.randint(0,len(lista)-1) 
        listaTemporal = lista[i]   #creamos un variable para almacenar los valores de la lista enla iteracion
        lista[i] = lista[aleatorio]  # solamente hacemos un intercambio 
        lista[aleatorio] =listaTemporal
    return lista
lista = [1,2,3,4,5,6,7,8,9]
print(desordenar(lista))

'''
evidentemente la respuesta lo podemos determinar ejecutando varias veces el algoritmo, y
efectivamente salen desordenados las listas introducidas, cuando ejecute tres veces, 
salian los sgtes, resultados
[5, 3, 7, 6, 1, 8, 2, 9, 4]
[6, 8, 2, 7, 3, 5, 1, 4, 9]
[4, 1, 2, 3, 7, 8, 5, 9, 6]; a partir de esto podemos concluir que  es aleatorio el orden
de los elementos de nuestra lista
'''