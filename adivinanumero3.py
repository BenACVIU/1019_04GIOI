#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:29:41 2019

@author: barroquia

Adivinar un numero por parte del usuario

1- Pedir el numero 5 veces
2- Decir si el numero es mayor, menor o adivinado

1.1- Si el nuero acierta deja de pedir numero
"""

import random

numero_secreto = random.randint(1, 20)
print(numero_secreto)
numero_veces = 5

for i in range(1, numero_veces+1):
    num_usuario = int(input("Dame un numero: "))
    if num_usuario == numero_secreto:
        print("Adivinado!!!\n")
        break
    elif num_usuario > numero_secreto:
        print("El numero es menor")
    else:
        print("El numero es mayor")
    print(f"Intento numero {i}")
    
print(f"El numero secreto era {numero_secreto}")



