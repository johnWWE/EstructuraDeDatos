#Escriba un programa recursivo y otro no recursivo para
#  calcular n!. Compare los tiempos requeridos por los programas.

import time
print("programa recursivo:")
def factorialRecursivo(n):
    if n==1:
        return 1
    else:
        return  n * factorialRecursivo(n-1)  #se vuelve a llamar la funcion recursiva para hacer el mismo proceso,pero disminuida en 1
print("El factorial con la funcion recursiva es: ", factorialRecursivo(5))

tiempo1= time.perf_counter()  #para tener acceso a tiempo y conversiones
#la funcion recursiva lo almacenamos en otra variable
nuevo =factorialRecursivo(5)
tiempo2= time.perf_counter() 
print("El resultado ", nuevo, "se hizo en un tiempo ", tiempo2-tiempo1)
print(".................")
def factorialNoRecursivo(n):
    resultado=1
    for i in range(1,n+1):
        resultado *= i
    return resultado
tiempo1 = time.perf_counter()
# la funcion no recursiva lo almacenamos de en una variable
nuevo2 = factorialNoRecursivo(5)
tiempo2 = time.perf_counter()
print("El factorial con la funcion no recursiva es: ", factorialNoRecursivo(5))
print("E;l resultado ", nuevo2, "se hizo en un tiempo ", tiempo2-tiempo1)

#print(".......programa no recursivo........")
#numero = int(input("Ingrese el numero deseado para calcular su factorial: "))
#factorial=1
#for i in range(1,numero +1):    # numero +1 para que la iteracion sea hasta el numero indicado
#    factorial *=i               # se multiplicado por todo los valores que tome a medida que vaye iterando
#print("el factorial del numero",numero, "es",factorial)

