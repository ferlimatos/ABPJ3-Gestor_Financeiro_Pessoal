
financeiro = {}

# Dicionário 1
dados_do_app = {
    "meses": ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    "despesas": ['Aluguel', 'Energia', 'Água', 'Internet', 'Cartão de Crédito'],
    "periodo_de_gasto": ['Semanal', 'Mensal', 'Bimestral', 'Trimestral', 'Semestral', 'Anual'],
    "ano": [],
    "valor": [],
    "historico": [] # Uma lista que vai guardando cada transação
}

# Loop para o menu principal do programa
while True:
  print('''Seja bem-vindo ao Oráculo Financeiro 2.0!
  '1 - Digite 1 para registrar uma receita.
  '2 - Digite 2 para registrar uma gasto.
  '3 - Digite 3 para registrar registro de receita ou gasto de um mês.
  '4 - Digite 4 para sair do programa.''')

  menu_escolha = int(input('Digite o número: '))

  match menu_escolha:
    case 1:
      # Como mostrar as opções de meses
      for i, nome_mes in enumerate(dados_do_app["meses"]):
          print(f"{i} - {nome_mes}")

      opcao_mes = int(input("Escolha o número do mês: "))
      mes_escolhido = (dados_do_app["meses"])[opcao_mes]

      # Inserir valor da receita
      receita_atual = float(input('Digite um valor de sua receita: '))
      print(f'Você adicinou: R${receita_atual}')
      print(f'Receita de R${receita_atual} adicionada no mês {mes_escolhido} com sucesso!')

      # Salvando histórico
      registro_receita = {
        "mes": mes_escolhido, 
        "valor": receita_atual
        }
      dados_do_app["historico"].append(registro_receita)

    case 2:
      # Como mostrar as opções de meses
      for i, nome_mes in enumerate(dados_do_app["meses"]):
          print(f"{i} - {nome_mes}")

      opcao_mes = int(input("Escolha o número do mês: "))
      mes_escolhido = (dados_do_app["meses"])[opcao_mes]

      # Inserir valor da receita
      gasto_atual = float(input('Digite um valor de seu gasto: '))
      print(f'Você adicinou: R${gasto_atual}')
      print(f'Receita de R${gasto_atual} adicionada no mês {mes_escolhido} com sucesso!')

      # Mostrar as opções de despesas
      for i, tipo_despesa in enumerate(dados_do_app["despesas"]):
          print(f"{i} - {tipo_despesa}")
      opcao_despesa = int(input("Escolha o tipo de despesa: "))
      despesa_escolhida = dados_do_app["despesas"][opcao_despesa]

      # Salvando histórico
      registro_gasto = {
        "mes": mes_escolhido, 
        "valor": gasto_atual, 
        "tipo_despesa": despesa_escolhida
        }
      dados_do_app["historico"].append(registro_gasto)

    case 3: 
      mes_solicitado = input('Informe u ')
      tipo_transacao = input('Você deseja ver todas as receitas ou gastos? ')

      if tipo_transacao == 'receitas':
        print() # Mostrar todas as receitas registradas do mês até o momento.
      elif tipo_transacao == 'gastos':
        print() # Mostrar todos os gastos registrados do mês até o momento.
      elif tipo_transacao != "meses":
        print() # Mostrar mensagem que está incorreto. 
      else:
        print() # Mostrar que ainda não foi adicionado nada, portanto não tem nada para ser mostrado.
    case _:
      print('Programa encerrado!')
      break

# Para o case 3, você terá que percorrer o seu historico.
# Melhorar o nome de dados e variáveis, organizar melhor o dicinário.
# Depois que aprender sobre modulo e função, atualizar o código pra isso.