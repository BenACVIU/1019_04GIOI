#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:39:47 2019

@author: barroquia

Calcular el precio de la habitacion

# Datos de entrada
1- Pedir las dimensiones de la baldosa
2- Pedir las dimensiones de la habitacion
3- Pedir el precio de unitario de baldosa

# Calculos
1- Calcular numero de baldosas
2- Calcular el precio de la habitacion 
(numero baldosas x precio unitario)

1.1- Obtener el numero de baldosas por eje
1.2- Si las baldosas no son enteras redondear al alza
"""

#bal_x = input("Dame las dimensiones (en centimetros) de la baldosa en x:")
#bal_y = input("Dame las dimensiones (en centimetros) de la baldosa en y:")
#xy = input("dame x, y")
#xy = xy.split(',')

# Dimension de una baldosa centimetros
bal_x, bal_y = 60, 20

# Dimensiones son en metros
hab_x, hab_y = 10, 20

hab_x, hab_y = hab_x * 100, hab_y * 100

precio_baldosa = 2.5

n_bal_x = hab_x / bal_x
n_bal_y = hab_y / bal_y

if (hab_x % bal_x) != 0:
    print("X es decimal")
    print(n_bal_x)
    n_bal_x = hab_x // bal_x
    n_bal_x += 1
    print(n_bal_x)

if (hab_y % bal_y) != 0:
    print("Y es decimal")
    print(n_bal_y)
    n_bal_y = hab_y // bal_y
    n_bal_y += 1
    print(n_bal_y)


num_baldosas = n_bal_x * n_bal_y
precio_total = num_baldosas * precio_baldosa

print(f"El precio total de las baldosas es: {precio_total}")

