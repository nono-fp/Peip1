# -*- coding: utf-8 -*-
 # -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import linregress
from math import *


def compteur (n):
    result = 0
    for  i in range(n):
        result+=1
    return result

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

fibo = [fibonacci(i) for i in range(20)]

def lancer2six():
    compteur = 1
    l1 = random.randint(1,6)
    l2 = random.randint(1,6)
    while (l1 and l2) != 6 :
        l1 = random.randint(1,6)
        l2 = random.randint(1,6)
        compteur += 1
    return compteur


tab= np.random.randint(1,21, size =15)

def tri_bulle(tab):
    n = np.size(tab)
    echange = True
    while echange:
        echange=False
        for i in range(0,n-1):
            if tab[i]>tab[i+1] :
                tab[i],tab[i+1] = tab[i+1], tab[i]
                echange = True
    return tab
    
"""EXERCICE 4"""

def f(x):
    return x**3-x**2

a = 0
b = 1
n = 100
x = (b-a)/n




inte = 0
for i in range(n):
    inte= inte+x*f(i)
print (inte)


"""EXERCICE 5"""


#1
 
#fonction = plt.plot([-1,3,5],[3,5,9])

#2
x = np.linspace(0,2*np.pi,60)
y = np.cos(x)
fonction2 = plt.plot(x,y,"X--","orange")
plt.show()

#3 
plt.xlim(0,2)
plt.ylim(-1.5,1.5)
fonction2 = plt.plot(x,y)
plt.title("ye ye ye ye ye, dans ma cabane, dans ma montagne")
plt.xlabel("dans ma forêt je suis en paix")
plt.ylabel("y")

fonction3 = np.sin(x)
plt.plot(x,fonction3,'o--',color = 'sandybrown')


fonction4 = np.arctan(x)
plt.plot(x,fonction4, 'P-',color ="mediumorchid")

plt.legend(["Pas là","envie de pioncer","flemme"])



"""EXERCICE 6 """


M = np.loadtxt('C:\\Users\\nfaivre\\Downloads\\mesures.txt',delimiter = ',', skiprows = 1)
U = M[:,0]
I = M[:,1]

plt.plot (I,U, 'o',color = 'red')

result = linregress(I,U)
print(result)
plt.plot(I,result[0]*I + result[1])


plt.xlabel("I en A")
plt.ylabel("U en V")
plt.title("Fichier Peip 1")

error = np.abs(U - (result[0]*I+result[1]))
ecM = np.max(error)

plt.errorbar(I,U, yerr = error)


"""EXERCICE 7"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


#1
x = np.linspace(0,np.pi,30)

plt.plot(x,np.cos(x))
plt.plot(x,x*x)

def f(x):
    return np.cos(x)-x**2
start = 0.5
solution = fsolve(f,start)
print(solution)
plt.plot(solution,solution**2 ,"o",color ="red")
 
















