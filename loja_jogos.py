# LOJA  DE JOGOS

# CRIAÇÃO DAS LISTAS

jogos_disponiveis = ["super mario world", "gta 5", "FIFA", "the last of us", "nba 2k"]
preco_jogo = [29.99, 199.90, 59.90, 129.90, 250]
qtd_disponivel = [100, 90, 50, 40, 10]
preco_fabrica = [10, 120, 35.50, 80, 150]
registro_vendas = []
registro_compras = []
execucao = True

# MENU INTERATIVO

while execucao:
    print("-----------MENU-----------")
    print("1. Registrar Venda")
    print("2. Compra de Estoque")
    print("3. Estoque")
    print("4. Ver Caixa")
    print("5. Sair")
    x = input("Opção desejada: ")

    if x == "1":
        y = True
        qtd = 0
        while y:
            nome = input("Nome do jogo: ")
            if nome in jogos_disponiveis:
                qtd = int(input("Quantidade: "))
                posicao = jogos_disponiveis.index(nome)
                if qtd_disponivel[posicao] < qtd:
                    print("Quantidade indísponivel!")
                else:
                    qtd_disponivel[posicao] -= qtd
                    registro_vendas.append(float(preco_jogo[posicao]) * qtd)
                    print("Jogo(s) vendido(s)!")
                    y = False
            else:
                print("Jogo indisponível!")
                y = True

    elif x == "2":
        compra = input("Qual jogo deseja comprar: ")
        quantos = int(input("Quantas unidades: "))
        if compra in jogos_disponiveis:  # SE O JOGO TA NA LISTA
            posicao2 = jogos_disponiveis.index(compra)  # ACHA A POSIÇÃO DELE NA LISTA
            qtd_disponivel[posicao2] += quantos  # ACRESCENTA A QUANTIDADE
            registro_compras.append(preco_fabrica[posicao2] * quantos)
            print("Jogo(s) Comprado(s)!")
        else:
            valor_pago = float(input("Valor de fábrica: "))
            preco_de_venda = input("Qual será o valor de venda: ")
            jogos_disponiveis.append(compra)
            qtd_disponivel.append(quantos)
            preco_jogo.append(preco_de_venda)
            registro_compras.append(valor_pago * quantos)
            print("Jogo(s) Comprado(s)!")

    elif x == "3":
        ind = 0
        print("----------ESTOQUE----------")
        for i in jogos_disponiveis:
            print(f"{i.title()} (R$ {preco_jogo[ind]}) Qtd em Estoque: {qtd_disponivel[ind]}")
            ind += 1
    elif x == "4":
        print("----------CAIXA----------")
        print(f"Lucros: R$ {sum(registro_vendas):6.2f}")
        print(f"Despesas: R$ {sum(registro_compras):6.2f}")
        print(f"Saldo Total: R$ {sum(registro_vendas) - (sum(registro_compras)):6.2f}")

    elif x == "5":
        print("Caixa Fechado!")
        execucao = False

    else:
        print("Opção Inválida!")
        execucao = True
