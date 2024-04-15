print("-----------------------------------------------------\n"
      "\t\t\tBEM VINDO AO BANCO FRADESCO!!\n"
      "-----------------------------------------------------\n")
titular = input("Digite o nome do titular da conta:\nR- ")
saldo = float(input("Digite o seu saldo:\nR-"))
limite = input("Digite o limite de sua preferencia:\nR- ")
numero = input("Digite o numero correspodente a sua conta:\nR- ")
status = False

class contaBancaria:
    def _init_(self, titular, saldo, limite, numero, status):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.numero = numero
        self.status = status

#-----------------------------------------------------------------------
    def visualizarSaldo(self):
        if self.status == True:
            print(f"{self.titular} Seja Bem Vindo.\n")
            print(f"{self.saldo} este é seu saldo Atual. \n")
        else:
            print(f"{self.titular}, sua conta está bloquada, ative ela antes de qualquer operação. ")
        input("Aperte ENTER para prosseguir.")

    def sacarSaldo(self):
        if self.status == True:
            saque = float(input("Quanto você quer sacar?\n"))
            if self.saldo > 0 and saque <= self.saldo:
                self.saldo -= saque
                print(f"Você sacou {saque}, seu saldo atua é: {self.saldo}")
            else:
                print("Saldo insuficiente")
        else:
            print(f"{self.titular}, sua conta está bloquada ou voce nao tem saldo suficiente")
        input("Aperte ENTER para prosseguir.")
        


    def depositarSaldo(self):
        if self.status == True:
            deposito = float(input("Quanto você quer depositar?\n"))
            self.saldo = self.saldo + deposito
            print(f"Você depositou {deposito}, seu saldo atua é: {self.saldo}")
        else:
            print(f"{self.titular}, sua conta está bloquada, ative ela antes de qualquer operação. ")
        input("Aperte ENTER para prosseguir.")


    def desbloquear(self):
        if self.status == False:
            escolhaDesbloqueio = input("Sua conta está bloqueada, deseja desbloquear?\nSim/Não\n")
            if escolhaDesbloqueio == "Sim" or "sim":
                self.status = True
                print("Sua conta foi desbloqueada")
            else:
                self.status = False
                print("Sua conta continua bloqueada")
        input("Aperte ENTER para prosseguir.")


    def mudarLimite(self):
        if self.status == True:
            r = str(input(
                f"O seu limite é {self.limite}"
                ""
                "Deseja alterar o limite? S ou N"
                "R => "
            ))
            if r == "N" or r == "n":
                f"Seu limite não foi alterado: {self.limite}"
            elif r == "S" or r == "s":
                novoLimite = int(input("Insira o novo limite: R$"))
                self.limite = novoLimite

        else:
            print(f"{self.titular}, sua conta está bloquada, ative ela antes de qualquer operação. ")
        input("Aperte ENTER para prosseguir.")

bancaria = contaBancaria(titular, saldo, limite, numero, status)

while True:

    print("Temos algumas opções, qual deseja?\n"
          "1 - Sacar\n"
          "2 - Depositar\n"
          "3 - Bloqueio\Desbloqueio\n"
          "4 - Verificar Saldo\n"
          "-------------------\n"
          "5 - Parar de executar\n")

    escolhaMenu = int(input("Digite a opção que deseja:\nR=  "))

    if escolhaMenu == 1:
        bancaria.sacarSaldo()

    elif escolhaMenu == 2:
        bancaria.depositarSaldo()

    if escolhaMenu == 3:
        bancaria.desbloquear()

    elif escolhaMenu == 4:
        bancaria.visualizarSaldo()

    if escolhaMenu == 5:
        break