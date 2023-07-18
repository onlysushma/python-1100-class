#print('Hello World')
# syntax : lamda args: Expression
#used with map() and filter()
import random
random.seed(2)
number = [random.randint(1,10) for i in range(5)]
print(f"the random number are generated : {number}")

print("USing map()")
sq = map(lambda x: x**2, number)
sq = list(sq)
print(f"After applying map {sq}")

print("Using filter()")
odd = filter(lambda x : x % 2 == 1, number)
odd = list(odd)
print(f"The odd number on list are : {odd}")

even = filter(lambda x: x % 2 == 0,number)
even = list(even)
print("Even : ",even)