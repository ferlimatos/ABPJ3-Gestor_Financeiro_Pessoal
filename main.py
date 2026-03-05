
# Dicionário de configuração da aplicação
dados_do_app = {
    "meses": ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    "categorias": ['Aluguel', 'Energia', 'Água', 'Internet', 'Cartão de Crédito'],
    "historico": []  
}

def percorrer_mes():
    # Mostra os meses disponíveis para o usuário
    for i, nome_mes in enumerate(dados_do_app["meses"], start=1):
        print(f"{i} - {nome_mes}")
    
def percorrer_despesas():
    # Mostra os tipos de despesas disponíveis para o usuário
    for i, tipo_despesa in enumerate(dados_do_app["categorias"], start=1):
        print(f"{i} - {tipo_despesa}")

def cadastrar_receita(mes, valor):
    # Adiciona valores de receita ao dicionário do mês correspondente.
    registro_receita = {
        "tipo": "receita",
        "mes": mes, 
        "valor": valor,
        "categoria": "Receita"
    }
    dados_do_app["historico"].append(registro_receita)
    print(f'Receita de R${valor:.2f} adicionada no mês {mes} com sucesso!')

def cadastrar_despesa(mes, valor, categoria):
    # Registra gastos e gera a lista atualizada de débitos.
    registro_gasto = {
        "tipo": "despesa",
        "mes": mes, 
        "valor": valor, 
        "categoria": categoria
    }
    dados_do_app["historico"].append(registro_gasto)
    print(f'Despesa de R${valor:.2f} ({categoria}) adicionada no mês {mes} com sucesso!')

def calcular_saldo(mes=None):
    # Realiza a subtração entre receitas e despesas, informando se o saldo está positivo ou negativo.
    receitas_totais = 0
    despesas_totais = 0
    
    for transacao in dados_do_app["historico"]:
        # Se um mês foi especificado, filtrar apenas aquele mês
        if mes and transacao["mes"] != mes:
            continue
            
        if transacao["tipo"] == "receita":
            receitas_totais += transacao["valor"]
        else:
            despesas_totais += transacao["valor"]
    
    saldo = receitas_totais - despesas_totais
    periodo = f"do mês {mes}" if mes else "de todos os meses"
    
    print(f"\n{'='*50}")
    print(f"SALDO FINANCEIRO {periodo.upper()}")
    print(f"{'='*50}")
    print(f"Receitas Total:    R$ {receitas_totais:.2f}")
    print(f"Despesas Total:    R$ {despesas_totais:.2f}")
    print(f"Saldo:             R$ {saldo:.2f}")
    
    if saldo > 0:
        print(f" POSITIVO - Situação financeira saudável!")
    elif saldo < 0:
        print(f"Saldo NEGATIVO - Você está em débito!")
    else:
        print(f"= Saldo ZERO - Receitas e despesas equilibradas!")
    print(f"{'='*50}\n")
    
    return saldo

def mostrar_relatorio():
    if not dados_do_app["historico"]:
        print("Histórico vazio!")
        return

    # Usamos um dicionário simples para somar os saldos
    saldos = {}

    for t in dados_do_app["historico"]:
        mes = t["mes"]
        valor = t["valor"]
        
        # Se o mês ainda não está no dicionário, começa com 0
        if mes not in saldos:
            saldos[mes] = 0.0
        
        # Se for receita soma, se for despesa subtrai
        if t["tipo"] == "receita":
            saldos[mes] += valor
        else:
            saldos[mes] -= valor

    print("\n--- RESUMO POR MÊS ---")
    for mes, valor_final in saldos.items():
        print(f"{mes}: R$ {valor_final:.2f}")

    # Encontrando o melhor e o pior mês de forma simples
    melhor_mes = max(saldos, key=saldos.get)
    pior_mes = min(saldos, key=saldos.get)

    print(f"\nMaior Lucro: {melhor_mes}")
    print(f"Maior Endividamento: {pior_mes}")

def imposto_gasto():
    gastos_por_categoria = {}

    for t in dados_do_app["historico"]:
        # Só nos interessam as despesas
        if t["tipo"] == "despesa":
            cat = t["categoria"]
            valor = t["valor"]

            if cat not in gastos_por_categoria:
                gastos_por_categoria[cat] = 0.0
            
            gastos_por_categoria[cat] += valor

    if not gastos_por_categoria:
        print("Nenhuma despesa encontrada.")
        return

    print("\n--- GASTOS POR CATEGORIA ---")
    for cat, total in gastos_por_categoria.items():
        print(f"{cat}: R$ {total:.2f}")

    # Descobre qual categoria tem o maior valor
    maior_cat = max(gastos_por_categoria, key=gastos_por_categoria.get)
    print(f"\nCategoria que mais pesou no bolso: {maior_cat}")

# Loop para o menu principal do programa
while True:
    print('\n--- ORÁCULO FINANCEIRO 2.0 ---')
    print('1 - Registrar Receita')
    print('2 - Registrar Gasto')
    print('3 - Ver Relatório Geral')
    print('4 - Sair')

    escolha = int(input('\nEscolha uma opção: '))

    match escolha:
        case 1:
            percorrer_mes()
            idx = int(input("Número do mês: ")) - 1
            mes = dados_do_app["meses"][idx]
            valor = float(input(f"Valor da receita para {mes}: R$ "))
            cadastrar_receita(mes, valor)

        case 2:
            percorrer_mes()
            idx_m = int(input("Número do mês: ")) - 1
            mes = dados_do_app["meses"][idx_m]
            
            percorrer_despesas()
            idx_d = int(input("Número da categoria: ")) - 1
            cat = dados_do_app["categorias"][idx_d]
            
            valor = float(input(f"Valor do gasto em {cat}: R$ "))
            cadastrar_despesa(mes, valor, cat)

        case 3:
            mostrar_relatorio()

        case 4:
            print('Encerrando... Até logo!')
            break
        case _:
            print('Opção inválida!')