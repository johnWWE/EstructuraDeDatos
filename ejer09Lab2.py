#Implemente un programa recursivo que sume dos números a + b. 
# Considera que la suma a+b = a + 1 + 1 + ...+ 1 (b veces)

def sumaRecursiva(a,b):
    if a == 0 and b==0:
        return 0
    elif a==0:
        return b
    elif b==0:
        return a
    else:
        return 1 + sumaRecursiva(a,b-1) # con esta funcion recursiva sumamos 1+1+... hasta que 
                                        #uno se sus parametros sea cero, en tal caso deevuelve el valor a o b
        #return a + b*(1)

print(sumaRecursiva(2,4))

# el resultado es:
# 1 + sumaRecursiva(2,3)
# 1 +   1 +sumaRecursiva(2,2)
# 1 + 1+    1 +sumaRecursiva(2,1)
# 1+ 1+ 1+    1 +sumaRecursiva(2,0)   aqui b ya es cero, entioonces se cumple la 2da. condicional elif
# 1+ 1+ 1+ 1+ 2 ====6