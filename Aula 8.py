'''
nomes = ["Ana", "João", "Maria", "Pedro"]
idades = [ 10,20,15,18]

cont = 0
while cont<4:
    print(nomes[cont], idades[cont])
    cont = cont + 1
'''
'''
#Exercício 1

num = []

cont = 0
vzs = 0
while cont<10:
    num.append(int(input("Digite um número:")))
    print(num)
    cont = cont+1

print(num[0])
print(num[9])

num1=int(input("Número:"))
cont = 0
while cont<10:
    if num1 == num[cont]:
        vzs = vzs + 1
    cont = cont + 1
print("Número de vezes:", vzs)
'''
"""
#Exercício 2

nomes = []
cont = 0
el = 0
nome = input("Nome:")
while nome != "sair":
    nomes.append(nome)
    nome = input("Nome:")

print(nomes)

nomeEnc = input("Nome p/ contar:")

while cont < len(nomes):
    print(nomes[cont])
    if nomeEnc == nomes[cont]:
        el = el + 1
    cont = cont + 1
print(nomeEnc, "aparece", el, "vezes")
"""
"""
#Exercício 3

lista = []
cont = 0
soma = 0

num = float(input("Digite um numero: "))
while num > 0:
    lista.append(num)
    soma = soma + num
    cont = cont + 1
    num = float(input("Digite um numero: "))
    
    
print("Soma:", soma)

cont = len(lista) - 1
while cont >= 0:
    print(lista[cont])
    cont = cont - 1
"""
#Exercício 4
