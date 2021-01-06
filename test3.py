from colorama import init, Fore, Style, Back
init (autoreset=True)
n1 = ( input ( 'Please enter the number 1 : '))
while type(n1) != int:
    try:
        n1 = int(n1)
    except ValueError:
        print("Type Error!")
        n1 = input('Please enter the number 1 : ') 
n2 = ( input ( 'Please enter the number 2 : '))
while type(n2) != int:
    try:
        n2 = int(n2)
    except ValueError:
        print("Type Error!")
        n2 = input("Please enter the number 2 : ")
n3 = ( input ( 'Please enter the number 3 : '))
while type(n3) != int:
    try:
        n3 = int(n3)
    except ValueError:
        print("Type Error!")
        n3 = input("Please enter the number 3 : ")
n4 = ( input ( 'Please enter the number 4 : '))
while type(n4) != int:
    try:
        n4 = int(n4)
    except ValueError:
        print("Type Error!")
        n4 = input("Please enter the number 4 : ")
n5 = ( input ( 'Please enter the number 5 : '))
while type(n5) != int:
    try:
        n5 = int(n5)
    except ValueError:
        print("Type Error!")
        n5 = input("Please enter the number 5 : ")
n6 = ( input ( 'Please enter the number 6 : '))
while type(n6) != int:
    try:
        n6 = int(n6)
    except ValueError:
        print("Type Error!")
        n6 = input("Please enter the number 6 : ")
n7 = ( input ( 'Please enter the number 7 : '))
while type(n7) != int:
    try:
        n7 = int(n7)
    except ValueError:
        print("Type Error!")
        n7 = input("Please enter the number 7 : ")
m= [(n1), (n2), (n3), (n4), (n5), (n6), (n7)]
print ( Back.WHITE + Fore.RED + 'You entered:' + Back.WHITE + Fore.RED +str(m))
ans=bool(input('Press "Enter" for sorting')) 
b=[]
for i in m:
    if i%3==0:
       b.append(i)
print (str (Fore.BLACK + Back.WHITE + str (b)))
print ('The numbers are sorted multiples of 3')
input ()