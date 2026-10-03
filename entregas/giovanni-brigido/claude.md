## Qual história meu dashboard conta?

Dois em cada três prefeitos eleitos em 2024 se autodeclararam brancos (65,8%), num país em que brancos são 43,5% da população; pretos são 128 em 5.553 municípios. O retrato muda com o território (94% de brancos no Sul, maioria parda no Norte), fica um pouco mais diverso na vice e se estreita ainda mais quando raça e gênero se cruzam: mulheres negras são 4% dos prefeitos. O painel termina dizendo, com a mesma clareza, o que a base permite e o que ela não permite afirmar.

## Contexto do projeto

- **Tema recebido:** 2. A cor do poder municipal.
- **Pergunta norteadora:** que retrato racial emerge das pessoas eleitas para governar os municípios brasileiros em 2024?
- **Encomenda:** um observatório da sociedade civil que acompanha a representação política vai lançar seu relatório anual e quer um dashboard para abrir a publicação.
- **Base:** `dados/eleitos.csv` (11.106 pessoas, 5.553 municípios, 72 colunas), lida junto com `dados/dicionario.md`.
- **Cuidados de leitura adotados:**
  - CSV lido com separador `;`, vírgula decimal, UTF-8 com BOM e todos os códigos como texto.
  - Contagens sempre por cargo (`cargo = Prefeito` ou `cargo = Vice-prefeito`); chapas unidas por `id_chapa`; nenhum voto somado.
  - A variável central é `raca_cor_autodeclarada`. As 42 células vazias (16 prefeitos, 26 vices) viram a categoria "sem informação" e entram no denominador; nunca são tratadas como zero nem redistribuídas.
  - `quilombola_autodeclarado` e `etnia_indigena_autodeclarada` são campos distintos de raça/cor e aparecem separados.
  - A base retrata a eleição de 2024 (extração de 01/10/2026), não quem está no cargo hoje. Foram mantidos os três valores de `classificacao_validacao`; um teste só com `ELEITO_ATUAL_TSE` (5.530 municípios) dá os mesmos 65,8% de brancos, e isso é dito no painel.
  - O único dado externo é a distribuição da população por cor ou raça no Censo 2022 (IBGE), identificado como externo no gráfico e no rodapé.

## Público-alvo

Leitores do relatório anual do observatório: pesquisadores, jornalistas, gestores públicos e cidadãos interessados. Leem on-line, sozinhos, muitas vezes no celular e sem conhecer a base. Precisam entender a mensagem em poucos segundos, poder citar um número com segurança e saber até onde a conclusão vai. Parte desse público vai conferir os números, então cada gráfico tem a tabela correspondente.

## Perguntas que os dados respondem

1. Como os prefeitos eleitos em 2024 se declararam quanto à raça/cor?
2. Esse retrato se parece com o da população brasileira?
3. O retrato é o mesmo em todas as regiões e estados?
4. Os vice-prefeitos têm o mesmo perfil dos prefeitos? Como prefeito e vice se combinam na chapa?
5. O que acontece quando se cruza raça/cor com gênero?
6. Quantas pessoas indígenas, amarelas e quilombolas foram eleitas, e onde?
7. O que a base permite e o que ela não permite afirmar?

## Decisões de design

- **Skill seguida:** `skill.md` (painel-narrativo-rigoroso).
- **Título com a conclusão.** O título do painel e o de cada seção são frases com a descoberta, não rótulos de tema, porque ninguém estará ao lado para explicar.
- **Ordem do geral ao particular.** Número nacional, comparação com a população, território, chapa, gênero, grupos pequenos e, por fim, os limites. Cada seção responde a uma pergunta da lista acima.
- **Um número herói.** 65,8% abre o painel; três fichas ao lado dão o contraponto (negros, pretos, amarelos e indígenas).
- **Barras empilhadas a 100% para composição.** Raça/cor é parte de um todo, e o que interessa é comparar a composição entre regiões, estados e cargos. Todas as barras usam a mesma escala de 0 a 100%.
- **Barras simples para o resto.** Comparação com o Censo em pares de barras (eleitos em azul, população em cinza); chapas e gênero em barras horizontais de uma cor só. Sem pizza, sem mapa, sem eixo duplo.
- **Três cores mais um cinza.** Branca, parda e preta têm cores fixas em todo o painel, tiradas de uma paleta testada para daltonismo; nenhuma imita tom de pele. Amarela, indígena e sem informação somam menos de 1% e ficam juntas em cinza nas barras.
- **Grupos pequenos em números absolutos.** Nove prefeitos indígenas não cabem numa fatia de gráfico: aparecem em lista, com município e etnia declarada. O mesmo vale para amarelos e quilombolas.
- **Vocabulário explicado uma vez.** "Negros = pretos + pardos" e "autodeclaração" são definidos no início e repetidos onde são usados.
- **Limites como parte da história.** A última seção tem duas colunas, "permite afirmar" e "não permite afirmar". As ressalvas específicas (dado externo, estados com poucos municípios, campo de gênero) ficam junto do gráfico a que se referem.
- **Um único filtro.** Prefeitos ou vice-prefeitos, só na seção de território, para não multiplicar as leituras possíveis.
- **O que ficou de fora:** partidos, bens declarados, idade, escolaridade, votação e porte do município. Cruzá-los com raça/cor abriria leituras causais que a base, só com eleitos, não sustenta.

## Instruções para o Claude

- Gerar um único arquivo `dashboard.html`, autocontido, com os dados agregados embutidos e sem bibliotecas externas.
- Seguir a skill descrita em `skill.md`.
- Calcular todos os números por script a partir do `eleitos.csv`; nenhum número do painel é digitado de memória. Conferir os números citados no texto contra as tabelas agregadas.
- Usar sempre "se autodeclararam" ou "se declararam": o dado é uma declaração da pessoa, não uma classificação feita por terceiros.
- Não fazer afirmações causais nem falar em "chance de ser eleito": a base não tem os candidatos derrotados.
- Manter os registros sem informação visíveis e no denominador.
- Marcar o dado do Censo 2022 como externo à base sempre que ele aparecer.
- Escrever em português claro, sem jargão eleitoral ou estatístico.
