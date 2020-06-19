l = int(input("Ingrese un número para saber si es primo: "))

def is_prime(n):
	for i in range (2, n):
		if(n % i == 0 or n % i == n):
			return False
	return True

if(is_prime(l)):
	print("Es número primo")
else:
	print("No es primo")

