#Questão 2

lista_n = [30,2,3,4,5,6,44,8,9,10,11,12,13,32,15,16,17,18,19,20,21,22,23,24,25]
print(lista2)

menor = 30
maior = 30
for i in range(len(lista2)):
	if lista_n[i]>maior:
		maior=lista_n[i]
	elif lista_n[i] < menor:
		menor=lista_n[i]
		
		
for i in range(len(lista_n)):
	if lista_n[i]==maior:
		print("Maior número é: {}".format(lista_n[i]))
		print("O índice do maior número é: {}".format(i))

for i in range(len(lista_n)):
	if lista_n[i]==menor:
		print("O menor número é: {}".format(lista_n[i]))
		print("O índice do menor número é: {}".format(i))
		
def media(l):
	soma=0
	for i in l:
		soma=i+soma
		m=soma/len(l)	
	return m
	
print("A média é: {}".format(media(lista_n)))

pad = 0 
for x in lista_n:
	p=(x-media(lista_n))**2
	pad+=p/(len(lista_n)-1)

print(pad**0.5)
	
