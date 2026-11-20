def menu():
    while True:
        print("\n===== MENU ======")
        print("1. Diferença entre dois números")
        print("2. Negativo ou positivo")
        print("3. Par/ímpar e igual/maior")
        print("4. Salário")
        print("5. Notas")
        print("6. Idade")
        print("7. Calculadora")
        print("0. Sair")
        
        try:
            opcao = int(input("Escolhe uma opção: "))
        except ValueError:
            print("Opção inválida, escreve um número.")
            continue
            
        if opcao == 1:
            diferenca()
        elif opcao == 2:
            negativo_ou_positivo()
        elif opcao == 3:
            par_impar_igual_menor()
        elif opcao == 4:
            salario()
        elif opcao == 5:
            notas()
        elif opcao == 6:
            idade()
        elif opcao == 7:
            calculadora()
        elif opcao == 0:
            print("Até à próxima!")
            break
        else:
            print("Opção inválida.")

def diferenca():
    n1 = int(input("Diz um numero: "))
    n2 = int(input("Diz outro numero: "))
    if n1 == n2:
        dif = 0
    elif n1 < n2:
        dif = n2 - n1
    else:
        dif = n1 - n2
    print(f"A diferença é {dif}")

def negativo_ou_positivo():
    n1 = int(input("Diz um numero: "))
    if n1 == 0:
        print("O número é nulo")
    elif n1 < 0:
        print("O número é negativo")
    else:
        print("O número é positivo")

def par_impar_igual_menor():
    n1 = int(input("Diz um numero: "))
    if n1 % 2 == 0:
        print("O n1 é par")
    else:
        print("O n1 é ímpar")
        
    n2 = int(input("Diz outro numero: "))
    if n1 == n2:
        print("Os números são iguais")
    elif n1 < n2:
        print("n2 é maior")
    else:
        print("n1 é maior")

def salario():
    horas_semanais = float(input("Quantas horas trabalhas: "))
    print("1. Manhã")
    print("2. Noite")
    turno = int(input("Escolhe uma opção: "))
    if turno == 1:
        valor = 7.5 * horas_semanais
    else:
        valor = 10 * horas_semanais
    print(f"O teu salário é {valor}")

def notas():
    nome = str(input("Qual o teu nome: "))
    nota_portfolio_fichas = float(input("Nota do portfolio: "))
    nota_mini_teste = float(input("Nota do mini teste: "))
    nota_trabalho_aula = float(input("Nota do trabalho de aula: "))
    nota_teste = float(input("Nota do teste: "))
    
    nota_final = 0.2 * nota_portfolio_fichas + 0.2 * nota_mini_teste + 0.2 * nota_trabalho_aula + 0.4 * nota_teste
    
    if nota_final <= 9:
        print(f"O aluno {nome} tem {nota_final:.2f} de média e é fraco")
    elif nota_final <= 15:
        print(f"O aluno {nome} tem {nota_final:.2f} de média e é médio")
    elif nota_final <= 17:
        print(f"O aluno {nome} tem {nota_final:.2f} de média e é bom")
    else:
        print(f"O aluno {nome} tem {nota_final:.2f} de média e é excelente")

def idade():
    nome = str(input("Qual o teu nome: "))
    anos = int(input("Qual a tua idade: "))
    
    if 0 < anos <= 12:
        print(f"O aluno {nome} tem {anos} anos e é criança")
    elif 13 <= anos <= 17:
        print(f"O aluno {nome} tem {anos} anos e é adolescente")
    elif 18 <= anos <= 59:
        print(f"O aluno {nome} tem {anos} anos e é adulto")
    else:
        print(f"O aluno {nome} tem {anos} anos e é idoso")

def calculadora():
    def menu_calc():
        while True:
            print("\n===== CALCULADORA =====")
            print("1. Diferença")
            print("2. Soma")
            print("3. Produto")
            print("4. Divisão")
            print("0. Voltar ao menu principal")
            
            try:
                opcao = int(input("Escolhe uma opção: "))
            except ValueError:
                print("Opção inválida, escreve um número.")
                continue
                
            if opcao == 1:
                calc_diferenca()
            elif opcao == 2:
                soma()
            elif opcao == 3:
                produto()
            elif opcao == 4:
                divisao()
            elif opcao == 0:
                break
            else:
                print("Opção inválida.")

    def calc_diferenca():
        n1 = int(input("Diz um numero: "))
        n2 = int(input("Diz outro numero: "))
        print(f"A diferença (n1 - n2) é {n1 - n2}")

    def soma():
        n1 = int(input("Diz um numero: "))
        n2 = int(input("Diz outro numero: "))
        print(f"A soma entre {n1} e {n2} é {n1 + n2}")

    def produto():
        n1 = int(input("Diz um numero: "))
        n2 = int(input("Diz outro numero: "))
        print(f"O produto entre {n1} e {n2} é {n1 * n2}")

    def divisao():
        n1 = int(input("Diz um numero: "))
        n2 = int(input("Diz outro numero: "))
        if n2 == 0:
            print("Nao podes dividir por 0 ")
        else:
            print(f"A divisão entre {n1} e {n2} é {n1 / n2:.2f}")

    menu_calc()


menu()
