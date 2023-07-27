x = "n"

while x !="y":

    if 1945 > 2:
        print("Bem vindo ao negas.py o melhor algoritimo que ta tendo.") 

    x = int(input("Informe um numero: "))


    if x > 0:
        print(f"É Positivo")

    elif x == 0:
        print(f"É zero")

    if x < 0: 
        print(f"É negativo")

    x = input("Deseja sair? \n y = SIM \n n = NÃO \n")
    if x == "Y" or x == "sim":
        x = "y"
    elif x == "N" or x == "não":
        x = "n"
