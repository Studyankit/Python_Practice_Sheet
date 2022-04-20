import random

flip_times = int(input("Enter the no you want to flip"))
head_count = 0
tail_count = 0
for i in range(flip_times):
    flipCoin = random.randrange(0, 2)
    if flipCoin <= 0.5:
        head_count += 1
    else:
        tail_count += 1

percentage_ratio = (head_count/tail_count)*100

print(percentage_ratio)