# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:06:51 2022

@author: Elita
"""

def ordinal():
    print("Ordinal Number")
    print("ketik 0 untuk menghentikan program")
    while True:
        num = int(input("Masukan sebuah angka: "))
        if num in [10, 11, 12, 13]:
            print("(", num, "'th'", ")")
        else:
            ka = num % 10
            if ka == 1:
                print("(", num, "'st", ")")
            elif ka == 2:
                print("(", num, "'nd'", ")")
            elif ka == 3:
                print("(", num, "'rd'", ")")
            else:
                print("(", num, "'th'", ")")
        if num == 0:
            print("Terima kasih sudah menggunakan program saya")
            print("Elita Wahyu Firdasari - 065002200038")
            break
a = ordinal()
print(a)