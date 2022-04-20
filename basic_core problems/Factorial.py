factorial_No = input("Enter a no to find factorial")

factNo = int(factorial_No)
i = 1
for i in range(1, factNo+1):
    factNo = i*i
    print(factNo)