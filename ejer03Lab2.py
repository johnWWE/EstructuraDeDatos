'''Implemente la selección por orden como un programa: El algoritmo de selección por 
orden acomoda la sucesión s1, . . . , sn en orden no decreciente, para ello encuentra 
primero el elemento más pequeño, por ejemplo si, y lo coloca en el primer lugar intercambiando
s1 y si. después encuentra el algoritmo más pequeño en s2, . . . , sn, de nuevo digamos si, y lo
coloca en el segundo lugar intercambiando s2 y si. Continua hasta que la sucesión 
esté ordenada.'''

lista = [3,4,2,1,5]
for i in range(len(lista)): #un for para el tamanio de la lista
    valorMinimo = i       # 
    for j in range(i,len(lista)): # iteraremos con 2 iteradores
        if lista[j]<lista[valorMinimo]:#se compara cada valor del elemneto con el siguiente valor del elemento
            valorMinimo = j         # el menor de las cantidas queda aalamcenada en la variable
    auxiliador = lista[i]        
    lista[i] = lista[valorMinimo]    # hacemos un intercambio de valores para que la comparacion siga iterando
    lista[valorMinimo] = auxiliador
    print(lista)    #imprime todos las iteraciones en una lista, hasta que  quede ordena de menor a mayor
print(f'\n')
