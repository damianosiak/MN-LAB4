import matplotlib.pyplot as plt
import numpy as np

n = int(input("Podaj wartosc n: "))
h = float(input("Podaj wartosc skoku h: "))

x = np.zeros(n)
y = np.zeros(n)

x[0] = float(input("Podaj wartosc x0: "))
y[0] = float(input("Podaj wartosc y0: "))

a = float(input("Podaj wartosc a: "))
b = float(input("Podaj wartosc b: "))

print("Wybierz format funkcji F(x, y):")
print("1. F(x, y) = a*x + b*y")
print("2. F(x, y) = a*x - b*y")
print("3. F(x, y) = a*x * b*y")
print("4. F(x, y) = a*x / b*y")
wybor = int(input("Twoj wybor: "))


def funkcja(a, b, x, y, wybor):
    if wybor == 1:
        return (a * x) + (b * y)
    elif wybor == 2:
        return (a * x) - (b * y)
    elif wybor == 3:
        return (a * x) * (b * y)
    elif wybor == 4:
        return (a * x) / (b * y)


for i in range(1, n):
    x[i] = x[0] + i * h

for i in range(n-1):
    m1 = funkcja(a, b, x[i], y[i], wybor)
    m2 = funkcja(a, b, (x[i] + 0.5 * h), (y[i] + 0.5 * h * m1), wybor)
    m3 = funkcja(a, b, (x[i] + h), (y[i] - h * m1 + 2 * h * m2), wybor)
    y[i+1] = y[i] + h/6 * (m1 + 4 * m2 + m3)

for i in range(n):
    print(f"x{i} = {x[i]}, y{i} = {y[i]}")

plt.plot(x, y, 'ks',markerfacecolor='none')
plt.plot(x, y, 'r')
plt.xlabel("x")
plt.ylabel("y")
plt.title("MN-LAB3: metoda R-K rzedu 3")
plt.grid(True)
plt.show()

