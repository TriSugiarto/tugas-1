bilangan       =int  (input  ("masukan bilangan dimulai dari :"))
kelipatan      =int  (input  ("masukan kelipatan yang di inginkan :"))
sebanyak       =int  (input  ("masukan yang di inginkan :"))

d=0

print ("hasil :")
while(d <=sebanyak):
    if (bilangan % kelipatan) == 0:
        print(bilangan)
        bilangan+=1
        d+=1
    else:
        bilangan+=1
