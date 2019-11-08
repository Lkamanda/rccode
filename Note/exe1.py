import random


blue = random.randint(1,22)
print(blue)

red_list = []
for y in range(1,7):
    x = random.randint(1,33)
    if x in red_list:
        x = random.randint(1,33)

    red_list.append(x)

print(red_list)
