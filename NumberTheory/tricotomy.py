# This is a commit
a = 5

print("La variable a: ", a, " es del tipo: ", type(a))
lista = [1,1,2,3,5,8,13]
tupla = (2,4,6,8)

print("Est es una lista", lista)
a = 54
b = 2
c = a % 2
print("El residuo de: ", a, " y ", b, " es: ", c)
v, b = 3.1, 4.2
print(type(v))
print("la suma de 3.1 y 4.3 es: ", v + b)


a = int( input("Ingrese un número para la tricotomía de los reales: "))


if(a > 0):
	print("El número ", a, " es positivo")
elif(a == 0):
	print("Eso es cero")
else:
	print("El número ", a, " es negativo")
