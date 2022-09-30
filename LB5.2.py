import math

x = float(input("X ="))
y = float(input("Y ="))
d = float(input("D ="))
r = d/2
h = math.sqrt(x  2 + y  2)
if h > r:
    print("Точка знаходиться за межами кола")
else:
    print("Точка належить кругу")
