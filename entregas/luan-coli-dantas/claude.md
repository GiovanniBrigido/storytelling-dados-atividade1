## Qual história meu dashboard conta?

Nas eleições municipais de 2024, 5.553 prefeitos foram eleitos no Brasil — mas nenhum partido chegou perto de controlar sozinho o poder local. O PSD lidera com apenas 16% das prefeituras, e mesmo os três maiores partidos juntos somam menos da metade do país. Em vez de um "dono nacional" do poder municipal, cada região tem o seu próprio líder — um partido diferente no Norte, no Centro-Oeste, no Sudeste e no Sul — e quase ninguém vence sem costurar uma coligação ampla, com em média 4,4 partidos por chapa. A mensagem central: o poder municipal brasileiro é fragmentado e regionalizado, construído por alianças pragmáticas, não por grandes legendas nacionais.

## Contexto do projeto

O professor abriu a escolha do tema livremente para este trabalho. Entre as histórias possíveis na base `dados/eleitos.csv` (prefeitos e vices eleitos nas eleições municipais de 2024, TSE/IBGE), escolhi investigar o mapa partidário do poder local: quem vence, com que força, em quais regiões e de que forma (sozinho ou em coligação).

Base de dados usada: `dados/eleitos.csv`, filtrando sempre `cargo = Prefeito` para não contar o vice-prefeito em dobro (o vice compartilha a votação da chapa, conforme o dicionário de dados). Cuidados do dicionário aplicados nesta análise:
- Contagem de prefeituras por `codigo_municipio_tse`/`id_chapa`, evitando duplicar a linha do vice.
- `partido` é a sigla da candidatura à Prefeitura; o vice pode ter partido diferente, por isso ele não entra nesta análise.
- `tipo_agremiacao` e `composicao_coligacao` foram usados para medir coligação vs. candidatura isolada vs. federação, e o número de partidos por coligação (contando os nomes separados por "/" em `composicao_coligacao`).
- `regiao` (grande região do IBGE) foi usada para o recorte regional, não a UF, para manter os grupos comparáveis em tamanho.
- Os 5.553 prefeitos incluem todas as linhas confirmadas pelos três critérios do dicionário (`ELEITO_ATUAL_TSE`, `CHAPA_CASSADA_TSE`, `ELEICAO_HISTORICA_DOCUMENTADA`); o dashboard não distingue esses critérios porque o recorte histórico é pequeno (46 pessoas) e não muda a leitura partidária.

## Público-alvo

Colegas de mestrado em Administração Pública, professores e qualquer pessoa com formação geral em política brasileira — alguém que já sabe o que é um prefeito, um partido e uma coligação, mas não tem de cor a distribuição partidária municipal. É um público com 2 a 3 minutos de atenção, que não vai manipular os dados, só entender a mensagem e, se quiser, checar os números por trás de cada afirmação.

## Perguntas que os dados respondem

1. Qual partido tem mais prefeituras eleitas no Brasil, e qual é o tamanho real dessa liderança?
2. Como o poder se distribui entre os dez maiores partidos — é concentrado ou pulverizado?
3. Cada região do país tem o seu próprio "partido dominante", ou o padrão nacional se repete em todo lugar?
4. Os prefeitos eleitos venceram sozinhos ou dependeram de amplas coligações multipartidárias?

## Decisões de design

- Segui a skill `skill.md` (criada por mim para este trabalho) em toda a construção do dashboard.
- Abri com o número que resume a história (hero figure: "1 em cada 6") antes de qualquer gráfico, porque é a constatação mais contraintuitiva: o maior partido do país governa uma fração pequena dos municípios.
- O ranking de partidos é um gráfico de barras horizontais em uma única cor (azul sequencial), não em cores categóricas por partido — a cor aqui mede magnitude (quantas prefeituras), não identidade, e usar oito cores diferentes sem motivo narrativo só adicionaria ruído. A barra "Outros 14 partidos" fica em cinza neutro, por ser um agregado, não uma entidade real.
- O mapa regional é um heatmap (região × partido), porque a pergunta é "onde cada partido é forte", uma comparação de magnitude em grade — e um heatmap deixa o padrão regional mais visível do que 5 gráficos de pizza separados. Os cartões abaixo do heatmap (os "5 campeões regionais") existem porque o heatmap mostra o padrão geral, mas a resposta exata ("quem é o campeão de cada região") merece destaque direto, sem exigir que o leitor escaneie a grade.
- O gráfico de coligação é uma única barra empilhada horizontal (parte-todo), porque são só três categorias (coligação, partido isolado, federação) e a pergunta é "qual fração do total", não uma comparação de muitos itens.
- Todos os gráficos têm legenda (quando têm mais de uma série), rótulos diretos nos valores mais importantes e uma visão em tabela alternativa, para não depender só de cor.
- O que ficou de fora: dados de votação (votos nominais), idade, gênero e patrimônio dos prefeitos — são histórias válidas, mas diluiriam o foco partidário/regional escolhido aqui.

## Instruções para o Claude

- Gerar um único arquivo `dashboard.html`, autocontido, com os dados agregados embutidos (sem ler `eleitos.csv` nem qualquer arquivo externo, sem dependência de CDN).
- Seguir a skill descrita em `skill.md` para paleta, tipografia, estrutura narrativa e escolha de gráficos.
- Todos os números do dashboard devem vir de agregações verificáveis de `dados/eleitos.csv` filtrando `cargo = Prefeito`; não inventar ou arredondar de forma que mude a leitura.
- O HTML precisa abrir direto no navegador, sem erros de console, e funcionar em telas de celular e desktop.
