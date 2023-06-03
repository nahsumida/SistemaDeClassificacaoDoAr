import numpy as np
from itertools import chain

#alfabeto
T=["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]

#chave da criptografia
A=[[4,1],[3,2]]

#inversa da chave
AInversa=[[A[1][1], -(A[0][1])],[-(A[1][0]), A[0][0]]]

matrix = np.array(A) 

#encontra a determinante da chave
det = np.linalg.det(matrix)
det = round(det)

#conjunto z26
Z26 = [[1,1],[3,9],[5,21],[7,15],[9, 3], [11,19], [15, 7],[17,23],[19, 11], [21,5], [23, 17], [25,25]]

#encontra o determinante da chaveInversa
detInversa = 0
for i in range(len(Z26)):
	if Z26[i][0] == det:
		detInversa = Z26[i][1]
		

#multipica a chave inversa pela sua determinante
for i in range(len(AInversa)):
	AInversa[i][0] *= detInversa
	AInversa[i][1] *= detInversa
	


#Palavra a ser descriptografada
Palavra = "SAKNOXAOJX"
	
#criacao da matriz P baseada nos indices da T
common = []
for i in range(len(Palavra)): 
	for j in range(len(T)):
		if Palavra[i] == T[j]:
			common.append(j) 
pLinha1 = []
pLinha2 = []
P = []
		
for i in range(len(common)): 
	if i % 2 == 0:
		pLinha1.append(common[i])
	if i % 2 > 0: 
		pLinha2.append(common[i])
		


#matriz P
P.append(pLinha1)
P.append(pLinha2)

#P = AInversa * C
resultado = np.dot(AInversa, P)
	
for i in range(len(resultado)):
	for j in range(len(resultado[i])):
		val = resultado[i][j]
		if val > 0:
			resultado[i][j] = val%26
		if val < 0:
			while val < 0: 
				val += 26
			resultado[i][j] = val
			
linha1 = resultado[0]
linha2 = resultado[1]
res = list(chain.from_iterable(zip(linha1, linha2)))

#encontra a palavra baseada em T
palavra = []
for i in res: 
	for j in range(len(T)):
		if i == j:
			palavra.append(T[j])

pFinal = "".join(palavra)

print (pFinal)
