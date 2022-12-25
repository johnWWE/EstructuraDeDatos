#Implemente un programa recursivo que calcule la potencia de un numero 
# elevado a otro. Sabemos que 2n = 2n/2. 2n/2 donde n es un nro par; 
# y 2n = 2(n-1)/2. 2(n-1)/2.2 si n es impar

def potencia(base, exponente):
    if exponente == 1:
        return base
    elif exponente ==0 and base !=0:
        return 1
    elif base==0 and exponente==0:
        return 'Es indeterminado'
    else:
        return base * potencia(base, exponente-1)
print(potencia(0,0))