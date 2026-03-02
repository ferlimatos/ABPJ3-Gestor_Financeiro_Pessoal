# Oráculo Financeiro 2.0 - Gestor Financeiro Pessoal 🔮

Este projeto é uma evolução da primeira versão do [Oráculo Financeiro](https://github.com/ferlimatos/ABPJ1-Oraculo_Financeiro), focada em transformar um script de execução única em um sistema de gestão modular, escalável e com persistência de dados.

## ♻️ O que será aproveitado da Versão 1.0
Da estrutura original desenvolvida no GitHub, os seguintes pontos fundamentais serão mantidos e aprimorados:
- **Lógica de Cálculo Base**: A fórmula fundamental de `Receitas - Despesas = Saldo` permanece como o coração do processamento de dados.
- **Categorização de Gastos**: O conceito de separar despesas (como Aluguel, Energia e Lazer) será mantido, mas agora de forma dinâmica e não fixa.
- **Feedback ao Usuário**: As mensagens de diagnóstico (Saldo Positivo ou Negativo) continuarão a oferecer uma visão rápida da saúde financeira.
- **Identidade Visual (UI no Terminal)**: O uso de separadores visuais e formatação de valores com duas casas decimais (`:.2f`) será preservado para garantir uma boa experiência de leitura.

## 🚀 Evoluções para o Oráculo 2.0
Para atender aos novos requisitos técnicos, o sistema passará pelas seguintes transformações:
- **Armazenamento Escalável**: Substituição de variáveis isoladas por uma Lista de Dicionários, permitindo o registro ilimitado de transações.
- **Menu Interativo**: Implementação de um laço `while True` com a estrutura `match case`, permitindo que o usuário realize várias operações sem fechar o programa.
- **Persistência de Dados**: Diferente da primeira versão, os dados agora serão salvos e carregados de um arquivo externo, garantindo que o histórico não seja perdido.
- **Gestão Completa (CRUD)**: Além de registrar, o usuário poderá listar, atualizar e remover entradas específicas.

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
