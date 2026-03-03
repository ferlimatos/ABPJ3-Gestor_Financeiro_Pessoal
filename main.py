
financeiro = {}
valor_receita = []

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
ano = []
tipo_de_gasto_de_gasto = ['Aluguel', 'Energia', 'Água', 'Internet', 'Cartão de Crédito'],
periodo_de_gasto = ['Semanal', 'Mensal', 'Bimestral', 'Trimestral', 'Semestral', 'Anual']

dados_do_app = {
    "meses": [...],
    "categorias": [...],
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
      receita_atual = float(input('Digite um valor de sua receita: '))
      print(f'Você adicinou: R${valor_receita}')
      financeiro.append(receita_atual)
      print(f'Receita adicionada com sucesso em sua conta!')

    case 2:
      mes_solicitado = input('Informe u ')
      valor_gasto = float(input('Digite um valor de seu gasto: '))
      print(f'Você adicinou: R${valor_gasto}')

      financeiro.append(valor_gasto)
      print(f'Gasto adicionado com sucesso em sua conta!')
    case 3: 
      mes_solicitado = input('Informe u ')
      tipo_transacao = input('Você deseja ver todas as receitas ou gastos? ')

      if tipo_transacao == 'receitas':
        print() # Mostrar todas as receitas registradas do mês até o momento.
      elif tipo_transacao == 'gastos':
        print() # Mostrar todos os gastos registrados do mês até o momento.
      elif tipo_transacao != mes:
        print() # Mostrar mensagem que está incorreto. 
      else:
        print() # Mostrar que ainda não foi adicionado nada, portanto não tem nada para ser mostrado.
    case _:
      print('Programa encerrado!')
      break