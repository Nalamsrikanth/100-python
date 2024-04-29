
names = []
for i in range(5):
    name = input()
    names.append(name)
print(names)

import random
num = len(names)
random_name = random.randint(0, num-1)
print(f"{names[random_name]} is going to buy the meal today!")