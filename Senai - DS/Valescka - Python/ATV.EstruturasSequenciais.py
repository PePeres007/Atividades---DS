#Atividade Python 28/02/2024

#questão 1
print("alo mundo")

#questão 2
numero = int(input("Digite um número: "))
print(f"O número informado foi {numero}")

#questão 3
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = a + b
print("A soma: ", c)

#questão 4
a = float(input("Digite a sua nota: "))
b = float(input("Digite a sua outra nota: "))
c = float(input("Digite a sua nota: "))
d = float(input("Digite a sua outra nota: "))
e = (a+b+c+d)/4
print("A sua média é", e)

#questão 5
x = int(input("digite um numero em metros: "))
print("o numero digitado em centrimetros será: ", x*100)

#questão 6
a = float(input("Qual o raio do circulo?: "))
area = (a**2) * 3.14
print("A área do círculo é: ", area)

#questão 8
ganho = float(input("Quanto você recebe por hora? "))
hora = float(input("Quantas horas você trabalhou? "))
recebimento = hora * ganho
print("Você receberá ", recebimento)

#questão 9
F = float(input("Digite a temperatura em Fahrenheit: "))
C = 5 * ((F-32) / 9)
print("A temperatura em Celsius é: ", C)

#questão 10
C = float(input("Digite a temperatura em Celsius: "))
F = (C * 9/5) + 32
print("A temperatura em Fahrenheit é: ", F)

#questão 11
a = int(input("Digite um numero inteiro: "))
b = int(input("Digite outro numero inteiro: "))
c = float(input("Digite um numero real: "))
d = (a * 2) * (b / 2)
e = (a * 3) + c
f = c**3
print("O produto do dobro do primeiro com metade do segundo é: ", d)
print("A soma do triplo do primeiro com o terceiro é: ", e)
print("O terceiro elevado ao cubo é: ", f)

#questão 12
peso_peixes = float(input("Qual o peso dos peixes? "))

if peso_peixes > 50:
    excesso = peso_peixes - 50
    multa = excesso * 4
    print("O peso excedente é de", excesso, "kg")
    print("O valor da multa é de R$", multa)
else:
    print("O peso dos peixes está dentro do limite permitido.")

#questão 13
valor_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou no mês? '))

salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f'Salário bruto: R${salario_bruto:.2f}')
print(f'IR (11%): R${ir:.2f}')
print(f'INSS (8%): R${inss:.2f}')
print(f'Sindicato (5%): R${sindicato:.2f}')
print(f'Descontos: R${descontos:.2f}')
print(f'Salário líquido: R${salario_liquido:.2f}')

