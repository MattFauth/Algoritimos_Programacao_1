"""
#Exercicio 1
i = 0
menor = 0
media = 0
while i < 4:
    idade = float(input("Idade:"))
    sexo = int(input("Sexo(1 = Masculino; 2 = feminino:"))
    if idade >= 18:
        if sexo == 1:
            print("Deve se alistar")
            i = i + 1
            media = media + idade
        else:
            print("Nao Deve se alistar")
            i = i + 1
            media = media + idade
    else:
        print("Nao deve se alistar!")
        i = i + 1
        menor = menor + 1
        media = media + idade
print("Media:", media/4)
print("Qt. de menores:", menor)
"""
#Exercicio 2
valorT = 0
i = 1
while i > 0:
    qtP = float(input("Quantidade de produtos:"))
    valP = float(input("Valor unitario do produto:"))
    i = i*valP
    valTP = qtP * valP
    print("Valor do total do produto:", valTP)
print("Valor total do estoque:", valorT)
