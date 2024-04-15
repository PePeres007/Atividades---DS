#questão 1

#questão 2
def fatorial(n):
  fat = 1
  for i in range(1, n + 1):
    fat *= i
  return fat

n = int(input("Digite o valor de n: "))
print(fatorial(n))

#questão 3
def verifica_primo(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

n = int(input("Digite o valor de n: "))
print(verifica_primo(n))

#questão 4
def inverte_string(s):
  invertida = ""
  for i in range(len(s) - 1, -1, -1):
    invertida += s[i]
  return invertida

s = input("Digite a frase ou palavra: ")
print(inverte_string(s))

#questão 5
def maior_valor(lista):
  maior = lista[0]
  for i in range(1, len(lista)):
    if lista[i] > maior:
      maior = lista[i]
  return maior

# Testes
lista = [10, 2, 3, 1, 5, 6]
print(maior_valor(lista))  # Saída: 10

lista = [-2, -5, -1, -3, -4]
print(maior_valor(lista))  # Saída: -1

#questão 6

#questão 5
def soma_quadrados(lista):
  soma = 0
  for i in range(len(lista)):
    soma += lista[i] ** 2
  return soma

# Testes
lista = [1, 2, 3, 4, 5]
print(soma_quadrados(lista))  # Saída: 55

lista = [-2, -5, -2, -3, -4]
print(soma_quadrados(lista))  # Saída: 55