import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = (b * b) - (4 * a * c)

print('delta wynosi: ',delta)

if delta > 0:
    x1 = -b - math.sqrt(delta) / (2 * a)
    x2 = -b + math.sqrt(delta) / (2 * a)

    print("x1 = ", x1)
    print("x2 = ", x2)

else:
    if delta == 0:
        x = -b / (2 * a)
        print("x = ", x)
    else:
        print("brak miejsc zerowych")






