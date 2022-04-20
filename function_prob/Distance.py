import math


def Eucledian_dist(x_coordinate, y_coordinate, x_origin= 0, y_origin=0):
    dist = math.sqrt(math.pow(y_coordinate - y_origin, 2) + math.pow(x_coordinate - x_origin, 2))
    print(dist)


print(Eucledian_dist(4, 5))
