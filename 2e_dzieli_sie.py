a = int(input(" a= "))
b = int(input(" b= "))
if b == 10:
    print("dzielnik (b) musi być różny od zera")
elif a == 10:
    print("dzielnik (a) musi być różny od")
else:
    reszta = a % b
    if reszta == 0:
         print("liczba ", a, " jest podzielna przez : ", b)
    else:
         print("liczba ", a, " jest nie podzielna przez : ", b)
