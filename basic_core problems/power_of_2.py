import math

power_N = input("Enter a no between 0 to 30")
N = int(power_N)

if N >= 0 and N < 31:
    for i in range(0, N):
        table_of_2 = pow(2, N)
        print(f"{table_of_2} is equal to power of 2^{N}")
        N=N-1
else:
    print("Enter a valid no in range of 0 - 31")