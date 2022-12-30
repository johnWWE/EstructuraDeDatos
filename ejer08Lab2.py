#Implemente un programa recursivo que calcule la potencia de un numero 
# elevado a otro. Sabemos que 2n = 2n/2. 2n/2 donde n es un nro par; 
# y 2n = 2(n-1)/2. 2(n-1)/2.2 si n es impar

def potencia(base, exponente):
    if exponente == 1:    #cualquier numero elevado a uno sigue siendo la misma
        return base   
    elif exponente ==0 and base !=0:   #todo numero eleevado a cero es 1,
        return 1                        #pero la base diferente a cero sino seria indetermiado
    elif base==0 and exponente==0:
        return 'Es indeterminado' 
    else:
        # utilizamos la funcion recursiva ya que es un paso iterativo
        return base * potencia(base, exponente-1)   #esto es 2 + potencia(2,4) iterativamente hasta que las condiciones ya no se cumplan
print(potencia(2,5))