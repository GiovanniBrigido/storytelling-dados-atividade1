---
name: painel-narrativo-rigoroso
description: Regras de narrativa, gráficos, cores, linguagem e rigor para dashboards em HTML de arquivo único, lidos on-line por um público amplo sem ninguém para explicar. Use sempre que for criar ou revisar um dashboard, painel ou relatório visual que precise contar uma história e deixar claros os limites dos dados.
---

# Painel narrativo rigoroso

## Quando usar

Use esta skill ao construir ou revisar qualquer dashboard em HTML que será lido sem apresentador: publicações on-line, relatórios, aberturas de estudo. Ela vale para qualquer base de dados. O contexto específico (tema, público, perguntas, colunas) vem do arquivo de contexto do projeto, não daqui.

## Antes de desenhar

- Leia a documentação da base antes de abrir os dados. Anote a unidade de cada linha, o que duplica contagens e o que significam os valores vazios.
- Calcule todos os números por script, a partir do arquivo original. Nunca digite um número de memória.
- Escreva a história em três ou quatro frases antes de escolher qualquer gráfico. Se não couber, a análise ainda não terminou.
- Liste o que a base permite e o que não permite afirmar. Essa lista entra no painel.

## Estrutura narrativa

- Abra com a conclusão principal como título, em uma frase com verbo e número ("Dois em cada três X são Y"), não com o nome do tema.
- Logo abaixo, escreva um parágrafo de contexto e uma caixa "Como ler" com as definições que o leitor precisa para todo o resto.
- Organize o painel em seções numeradas, do geral para o particular. Cada seção responde a uma pergunta e tem: título com a descoberta, um parágrafo de duas a três frases e um gráfico.
- Use um único número herói em todo o painel, no topo. Os demais indicadores vão em fichas menores.
- Feche com uma seção de limites em duas colunas: "permite afirmar" e "não permite afirmar".
- Termine com fonte e método em linguagem comum: de onde vêm os dados, a data da extração e como os percentuais foram calculados.

## Escolha de gráficos

- Decida primeiro o que o dado faz, depois o gráfico:
  - composição de um todo comparada entre grupos: barras horizontais empilhadas a 100%, todas na mesma escala;
  - comparação de valores entre categorias: barras horizontais de uma cor, ordenadas;
  - duas fontes lado a lado: pares de barras, a fonte principal em cor e a de referência em cinza;
  - um único valor importante: número grande, sem gráfico;
  - contagens muito pequenas: lista ou número absoluto, nunca fatia de gráfico.
- Comece toda barra no zero. Nunca use eixo duplo, pizza com mais de duas fatias, 3D ou escala cortada.
- Ordene as barras por valor ou por uma ordem que o leitor já conhece. Evite ordem alfabética quando ela não ajuda.
- Mostre o tamanho de cada grupo (n) junto do rótulo quando os grupos tiverem tamanhos muito diferentes, e avise quando um grupo for pequeno demais para o percentual ser estável.
- Coloque o valor na ponta da barra ou dentro do segmento apenas quando o texto couber. O que não couber vai para a dica e para a tabela.
- Todo gráfico tem: título descritivo, subtítulo com unidade e denominador, legenda quando houver duas ou mais séries, dica ao passar o mouse ou focar com o teclado, e uma tabela recolhível com os mesmos dados.
- Use no máximo um filtro, e só quando ele responder a uma pergunta da história. Posicione o filtro acima dos gráficos que ele altera.

## Paleta de cores

A cor identifica a categoria. A mesma categoria tem a mesma cor em todos os gráficos do painel.

| Função | Claro | Escuro |
| --- | --- | --- |
| Série 1 (categoria principal) | `#2a78d6` | `#3987e5` |
| Série 2 | `#eb6834` | `#d95926` |
| Série 3 | `#1baf7a` | `#199e70` |
| Outros, referência, sem informação | `#a8a69f` | `#6f6d68` |
| Fundo da página | `#f9f9f7` | `#0d0d0d` |
| Fundo dos cartões | `#fcfcfb` | `#1a1a19` |
| Texto principal | `#0b0b0b` | `#ffffff` |
| Texto secundário | `#52514e` | `#c3c2b7` |
| Linhas de grade | `#e1e0d9` | `#2c2c2a` |

- Use no máximo três cores de série por gráfico. A partir da quarta categoria, agrupe as menores em "outros", em cinza, e diga na legenda o que o grupo contém.
- Nunca escolha cores que imitem ou caricaturem a característica representada (aparência de pessoas, bandeiras, símbolos de grupos). Atribua as cores pela ordem da paleta.
- Reserve vermelho e verde para estados (erro, sucesso). Não os use como cor de série.
- Texto nunca usa a cor da série. A identidade vem do quadradinho de cor ao lado do rótulo.
- Separe segmentos vizinhos com 2px de espaço na cor do fundo, sem contorno.
- Defina as cores como variáveis CSS e ofereça o modo escuro com `prefers-color-scheme`.

## Tipografia e layout

- Fonte do sistema (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`) em todo o painel. Sem fontes externas.
- Hierarquia: título do painel 28–44px; título de seção 21–28px; texto 16px; legendas e notas 12,5–14px. Número herói com pelo menos 56px.
- Coluna única com no máximo 980px de largura. Parágrafos com até 68 caracteres por linha.
- Cada gráfico fica em um cartão com fundo próprio, borda fina e cantos de 12px.
- Barras finas (16 a 22px de altura), com a ponta arredondada em 4px.
- Em telas com menos de 720px, tudo passa para uma coluna, os rótulos das barras encolhem e as tabelas ganham rolagem horizontal própria. A página nunca rola para o lado.
- Números em formato brasileiro (ponto de milhar, vírgula decimal). Uma casa decimal para percentuais; duas apenas abaixo de 1%.

## Linguagem

- Escreva para quem nunca viu a base: frases curtas, voz ativa, sem siglas não explicadas e sem nomes de colunas.
- Diga o que o dado é. Se é uma declaração, escreva "declararam"; se é um registro administrativo, diga de quem.
- Defina cada termo técnico uma vez, na caixa "Como ler", e use sempre a mesma palavra para a mesma coisa.
- Prefira "66 em cada 100" ou "dois em cada três" quando ajudar, e dê também o número absoluto.
- Descreva diferenças; não as explique sem evidência. Evite "por causa de", "leva a", "prova que" quando a base só mostra uma distribuição.

## Rigor

- Valor vazio não é zero nem "não". Mantenha-o como categoria própria ("sem informação"), visível e dentro do denominador.
- Informe o denominador de todo percentual, no subtítulo ou na dica.
- Quando a base tiver mais de uma linha por unidade, filtre antes de contar e diga no método como contou.
- Marque todo dado que não vem da base principal como externo, com fonte e ano, junto do gráfico em que ele aparece.
- Ponha cada ressalva ao lado do gráfico a que ela se refere, além do resumo na seção de limites.
- Se houver critérios de inclusão diferentes na base, refaça o número principal com o critério mais restrito e relate se ele muda.

## Arquivo

- Um único `.html`, com CSS e JavaScript embutidos e os dados já agregados em um objeto JSON dentro do próprio arquivo.
- Sem dependência de arquivos locais. Prefira não depender de bibliotecas externas; se usar, só por CDN.
- Gere os gráficos a partir do objeto de dados, para que gráfico, dica e tabela mostrem sempre o mesmo número.
- Inclua `lang`, `meta viewport`, `title` descritivo e rótulos acessíveis (`aria-label`) nas marcas dos gráficos.

## Checklist final

- [ ] O título do painel e o de cada seção são frases com a conclusão.
- [ ] Cada número citado no texto foi conferido contra a tabela agregada.
- [ ] Todo percentual tem denominador explícito e todo gráfico tem tabela.
- [ ] As cores são as mesmas para as mesmas categorias em todo o painel; no máximo três por gráfico.
- [ ] Valores vazios aparecem como "sem informação" e não foram somados a outro grupo.
- [ ] Dados externos estão marcados como externos, com fonte e ano.
- [ ] Há uma seção dizendo o que a base permite e o que não permite afirmar.
- [ ] Nenhuma frase afirma causa sem que a base sustente.
- [ ] O arquivo abre com dois cliques, sem internet e sem erros no console.
- [ ] O painel foi aberto e conferido em tela larga e em tela de celular, sem rolagem lateral nem texto cortado.
