 # -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt
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
    
"""EXERCICE 5"""

def f(x):
    return x**3-x**2

a = 0
b = 1
n = 100
x = np.linspace(a,b,n+1)


"""EXERCICE 6"""


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

















