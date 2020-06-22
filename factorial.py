# Define n factorial

def the_factorial(n):
	
	if(n == 1 or n == 0):
		return 1
	return n *  the_factorial(n-1)



