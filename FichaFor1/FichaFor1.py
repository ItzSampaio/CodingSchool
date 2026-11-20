def analisar_10_numeros():
    conta_maiores_iguais_10 = 0
    soma_inferiores_10 = 0

    for _ in range(10):
        num = int(input("Digite um número inteiro: "))
        if num >= 10:
            conta_maiores_iguais_10 += 1
        else:
            soma_inferiores_10 += num

    print(f"\nQuantidade de números iguais ou superiores a 10: {conta_maiores_iguais_10}")
    print(f"Soma dos números inferiores a 10: {soma_inferiores_10}")


def idade_e_peso_7_pessoas():
    total_pessoas = 7
    soma_idades = 0
    conta_mais_90kg = 0

    for i in range(total_pessoas):
        print(f"\nPessoa {i + 1}")
        idade = int(input("Idade: "))
        peso = float(input("Peso (kg): "))

        soma_idades += idade
        if peso > 90:
            conta_mais_90kg += 1

    media_idade = soma_idades / total_pessoas

    print(f"\nMédia das idades das 7 pessoas: {media_idade:.2f}")
    print(f"Quantidade de pessoas com mais de 90 kg: {conta_mais_90kg}")


def menu():
    while True:
        print("\n=== MENU EXERCÍCIOS FOR ===")
        print("1 - Ler 10 números (>= 10 e soma dos < 10)")
        print("2 - Idade e peso de 7 pessoas (média idades e > 90kg)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            analisar_10_numeros()
        elif opcao == "2":
            idade_e_peso_7_pessoas()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()