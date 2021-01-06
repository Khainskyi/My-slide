#-*- coding: utf-8 -*-
a = ( input ('Введи число : '))
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print ("Неправильно ввели!")
        a = input("Введи число : ")
if a > 7:
	print ('Привет')
input ()
	