class Animal:
        def __init__(self, nome, peso, idade):
            self.nome = nome
            self.peso = peso
            self.idade = idade
            self.bucho = []
    
        def comer(self, alimento):
            print(f"{self.nome} comeu {alimento}.")
            self.bucho.append(alimento)
    
        def verBucho(self):
            print(self.bucho)
    
        def digerir(self):
            self.bucho.pop(0)
    
        def fazer_som(self, som):
            print(f"o cachorro faz {som}")
    
 
class Dog(Animal):
        def __init__(self, nome, peso, idade, raca_dog):
            super().__init__(nome, peso, idade)
            self.raca_dog = raca_dog
 
dog1 = Dog(nome = "Totó", peso = 15.6, idade = 5, raca_dog = "Vira-lata")
dog1.comer("ração")
dog1.comer("lixo")
dog1.verBucho()
dog1.digerir()
dog1.verBucho()
 
class Cat(Animal):
        def __init__(self, nome, peso, idade, raca_cat, personalidade):
            super().__init__(nome, peso, idade)
            self.raca_cat = raca_cat
            self.personalidade = personalidade
 
cat1 = Cat(nome = "Naninha", peso = 4, idade = 4, raca_cat = "Persa", personalidade = "Amável")
cat1.comer("petisco")
cat1.comer("cavalo")
cat1.verBucho()
