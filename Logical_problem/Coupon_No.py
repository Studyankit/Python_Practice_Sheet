import random


def Coupon_No():
    coupon_arr = []
    n = int(input("Enter a no"))

    for i in range(n):
        coupon_no = random.randint(1, 10)
        coupon_arr.append(coupon_no)
    print(coupon_arr)


print(Coupon_No())
