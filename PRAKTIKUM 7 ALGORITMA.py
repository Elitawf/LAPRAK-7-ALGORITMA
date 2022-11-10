# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:54:23 2022

@author: Elita
"""

def bilprima():
    angka = int(input("Masukan sebuah Angka: "))
    if angka < 2:
        print(angka, "adalah bilangan prima")
        return False
    for prima in range (2, angka):
        if angka % prima == 0:
            print (angka, "bukan bilangan prima")
        return print(angka, "bilangan prima")
a = bilprima()
print(a)