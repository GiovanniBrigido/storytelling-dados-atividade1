# Storytelling de Dados · Atividade 1

**Disciplina:** PCDIA – Storytelling de Dados · Mestrado em Administração Pública · IDP
**Professor:** Prof. Danny
**Prazo de entrega:** 03/10/2026, às 11h30 (horário de Brasília)
**Galeria das entregas:** https://prof-danny-idp.github.io/storytelling-dados-atividade1/

---

## Objetivo

Usar o Claude para analisar uma base de dados real e construir um **dashboard em HTML que conte uma história** com esses dados. O tema e a pergunta norteadora de cada estudante são entregues pelo professor.

Além do dashboard, você vai entregar o "bastidor" do trabalho: o contexto que deu ao Claude (`claude.md`), uma skill de visualização criada por você (`skill.md`) e o registro dos prompts usados (`prompts.md`).

---

## A base de dados

A base fica na pasta [`dados/`](dados/):

| Arquivo | O que é | Download direto |
| --- | --- | --- |
| [`dados/eleitos.csv`](dados/eleitos.csv) | Prefeitos e vice-prefeitos eleitos nas eleições municipais de 2024 | [link raw](https://raw.githubusercontent.com/prof-danny-idp/storytelling-dados-atividade1/main/dados/eleitos.csv) |
| [`dados/dicionario.md`](dados/dicionario.md) | Descrição de cada coluna, critérios de inclusão e cuidados de leitura | [link raw](https://raw.githubusercontent.com/prof-danny-idp/storytelling-dados-atividade1/main/dados/dicionario.md) |

> **Leia o dicionário antes de começar.** O CSV usa `;` como separador, vírgula como separador decimal e codificação UTF-8. Para baixar pelo link raw, clique com o botão direito e escolha "Salvar link como...".

---

## O que entregar

Cada estudante cria **uma pasta** dentro de `entregas/` com o próprio nome, no formato `nome-sobrenome`: letras minúsculas, sem acentos, palavras separadas por hífen. Exemplos: `maria-souza`, `joao-pedro-lima`.

A pasta precisa ter **exatamente estes 4 arquivos**. Os modelos estão em [`entregas/_modelo/`](entregas/_modelo/).

```
entregas/
└── maria-souza/
    ├── claude.md
    ├── skill.md
    ├── prompts.md
    └── dashboard.html
```

### `claude.md`: o contexto do projeto
É o arquivo de instruções que você deu ao Claude. Ele **começa obrigatoriamente** com a seção:

```markdown
## Qual história meu dashboard conta?
```

Escreva ali, em poucas frases, a história do seu dashboard. **Esse trecho aparece no card da galeria.** Depois vêm as seções: contexto do projeto, público-alvo, perguntas que os dados respondem e decisões de design.

### `skill.md`: a sua skill de visualização
Uma skill do Claude criada por você, com regras de estilo visual, estrutura narrativa, paleta, tipografia etc. Ela segue o formato de uma skill do Claude: um cabeçalho com `name` e `description`, seguido das instruções.

> **A skill deve ser genérica.** Ela precisa servir para qualquer dashboard, com qualquer base de dados. Não cite esta base, suas colunas ou o seu tema. O que é específico deste trabalho vai no `claude.md`.

### `prompts.md`: o diário de prompts
Os prompts que você usou, **em ordem cronológica**. Abaixo de cada um, uma linha "**O que funcionou / o que mudei:**". Se quiser, inclua o link compartilhado da conversa (campo opcional).

### `dashboard.html`: o dashboard
Um **único arquivo**, autocontido, que abre direto no navegador com dois cliques:
- CSS e JavaScript embutidos no próprio arquivo, ou bibliotecas carregadas por CDN (ex.: Chart.js, D3, Plotly);
- os dados que o dashboard usa **embutidos no HTML**, já agregados. O dashboard **não pode** ler o `eleitos.csv` nem outros arquivos locais.

---

## Passo a passo da entrega

Você precisa de uma conta gratuita no [GitHub](https://github.com/signup). Escolha **um** dos dois caminhos.

### Caminho A: pelo navegador (sem terminal)

1. No seu computador, crie uma pasta com o seu nome no padrão (ex.: `maria-souza`) e coloque nela os 4 arquivos: `claude.md`, `skill.md`, `prompts.md` e `dashboard.html`.
2. **Fork:** no topo desta página, clique em **Fork** → **Create fork**. Você terá uma cópia do repositório na sua conta.
3. No **seu fork**, entre na pasta `entregas/` e clique em **Add file** → **Upload files**.
4. **Arraste a pasta inteira** (`maria-souza`, não só os arquivos) para a área de upload. Confira se os arquivos aparecem como `maria-souza/claude.md` etc. e clique em **Commit changes**.
   > Se o seu navegador não aceitar arrastar pastas: clique em **Add file** → **Create new file**, digite `maria-souza/claude.md` no campo do nome (a `/` cria a pasta), cole o conteúdo e faça o commit. Depois entre em `entregas/maria-souza/`, clique em **Add file** → **Upload files** e envie os outros 3 arquivos.
5. Volte à página inicial do seu fork e clique em **Contribute** → **Open pull request**.
6. Preencha o checklist que aparece e clique em **Create pull request**.

### Caminho B: pelo terminal (git)

```bash
# 1. Faça o fork pelo botão "Fork" no GitHub e depois clone o SEU fork
git clone https://github.com/SEU-USUARIO/storytelling-dados-atividade1.git
cd storytelling-dados-atividade1

# 2. Copie o modelo para a sua pasta (troque maria-souza pelo seu nome)
cp -r entregas/_modelo entregas/maria-souza        # macOS / Linux / Git Bash
# Copy-Item -Recurse entregas\_modelo entregas\maria-souza   # PowerShell no Windows

# 3. Edite os 4 arquivos dentro de entregas/maria-souza/

# 4. Registre e envie as alterações
git add entregas/maria-souza
git commit -m "Entrega de Maria Souza"
git push

# 5. Abra o Pull Request
gh pr create --fill        # se tiver o GitHub CLI
# ou entre no seu fork no navegador e clique em "Contribute" → "Open pull request"
```

### Depois de abrir o Pull Request

Uma verificação automática roda em alguns segundos e **comenta no seu PR** com o resultado:
- ✅ **Tudo certo:** aguarde a aprovação do professor. Depois da aprovação, seu dashboard aparece na [galeria](https://prof-danny-idp.github.io/storytelling-dados-atividade1/).
- ❌ **Algo a corrigir:** o comentário explica o que ajustar. Corrija no **seu fork**, no mesmo lugar. O PR é atualizado sozinho e a verificação roda de novo. **Não abra um novo PR.**

---

## Regras

- Cada Pull Request só pode alterar arquivos **dentro da sua própria pasta** em `entregas/`. Não altere `_modelo`, `dados`, o README nem as pastas de colegas.
- Um PR por estudante.
- **Prazo:** 03/10/2026, às 11h30. Vale o horário do último commit no PR.
- Galeria publicada: https://prof-danny-idp.github.io/storytelling-dados-atividade1/

---

## Critérios de avaliação

| Critério | O que é observado |
| --- | --- |
| Qualidade da narrativa | A história é clara, tem começo, meio e fim e responde à pergunta norteadora. O público entende a mensagem central. |
| Adequação das visualizações | Os gráficos escolhidos combinam com os dados e com a mensagem, sem distorcer escalas nem poluir a leitura. |
| Qualidade da skill e do `claude.md` | A skill é genérica, reutilizável e tem instruções acionáveis. O `claude.md` explica o contexto, o público e as decisões de design. |
| Registro dos prompts | Os prompts estão em ordem, com a reflexão do que funcionou e do que mudou ao longo do processo. |
| Funcionamento do HTML | O arquivo abre direto no navegador, sem erros, sem depender de arquivos locais, e funciona em telas diferentes. |
