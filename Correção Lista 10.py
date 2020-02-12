'''
 
'''

'''
den = 2  #02
a = 0

for num in range(100,51,-4):
    a = a+num/den
    den = den+2

print("Valor de A:", a*5)
'''

'''
num1 = -10 #03
num2 = 20

for cont in range(100):
    if cont%2 == 0:
        print(num1)
        num1 = num1-20
    else:
        print(num2)
        num2 = num2+20
'''

'''
num = 10   #03 Forma diferente
sinal = -1

for cont in range(100):
    print(num*sinal)
    num = num+10
    sinal = sinal * -1
'''

lista = []  #05
cont_nome = 0

nome = input("Digite nome:")

while nome != "sair":
    lista.append(nome)
    nome = input("Digite nome:")
print("Lista:", lista)

nome_pesq = input("Nome que quer pesquisar:")

for nome in lista:
    if nome == nome_pesq:
        cont_nome = cont_nome+1

print("Quantidade de Vezes:", cont_nome)
