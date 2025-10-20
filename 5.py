# Calcula a média final e da o seu conceito e sua situação
def mediafinal(nota1, nota2, nota3, mediaex):
    media = (nota1 + (nota2 * 2) + (nota3 * 3) + mediaex) / 7

    if media >= 9.0:
        conceito = "A"
    elif media >= 7.5:
        conceito = "B"
    elif media >= 6.0:
        conceito = "C"
    elif media >= 4.0:
        conceito = "D"
    else:
        conceito = "E"

    if conceito in ("A", "B", "C"):
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return media, conceito, situacao

# Função principal
def main():

    # Entrada de dados
    matricula = input("Digite o número da sua matrícula: ")
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digite sua terceira nota: "))
    mediaex = float(input("Digite a média das nota: "))

    # Processamento
    media, conceito, situacao = mediafinal(nota1, nota2, nota3, mediaex)

    # Saída de dados
    print(f"\nSua Matrícula: {matricula}")
    print(f"Média final: {media:.2f}")
    print(f"Conceito: {conceito}")
    print(f"Situação: {situacao}")

    # Chama a função principal
if __name__ == '__main__':
    main()
