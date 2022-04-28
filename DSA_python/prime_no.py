def primes(x=0, y=1000):
    for num in range(x, y + 1):
        if num > 1:  # num should be greater than 1
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    print(num)


primes()

# def get_prime_nos(x: int = 0, y: int = None):
#     if not y:
#         y = int(input("insert max range to get prime nos: "))
#     return primes(x, y)
