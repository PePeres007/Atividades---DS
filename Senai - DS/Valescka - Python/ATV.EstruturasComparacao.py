#questão 1
a = int(input("Digite um valor: "))
if a > 0:
  print("O valor digitado é positivo")
else:
  print("O valor digitado é negativo")

#questão 2
a = input("Digite F ou M: ")
if a == "F":
  print("Feminino")
elif a == "M":
  print("Masculino")
else:
  print("Sexo Inválido")

#questão 3
a = input("Digite uma letra: ")
if a == "a" or a == "e" or a == "i" or a == "o":
  print("é uma vogal :)")
else:
  print("é uma consoante :(")

#questão 4
notaUm = float(input("Digite a primeira nota: "))
notaDois = float(input("Digite a segunda nota: "))
media = (notaUm + notaDois) / 2

if media >= 7 and media < 10:
  print("Aprovado")
elif media < 7:
  print("Reprovado")
elif media == 10:
  print("Aprovado com Distinção")

#questão 5
nUm = float(input("Digite o primeiro número: "))
nDois = float(input("Digite o segundo número: "))
nTres = float(input("Digite o terceiro número: "))

if nUm > nDois and nUm > nTres:
  print("O maior número é: ", nUm)
elif nDois > nUm and nDois > nTres:
  print("O maior número é: ", nDois)
elif nTres > nUm and nTres > nDois:
  print("O maior número é: ", nTres)

#questão 6
nUm = float(input("Digite o primeiro número: "))
nDois = float(input("Digite o segundo número: "))
nTres = float(input("Digite o terceiro número: "))

if nUm < nDois and nUm < nTres:
  print("O menor número é: ", nUm)
elif nDois < nUm and nDois < nTres:
  print("O menor número é: ", nDois)
elif nTres < nUm and nTres < nDois:
  print("O menor número é: ", nTres)

#questão 7
preco1 = float(input('Informe o preço do primeiro produto: '))
preco2 = float(input('Informe o preço do segundo produto: '))
preco3 = float(input('Informe o preço do terceiro produto: '))

if preco1 <= preco2 and preco1 <= preco3:
    print('Você deve comprar o primeiro produto, que custa R${:.2f}.'.format(preco1))
elif preco2 <= preco1 and preco2 <= preco3:
    print('Você deve comprar o segundo produto, que custa R${:.2f}.'.format(preco2))
else:
    print('Você deve comprar o terceiro produto, que custa R${:.2f}.'.format(preco3))

#questão 8
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 >= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)

#questão 9
salario = float(input('Informe o salário do colaborador: R$ '))

if salario <= 280:
    aumento = salario * 0.2
elif salario <= 700:
    aumento = salario * 0.15
elif salario <= 1500:
    aumento = salario * 0.1
else:
    aumento = salario * 0.05

novo_salario = salario + aumento

print('Salário antes do reajuste: R${:.2f}'.format(salario))
print('Percentual de aumento aplicado: {:.0f}%'.format(aumento * 100))
print('Valor do aumento: R${:.2f}'.format(aumento))
print('Novo salário, após o aumento: R${:.2f}'.format(novo_salario))

#questão 10
lado1 = float(input('Informe o primeiro lado do triângulo: '))
lado2 = float(input('Informe o segundo lado do triângulo: '))
lado3 = float(input('Informe o terceiro lado do triângulo: '))

if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print('Os lados informados não formam um triângulo.')
else:
    if lado1 == lado2 == lado3:
        print('O triângulo é equilátero.')
    elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')

