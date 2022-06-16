import string
import random

characters = list(string.digits)
print('0 will close the program if you want.')
print()
def generate_random_password():
	length = int(input("Enter password length: "))
	print()
	if length == 0:
		exit()
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	print("".join(password))
	print()	

while True:	
	generate_random_password()
