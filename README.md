# Gestor Financeiro Pessoal

O Oráculo Financeiro é um gestor de finanças pessoais desenvolvido em Python, focado em escalabilidade e organização de dados através de estruturas de dicionários.

## 📌 Sobre o Projeto
Este projeto nasceu da evolução de um script inicial, buscando resolver o problema da persistência de dados. A ideia central é permitir que o usuário não apenas registre entradas e saídas, mas consiga visualizar a saúde financeira em diferentes períodos:

- **Semanal**
- **Mensal**
- **Semestral e Anual**

## 🛠️ Estrutura de Dados
Para garantir a escalabilidade, o projeto utiliza uma arquitetura de Dicionários Aninhados:
- **Receitas**: Armazenadas por mês com valores específicos.
- **Despesas**: Categorizadas para identificar onde o usuário mais gasta.

## ⚙️ Funcionalidades Planejadas
- `cadastrar_receita`: Adiciona valores ao dicionário do mês correspondente.
- ``cadastrar_despesa``: Registra gastos e gera a lista atualizada de débitos.
- ``calcular_saldo``: Realiza a subtração entre receitas e despesas, informando se o saldo está positivo ou negativo.
- ``mostrar_relatorio``: Identifica o mês de maior lucro e o mês de maior endividamento, sugerindo o valor necessário para a quitação.
- ``imposto_gasto``: Analisa qual categoria de despesa consumiu a maior parte do orçamento no período.

## 🗺️ Fluxograma
O fluxo detalha o caminho da informação desde a entrada do dado até a geração do relatório final.

## 📚 Aprendizados
- Estruturação de dados complexos com dicionários e listas em Python.
- Lógica de comparação temporal para relatórios financeiros.

## 👤 Autora
Fernanda Matos – Estudante de Sistemas de Análise e Desenvolvimento (Estácio) e Desenvolvedora Web e Mobile em formação (Escola do Futuro de Goiás).
