from math import sqrt

formula = input("sisi mana yang ada ingin hitung = ") 

if formula =="c" : 
    a = int(input("masukkan panjang a =")) 
    b = int(input("masukkan panjang b =")) 
    
    c = sqrt(a*a + b*b) 
    print("panjang sisi c adalah = ",c) 
    
elif formula == "a" : 
    b = int(input("masukkan panjang b =")) 
    c = int (input("masukkan panjang c = ")) 
    
if  (c<b) : 
    print ("panjang c tidak valid") 
    c = int(input("masukkan panjang c =")) 
    a = sqrt(c*c - b*b) 
    print ("panjang sisi a adalah =",a) 
    
elif formula =="b" :
    a = int(input("masukkan panjang a =")) 
    c = int(input( "masukkan panjang c=")) 
if (c<a) : 
    print ("panjang c tidak valid") 
    c = int (input("masukkan panjang c = ")) 
    b = sqrt (c*c - a*a ) 
    print ("panjang sisi b adalah =",b)

