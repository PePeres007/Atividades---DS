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
        def __init__(self, nome, peso, idade, raca):
            super().__init__(nome, peso, idade)
            self.raca = raca
 
dog1 = Dog(nome = "Totó", peso = 15.6, idade = 5, raca = "Vira-lata")
dog1.comer("ração")
dog1.comer("lixo")
dog1.verBucho()
dog1.digerir()
dog1.verBucho()
