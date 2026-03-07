import modulo

print('\nSeja bem-vindo ao Oráculo Financeiro 2.0!')

# Loop para o menu principal do programa
while True:
    print('\nEscolha um comando:')
    print('1 - Registrar Receita')
    print('2 - Registrar Despesa')
    print('3 - Ver Relatório Geral')
    print('4 - Sair')

    escolha = int(input('\nEscolha uma opção: '))

    match escolha:
        case 1:
            modulo.percorrer_mes()
            indice_mes = int(input("Número do mês: ")) - 1
            mes = modulo.obter_mes_validado(indice_mes)

            if mes:
                valor = float(input(f"Valor da receita para {mes}: R$ "))
                modulo.cadastrar_receita(mes, valor)
        case 2:
            modulo.percorrer_mes()
            indice_mes = int(input("Número do mês: ")) - 1
            mes = modulo.obter_mes_validado(indice_mes)

            if mes:
                modulo.percorrer_despesas()
                indice_despesa = int(input("Número da categoria: ")) - 1
                
                # Validação simples para categoria também
                if 0 <= indice_despesa < len(modulo.dados_do_app["categorias"]):
                    categoria = modulo.dados_do_app["categorias"][indice_despesa]
                    valor = float(input(f"Valor do gasto em {categoria} para {mes}: R$ "))
                    modulo.cadastrar_despesa(mes, valor, categoria)
                else:
                    print("Categoria inválida!")

        case 3:
            modulo.mostrar_saldo()

        case 4:
            print('Encerrando... Até logo!')
            break
        case _:
            print('Opção inválida!')
