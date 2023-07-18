import random
random.seed(2)
number = [random.randint(1,10) for i in range(5)]
print(f"the random number are generated : {number}")

print("Calculating cube using while loop")
index = 0
cube = []
while index <len(number):
    c = number[index] ** 2
    cube.append(c)
    index = index + 1
print(cube)