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

def gen_primes(k):
	counter = 2
	primes = []
	while(len(primes) != k):
		if(is_prime(counter)):
			primes.append(counter)
		counter += 1
			
	return primes

s = int(input("Cuántos números quiere usted generar: "))
print(gen_primes(s))

def gen_Prev_Primes(r):
	primes = []
	for i in range (0, r):
		if(is_prime(i)):
			primes.append(i)
	return primes


def twins(n):
	twins = []
	previus_List = gen_Prev_Primes(n)
	i = 1
	while(i < len(previus_List)):
		if(previus_List[i] -previus_List[i-1] == 2):
			twins.append((previus_List[i-1], previus_List[i]))
		i += 1
	return twins

o = int(input("Ingrese la que quiere saber de primos: "))
print(twins(o))




def break_primes(n):
	powers = ""
	if (is_prime(n)):	
		return n

	counter = 0
	primes = gen_Prev_Primes(n)
	seed = 0
	while(seed < len(primes)):
		if n % n/ primes[seed] == 0:
			n = n/ primes[seed]
			powers = powers + str(primes[seed])
		else:
			seed += 1
	return powers
		

s= int(input("Ingrese un numero para descomponerlo en potencias: "))
print(break_primes(s))


