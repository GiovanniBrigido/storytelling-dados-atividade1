# Diário de prompts

**Link compartilhado da conversa (opcional):** —

---

## Prompt 1

```
tenho este trabalho para entregar:

https://github.com/prof-danny-idp/storytelling-dados-atividade1
```

**O que funcionou / o que mudei:** Claude abriu o repositório, leu o README, o dicionário de dados e os modelos de `claude.md`/`skill.md`/`prompts.md`, e entendeu a estrutura exata da entrega (pasta `entregas/nome-sobrenome/` com 4 arquivos) e o prazo. Antes de qualquer coisa, me perguntou qual era o tema/pergunta norteadora e meu nome — não tentou inventar um tema.

---

## Prompt 2

```
o professor pediu para eu escolher uma história do meu interesse. me passe ideias. luan coli dantas
```

**O que funcionou / o que mudei:** Em vez de sugerir temas genéricos, Claude baixou a base real (`eleitos.csv`), rodou uma análise rápida e trouxe 6 ideias de história já com números concretos (ex.: % de mulheres prefeitas por região, concentração partidária, reeleição, patrimônio declarado). Isso ajudou a escolher com base em dados reais, não em suposições. Escolhi a ideia 4, sobre o mapa partidário do poder local.

---

## Prompt 3

```
vamos com a 4, mapa partidário
```

**O que funcionou / o que mudei:** Claude aprofundou a análise só da linha escolhida: concentração por partido (top 10 + outros), força regional de cada partido (heatmap região × partido), e como as chapas vencem (coligação vs. candidatura isolada, número médio de partidos por coligação). Com esses números, montou a mensagem central do dashboard ("o poder municipal é fragmentado e regionalizado") e perguntou qual conta do GitHub usar para o fork/PR antes de tocar em qualquer coisa fora da minha pasta local — não assumiu a conta ativa por padrão.

**O que funcionou / o que mudei:** A partir da mensagem central e das perguntas que os dados respondem, Claude seguiu a skill de visualização (`skill.md`, criada nesta mesma conversa) para montar o `dashboard.html`: hero number de abertura, ranking de partidos em barras (uma cor, "Outros" em cinza), heatmap regional, cartões com os "campeões" de cada região e uma barra empilhada para coligação vs. candidatura isolada. Também escreveu o `claude.md` explicando o contexto, o público-alvo e as decisões de design, e esta skill genérica de storytelling de dashboards.
