def pesoideal(altura, sexo):
    if sexo == "1":
        return (72.7 * altura) - 58
    elif sexo == "2":
        return (62.1 * altura) - 44.7
    
def main():

    # entrada de dados
    altura = float(input("Digite sua altura em metros: "))
    sexo = input("Digite seu sexo (1 = Homem, 2 = Mulher: ")
                 
    # processamento
    peso = pesoideal(altura, sexo)
    
    # saída de dados
    print(f"Seu peso ideal é: {peso:.2f} KG")
    
# chama a função principal
if __name__ == "__main__":
    main()