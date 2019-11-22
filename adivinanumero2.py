#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:20:22 2019
@author: viuct
"""

import random

num_adivina = 18

for i in range(1, 6):
    numero_usuario = int(input("dame un numero:\n"))
    if num_adivina == numero_usuario:
        print("Adivinado!!!\n")
        break
    elif num_adivina < numero_usuario:
        print("el numero secreto es menor")
    else:
        print("el numero secreto es mayor")
    print("Intento numero: ", i)


print("El numero secreto es: ", num_adivina)
print("Termina")