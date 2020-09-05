from random import randint
n = randint(0,1)
print(f"Am I the master? {'Yes. I am the master.' if n == 1 else 'No. I am not the master.'}")
for i in range(1,11):
	print(f'We are square: {i*i}')
