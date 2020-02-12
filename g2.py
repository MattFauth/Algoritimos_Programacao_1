## 1. (0.5) Apresente a saída (o que é impresso na tela) do programa a seguir:
num = 10

for cont in range(6):
	num = num + 10
	print(num)

## Resposta: (20, 30, 40, 50, 60, 70)

## 2. (1.0) Apresente a saída (o que é impresso na tela) do programa a seguir:
lista = [18.5,30,10,2,5]
soma = 0

for num in lista:
	if num < 10:
		soma = soma + num
print("Soma: ",soma)

for i in range(5):
	if i%2==0:
		lista[i] = lista[i] + 10
	else:
		lista[i] = 5
print(lista)

## Resposta: Soma: 7
## [28.5, 5, 20, 5, 15]

## 3. (1.0) Faça um programa que, considerando a série: 500, 490, 480, 470 ... 10, imprima:
## A. Todos os termos da série, na ordem que foram apresentados;
## B. A soma dos termos menores que 200;
## **Use o comando for para resolver esta questão.

num = 0
for num in range(500,9,-10):
	print(num)

	if num < 200:
		soma = soma + num

print(soma)

## 4. (1.5) Faça um programa que leia 100 números inteiros e guarde em uma lista. Apresente:
## A. A média dos 20 últimos elementos;
## B. A posição de cada elemento maior que 10;
## C. Se existe algum elemento ímpar na lista
## **Apresente a mensagem: '"Existe número ímpar" ou "Não existe número ímpar"'.

soma = 0
listaNum = []
cont = 0
while cont < 100:
	num = int(input("Número: "))
	listaNum.append(num)

	while cont > 79:
		soma = soma + listaNum[cont]

	media = soma/20
	

## 5. (2.0) Faça um programa que leia o nome e a quantidade em estoque de um número indeterminado de produtos sendo que
## a leitura deverá ser encerrada quando o usuário digitar 0 (zero) ao lugar da quantidade em estoque. Os nomes e as
## quantidades de habitantes devem ser armazenados em duas lista, de forma que o índice corresponde ao código do
## produto. 
## Faça a leitura dos dados, determine e apresente (0.5):
## A. (0.5) Os nomes dos produtos que estão com menos de 10 unidades em estoque;
## B. (0.5) A maior quantidade em estoque;
## C. (0.5) O código dos produtos que possuem quantidade em estoque igual a maior quantidade.
##	**Use o comando for para resolver esta solicitação.
