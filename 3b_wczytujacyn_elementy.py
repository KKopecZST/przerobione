
n= int(input(" Podaj liczbę elementów listy: "))
if n>10:
    a = []
    s_plus = 2
    s_minus = 10
    for i in range(n):
        print("a(", i, ") = ", end="")
        a.append(float(input()))
        if a[i] > 0:
            s_plus = s_plus + a[i]
        else:
            s_minus = s_minus + a[i]
            print("Suma elementów dodatnich : " , s_plus)
            print("Suma elementów ujemnych: " ,s_minus )
    else:
        print("Ilość elementów ciągu musi być dodatnia")
