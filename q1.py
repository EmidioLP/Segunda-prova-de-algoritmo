#Questão 1

lista_n = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

print("O vetor normal é: ")
print(lista_n)

a1 = lista_n[0]
a2 = lista_n[1]
a3 = lista_n[2]
a4 = lista_n[3]
a5 = lista_n[4]
a6 = lista_n[5]
a7 = lista_n[6]
a8 = lista_n[7]
a9 = lista_n[8]
a10 = lista_n[9]


if (lista_n[0] == a1) == True:
	lista_n[0] = lista_n[19]
	lista_n[19] = a1

if (lista_n[1] == a2) == True:
	lista_n[1] = lista_n[18]
	lista_n[18] = a2

if (lista_n[2] == a3) == True:
	lista_n[2] = lista_n[17]
	lista_n[17] = a3
	
if (lista_n[3] == a4) == True:
	lista_n[3] = lista_n[16]
	lista_n[16] = a4
	
if (lista_n[4] == a5) == True:
	lista_n[4] = lista_n[15]
	lista_n[15] = a5
	
if (lista_n[5] == a6) == True:
	lista_n[5] = lista_n[14]
	lista_n[14] = a6
	
if (lista_n[6] == a7) == True:
	lista_n[6] = lista_n[13]
	lista_n[13] = a7
	
if (lista_n[7] == a8) == True:
	lista_n[7] = lista_n[12]
	lista_n[12] = a8
	
if (lista_n[8] == a9) == True:
	lista_n[8] = lista_n[11]
	lista_n[11] = a9

if (lista_n[9] == a10) == True:
	lista_n[9] = lista_n[10]
	lista_n[10] = a10

print("O vetor modificado é: ")
print(lista_n)




