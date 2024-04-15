#questão 1
idades = []
alturas = []

for i in range(5):
  idade = int(input("Digite sua idade: "))
  altura = float(input("Digite sua altura: "))
  idades.append(idade)
  alturas.append(altura)

print("Idades na ordem inversa:")
for idade in reversed(idades):
  print(idade)

print("Alturas na ordem inversa:")
for altura in reversed(alturas):
  print(altura)

#questão 2
import random

vetor_a = [random.randint(0, 10) for _ in range(10)]

soma_dos_quadrados = 0

for elemento in vetor_a:
  soma_dos_quadrados += elemento ** 2

print(vetor_a)
print(f"A soma dos quadrados dos elementos do vetor é: {soma_dos_quadrados}")

#questão 3
vetor_1 = []
vetor_2 = []
vetor_3 = []

for i in range(10):
  valor_1 = int(input("Digite o valor para o vetor 1: "))
  valor_2 = int(input("Digite o valor para o vetor 2: "))
  vetor_1.append(valor_1)
  vetor_2.append(valor_2)

for i in range(10):
  vetor_3.append(vetor_1[i])
  vetor_3.append(vetor_2[i])

print("Vetor 1:", vetor_1)
print("Vetor 2:", vetor_2)
print("Vetor 3:", vetor_3)

#questão 4
import random

vetor1 = [random.randint(0, 10) for _ in range(10)]
vetor2 = [random.randint(0, 10) for _ in range(10)]
vetor3 = [random.randint(0, 10) for _ in range(10)]

vetor4 = []

for i in range(10):
  vetor4.append(vetor1[i])
  vetor4.append(vetor2[i])
  vetor4.append(vetor3[i])

print(vetor1)
print(vetor2)
print(vetor3)
print(vetor4)

#questão 5
idades = []
alturas = []

for i in range(10):
  idade = int(input("Digite a idade do aluno: "))
  altura = float(input("Digite a altura do aluno: "))
  idades.append(idade)
  alturas.append(altura)

media_altura = sum(alturas) / len(alturas)

#alunos acima 13 anos abaixo media
x = 0

for i in range(10):
  if idades[i] > 13 and alturas[i] < media_altura:
    x += 1

print("Todas as idades dos alunos: ", idades)
print("Todas as alturas dos alunos: ", alturas)
print("A media das idades é: ", media_altura)
print(f"Existem {x} alunos com mais de 13 anos e altura inferior à média de altura.")