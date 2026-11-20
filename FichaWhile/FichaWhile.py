def media_altura_mais_50():
    pessoas_idade = 0
    soma_altura = 0.0

    idade = int(input("Idade (0 para sair): "))
    while idade != 0:
        altura = float(input("Altura (em m): "))
        if idade > 50:
            pessoas_idade += 1
            soma_altura += altura
        idade = int(input("Idade (0 para sair): "))

    if pessoas_idade > 0:
        media_altura = soma_altura / pessoas_idade
        print(f"\nA média da altura das pessoas com mais de 50 anos é: {media_altura:.2f}m")
    else:
        print("\nNão foram registadas pessoas com mais de 50 anos.")


def avaliacao_turma_while():
    aprovados = 0
    reprovados = 0
    maior_nota = 0.0
    menor_nota = 999999.0
    houve_alunos = 0

    nome = input("\nNome do aluno (FIM para terminar): ")
    while nome.upper() != "FIM":
        teste1 = float(input("Nota do Teste 1: "))
        teste2 = float(input("Nota do Teste 2: "))
        notafichas = float(input("Nota das fichas de trabalho: "))
        notaTA = float(input("Nota do trabalho da aula: "))

        media_testes = (teste1 + teste2) / 2
        nota_final = media_testes * 0.45 + notafichas * 0.40 + notaTA * 0.15

        houve_alunos += 1
        if nota_final > maior_nota:
            maior_nota = nota_final
        if nota_final < menor_nota:
            menor_nota = nota_final

        if nota_final >= 9.5:
            print(f"O/A {nome} está aprovad@ com a classificação de {nota_final:.1f}")
            aprovados += 1
        else:
            print(f"O/A {nome} está reprovad@ com a classificação de {nota_final:.1f}")
            reprovados += 1

        nome = input("\nNome do aluno (FIM para terminar): ")

    print(f"\nTotal de alunos aprovados: {aprovados}")
    print(f"Total de alunos reprovados: {reprovados}")

    if houve_alunos > 0:
        print(f"Maior nota final da turma: {maior_nota:.2f}")
        print(f"Menor nota final da turma: {menor_nota:.2f}")
    else:
        print("Não foram inseridos alunos.")


def analisar_numeros_while():
    soma_posi = 0.0
    soma_nega = 0.0
    total_numeros = 0

    num = float(input("Diz um número (0 para acabar): "))
    while num != 0:
        total_numeros += 1
        if num > 0:
            soma_posi += num
        elif num < 0:
            soma_nega += num
        num = float(input("Diz um número (0 para acabar): "))

    soma_total = soma_posi + soma_nega
    if total_numeros > 0:
        media = soma_total / total_numeros
    else:
        media = 0.0

    print(f"\nA soma dos números positivos é: {soma_posi:.2f}")
    print(f"A soma dos números negativos é: {soma_nega:.2f}")
    print(f"A soma de todos os números é: {soma_total:.2f}")
    print(f"A média dos números é: {media:.2f}")


def menu():
    while True:
        print("\n=== MENU EXERCÍCIOS CICLO WHILE ===")
        print("1 - Média da altura de pessoas com mais de 50 anos")
        print("2 - Avaliação de alunos até digitar FIM")
        print("3 - Soma e média de vários números até digitar 0")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            media_altura_mais_50()
        elif opcao == "2":
            avaliacao_turma_while()
        elif opcao == "3":
            analisar_numeros_while()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()