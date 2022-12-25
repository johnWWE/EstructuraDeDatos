#Escriba un programa recursivo y otro no recursivo para
#  calcular n!. Compare los tiempos requeridos por los programas.


print("programa recursivo:")

def factorialRecursivo(n):
    if n==0:
        return 1
    else:
        return  n * factorialRecursivo(n-1)  #se vuelve a llamar la funcion recursiva para hacer el mismo proceso,pero disminuida en 1
print(factorialRecursivo(4))



print(".......programa no recursivo........")
numero = int(input("Ingrese el numero deseado para calcular su factorial: "))
factorial=1
for i in range(1,numero +1):    # numero +1 para que la iteracion sea hasta el numero indicado
    factorial *=i               # se multiplicado por todo los valores que tome a medida que vaye iterando
print("el factorial del numero",numero, "es",factorial)

