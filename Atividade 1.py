import numpy as np #importando as bibliotecas
import scipy as scp
import matplotlib.pyplot as plt
import scipy.integrate as it

n = 300
x = np.linspace(-20,20,n) # definindo um domínio para uso posterior

def gauss(x,μ,σ): #definindo a função gaussiana
  return 1/(np.sqrt(2*np.pi*σ**2))*np.exp(-((x-μ)**2)/(2*σ**2))

y = gauss(x,0,1) # teste de uma função gaussiana
plt.plot(x,y)
plt.show()

def interpolate(z,y,x): # definição da função de interpolação. Aqui, z,x,y são listas de números 
  p=[]                   # os dois últimos argumentos fornecem os pontos da curva y(x) a ser interpolada
  for j in range(np.size(x)-1):   # o primeiro argumento z fornece os pontos do domínio que se deseja projetar sobre a curva
    a = (y[j+1]-y[j])/(x[j+1]-x[j]) 
    b = y[j]-a*x[j]
    p.append([a,b])
    
  inter = []                    # A função se encontra definida em duas partes. A primeira acima calcula os coeficientes das retas que aproximam a função em cada intervalo.
  for i in range(np.size(z)):   # A segunda parte usa os coeficientes anteriores para projetar os pontos de z sobre a curva y(x) fornecida.
    for j in range(np.size(x)):
      if x[j]<z[i] and z[i]<x[j+1]:
        q = (p[j][0])*z[i]+(p[j][1])
        inter.append(q)
  return inter


a = 3*np.pi     # aqui está um teste da função de interpolação. Definimos um domínio z, e q é o conjunto de pontos interpolados.
b = 3
w = 150
z = np.linspace(-a,a,w)

q = interpolate(z,y,x)

plt.plot(z,q) # o plot da interpolação mostra que tal função cumpre o papel que desejávamos
plt.show()

g = np.linspace(-8,8,100)
ç = interpolate(g,np.exp(x),x)
plt.plot(x,np.exp(x), color='blue')
plt.plot(g,ç, color='red') # repetindo o processo agora para uma função do tipo coseno. Note que os pontos interpolados preenchem apenas uma parte da função, pois originalmente x foi definido de -20 a 20.
plt.show()