import math

x = float(input("Введіть число х: "))

def f1(x1):
    rez = math.pow(3,x-4)+math.log(x)+math.log(x)
    return(rez)
def f2(x2):
    rez = x**2 + math.sin(2*x)
    return(rez)
def f3(x3):
    rez = 2 + 2,7 * x**2
    return(rez)

y = 0.0

if x >= 6:
    y = f1(x)
elif -1 < x < 6:
    y = f2(x)
elif x <= f3(x):
    y = f3(x)

print(y)