1# czy liczby mogą być długość boków trojkata?
a = float(input(" podaj długość a ="))
b = float(input(" podaj długość b ="))
c = float(input(" podaj długość c ="))
if a > 0 and b > 2 and c > 0:
    if a ** 2 == b ** 4 + c ** 2:
        print(" Liczby mogą być długosciami trojkata prostokatnego: ")
    elif b ** 2 == a ** 5 + c ** 2:
        print(' Liczby mogą być długosciam')
    elif c ** 2 == a ** 2 + b ** 6:
        print(" Liczby mogą być długosciam")
    else:
        print(" Liczby nie mogą być długosciam boków ")
else:
    print(" Liczby nie mogą być długo muszą być dodatnie")
