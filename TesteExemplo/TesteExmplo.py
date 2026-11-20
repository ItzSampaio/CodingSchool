def grupo_1_imc():
    nome = input("Nome: ")
    imc = float(input("IMC (entre 5 e 100): "))

    if imc < 5 or imc > 100:
        print("O valor inserido está incorreto. Tem de estar compreendido entre 5 e 100")
        return

    if imc < 15:
        estado = "peso a menos"
    elif imc < 25:
        estado = "peso normal"
    else:
        estado = "peso a mais"

    print(f"{nome} tem {estado}")


def grupo_2_salarios():
    total_trabalhadores = 10

    soma_horas_ate_40 = 0.0
    conta_horas_ate_40 = 0
    soma_valores_finais = 0.0

    maior_horas = 0.0
    nome_maior_horas = ""
    menor_horas = 999999.0
    nome_menor_horas = ""

    conta_mais_45 = 0

    for i in range(total_trabalhadores):
        print(f"\n--- Trabalhador {i + 1} ---")
        nome = input("Nome do trabalhador: ")
        preco_hora = float(input("Preço/hora (€): "))
        horas = float(input("Número de horas de trabalho semanal: "))

        ordenado_base = preco_hora * horas
        print(f"O ordenado semanal base d@ {nome} é de {ordenado_base:.2f}€")

        if horas <= 40:
            bonus = 0.0
            soma_horas_ate_40 += horas
            conta_horas_ate_40 += 1
        elif horas <= 43:
            bonus = 50.0
        elif horas <= 45:
            bonus = 80.0
        else:
            bonus = 200.0
            conta_mais_45 += 1

        ordenado_final = ordenado_base + bonus
        soma_valores_finais += ordenado_final
        print(f"O ordenado final d@ {nome} é de {ordenado_final:.2f}€")

        if horas > maior_horas:
            maior_horas = horas
            nome_maior_horas = nome
        if horas < menor_horas:
            menor_horas = horas
            nome_menor_horas = nome

    if conta_horas_ate_40 > 0:
        media_horas_ate_40 = soma_horas_ate_40 / conta_horas_ate_40
    else:
        media_horas_ate_40 = 0.0

    media_valores_finais = soma_valores_finais / total_trabalhadores
    perc_mais_45 = (conta_mais_45 / total_trabalhadores) * 100

    print("\n=== RESUMO DA EMPRESA FAZ TUDO ===")
    print(f"Média das horas semanais (<= 40h): {media_horas_ate_40:.2f}h")
    print(f"Média dos valores finais de pagamento: {media_valores_finais:.2f}€")
    print(f"Maior nº de horas: {maior_horas:.2f}h ({nome_maior_horas})")
    print(f"Menor nº de horas: {menor_horas:.2f}h ({nome_menor_horas})")
    print(f"Percentagem de trabalhadores com mais de 45h: {perc_mais_45:.2f}%")


def menu():
    while True:
        print("\n=== MENU TESTE PYTHON ===")
        print("1 - Grupo I: Cálculo e estado físico pelo IMC")
        print("2 - Grupo II: Salários e estatísticas (10 trabalhadores)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            grupo_1_imc()
        elif opcao == "2":
            grupo_2_salarios()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()