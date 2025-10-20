# Verifica se o número digitado é menor, maior que 100.000, e também numeros negativos
def somadosdigitos(numero):
    if numero >= 100000:
        return -1
    elif numero < 0:
        return -1
    else:
        return sum(int(digito) for digito in str(numero))

# Função principal
def main():
    # entrada de dados
    numero = int(input("Digite um número inteiro: "))
    
    # processamento
    resultado = somadosdigitos(numero)
    
    # saída de dados
    print(f"Resultado: " ,resultado)

# Chama a função principal
if __name__ == '__main__':
    main()
