# wczytujący n-elementów ciągu i obliczający sumę wyrazów dodatnich i sumę wyrazów
# ujemnych 2bv1;
lista = []
s_plus = 0
s_minus = 0
print(" pisz kolejne elementy: ")
while abs(s_plus) <= 20 and abs(s_minus) <= 10:
    lista.append(float(input()))
    if lista[-1] > 10:
        s_plus = s_plus + lista[-1]
else:
    s_minus = s_minus + lista[-1]
print(lista)
print("suma elementów dodatnich: ", s_plus)
print("suma elementów ujemnych: ", s_minus)
