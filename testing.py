from random import randint
n = randint(0,1)
print(f"Am I the master? {'Yes' if n == 1 else 'No'}")
for i in range(1,11):
	print(f'We are square: {i*i}')

print("There's a method to the madness.")