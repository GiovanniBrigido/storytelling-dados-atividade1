# Diário de prompts

**Link compartilhado da conversa (opcional):** não há link; o trabalho foi feito no Claude Code (extensão do VS Code), dentro do clone do meu fork.

---

## Prompt 1

```
Bom dia!
```

**O que funcionou / o que mudei:** Só abriu a sessão. O Claude respondeu perguntando em que podia ajudar no projeto; nada foi produzido. No prompt seguinte passei o contexto completo de uma vez.

---

## Prompt 2

```
Estou fazendo uma atividade acadêmica com o seguinte briefing:
Storytelling de Dados
Quem governa as cidades: um dashboard sobre as eleições municipais de 2024

Você vai receber uma base com todas as pessoas eleitas para prefeito e vice em 2024, receberá um tema e irá construir, com a ajuda do Claude ou seu agente de IA, um dashboard em HTML que conte uma história para um público específico.

A base de dados

O arquivo eleitos.csv tem 11.106 linhas e 72 colunas. Cada linha é uma pessoa: o prefeito ou o vice de um dos 5.553 municípios cobertos.
Há informações de território, partido e coligação, perfil declarado (gênero, raça/cor, idade, escolaridade, ocupação), reeleição, bens declarados e votação -
eleitos.csv (A base completa)
dicionario.md  	O que significa cada coluna e como interpretá-la. Leia antes de começar.

Cuidados que evitam erros comuns

    Cada município aparece duas vezes (prefeito e vice). Para falar de prefeitos, filtre cargo = Prefeito. Para contar municípios, use codigo_municipio_tse.
    Os votos se repetem nas duas linhas da chapa. Some votos apenas com cargo = Prefeito, ou você vai contar tudo em dobro.
    Célula vazia não é zero nem "Não". Significa dado indisponível ou não aplicável.
    O CSV usa ponto e vírgula como separador e vírgula como decimal. Importe códigos como texto para não perder zeros à esquerda.
    A base retrata a eleição de 2024, não quem está no cargo hoje. A coluna classificacao_validacao explica os critérios de inclusão.

Meu tema é: 2. A cor do poder municipal

Que retrato racial emerge das pessoas eleitas para governar os municípios brasileiros em 2024?

Para quem: leitores do relatório anual de um observatório da sociedade civil. Público amplo, on-line, sem ninguém para explicar. Exige rigor sobre o que a base permite e não permite afirmar.

Pergunta norteadora
Que retrato racial emerge das pessoas eleitas para governar os municípios brasileiros em 2024?
Briefing
Um observatório da sociedade civil que acompanha a representação política vai lançar um relatório anual e encomendou um dashboard que abra a publicação.
O público é amplo: pesquisadores, jornalistas, gestores públicos e cidadãos interessados. O dashboard será compartilhado on-line e precisa ser compreendido sem que alguém esteja ao lado para explicá-lo.
Sua história deve apresentar o retrato racial de quem governa os municípios e tratar o tema com rigor, respeitando o que a base permite e o que ela não permite afirmar.

O que entregar

Quatro arquivos, numa pasta com seu nome. Além do dashboard, quero ver como você trabalhou com o Claude.
Arquivo 	O que deve conter
dashboard.html 	O dashboard final. Um arquivo único, que abre direto no navegador, sem depender de outros arquivos do seu computador.
claude.md 	Começa com a seção "Qual história meu dashboard conta?". Depois: tema escolhido, público, perguntas que os dados respondem e principais decisões de design.
skill.md 	A skill que você criou para orientar o Claude: regras de estilo visual, estrutura narrativa, paleta, linguagem para o público. Com nome, descrição e instruções.
prompts.md 	Os prompts que você usou, em ordem, cada um com uma linha sobre o que funcionou ou o que você mudou. Se quiser, inclua o link compartilhado da conversa.

Como entregar

O passo a passo detalhado, com e sem terminal, está no README do repositório.

    Faça um fork do repositório da disciplina.
    Copie a pasta entregas/_modelo e renomeie para entregas/nome-sobrenome (minúsculas, sem acentos, com hífen).
    Coloque seus quatro arquivos nessa pasta, substituindo os do modelo.
    Abra um Pull Request e preencha o checklist.
    Confira a verificação automática no PR. Se aparecer erro, a mensagem explica o que corrigir.

O fork já foi feito. Faça apenas o que está abaixo dessa instrução. Meu nome e sobrenome é giovanni brigido.

Como será avaliado
Narrativa
A história responde à pergunta norteadora e serve ao público do briefing?
Visualizações e rigor
Gráficos adequados, números corretos, limites da base respeitados.
Skill e claude.md
Instruções claras, específicas e que de fato orientaram o resultado.
Registro dos prompts
Processo documentado e reflexão sobre o que mudou ao longo do caminho.
Entrega
Arquivos completos, pasta no padrão, HTML funcionando no navegador.
```

**O que funcionou / o que mudei:** Passar o briefing inteiro, com tema, público, cuidados da base e critérios de avaliação, bastou para o Claude fazer o percurso completo em uma rodada: leu o README, o dicionário e o validador do repositório; calculou as tabelas por script a partir do `eleitos.csv` (por cargo, região, estado, chapa e gênero); montou o `dashboard.html` com os dados agregados embutidos; conferiu o resultado em capturas de tela de desktop e de celular (e ajustou a largura das barras no celular, onde um rótulo passava da borda); e escreveu o `claude.md` e a `skill.md` a partir das decisões que tomou. Decisões que vieram do Claude e que mantive: incluir o Censo 2022 como única referência externa, sempre marcada como tal; mostrar indígenas, amarelos e quilombolas em números absolutos; deixar partidos, bens e porte do município de fora; e fechar com a seção "permite / não permite afirmar". O ponto fraco do processo foi a ordem: a skill e o `claude.md` foram escritos junto com o dashboard, e não antes, como instruções prévias. Numa próxima vez, eu pediria primeiro a skill e o contexto, revisaria os dois e só então pediria o painel.
