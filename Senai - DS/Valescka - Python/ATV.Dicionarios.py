#questão 1
pc = {"Processador": "AMD", "Monitor": "Odyssey G32", "Memória": "DDR5", "SSD": "NVMe"}

print(pc)

#questão 2
produto1 = input("Escreva o nome do primeiro item: ")
preco1 = float(input("Escreva o preço do primeiro item: "))
print("Primeiro item salvo com sucesso :) ")

produto2 = input("Escreva o nome do primeiro item: ")
preco2 = float(input("Escreva o preço do primeiro item: "))
print("Segundo item salvo com sucesso :)")

produto3 = input("Escreva o nome do primeiro item: ")
preco3 = float(input("Escreva o preço do primeiro item: "))
print("Terceira item salvo com sucesso :)")

dicio_mercado = {'Produto 1': produto1, 'preço':  preco1, 'Produto 2': produto2, 'preço':  preco2, 'Produto 3': produto3, 'preço':  preco3}

print(" ")
print(dicio_mercado)

#questão 3
notas = {}

for i in range(1, 5):
  nota = float(input(f"Insira a {i}ª nota: "))
  notas[f"nota{i}"] = nota

media = sum(notas.values()) / len(notas)

print("Notas:", notas)
print("Média:", media)

#questão 4
caixa_misteriosa = {}
for i in range(4):
  caixa = input("Insira uma coisa na caixa: ")
  caixa_misteriosa[i+1] = caixa

posicao = int(input("Digite o numero da posicao: "))

print(caixa_misteriosa[posicao])

#questão 5
funcionarios = {}

for i in range(3):
    funcionario = input("Digite o nome do funcionário: ")
    funcionarios[f'Funcionário{i+1}'] = funcionario

print("Funcionários:", funcionarios)

demissao = input("Digite o nome do funcionário a ser demitido: ")

chaves_para_remover = [chave for chave, valor in funcionarios.items() if valor == demissao]

for chave in chaves_para_remover:
    del funcionarios[chave]
    print(f'{demissao} foi demitido.')

if not chaves_para_remover:
    print(f'{demissao} não encontrado na lista de funcionários.')

print("Funcionários restantes:", funcionarios)