# Oráculo Financeiro 2.0 - Gestor Financeiro Pessoal 🔮

Este projeto é uma evolução da primeira versão do [Oráculo Financeiro](https://github.com/ferlimatos/ABPJ1-Oraculo_Financeiro), focada em transformar um script de execução única em um sistema de gestão modular, escalável e com persistência de dados.

## 🚀 Evoluções da Versão 2.0
- **Armazenamento em Lista de Dicionários**: Diferente de variáveis soltas, agora utilizamos uma lista centralizada que permite o registro ilimitado de transações, facilitando a manipulação dos dados.
- **Menu Interativo com Match Case**: Implementação de um fluxo contínuo que permite ao usuário realizar múltiplas operações em uma única execução.
- **Modularização**: O código foi dividido em funções específicas para cada tarefa (cadastro, cálculo e relatórios), seguindo boas práticas de organização.

## 🛠️ Estrutura de Dados
O sistema utiliza um dicionário principal (dados_do_app) que contém:
- **Configurações**: Listas fixas de meses e categorias.
- **Histórico**: Uma lista onde cada entrada é um dicionário contendo tipo, mes, valor e categoria.

## ⚙️ Funcionalidades Planejadas
- `cadastrar_receita`: Registra entradas financeiras vinculadas a um mês.
- ``cadastrar_despesa``: Registra saídas categorizadas (Ex: Aluguel, Internet).
- ``calcular_saldo``: Exibe o balanço geral entre entradas e saídas.
- ``mostrar_relatorio``: Identifica os meses de melhor e pior desempenho financeiro.
- ``imposto_gasto``: Calcula a porcentagem de impacto de cada categoria no orçamento total.

## 🗺️ Fluxograma
O fluxo detalha o caminho da informação desde a entrada do dado até a geração do relatório final.

![Fluxograma](Oráculo%20Financeiro%202.0.webp)

## 📚 Aprendizados
- Estruturação de dados complexos com dicionários e listas em Python.
- Lógica de comparação temporal para relatórios financeiros.

## 👤 Autora
Fernanda Matos – Estudante de Sistemas de Análise e Desenvolvimento (Estácio) e Desenvolvedora Web e Mobile em formação (Escola do Futuro de Goiás).
