'''l1 = list(range(5))
l2 = list(range(2,10))
l3 = list(range(3, 16, 3))

print(l1)
print(l2)
print(l3)

#Questão 1(Aula 09)
for num in range(15, 1501,5):
    print(num)
#Questão 2:
soma=0
cont=0
for num in range(15,1501,5):
    soma=soma+1
    cont=cont+1
print("Média :", soma/cont)

#Questão 03
s=0
x=int(input("x")
for termo in range(20, 1001, 10):
      s=s+termo*x
print("s :",s/100)

#Questão 5:
fat=1
numero=int(input("Número"))
for n in range(numero,1 ,-1):
    fat=fat*n
print(fat)

#Questão 6:
pot=1
x=int(input("x"))
y=int(input("y"))
for cont in range(y):
    pot=pot*x
print(pot)

#Questão 04:

s=0
den=8
for num in range(10,101,5)
    s=s+num/den
    den=den+s
print(s)
#ou
s=0
for numin range(10,101,5):
    s=s+num/(num-2)
print(s)

#Questão 15:
qt=0
lista=[]

for i in range(10):
    lista.append(input("Nome:"))
print(lista)

nome_pesq=input("nome que deve ser contado :")

for nome in lista:
    if nome==nome_pesq:
        qt=qt+1
print("Quantidade :", qt)

# Questão 14:

lista=[]

nome=input("nome :")
while nome!="sair":
    lista.append("nome :")
    nome=input("Nome :")
for n in lista:
    print(n)

#Questão 16:

G=[]
R=[]
acertos=0
for i in range(10):
    G.append(input("G:"))
print("G :" G)
for i in range(10):
    R.append(input("R :")
print("R :" , R)
print("Questões q o aluno errou :")
for i in range(10):
    if G[i]!=R[i]:
        print(i)
    else:
        acertos=acertos+1

'''
#Questão 17:
lista = []
for i in range(6):
   lista.append(input("Nome:"))
print(lista)

nomeExc = input("Nome que você quer excluir da lista:")
while nomeExc != "sair":
   while nomeExc in lista:
      lista.remove(nomeExc)
   print(lista)
   nomeExc = input("Nome que você quer excluir da lista:")
        






















































