harmonic_no = input("Enter a no to find it's harmonic series")

H_No = int(harmonic_no)

for i in range(1, H_No):
    h_No_series = 0
    h_No_series = h_No_series + (1 / i)
    if H_No != 0:
        print(f"{H_No} result is {h_No_series}")
    else:
        print("Enter a valid no")