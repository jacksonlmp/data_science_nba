# Projeto Data Science - NBA

## Sobre o projeto

O sistema deve proporcionar aos stakeholders um conjunto de funcionalidades que os
auxiliem no processo de tomada de decisão. Os dados utilizados serão os da atual
temporada (24-25) da NBA e da temporada passada (23-24). O sistema deverá atender
aos Requisitos Funcionais (RF) definidos e detalhados neste documento de especificação.

## Instalação de dependências

```
pip install -r requirements.txt
```

## Requisitos - Parte 1
- [x] RF1 - Listar todos os times da NBA agrupados por Conferência
- [x] RF2 - Apresentar a classificação atual dos times [Agrupados por Conferência]
- [x] RF3 - Apresentar o total de vitórias e derrotas do time, separados por partidas jogadas em casa (mandante) e fora de casa (visitante), conforme Tabela 2;
- [x] RF4 - Apresentar o total dos dados do seu time [temporada 23-24 e temporada atual], conforme Tabelas 3 e 4;
- [x] RF5 - Apresentar a divisão de alguns dados da Tabela 3, conforme Tabelas 4
- [x] RF6 - Apresentar os dados referentes a performance defensiva do time [temporada 23-24 e temporada atual], conforme Tabela 5.
- [x] RF7 - Apresentar os jogos do seu time [temporada 23-24 e temporada atual], conforme Tabela 6.
- [x] RF8 - Apresentar gráficos de desempenho do seu time [temporada 23-24 e temporada atual] para compor o Dashboard do projeto:
    - Gráfico de Barras Empilhado para Vitórias [Cor verde] e Derrotas [Cor vermelha].
    - Gráfico de Barras Agrupado para Vitórias em casa [Cor verde], Vitórias fora de casa [Cor azul], Derrotas em casa [Cor vermelha] e Derrotas fora de casa [Cor
marrom].
    - Gráfico Histograma para exibir a frequência de vitórias e derrotas do time.
    - Gráfico de Setor [Pizza] para o percentual de para Vitórias em casa, Vitórias fora de casa, Derrotas em casa e Derrotas fora de casa.
    - Gráfico de Radar exibindo a média de pontos marcados e sofridos nos jogos em casa e fora de casa.
    - Gráfico de Linhas exibindo a sequência de vitórias e derrotas ao longo da temporada.
    - Gráfico de Dispersão exibindo equipes e a média de pontos marcados e sofridos durante a temporada
    - Apresente um gráfico da sua escolha para exibir os dados referentes a Tabela 5 do RF6 e a Tabela 6 do RF7.
- [ ] RF9 – Para cada tabela e/ou requisito que exiba dados gerados pelo sistema será necessário que os dados sejam salvos em um arquivo csv.
- [ ] RF10 – Para cada gráfico gerado pelo sistema será necessário que sejam exibidos em formato HTML e abertos no Browser.

## Requisitos - Parte 2
- [x] RF1 - Apresentar os seguintes dados dos Jogadores [Dependendo de “onde esteja extraindo” os dados, existe um Id, exiba também o Id de cada Jogador]
- [x] RF2 - Para cada jogador do seu time apresente os dados conforme a tabela. [OBS.: O sistema deve fornecer automaticamente os dados de todos os jogos ocorridos durante a temporada atual em tempo real]. 
- [x] RF3 - O sistema deve fornecer os dados das partidas que o usuário escolher. Ex. Partidas contra time X e apresentar esses dados conforme a tabela.
- [x] RF4 - O sistema deve apresentar a quantidade de jogos realizados dentro e fora de casa e a quantidade de jogos dentro e fora de casa contra um determinado time [da escolha do usuário].  
- [x] RF5 - Apresentar e calcular a média de pontos, rebotes e assistências dos jogadores.
    - [x] RF5 – A – Apresentar ao usuário a porcentagem de pontos, rebotes e assistências abaixo da média
- [x] RF6 - Apresentar e calcular a mediana de pontos, rebotes e assistências dos jogadores.
    - [x] RF6 – A – Apresentar ao usuário a porcentagem de pontos, rebotes e assistências abaixo da mediana   
- [x] RF7 - Apresentar e calcular a moda de pontos, rebotes e assistências dos jogadores. Exibir a quantidade de vezes que a moda aparece para cada item [pontos, rebotes e assistências].
    - [x] RF7 – A – Apresentar ao usuário a porcentagem de pontos, rebotes e assistências abaixo da média   
- [x] RF8 - Apresentar o Desvio Padrão de pontos, rebotes e assistências dos jogadores. Quanto mais próximo de zero, mais agrupado em torno da média os dados estão. 
- [ ] RF9 – O sistema deve apresentar a quantidade de pontos, assistências e rebotes de toda a carreira do jogador. 
- [ ] RF10 – O sistema deve apresentar a quantidade de pontos, assistências e rebotes de toda a carreira 10do jogador e comparada com a atual temporada conforme a tabela.
    - [ ] RF10 - Apresentar gráficos de desempenho dos seus jogadores [temporada atual] para compor o Dashboard do projeto: 
                • Gráfico de distribuição de pontos por jogo em relação a média, mediana e moda 
                • Gráfico de distribuição de rebotes por jogo em relação a média, mediana e moda 
                • Gráfico de distribuição de assistências por jogo em relação a média, mediana e 
                moda 
                • Gráfico BOX PLOT de pontos, rebotes e assistências por jogo [detalhar todas as informações (Max, Min, Mediana, Outliers, etc.) possíveis nos quartis]
- [ ] RF11 – Para cada tabela e/ou requisito que exiba dados gerados pelo sistema será necessário que os dados sejam salvos em um arquivo c.v. 
- [ ] RF12 – Para cada gráfico gerado pelo sistema será necessário que sejam exibidos em formato  HTML e abertos no Browser. 
