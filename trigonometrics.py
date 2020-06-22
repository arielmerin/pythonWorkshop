from factorial import the_factorial as fact
from decimal import Decimal

'''
Using Taylor's formula, computes an approximation to the value of cosine, given a point and order
'''
def cosine(point,order):
	aux = 0
	for i in range(order -1 ):
		aux = aux + ((-1)**i *(point**(2 * i)))/fact(2 * i)
	return Decimal(aux)


'''
Allows to reach the values for the approximation :) 
main poin in the script
'''
def run():
	print("Welcole to calculate Taylor's approximation for Cosine")
	order = int(input("Order: "))
	point = float(input('Point: '))
	print(cosine(point, order))

if __name__ == "__main__":
	run()
