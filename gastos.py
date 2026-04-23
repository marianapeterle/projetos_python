gastos = []

while True:
    print("CONTROLE DE GASTOS")
    print("1 - Adicionar gasto")
    print("2 - Ver gastos")
    print("3 - Ver total")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do gasto: ")
        valor = float(input("Valor: "))
        gastos.append((nome, valor))
        print("Gasto adicionado!")

    elif opcao == "2":
        for g in gastos:
            print(f"{g[0]} - R$: {g[1]}")

    elif opcao == "3":
        total = sum(g[1] for g in gastos)
        print(f"Total: R${total}")
        break

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")

continuar = input("Deseja voltar ao menu? (sim/não): ").lower()

if continuar != "s":
    print("Encerrando programa...")
    exit


