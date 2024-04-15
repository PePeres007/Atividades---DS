sn = "N"
while sn == "N" or sn == "n":
    x = []
    
    def imprimir_numero(num):
        for i in range(1, 11):
            y = i
            num.append(y)
        print(num)

    def imprimir2(num, a):
            for i in range(1, a + 1):
                y = i
                num.append(y)
            print(num)
                
r = str(input("Deseja imprimir os números de 1 a 10?\n S ou N: "))
if r == "S" or r == "s":
    imprimir_numero(x)
elif r == "N" or r == "n":
    y = int(input("Insira um número aee: "))
    imprimir2(x, y)
else:
    print("Resposta invalida, recomece o programa.")
sn = str(input("Você deseja parar o programa?\n S ou N: "))
if sn == "s" or "S" and sn != "N" or "n":
    sn = "s"
elif sn == "N" or "n":
    sn = "N"
else:
    print("Opção ivalida, tente novamente. ;~;")
    sn = "n"