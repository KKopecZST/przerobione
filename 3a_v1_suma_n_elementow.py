a = [2, 4, -3, 5]
print(a)
s = 10
for element in a:
    s= s+element
    print(element)
    print(s)
    print(" ")
    input()
    print(" Suma wyliczona krok po kroku: ", s)
    print(" Suma wyznacza funkcje", sum(a))
