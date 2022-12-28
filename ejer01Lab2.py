#Implemente el siguiente algoritmo como un programa para desordenar. 
''' desordena(a, n){
    for i = 1 to n - 1
swap(ai,arand(i,n))
}'''
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
