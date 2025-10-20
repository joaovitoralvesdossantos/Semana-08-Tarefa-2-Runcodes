# Verifique se um número é ímpar ou par, e adiciona valores
def ehimparoupar(impar, par):
    if impar % 2 != 0:
        return impar + 8
    else:
        return par + 5
    
# Função principal    
def main():
    # entrada de dados
    numero = int(input("Digite um número inteiro: "))

    # Processamento
    resultado = ehimparoupar(numero, numero)
    
    # Saída de dados
    print("Resultado:", resultado)

# Chama a função principal
if __name__ == "__main__":
    main()