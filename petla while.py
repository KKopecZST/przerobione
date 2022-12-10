a=[2, 7, -3, 5]
print(a)
n = int(input("Podaj liczbę elementów ciągu n= "))
a= []
s= 0
for i in range(n):
    print("a(", i, ") = ", end="")
    a.append(float(input()))
    print(a)
    print(" Suma wyliczeniowa kro po kroku", s)
    print(" Suma wyznaczona funkcja sum: ", sum(a))

