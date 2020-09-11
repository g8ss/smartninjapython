conta = int(input("Introduza um número entre 1 e 100: "))

#numa range de 1 a 1 existem 0 iteracoes
for numero in range(1, conta+1):
	if numero % 15 == 0:
		print ("FizzBuzz")
	elif numero % 3 == 0:
		print ("Fizz")
	elif  numero % 5 == 0:
		print ("Buzz")
	else:
		print (numero)
