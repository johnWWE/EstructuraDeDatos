#Un robot puede dar pasos de 1, 2 o 3 metros. Escriba un programa para 
# numerar todas las maneras en que el robot camina n metros.

def robot(n):
    if n==1 or n==2: # si solo son 2 metros o 1, solo puede recorrer de 1 manera, ya sea de 1m o 2m
        return n    
    elif n==3:          # maneras
        return n+1      #  1m-1m-1m; 1m-2m; 2m-1m; 3m
    else:
        return robot(n-1)+robot(n-2)+robot(n-3)   # se vuelve a llamar a la fauncion reeceursiva
                                                # pero cada vez disminuido en uno con respectto  a la anterior recursiva
print(robot(5))

# es claro que si la cantidad de metros es mayor a 3, se utiliza la recursividad , pero es un poco
# especificos ya que se llama la recursividad disminuida en uno, sumada con otra recursividad disminuida
#y asi sucesivamente