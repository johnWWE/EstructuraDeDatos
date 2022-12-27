#Un robot puede dar pasos de 1 o 2 metros. Escriba un programa para 
#numerar todas las maneras en que el robot camina n metros.

def pasosRobot(n):
    if n==1 or n==2:
        return n
    return pasosRobot(n-1)+pasosRobot(n-2)
print("El bot puede caminar de ", pasosRobot(4), "maneras diferentes")

#si son 4 metros, existen estas posibilidades 
#1ra. Se puede caminar siempre de 1m: 1-1-1-1
#2da. se puede caminar 2 metros con pasos de 1m y lo restante con pasos de 2m : 1-1-2
#3ra. 2metros con pasos de 2m, el restante con paasos de 1: 2-1-1
#4ta. 1 paso de 1m, luego un paso de 2m y finalmente 1 paso de 1 :1-2-1
#5ta . 2 pasos de 2m cada una : 2-2