#Escriba un programa recursivo y otro no recursivo para 
# calcular la sucesión deFibonacci.
# Compare los tiempos requeridos por los programas
import time
def fibonacci(n):
  if n ==0:
    resultado=0
  elif n==1:
    resultado=1
  else:
    resultado=fibonacci(n-1)+fibonacci(n-2) 
  return resultado
print("El resultado de la sucesion de fibonacci es ", fibonacci(10))
tiempo1 = time.perf_counter()
fibonacci(10)
tiempo2 = time.perf_counter()
print("fibonacci recursivo en ", tiempo2-tiempo1)
print("...............")

# programa  no recursivo
def fibonacciNormal(n):
  a= 0
  b=1
  for i in range(n+1):
    c = b+a
    a= b
    b=c
  return a
tiempo1 = time.perf_counter()
fibonacciNormal(10)
tiempo2 = time.perf_counter()
print("El resultado de la sucesion de fibonacci es ", fibonacciNormal(10))
print("fibonacci no recursivo en ", tiempo2-tiempo1)