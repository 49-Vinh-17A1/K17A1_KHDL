import math

x = float(input("Nhap vao x: "))

Ex = 1
n = 1
t = x

while math.fabs(t)>=0.0001:
    Ex += t
    n += 1
    t *= (x / n)

print("Gia tri gan dung cua e mu x la:", Ex)