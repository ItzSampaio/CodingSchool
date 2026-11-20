def exercicio_1():
    print("\n--- Exercicio 1 ---")
    maior = 0
    menor = 9999999
    nome_aluno_max = ""
    nome_aluno_min = ""

    for x in range(8):
        nome_aluno = str(input("\nNome: "))
        idade = int(input("Idade: "))

        if idade < menor:
            menor = idade
            nome_aluno_min = nome_aluno
        if idade > maior:
            maior = idade
            nome_aluno_max = nome_aluno

    print(f"\n{nome_aluno_max} tem {maior} anos, sendo o/a mais velho(a).")
    print(f"{nome_aluno_min} tem {menor} anos, sendo o/a mais novo(a).")


def exercicio_2():
    print("\n--- Exercicio 2 ---")
    homens = 0
    mulheres = 0
    soma_pesos_ideais = 0.0

    while True:
        nome = input("\nNome (ou 'fim' para terminar): ")
        if nome.lower() == "fim":
            break

        genero = input("Género (M/F): ").lower
        altura = float(input("Altura em m: "))

        peso_ideal = 0
        if genero == "M":
            peso_ideal = (72.7 * altura) - 58
            homens += 1
        elif genero == "F":
            peso_ideal = (62.1 * altura) - 44.7
            mulheres += 1
        else:
            print("Género inválido. Use M ou F.")
            continue

        print(f"O peso ideal para {nome} é de {peso_ideal:.2f} kg.")
        soma_pesos_ideais += peso_ideal

    analisadas = homens + mulheres
    if analisadas > 0:
        media = soma_pesos_ideais / analisadas
        print("\nResumo:")
        print(f"Total de pessoas analisadas: {analisadas}")
        print(f"Quantidade de homens: {homens}")
        print(f"Quantidade de mulheres: {mulheres}")
        print(f"Média dos pesos ideais: {media:.2f} kg")
    else:
        print("\nNenhuma pessoa foi analisada.")


def Exercicio_3():
    print("\n--- Exercicio  3 ---")
    aprovados = 0
    reprovados = 0
    alunos = 0
    max_media = 0
    min_media = 999999.0

    opcao = "s"
    while opcao.lower() == "s":
        alunos += 1
        nome_aluno = str(input("\nNome do aluno: "))
        nota_1 = float(input("Valor da nota 1: "))
        nota_2 = float(input("Valor da nota 2: "))
        media = (nota_1 + nota_2) / 2

        if media < min_media:
            min_media = media
        if media > max_media:
            max_media = media

        if media >= 9.5:
            aprovados += 1
        else:
            reprovados += 1

        print(f"A média de {nome_aluno} é {media:.2f}")

        opcao = input("\nCalcular a média de outro aluno? (S/N): ")

    if alunos > 0:
        percentagem_reprovados = (reprovados / alunos) * 100
        print("\n--- Resultados Globais ---")
        print(f"Percentagem de alunos reprovados: {percentagem_reprovados:.1f}%")
        print(f"Quantidade de alunos aprovados: {aprovados}")
        print(f"Média mais baixa: {min_media:.2f}")
        print(f"Média mais alta: {max_media:.2f}")


def Exercicio_4():
    print("\n--- Exercicio 4 ---")
    conta = 0
    maior_altura = 0
    nome_mais_alta = ""

    nome = input("\nPrimeiro nome (FIM para terminar): ")

    while nome.lower() != "FIM":
        altura = int(input("Altura em cm: "))
        conta += 1

        if altura > maior_altura:
            maior_altura = altura
            nome_mais_alta = nome

        nome = input("Nome (FIM para terminar): ")

    if conta == 0:
        print("\nNão foram inscritas adolescentes.")
    else:
        print(f"\nAdolescente mais alta: {nome_mais_alta}, com {maior_altura} cm")
        print(f"Número de adolescentes no concurso: {conta}")


def Exercicio_5():
    print("\n--- Exercicio 5  ---")
    conta = 0
    soma = 0
    idade = int(input("\nQual a sua idade (0 para terminar): "))
    
    while idade != 0:
        conta += 1
        soma += idade
        idade = int(input("Qual a sua idade (0 para terminar): "))
        
    if conta > 0:
        media = soma / conta
        print(f"\nForam inseridas {conta} idades e a média é {media:.2f} anos.")
    else:
        print("\nNenhuma idade foi inserida.")


def Exercicio_6():
    print("\n--- Exercicio 6  ---")
    nome = input("\nNome (FIM para terminar): ")

    quantidade = 0
    soma_alturas = 0
    soma_alturas_mulheres = 0
    quantidade_mulheres = 0
    quantidade_homens = 0
    maior_altura = 0
    menor_altura = 9999

    while nome.lower() != "FIM":
        altura = float(input("Altura em cm: "))
        genero = input("Género (F/M): ").lower

        quantidade += 1
        soma_alturas += altura

        if altura > maior_altura:
            maior_altura = altura

        if altura < menor_altura:
            menor_altura = altura

        if genero == "F":
            soma_alturas_mulheres += altura
            quantidade_mulheres += 1
        elif genero == "M":
            quantidade_homens += 1
        else:
            print("Género inválido (use F ou M).")

        nome = input("\nNome (FIM para terminar): ")

    if quantidade == 0:
        print("\nNão foram introduzidas pessoas.")
    else:
        print("\n--- Resultados ---")
        print(f"Maior altura: {maior_altura} cm")
        print(f"Menor altura: {menor_altura} cm")
        print(f"Média de altura da população: {soma_alturas / quantidade:.2f} cm")

        if quantidade_mulheres > 0:
            print(f"Média de altura das mulheres: {soma_alturas_mulheres / quantidade_mulheres:.2f} cm")
        else:
            print("Não foram introduzidas mulheres.")

        print(f"Percentagem de homens: {(quantidade_homens / quantidade) * 100:.1f}%")


def main():
    while True:
        print("\n" + "="*40)
        print("          MENU DE FICHAS DE REVISÃO")
        print("="*40)
        print("1. Exercicio 1 - Idades (Mais velho/novo)")
        print("2. Exercicio 2 - Peso Ideal (F/M)")
        print("3. Exercicio 3 - Média de Alunos e Aprovações")
        print("4. Exercicio 4 - Concurso de Altura")
        print("5. Exercicio 5 - Média de Idades")
        print("6. Exercicio 6 - Estatísticas de Altura e Género")
        print("0. Sair")
        
        opcao = input("\nEscolhe uma opção (0-6): ")
        
        if opcao == "1":
            exercicio_1()
        elif opcao == "2":
            exercicio_2()
        elif opcao == "3":
            Exercicio_3()
        elif opcao == "4":
            Exercicio_4()
        elif opcao == "5":
            Exercicio_5()
        elif opcao == "6":
            Exercicio_6()
        elif opcao == "0":
            print("\nA encerrar o programa...")
            break
        else:
            print("\nOpção inválida! Tenta novamente.")

if __name__ == "__main__":
    main()