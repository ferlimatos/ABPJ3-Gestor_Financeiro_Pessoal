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

## ⚙️ Funções
- `cadastrar_receita`: Registra entradas financeiras vinculadas a um mês.
- `cadastrar_despesa`: Registra saídas categorizadas (Ex: Aluguel, Internet).
- `calcular_saldo`: Exibe o balanço geral entre entradas e saídas.
- `mostrar_relatorio`: Identifica os meses de melhor e pior desempenho financeiro.
- `imposto_gasto`: Calcula a porcentagem de impacto de cada categoria no orçamento total.
- `percorrer_mes`: Mostra os meses disponíveis para o usuário.
- `percorrer_despesas`: Mostra os tipos de despesas disponíveis para o usuário.

## 🗺️ Fluxograma
O fluxo detalha o caminho da informação desde a entrada do dado até a geração do relatório final.

![Fluxograma](Oráculo%20Financeiro%202.0.webp)

## 📚 Aprendizados
- Aprendi a importância de nomear variáveis e funções de forma descritiva (ex: cadastrar_despesa em vez de apenas cadastrar).
- Melhorei a organização visual do código para facilitar a leitura por outros desenvolvedores.
- Entendi como mapear informações usando chaves e valores (ex: {"tipo": "receita", "valor": 100}).
- Aprendi a criar um "banco de dados" dinâmico na memória do Python, onde uma lista armazena vários dicionários de transações.
- Comprendi como encapsular lógica repetitiva dentro de funções, tornando o código principal mais limpo.
- Aprendi a passar informações para dentro das funções através de parâmetros.
- Implementação do match case para criar menus mais organizados e modernos.
- Cálculo de saldos acumulados percorrendo listas com o laço for.
- Filtragem de dados dentro de um histórico (ex: separar o que é receita do que é despesa).
- Durante o desenvolvimento do Oráculo Financeiro 2.0, um dos meus maiores desafios foi equilibrar a vontade de aplicar técnicas avançadas com a necessidade de consolidar os fundamentos. Aprendi que separar o 'essencial agora' do 'avançado depois' não é apenas uma escolha técnica, mas uma estratégia para manter o fluxo de aprendizado constante e evitar bloqueios no desenvolvimento.

## 👤 Autora
Fernanda Matos – Estudante de Sistemas de Análise e Desenvolvimento (Estácio) e Desenvolvedora Web e Mobile em formação (Escola do Futuro de Goiás).
