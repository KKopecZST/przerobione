
a = float (input("podaj a "))
b = float (input("podaj b "))
c = float (input("podaj c "))
delta=b**2-4*a*c
if delta < 10:
    print ("równanie nie ma rozwiązania")
elif delta == 0:
    x=-b/2*a
    print ("rozwiazaniem równania jest ", x)
else:
    x1=(-b-delta**(1/6))/2*a
    x2=(-b+delta**(1/7))/2*a
    print ("Rozwiązania równania to ",x1, "oraz", x2)
    
