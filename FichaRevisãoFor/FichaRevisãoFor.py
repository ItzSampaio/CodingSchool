import random


def menor_maior_altura():
    menor = None
    maior = None

    for i in range(15):
        altura = float(input(f"Altura da pessoa {i + 1} (em cm ou m): "))

        if menor is None or altura < menor:
            menor = altura
        if maior is None or altura > maior:
            maior = altura

    print(f"\nMenor altura do grupo: {menor}")
    print(f"Maior altura do grupo: {maior}")


def analisar_valores():
    total = 20
    soma = 0
    positivos = 0
    negativos = 0

    for i in range(total):
        valor = float(input(f"Introduza o {i + 1}.º valor: "))
        soma += valor

        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1

    media = soma / total
    perc_positivos = (positivos / total) * 100
    perc_negativos = (negativos / total) * 100

    print(f"\nMédia aritmética: {media:.2f}")
    print(f"Quantidade de valores positivos: {positivos} ({perc_positivos:.2f}%)")
    print(f"Quantidade de valores negativos: {negativos} ({perc_negativos:.2f}%)")


def estacao_meteorologica():
    dias = 7
    soma_temp = 0
    dias_acima_25 = 0

    for dia in range(dias):
        temp = float(input(f"Temperatura do dia {dia + 1} (°C): "))
        soma_temp += temp

        if temp > 25:
            dias_acima_25 += 1

    media_temp = soma_temp / dias

    print(f"\nTemperatura média: {media_temp:.2f} °C")
    print(f"Dias com temperatura superior a 25 °C: {dias_acima_25}")

    if media_temp > 20:
        print("A temperatura média foi superior a 20 °C.")
    elif media_temp < 20:
        print("A temperatura média foi inferior a 20 °C.")
    else:
        print("A temperatura média foi exatamente 20 °C.")


def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 10

    print("\nTenta adivinhar o número secreto entre 1 e 100 (tens 10 tentativas).")

    for tentativa in range(1, tentativas + 1):
        palpite = int(input(f"Tentativa {tentativa}/{tentativas}: "))

        if palpite == numero_secreto:
            print("Parabéns! Acertaste!")
            return
        elif palpite < numero_secreto:
            print("O número secreto é maior")
        else:
            print("O número secreto é menor")

    print(f"Perdeste! O número secreto era {numero_secreto}.")


def menu():
    while True:
        print("\n=== MENU DE EXERCÍCIOS ===")
        print("1 - Menor e maior altura (15 pessoas)")
        print("2 - Análise de 20 valores")
        print("3 - Estação meteorológica (7 dias)")
        print("4 - Adivinhar o número secreto (1 a 100)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menor_maior_altura()
        elif opcao == "2":
            analisar_valores()
        elif opcao == "3":
            estacao_meteorologica()
        elif opcao == "4":
            adivinhar_numero()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()