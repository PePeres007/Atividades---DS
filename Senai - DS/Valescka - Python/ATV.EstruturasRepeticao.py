#questão 1
a = int(input("Digite uma nota de 0 a 10: "))
while a < 0 or a > 10:
  print("Número inválido")
  a = int(input("Digite uma nota de 0 a 10: "))
print("Número válido")

#questão 2
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
while usuario == senha:
  print("Erro!, A senha que você digitou não pode ser igual ao nome de usuário")
  usuario = input("Digite seu nome de usuário: ")
  senha = input("Digite sua senha: ")
print("Cadastro realizado com sucesso!")

#questão 3
for i in range(1,21):
  print(i)


for i in range(1,21):
  print(i, end=" ")

#questão 4
maior = 0

for i in range(5):
  num = float(input("Digite um número: "))
  if num > maior:
    maior = num

  else:
    maior = maior
print("O maior número é:", maior)

#questão 5
soma = 0
for i in range(5):
  num = int(input("Digite um número: "))
  soma += num

media = soma / 5
print("A soma dos números é: ", soma)
print("A média dos números é: ", media)

#questão 6
for i in range(50):
  if i%2 >= 1:
    print(i)

#questão 7
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um outro número inteiro: "))
soma = 0
for i in range(num1+1,num2):
  print(i)
  soma = soma + i
print(soma)

#questão 8
numUm = int(input("Digite um número: "))

for i in range(1,11):
  print(numUm * i)

#questão 9
base = int(input("Digite o número da base: "))
expoente = int(input("Digite o número do expoente: "))

print(base ** expoente)

#questão 10
count_par = 0
count_impar = 0

for i in range(10):
  num = int(input("digite um numero: "))
  if num % 2 == 0:
    count_par += 1
  else:
    count_impar += 1

print("A quantidade de numeros pares é:", count_par)
print("A quantidade de numeros impares é:", count_impar)

#questão 11
n = int(input("Digite a quantidade de termos: "))
f1 = 0
f2 = 1
if n <= 1:
  print("Quantidade invalida")
else:
  print("Sequencia de Fibonacci:")
  for i in range(n):
    print(f1)
    f3 = f1 + f2
    f1 = f2
    f2 = f3

#questão 12
f1 = 0
f2 = 1
while f1 <= 500:
  print(f1)
  f3 = f1 + f2
  f1 = f2
  f2 = f3

#questão 13
num = int(input("Digite um número inteiro: "))

fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print("O fatorial de", num, "é", fatorial)