#-*- coding: utf-8 -*-
from colorama import init, Fore, Style, Back
#init ()
init (autoreset=True)
import datetime
d1_tarif = float (1.5)
d2_tarif = float (1.9)
d3_tarif = float (1.3)
grn = str ('$')
print (str ('Calculator v.2.0'))
d = datetime.date.today()
print (d)
print ( Fore.RED + 'Employee1' )
#Detail1
d1 = ( input ('Detail1 : '))
while type(d1) != int:
    try:
        d1 = int(d1)
    except ValueError:
        print ("Type Error!")
        d1 = input("Detail1 : ")
#Detail2
d2 = ( input ( 'Detail2 : '))
while type(d2) != int:
    try:
        d2 = int(d2)
    except ValueError:
        print("Type Error!")
        d2 = input("Detail2 : ") 
#Detail3    
d3 = ( input ( 'Detail3 : '))
while type(d3) != int:
    try:
        d3 = int(d3)
    except ValueError:
        print("Type Error!")
        d3 = input('Detail3 : ')
summ_1 = float (d1 * d1_tarif)
summ_2 = float (d2 * d2_tarif)
summ_3 = float (d3 * d3_tarif)
summ_4 = str (summ_1 + summ_2 + summ_3)
print (str (Fore.GREEN + ('Salary : ' + str (summ_4) + '$')))
#Employee2
print ( Fore.RED + 'Employee2' )
#Detail1
d1 = ( input ('Detail1 : '))
while type(d1) != int:
    try:
        d1 = int(d1)
    except ValueError:
        print ("Type Error!")
        d1 = input("Detail1 : ")
#Detail2
d2 = ( input ( 'Detail2 : '))
while type(d2) != int:
    try:
        d2 = int(d2)
    except ValueError:
        print("Type Error!")
        d2 = input("Detail2 : ")
#Detail3 
d3 = ( input ( 'Detail3 : '))
while type(d3) != int:
    try:
        d3 = int(d3)
    except ValueError:
        print("Type Error!")
        d3 = input('Detail3 : ')
summ_1 = float (d1 * d1_tarif)
summ_2 = float (d2 * d2_tarif)
summ_3 = float (d3 * d3_tarif)
summ_5 = str (summ_1 + summ_2 + summ_3)
print (str (Fore.GREEN + ('Salary : ' + str(summ_5) + '$')))
#Employee3
print ( Fore.RED + 'Employee3' )
#Detail1
d1 = ( input ('Detail1 : '))
while type(d1) != int:
    try:
        d1 = int(d1)
    except ValueError:
        print ("Type Error!!")
        d1 = input("Detail1 : ")
#Detail2
d2 = ( input ( 'Detail2 : '))
while type(d2) != int:
    try:
        d2 = int(d2)
    except ValueError:
        print("Type Error!")
        d2 = input("Detail2 : ")
#Detail3 
d3 = ( input ( 'Detail3 : '))
while type(d3) != int:
    try:
        d3 = int(d3)
    except ValueError:
        print("Type Error!")
        d3 = input('Detail3 : ')
d1_tarif = float (1.5)
d2_tarif = float (1.9)
d3_tarif = float (1.3)
summ_1 = float (d1 * d1_tarif)
summ_2 = float (d2 * d2_tarif)
summ_3 = float (d3 * d3_tarif)
summ_6= str (summ_1 + summ_2 + summ_3)
print (str (Fore.GREEN + ('Salary : ' + str(summ_6) + '$')))
total_summ = float(summ_4)+ float(summ_5) + float(summ_6)
print ( str (Fore.YELLOW + ( 'Total Salary : ' + str (total_summ) + '$')))
input ()