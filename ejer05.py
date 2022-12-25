#Escriba un programa recursivo y otro no recursivo para 
# calcular la sucesión deFibonacci.
# Compare los tiempos requeridos por los programas
def fibonacci(n):
  if n>1:
    resultado=fibonacci(n-1)+fibonacci(n-2) 
  else:
    if n==0:
      resultado=0
    elif n==1:
      resultado=1
  return resultado
print(fibonacci(9))