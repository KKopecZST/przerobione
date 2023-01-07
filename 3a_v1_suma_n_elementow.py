#obliczający sumę elementów ciągu n-elementowego;
a = [2, 7, -3, 5]
print(a)
s = 0
for element in a:
    s= s+element
    print(element)
    print(s)
    print(" ")
    input()
    print(" Suma wyliczona krok po kroku: ", s)
    print(" Suma wyznacza funkcje", sum(a))
