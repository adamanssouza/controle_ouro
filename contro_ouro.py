
def cadastrar_valores(mensagem):
    valores = []

    while True:
        valor = float(input(mensagem))

        if valor == 0:
            break

        if valor < 0:
            print("Não são permitidos valores negativos.")
        else:
            valores.append(valor)

    return valores


def cadastrar_dias():
    while True:
        dias = int(input("Quantos dias foram trabalhados? "))

        if dias > 0:
            return dias

        print("Digite uma quantidade maior que zero.")


def cadastrar_pessoa():
    print("\n--- CADASTRAR PESSOA ---")

    nome = input("Digite o nome: ")

    ouro = cadastrar_valores(
        "Quantidade de ouro em gramas [0 para parar]: "
    )

    dias = cadastrar_dias()

    valores = cadastrar_valores(
        "Valor recebido em R$ [0 para parar]: "
    )

    total_ouro = sum(ouro)
    total_valor = sum(valores)
    valor_por_dia = total_valor / dias

    pessoa = {
        "nome": nome,
        "ouro": total_ouro,
        "dias": dias,
        "valor": total_valor,
        "valor_por_dia": valor_por_dia
    }

    return pessoa


def mostrar_pessoa(pessoa):
    print("\n" + "=" * 35)
    print(f"Nome: {pessoa['nome']}")
    print(f"Ouro total: {pessoa['ouro']:.2f} gramas")
    print(f"Dias trabalhados: {pessoa['dias']}")
    print(f"Valor total: R$ {pessoa['valor']:.2f}")
    print(f"Valor por dia: R$ {pessoa['valor_por_dia']:.2f}")
    print("=" * 35)


def mostrar_todas_pessoas(pessoas):
    if not pessoas:
        print("\nNenhuma pessoa cadastrada.")
        return

    print("\n--- TODAS AS PESSOAS ---")

    for pessoa in pessoas:
        mostrar_pessoa(pessoa)


def mostrar_total_geral(pessoas):
    if not pessoas:
        print("\nNenhuma pessoa cadastrada.")
        return

    total_ouro = 0
    total_valor = 0
    total_dias = 0

    for pessoa in pessoas:
        total_ouro += pessoa["ouro"]
        total_valor += pessoa["valor"]
        total_dias += pessoa["dias"]

    print("\n--- TOTAL GERAL ---")
    print(f"Total de ouro: {total_ouro:.2f} gramas")
    print(f"Total de dias: {total_dias}")
    print(f"Total recebido: R$ {total_valor:.2f}")

    media = total_valor / total_dias
    print(f"Média geral por dia: R$ {media:.2f}")


def mostrar_maior_valor_por_dia(pessoas):
    if not pessoas:
        print("\nNenhuma pessoa cadastrada.")
        return

    maior = pessoas[0]

    for pessoa in pessoas:
        if pessoa["valor_por_dia"] > maior["valor_por_dia"]:
            maior = pessoa

    print("\n--- MAIOR VALOR POR DIA ---")
    print(f"Nome: {maior['nome']}")
    print(f"Valor por dia: R$ {maior['valor_por_dia']:.2f}")


def mostrar_menu():
    print("\n" + "=" * 35)
    print("SISTEMA DE CONTROLE DE OURO")
    print("=" * 35)
    print("1 - Cadastrar pessoa")
    print("2 - Ver todas as pessoas")
    print("3 - Ver total geral")
    print("4 - Ver maior valor por dia")
    print("5 - Sair")


def main():
    pessoas = []

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pessoa = cadastrar_pessoa()
            pessoas.append(pessoa)
            print("\nPessoa cadastrada com sucesso!")

        elif opcao == "2":
            mostrar_todas_pessoas(pessoas)

        elif opcao == "3":
            mostrar_total_geral(pessoas)

        elif opcao == "4":
            mostrar_maior_valor_por_dia(pessoas)

        elif opcao == "5":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


main()
