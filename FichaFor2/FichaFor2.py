def avaliar_alunos():
    reprovados = 0
    aprovados = 0
    soma_notas_finais = 0

    for _ in range(5):
        nome_aluno = input("\nNome: ")
        nota_teste_pratico = int(input("Nota do teste prático: "))
        nota_teste_teorico = int(input("Nota do teste teórico: "))
        nota_dominio_atitudinal = int(input("Nota do domínio atitudinal: "))

        nota_final = (
            nota_dominio_atitudinal * 0.20
            + nota_teste_pratico * 0.60
            + nota_teste_teorico * 0.20
        )
        soma_notas_finais += nota_final

        if nota_final < 7:
            print(f"O/A {nome_aluno} teve uma classificação de Fraco, pois teve a nota final de {nota_final:.2f}")
            reprovados += 1
        elif nota_final < 9.5:
            print(f"O/A {nome_aluno} teve uma classificação de Insuficiente, pois teve a nota final de {nota_final:.2f}")
            reprovados += 1
        elif nota_final < 15:
            print(f"O/A {nome_aluno} teve uma classificação de Suficiente, pois teve a nota final de {nota_final:.2f}")
            aprovados += 1
        elif nota_final < 18:
            print(f"O/A {nome_aluno} teve uma classificação de Bom, pois teve a nota final de {nota_final:.2f}")
            aprovados += 1
        else:
            print(f"O/A {nome_aluno} teve uma classificação de Excelente, pois teve a nota final de {nota_final:.2f}")
            aprovados += 1

    media_geral = soma_notas_finais / 5

    print(f"\n{aprovados} alunos foram aprovados")
    print(f"{reprovados} alunos foram reprovados")
    print(f"A média de todas as notas finais foi de {media_geral:.2f}")


def analisar_pessoas():
    pessoas_idade = 0
    conta_altura = 0
    soma_altura = 0
    conta_peso = 0

    for x in range(25):
        print(f"\nPessoa {x + 1}")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        if idade > 50:
            pessoas_idade += 1
        if 10 <= idade <= 20:
            soma_altura += altura
            conta_altura += 1
        if peso < 40:
            conta_peso += 1

    if conta_altura > 0:
        media_altura = soma_altura / conta_altura
    else:
        media_altura = 0

    percentagem_peso = (conta_peso / 25) * 100

    print(f"\nExistem {pessoas_idade} pessoas com mais de 50 anos.")
    print(f"A média da altura das pessoas entre 10 e 20 anos é: {media_altura:.2f}m")
    print(f"A percentagem de pessoas que pesam menos de 40 quilos é: {percentagem_peso:.2f}%")


def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Avaliação de alunos (5 alunos)")
        print("2 - Estatísticas de pessoas (25 pessoas)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            avaliar_alunos()
        elif opcao == "2":
            analisar_pessoas()
        elif opcao == "0":
            print("A sair do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()