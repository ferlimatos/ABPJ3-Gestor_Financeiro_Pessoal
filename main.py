
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

def percorrer_mês():
    # Mostra os meses para o usuário
    for i, nome_mes in enumerate(dados_do_app["meses"], start=1):
          print(f"{i} - {nome_mes}")
    
def percorrer_despesas():
    # Mostra os tipos de despesas para o usuário
    for i, tipo_despesa in enumerate(dados_do_app["despesas"], start=1):
          print(f"\n{i} - {tipo_despesa}")

def cadastrar_receita():
   # Adicionar valores ao dicionário do mês correspondente.
   registro_receita = {
        "mes": mes_escolhido, 
        "valor": receita_atual
        }
   dados_do_app["historico"].append(registro_receita)

def calcular_saldo():
   # Realiza a subtração entre receitas e despesas, informando se o saldo está positivo ou negativo.
  registro_gasto = {
        "mes": mes_escolhido, 
        "valor": gasto_atual, 
        "tipo_despesa": despesa_escolhida
  }
  
            
  
  dados_do_app["historico"].append(registro_gasto)

"""def mostrar_relatorio():
   # Identifica o mês de maior lucro e o mês de maior endividamento, sugerindo o valor necessário para a quitação.

def imposto_gasto():
   # Analisa qual categoria de despesa consumiu a maior parte do orçamento no período."""

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
      percorrer_mês()
      opcao_mes = int(input("\nEscolha o número do mês: "))
      indice = opcao_mes - 1 
      mes_escolhido = (dados_do_app["meses"])[indice]
      print(f"Você escolheu: {mes_escolhido}")

      # Inserir valor da receita
      receita_atual = float(input('Digite um valor de sua receita: '))
      print(f'Você adicinou: R${receita_atual}')
      dados_do_app.setdefault("valor", {receita_atual})
      print(f'Receita de R${receita_atual} adicionada no mês {mes_escolhido} com sucesso!')

    case 2:
      percorrer_mês()
      opcao_mes = int(input("Escolha o número do mês: "))
      mes_escolhido = (dados_do_app["meses"])[opcao_mes]

      # Inserir valor do gasto
      gasto_atual = float(input('Digite um valor de seu gasto: '))
      print(f'Você adicinou: R${gasto_atual}')
      print(f'Receita de R${gasto_atual} adicionada no mês {mes_escolhido} com sucesso!')

      # Mostrar as opções de despesas
      percorrer_despesas()
      opcao_despesa = int(input("Escolha o tipo de despesa: "))
      despesa_escolhida = dados_do_app["despesas"][opcao_despesa]

    case 3: 
      percorrer_mês()
      opcao_mes = int(input("Escolha o número do mês: "))
      mes_escolhido = (dados_do_app["meses"])[opcao_mes]

      tipo_transacao = input('Você deseja ver todas as receitas ou gastos? (Receitas/Gastos): ')

      if tipo_transacao > 0:
        for i, receita_mes_selecionado in dados_do_app['historico']:
        # Mostrar todas as receitas registradas do mês até o momento.
          print(f"Registro de todas as receitas do mês de {mes_escolhido}:")
          print(f"{i}")
      else:
        print("Não há nenhuma transação registrada no histórico!")
    case 4:
      print('Programa encerrado!')
      break
    case _:
        print('Comando inválido! Tente novamente.')

# Para o case 3, você terá que percorrer o seu historico.
# Melhorar o nome de dados e variáveis, organizar melhor o dicinário.
# Depois que aprender sobre modulo e função, atualizar o código pra isso.