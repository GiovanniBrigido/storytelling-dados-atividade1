---
name: dashboard-storytelling
description: Regras de estilo visual, estrutura narrativa, paleta e tipografia para transformar uma base de dados em um dashboard HTML que conta uma história. Use sempre que for criar um gráfico, painel ou relatório visual a partir de dados tabulares.
---

# Dashboard Storytelling

## Quando usar

Use esta skill sempre que o objetivo não for só "mostrar os dados", mas **defender uma mensagem** com eles: um dashboard, um painel, um relatório visual ou qualquer página HTML com gráficos embutidos. Não se aplica a tabelas de referência puras, sem narrativa, nem a ferramentas de exploração livre de dados (dashboards de BI onde o usuário escolhe o próprio recorte).

## Estrutura narrativa

- Antes de desenhar qualquer gráfico, resuma a mensagem central em uma frase. Essa frase é o título ou subtítulo de abertura — o leitor precisa entender a conclusão antes de ver o primeiro gráfico.
- Abra com o número ou fato mais contraintuitivo da história (um "hero number" ou estatística de impacto), não com o gráfico mais detalhado. Detalhe vem depois de capturar atenção.
- Organize as seções na ordem em que a história deve ser lida, nunca na ordem em que os dados foram calculados. Cada seção deve responder a uma pergunta específica e avançar o argumento da anterior — se uma seção não muda o que o leitor entende, corte-a.
- Termine com uma síntese de uma ou duas frases que conecta todos os gráficos à mensagem de abertura. Não termine no último gráfico sem fechar o argumento.
- Cada gráfico leva uma legenda (caption) curta, escrita como uma afirmação ("X é duas vezes maior que Y"), nunca como uma descrição técnica ("gráfico de barras mostrando X por Y").
- Limite o dashboard a 4-6 blocos de conteúdo (hero + gráficos + síntese). Mais do que isso dilui a mensagem; se os dados pedem mais, está na hora de cortar um ângulo secundário, não de adicionar mais um gráfico.

## Escolha de gráficos

Decida a forma pelo trabalho que o leitor precisa fazer, nunca pelo gráfico "mais bonito":

| O leitor precisa... | Use | Evite |
|---|---|---|
| Entender um único número ou fato | Hero number / stat tile (valor grande, sem gráfico) | Um gráfico de barra única |
| Comparar magnitude entre itens, do maior ao menor | Barras horizontais, ordenadas | Pizza/rosca com mais de 2-3 fatias |
| Comparar magnitude em uma grade de duas dimensões | Heatmap (uma cor, do clara à escura) | Múltiplos gráficos de pizza lado a lado |
| Ver evolução ao longo do tempo | Linha (ou área, se for uma série só) | Barras para série temporal longa |
| Entender parte-todo (2 a 6 categorias) | Barra única empilhada, horizontal | Pizza com muitas fatias ou fatias parecidas |
| Comparar poucas séries nomeadas entre si | Barras agrupadas ou linhas múltiplas, com legenda | Mais de 6-7 séries na mesma cor-chave |
| Destacar um item específico entre muitos | Técnica de ênfase: 1 cor de destaque + resto em cinza | Cores diferentes para cada item quando só 1 importa |

Regras gerais:
- Nunca use dois eixos Y no mesmo gráfico — a sobreposição de escalas é sempre arbitrária e sugere correlações que não existem. Prefira dois gráficos separados ou indexar as duas séries a uma base comum.
- Nunca pinte um gráfico de barras com uma cor que varia conforme o próprio valor da barra (cor degradê por valor) quando as categorias não têm ordem natural — isso duplica a informação que o comprimento da barra já mostra. Uma cor sequencial degradê é só para grades (heatmaps) ou escalas contínuas reais.
- Rotule os valores com seletividade: o fim da barra, o ponto extremo, ou o único item que importa para a história. Nunca um número em cada ponto de um gráfico com muitas categorias — isso vira ruído e ninguém lê.
- Toda categoria que não muda a conclusão (uma cauda longa de itens pequenos) deve ser agrupada em "Outros", nunca listada item a item.

## Paleta de cores

Cor tem uma função, nunca é decoração. Antes de escolher uma cor, pergunte: essa cor representa identidade (categorias diferentes), magnitude (quanto maior, mais escuro) ou estado (bom/alerta/crítico)? Nunca misture essas três funções na mesma escala.

- **Paleta categórica (identidade):** até 4 cores sólidas, sempre na mesma ordem fixa para a mesma entidade em todos os gráficos do dashboard (nunca reatribua cores quando um filtro muda a lista visível). Sugestão de ordem: azul `#2a78d6`, laranja `#eb6834`, verde-água `#1baf7a`, amarelo `#eda100`. Acima de 4 categorias relevantes, use um "Outros" em cinza neutro em vez de uma 5ª cor.
- **Escala sequencial (magnitude):** uma única cor, do mais claro (perto de zero) ao mais escuro (valor máximo). Nunca um arco-íris de cores diferentes para representar quantidade.
- **Escala divergente (polaridade, acima/abaixo de um ponto central):** duas cores opostas (uma fria, uma quente) com um cinza neutro no meio — nunca duas cores frias ou duas quentes, porque o centro precisa "ler" como zero.
- **Cores de estado (bom/alerta/crítico):** reservadas exclusivamente para indicar status, nunca reaproveitadas como cor de categoria. Sempre acompanhadas de ícone ou texto, nunca só a cor.
- **Cores neutras (texto, grades, eixos):** cinza para tudo que não é dado — eixos, linhas de grade, texto de rótulos. Texto nunca usa a cor de uma série; a identidade vem do marcador ao lado do texto, não da cor da letra.
- Antes de finalizar, verifique visualmente se a paleta funciona para quem não distingue bem vermelho/verde: se duas cores adjacentes parecerem parecidas em escala de cinza, troque a ordem ou adicione um padrão/textura.

## Tipografia e layout

- Uma única fonte sans-serif do sistema (`system-ui`, `-apple-system`, `Segoe UI`, sem-serifa) em todo o dashboard — nunca uma fonte decorativa ou serifada, nem no número de destaque.
- Números grandes de destaque (hero number) usam algarismos proporcionais, não tabulares — algarismos tabulares (largura igual) são só para colunas de tabela que precisam alinhar verticalmente.
- Hierarquia visual clara: título > subtítulo/mensagem central > legendas de seção > rótulos de gráfico > texto de apoio. Cada nível visivelmente menor ou mais claro que o anterior.
- Espaço em branco generoso entre seções — compactar tudo para "caber" é sempre pior do que deixar o leitor rolar a página.
- Barras e linhas finas (nunca blocos grossos e saturados cobrindo toda a largura disponível); grades e eixos em linha fina e discreta, nunca tracejada.
- Layout responsivo: nenhum gráfico ou texto pode ser cortado ou exigir rolagem horizontal em uma tela de celular.
- Toda cor com contraste baixo sobre o fundo (amarelos e tons claros) precisa de um rótulo visível ao lado — nunca depender só da cor para ser lida.

## Checklist final

- [ ] A mensagem central está escrita em uma frase, visível antes do primeiro gráfico.
- [ ] Cada gráfico tem o tipo certo para a pergunta que responde (ver tabela de escolha de gráficos).
- [ ] Nenhum gráfico usa dois eixos Y, arco-íris sequencial ou cor degradê em categoria sem ordem natural.
- [ ] Toda cor tem uma função (identidade, magnitude ou estado) e segue a mesma ordem/paleta em todo o dashboard.
- [ ] Gráficos com 2 ou mais séries têm legenda; rótulos de valor aparecem só nos pontos que importam para a história.
- [ ] Existe uma visão alternativa em tabela (ou os números por extenso) para quem não consegue distinguir as cores.
- [ ] O dashboard termina com uma síntese que conecta os gráficos de volta à mensagem de abertura.
- [ ] A página funciona sem rolagem horizontal e sem cortes em uma tela de celular.
