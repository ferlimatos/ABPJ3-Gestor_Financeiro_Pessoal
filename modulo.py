# Dicionário de configuração da aplicação
dados_do_app = {
    "meses": ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    "categorias": ['Aluguel', 'Energia', 'Água', 'Internet', 'Cartão de Crédito'],
    "historico": []  
}

# Funções principais
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
    
    print(f"\nSALDO FINANCEIRO {periodo.upper()}")
    print(f"Receitas Total:    R$ {receitas_totais:.2f}")
    print(f"Despesas Total:    R$ {despesas_totais:.2f}")
    print(f"Saldo:             R$ {saldo:.2f}")
    
    if saldo > 0:
        print(f"Saldo POSITIVO - Situação financeira saudável!")
    elif saldo < 0:
        print(f"Saldo NEGATIVO - Você está em débito!")
    else:
        print(f"= Saldo ZERO - Receitas e despesas equilibradas!")
    print(f"{'='*50}\n")
    
    return saldo

def mostrar_saldo():
    # Verifica se existe algum registro no histórico.
    # Caso esteja vazio, informa ao usuário e encerra a função.
    if not dados_do_app["historico"]:
        print("Histórico vazio!")
        return

    # Cria um dicionário para armazenar o saldo total de cada mês
    saldos = {}

    # Percorre todas as transações registradas no histórico
    for i in dados_do_app["historico"]:
        mes = i["mes"]
        valor = i["valor"]
        
        # Se o mês ainda não está no dicionário, começa com 0
        if mes not in saldos:
            saldos[mes] = 0.0
        
        # Se for receita soma, se for despesa subtrai
        if i["tipo"] == "receita":
            saldos[mes] += valor
        else:
            saldos[mes] -= valor

    # Exibe o resumo final dos saldos por mês
    print("\n--- RESUMO POR MÊS ---")
    for mes, valor_final in saldos.items():
        print(f"{mes}: R$ {valor_final:.2f}")

# Funções secundárias
def percorrer_mes():
    # Mostra os meses disponíveis para o usuário
    for i, nome_mes in enumerate(dados_do_app["meses"], start=1):
        print(f"{i} - {nome_mes}")
    
def percorrer_despesas():
    # Mostra os tipos de despesas disponíveis para o usuário
    for i, tipo_despesa in enumerate(dados_do_app["categorias"], start=1):
        print(f"{i} - {tipo_despesa}")

def obter_mes_validado(indice_mes):
    while True:
        try:
            if 0 <= indice_mes < len(dados_do_app["meses"]):
                return dados_do_app["meses"][indice_mes]
            else:
                print('\nMês inválido! Tente um número entre 1 e 12.')
        except ValueError:
            break
