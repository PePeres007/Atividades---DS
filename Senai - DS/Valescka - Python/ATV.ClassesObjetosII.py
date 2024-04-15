#questão 1
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    def mostrar_endereco(self, endereco):
      print(self.endereco)

    def alterar_endereco(self, endereco):
      self.endereco = endereco
      print(self.endereco)


nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
endereco = input("Digite seu endereço: ")
pessoa = Pessoa(nome, idade, endereco)

escolha = int(input("Digite 1 para mostrar endereço ou 2 para alterar endereço: "))

if escolha == 1:
    pessoa.mostrar_endereco(endereco)

elif escolha == 2:
    pessoa.alterar_endereco(endereco)

#questão 2
class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self, curso):
      print(self.curso)

    def alterar_curso(self, novo_curso):
      self.curso = novo_curso


nome = input("Digite o nome do aluno: ")
matricula = int(input("Digite a matricula do aluno: "))
curso = input("Digite o curso do aluno: ")
aluno = Aluno(nome, matricula, curso)

escolha = int(input("Digite 1 para mostrar curso ou 2 para alterar curso: "))

if escolha == 1:
    aluno.mostrar_curso(curso)

elif escolha == 2:
    novo_curso = input("Digite o novo curso: ")
    aluno.alterar_curso(novo_curso)

#questão 3
class Aluno:
  def __init__(self, matricula, nome, nota1, nota2, nota3):
      self.matricula = matricula
      self.nome = nome
      self.nota1 = nota1
      self.nota2 = nota2
      self.nota3 = nota3

  def calcular_media(self):
      return (self.nota1 + self.nota2 + self.nota3) / 3

  def status_aprovacao(self):
      if self.calcular_media() >= 6:
          return "Aprovado"
      else:
          return "Reprovado"

alunos = []
for i in range(5):
  matricula = input("Matrícula do aluno {}: ".format(i+1))
  nome = input("Nome do aluno {}: ".format(i+1))
  nota1 = float(input("Nota da primeira prova do aluno {}: ".format(i+1)))
  nota2 = float(input("Nota da segunda prova do aluno {}: ".format(i+1)))
  nota3 = float(input("Nota da terceira prova do aluno {}: ".format(i+1)))
  alunos.append(Aluno(matricula, nome, nota1, nota2, nota3))

aluno_maior_media = max(alunos, key=lambda aluno: aluno.calcular_media())
print("Aluno com maior média geral:", aluno_maior_media.nome)


aluno_menor_media = min(alunos, key=lambda aluno: aluno.calcular_media())
print("Aluno com menor média geral:", aluno_menor_media.nome)

print("\nSituação de aprovação dos alunos:")
for aluno in alunos:
  print("Nome:", aluno.nome, "- Situação:", aluno.status_aprovacao())

#questão 4
class Horario:
  def __init__(self, hora, minuto, segundo):
    self.hora = hora
    self.minuto = minuto
    self.segundo = segundo

  def incrementar(self, segundos):
    self.segundo += segundos
    while self.segundo >= 60:
      self.segundo -= 60
      self.minuto += 1
    while self.minuto >= 60:
      self.minuto -= 60
      self.hora += 1

  def diferenca(self, outro_horario):
    segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo
    segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
    return segundos_self - segundos_outro

horario1 = Horario(10, 30, 0)
horario2 = Horario(11, 0, 0)

print("Horário 1:", horario1.hora, ":", horario1.minuto, ":", horario1.segundo)
print("Horário 2:", horario2.hora, ":", horario2.minuto, ":", horario2.segundo)

horario1.incrementar(3600)
print("Horário 1 após incremento:", horario1.hora, ":", horario1.minuto, ":", horario1.segundo)

diferenca = horario2.diferenca(horario1)
print("Diferença entre os horários:", diferenca, "segundos")

#questão 5
class Carro:
  def __init__(self, marca, ano, preco):
    self.marca = marca
    self.ano = ano
    self.preco = preco

  def mostrar_preco(self):
    print(f"O preço do carro é R${self.preco}")

  def exibir_dados(self):
    print(f"Marca: {self.marca}")
    print(f"Ano: {self.ano}")
    print(f"Preço: R${self.preco}")

# Criar um objeto da classe Carro
carro = Carro("Volkswagen", 2023, 100000)

# Mostrar o preço do carro
carro.mostrar_preco()

# Exibir os dados do carro
carro.exibir_dados()

#questão 6
class Tamagushi:
  def __init__(self, nome, fome, saude, idade):
    self.nome = nome
    self.fome = fome
    self.saude = saude
    self.idade = idade

  def alterar_nome(self, novo_nome):
    self.nome = novo_nome

  def alterar_fome(self, nova_fome):
    self.fome = nova_fome

  def alterar_saude(self, nova_saude):
    self.saude = nova_saude

  def alterar_idade(self, nova_idade):
    self.idade = nova_idade

  def retornar_nome(self):
    return self.nome

  def retornar_fome(self):
    return self.fome

  def retornar_saude(self):
    return self.saude

  def retornar_idade(self):
    return self.idade

  def retornar_humor(self):
    if self.fome < 3 and self.saude > 7:
      return "Feliz"
    elif self.fome > 5 and self.saude < 5:
      return "Triste"
    else:
      return "Neutro"

# Criar um objeto da classe Tamagushi
tamagushi = Tamagushi("Tama", 2, 8, 1)

# Alterar o nome do tamagushi
tamagushi.alterar_nome("cleitinho")

# Mostrar o nome do tamagushi
print(tamagushi.retornar_nome())

# Mostrar o humor do tamagushi
print(tamagushi.retornar_humor())

#questão 7
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.pop(0)

# Criar dois macacos
macaco1 = Macaco('Juca')
macaco2 = Macaco('Chico')

# Alimentar os macacos
macaco1.comer('banana')
macaco1.comer('maçã')
macaco2.comer('laranja')
macaco2.comer('pêssego')

# Ver o conteúdo do estômago dos macacos
macaco1.verBucho()
macaco2.verBucho()

# Digerir
macaco1.digerir()
macaco2.digerir()

# Tentar fazer um macaco comer o outro
macaco1.comer(macaco2)

# Ver o conteúdo do estômago do macaco que comeu o outro
macaco1.verBucho()