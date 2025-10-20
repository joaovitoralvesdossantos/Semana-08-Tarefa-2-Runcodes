# Verifica se o numero é divisível
def numero(n):
    if n % 3 == 0 and n % 5 == 0: 
       return "FIZZBUZZ!! Esse número é divisível por 3 e 5"
    elif n % 3 == 0:
        return "FIZZ!! Esse numero é divisível por 3"
    elif n % 5 == 0:
        return "BUZZ!! Esse número é divisível por 5"
    else:
        return f"O número {n} não é divisível por 3 nem por 5"
    

# função principal
def main():
    # entrada de dados
    valor = int(input("Digite um número inteiro: "))

    # processamento
    resultado = numero(valor)

    # saída de dados
    print(resultado)

# chama a função principal
if __name__ == "__main__":
    main()