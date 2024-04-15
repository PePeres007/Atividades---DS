#questão 1
class Quadrado:
     def __init__(self, lado):
         self.lado = lado

     def mudar_lado(self, novo_lado):
         self.lado = novo_lado

     def retornar_lado(self):
         return self.lado

     def calcular_area(self):
         return self.lado ** 2


meu_quadrado = Quadrado(5)
print("Lado do quadrado:", meu_quadrado.retornar_lado())
meu_quadrado.mudar_lado(7)
print("Novo lado do quadrado:", meu_quadrado.retornar_lado())
print("A área do quadrado é: ", meu_quadrado.calcular_area())

#questão 2
class Retangulo:
  def __init__(self, ladoA, ladoB):
    self.ladoA = ladoA
    self.ladoB = ladoB

  def mudar_valor(self):
    self.ladoA = int(input("Digite o lado A: "))
    self.ladoB = int(input("Digite o lado B: "))

  def retornar_valor(self):
    print("Lado A: ", self.ladoA)
    print("Lado B: ", self.ladoB)

  def calcular_area(self):
    area = self.ladoA * self.ladoB
    print("Área: ", area)

  def calcular_perimetro(self):
    perimetro = (self.ladoA * 2) + (self.ladoB * 2)
    print("Perímetro: ", perimetro)

retangulo1 = Retangulo(0, 0)
retangulo1.mudar_valor()
retangulo1.retornar_valor()
retangulo1.calcular_area()
retangulo1.calcular_perimetro()

#questão 3
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.altura += 0.5 * anos
    def engordar(self, peso):
        self.peso += peso
    def emagrecer(self, peso):
        self.peso -= peso
    def crescer(self, altura):
        self.altura += altura
pessoa1 = Pessoa(nome="João", idade=20, peso=70, altura=170)
print("Antes:")
print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
print("Peso:", pessoa1.peso)
print("Altura:", pessoa1.altura)

pessoa1.envelhecer()
pessoa1.engordar(5)
pessoa1.emagrecer(3)
pessoa1.crescer(2)

print("\nDepois:")
print("Nome:", pessoa1.nome)
print("Idade:", pessoa1.idade)
print("Peso:", pessoa1.peso)
print("Altura:", pessoa1.altura)

#questão 4
class ContaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

# Criação de uma conta corrente
conta = ContaCorrente(123, "João Silva", 1000)

# Alterar o nome do correntista
conta.alterarNome("Maria Souza")

# Depositar dinheiro
conta.deposito(500)

# Sacar dinheiro
conta.saque(200)

# Imprimir o saldo da conta
print(conta.saldo)