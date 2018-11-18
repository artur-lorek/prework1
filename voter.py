#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:54:45 2018

@author: artur
"""

import math
import numpy.random as npr
import matplotlib.pyplot as plt

w = 512                               #wyborcy
ik = 7                                  #ilość kandydatów
m = 4                                   #mandaty
print("Liczba kandydatów: " + str(ik))
lgnk = [[] for x in range(0, ik)]       #lista głosów na kandydatów


v = 1                                   #licznik głosów
while v in range(1, w+1):               #kolejne głosowania wyborców
    g = []                              #głosy preferencyjne
    c = []                              #kandydaci (indeks listy w lgnk)
    for x in range(1, ik+1):            
        g.append(x)
    npr.shuffle(g)
    for x in range(0, ik):
        c.append(x)
    npr.shuffle(c)
    for x in range(1, ik+1):
        lgnk[c.pop()].append(g.pop())
    v += 1

lgnk_raw = tuple([tuple(x) for x in lgnk])
sg = lgnk[:]


for i in range(0, ik):
    t = []
    while lgnk[i]:
        g = min(lgnk[i])
        t.append(lgnk[i].count(g))
        while g in lgnk[i]:
            lgnk[i].remove(g)
    sg[i] = t.copy()                           #sumy głosów preferencyjnych


#print(lgnk_raw)
print(sg)
pkt = lgnk.copy()


    
    

#print(type(lgnk_raw))
#print(type(lgnk_raw[0]))
'''
kwota = math.ceil(w/m)                 #kwota Hare'a (prosta)
win = 0
winners = []
while win < m:
    temp = []
    for i in range(0, ik):
        temp.append(sg[i][i-i])
    if max(temp) >= kwota:
        win +=1
        winners.append(i+1)
    else:
        temp.index(min(temp))
        
    break
        
'''



"""
for k in range(1, ik+1):
    #Kandydat1
    for glos in range(1, ik+1):
        print("Kandydat " + str(k) + ":   " + str({glos : lk[k-1].count(glos)}))
"""        
    
print("\n\tkoniec")