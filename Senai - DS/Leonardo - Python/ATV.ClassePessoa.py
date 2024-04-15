parada = False
class Pessoa:
        def __init__(self, id, nome, idade, altura, peso, genero):
            self.id = id
            self.nome = nome
            self.idade = idade
            self.altura = altura
            self.peso = peso
            self.genero = genero
    
            self.falando = False
            self.andando = False
            self.dormindo = False
            self.comendo = False
        def falar(self, fala):
            if not self.comendo and not self.dormindo:
                self.falando = True
                print(f"A pessoa está falando: {fala}")
            else:
                print("Essa pessoa está comendo ou dormindo nesse momento")
        def andar(self, destino):
            if not self.dormindo:
                self.andando = True
                print(f"A pessoa está andando para {destino}")
            else:
                print("Essa pessoa está dormindo nesse momento.")
        def dormir(self, lugar):
            if not self.falando and not self.andando and not self.comendo:
                self.dormindo = True
                print(f"A pessoa está dormindo em {lugar}.")
            else:
                print("Essa pessoa está falando ou andando ou comendo nesse momento")
        def comer(self, alimento):
            if not self.falando and not self.dormindo:
                self.comendo = True
                print(f"A pessoa está comendo {alimento}.")
            else:
                print("Essa pessoa está falando ou dormindo nesse momento")
    
        def parar_falar(self):
            if self.falando:
                self.falando = False
                print("Essa pessoa parou de falar.")
            else:
                print("A pessoa não está falando, então não pode parar de falar.")
        def parar_andar(self):
            if self.andando:
                self.andando = False
                print("Essa pessoa parou de andar.")
            else:
                print("A pessoa não está andando, então não pode parar de andar.")
        def parar_dormir(self):
            if self.dormindo:
                self.dormindo = False
                print("Essa pessoa parou de dormir.")
            else:
                print("A pessoa não está dormindo, então não pode parar de dormir.")
        def parar_comer(self):
            if self.comendo:
                self.comendo = False
                print("Essa pessoa parou de comer.")
            else:
                print("A pessoa não está comendo, então não pode parar de comer.")
 
pessoas = []
def adicionarP(pessoas):
    print("Digite as informações da pessoa:")
    id = int(input("Id: "))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    genero = str(input("Gênero: "))

    pessoa = Pessoa(id, nome, idade, altura, peso, genero)
    pessoas.append(pessoa)

def monitorar(id, pessoas):
    while True:

        print("----- Controle fisico -----\n"
            "digite 1 para comer | digite 5 para parar de comer\n"
            "digite 2 para falar | digite 6 para parar de falar\n"
            "digite 3 para andar | digite 7 para parar de andar\n"
            "digite 4 para dormir | digite 8 para parar de dormir\n"
            "        	Digite 9 para encerrar o código\n")

        escolha_menu = input("Digite a opção desejada: ")

        if escolha_menu == "1":
            comida = str(input("Insira o alimento que pessoa vai comer: "))
            pessoas[id - 1].comer(comida)

        elif escolha_menu == "2":
            fala = str(input("Insira o que pessoa vai falar: "))
            pessoas[id - 1].falar(fala)

        elif escolha_menu == "3":
            destino = str(input("Insira o destino da pessoa: "))
            pessoas[id - 1].andar(destino)

        elif escolha_menu == "4":
            dormir = str(input("Insira onde pessoa vai dormir: "))
            pessoas[id - 1].dormir(dormir)

        elif escolha_menu == "5":
            pessoas[id - 1].parar_comer()

        elif escolha_menu == "6":
            pessoas[id - 1].parar_falar()

        elif escolha_menu == "7":
            pessoas[id - 1].parar_andar()

        elif escolha_menu == "8":
            pessoas[id - 1].parar_dormir()

        elif escolha_menu == "9":
            break
 
 
r = int(input("""
==========MENU==========
1. Adicionar pessoa
2. Monitorar pessoa
3. Sair
r =>
"""))
 
if r == 1:
    try:
        adicionarP(pessoas)
    except:
        print("Valor inválido! Tente novamente.")
elif r == 2:
    try:
        escolha_id = int(input("Insira o id da pessoa que você quer monitorar: "))
        monitorar(escolha_id, pessoas)
    except:
        print("Valor inválido! Tente novamente.")
else:
        parada = True
