import math

t = input("Enter a no for t ")
t = int(t)
v = input("Enter a no for v ")
v = int(v)


def Wind_Chill():
    if abs(t) < 50 and (v > 120 or v < 3):
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.74) * math.pow(v, 0.16)
        print(w)
    else:
        print("no doesn't lie in t and v's range")


print(Wind_Chill())
