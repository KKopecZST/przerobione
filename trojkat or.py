a = float(input(" podaj długość a ="))
b = float(input(" podaj długość b ="))
c = float(input(" podaj długość c ="))
if a > 0 and b > 0 and c > 0:
    if a ** 2 == b ** 2 + c ** 2:
        if a**2 ==b ** 2+ c ** 2 or b**2 == a ** 2 or c**2 == b**2 == a**2+b**2:
         print(" Liczby mogą być długosciami trójkąta prostokątnego: ")
    elif b ** 2 == a ** 2 + c ** 2:
        print(' Liczby mogą być długościami')
    elif c ** 2 == a ** 2 + b ** 2:
        print(" Liczby mogą być długościami")
    else:
        print(" Liczby nie mogą być długościami boków ")
else:
    print(" Liczby nie mogą być długo muszą być dodatnie")
