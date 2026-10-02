"""Gera a galeria (index.html) com um card por entrega em entregas/.

Uso:
    python scripts/gerar_galeria.py [--saida index.html]

O repositório usado nos links do GitHub vem da variável GITHUB_REPOSITORY
(definida automaticamente no GitHub Actions) ou do valor padrão abaixo.
"""

import argparse
import html
import json
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ENTREGAS = RAIZ / "entregas"
REPO_PADRAO = "prof-danny-idp/storytelling-dados-atividade1"
ARQUIVOS_MD = ("claude.md", "skill.md", "prompts.md")
PARTICULAS = {"de", "da", "do", "das", "dos", "e"}
TAMANHO_TRECHO = 280
TITULO_HISTORIA = re.compile(r"^#{1,6}\s*Qual hist[óo]ria meu dashboard conta\??\s*$", re.I)
TITULO_QUALQUER = re.compile(r"^#{1,6}\s")


def nome_legivel(pasta: str) -> str:
    partes = pasta.split("-")
    return " ".join(
        p if (i > 0 and p in PARTICULAS) else p.capitalize() for i, p in enumerate(partes)
    )


def limpar_markdown(texto: str) -> str:
    texto = re.sub(r"<!--.*?-->", " ", texto, flags=re.S)
    texto = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", texto)          # imagens
    texto = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", texto)       # links -> texto
    texto = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", texto, flags=re.M)  # marcadores de lista
    texto = re.sub(r"^\s*>\s?", "", texto, flags=re.M)           # citações
    texto = re.sub(r"[*_`#]+", "", texto)
    return re.sub(r"\s+", " ", texto).strip()


def trecho_historia(claude_md: Path) -> str:
    if not claude_md.is_file():
        return ""
    linhas = claude_md.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    capturando, corpo = False, []
    for linha in linhas:
        if TITULO_HISTORIA.match(linha.strip()):
            capturando = True
            continue
        if capturando and TITULO_QUALQUER.match(linha):
            break
        if capturando:
            corpo.append(linha)
    texto = limpar_markdown("\n".join(corpo))
    if texto.startswith("[Em 2 a 4 frases"):  # texto do modelo não substituído
        return ""
    if len(texto) > TAMANHO_TRECHO:
        texto = texto[:TAMANHO_TRECHO].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
    return texto


def coletar(repo: str) -> list[dict]:
    entregas = []
    if not ENTREGAS.is_dir():
        return entregas
    for pasta in sorted(p for p in ENTREGAS.iterdir() if p.is_dir()):
        if pasta.name.startswith(("_", ".")):
            continue
        base_github = f"https://github.com/{repo}/blob/main/entregas/{pasta.name}"
        entregas.append({
            "pasta": pasta.name,
            "nome": nome_legivel(pasta.name),
            "trecho": trecho_historia(pasta / "claude.md"),
            "dashboard": f"entregas/{pasta.name}/dashboard.html" if (pasta / "dashboard.html").is_file() else "",
            "arquivos": [
                {"nome": md, "url": f"{base_github}/{md}"} for md in ARQUIVOS_MD if (pasta / md).is_file()
            ],
        })
    return entregas


def card(e: dict) -> str:
    esc = html.escape
    trecho = esc(e["trecho"]) if e["trecho"] else '<span class="vazio">História ainda não descrita no claude.md.</span>'
    botao = (
        f'<a class="botao" href="{esc(e["dashboard"])}" target="_blank" rel="noopener">Abrir dashboard</a>'
        if e["dashboard"] else '<span class="botao desativado">Sem dashboard</span>'
    )
    links = "".join(
        f'<a href="{esc(a["url"])}" target="_blank" rel="noopener">{esc(a["nome"])}</a>' for a in e["arquivos"]
    )
    busca = esc(f'{e["nome"]} {e["pasta"]} {e["trecho"]}'.lower())
    return f"""
      <article class="card" data-busca="{busca}">
        <h2>{esc(e["nome"])}</h2>
        <p class="trecho">{trecho}</p>
        <div class="acoes">{botao}<nav class="arquivos">{links}</nav></div>
      </article>"""


def pagina(entregas: list[dict], repo: str) -> str:
    agora = datetime.now(timezone(timedelta(hours=-3))).strftime("%d/%m/%Y às %H:%M")
    cards = "".join(card(e) for e in entregas) or '<p class="nenhuma">Nenhuma entrega publicada ainda.</p>'
    slides = json.dumps(
        [{"nome": e["nome"], "url": e["dashboard"]} for e in entregas if e["dashboard"]], ensure_ascii=False
    ).replace("</", "<\\/")
    total = len(entregas)
    rotulo = "entrega" if total == 1 else "entregas"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Galeria de Dashboards</title>
<style>
  :root {{
    --fundo: #f4f6f9; --card: #ffffff; --texto: #1b2430; --suave: #5a6574; --borda: #dde3ea;
    --destaque: #1f3a5f; --destaque-texto: #ffffff; --sombra: 0 1px 3px rgba(20,30,45,.08);
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --fundo: #11161d; --card: #1a212b; --texto: #e6ebf1; --suave: #9aa6b4; --borda: #2b3542;
      --destaque: #7fb0e6; --destaque-texto: #0d1520; --sombra: none;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--fundo); color: var(--texto);
         font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; line-height: 1.5; }}
  header, main, footer {{ max-width: 1200px; margin: 0 auto; padding: 0 16px; }}
  header {{ padding-top: 40px; padding-bottom: 8px; }}
  .sobre {{ color: var(--suave); font-size: 14px; margin: 0; letter-spacing: .02em; }}
  h1 {{ margin: 6px 0 4px; font-size: clamp(26px, 4vw, 36px); color: var(--destaque); }}
  .barra {{ display: flex; flex-wrap: wrap; gap: 12px; align-items: center; margin: 20px 0 24px; }}
  .barra input {{ flex: 1 1 260px; padding: 10px 14px; font-size: 15px; border-radius: 8px;
                 border: 1px solid var(--borda); background: var(--card); color: var(--texto); }}
  .contagem {{ color: var(--suave); font-size: 14px; }}
  .grade {{ display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); padding-bottom: 40px; }}
  .card {{ background: var(--card); border: 1px solid var(--borda); border-radius: 12px; padding: 20px;
          display: flex; flex-direction: column; box-shadow: var(--sombra); }}
  .card h2 {{ margin: 0 0 8px; font-size: 18px; }}
  .trecho {{ margin: 0 0 16px; color: var(--suave); font-size: 14.5px; flex: 1; }}
  .vazio {{ font-style: italic; }}
  .acoes {{ display: flex; flex-wrap: wrap; gap: 10px 14px; align-items: center; }}
  .botao, button {{ display: inline-block; padding: 8px 14px; border-radius: 8px; border: 0; cursor: pointer;
                   background: var(--destaque); color: var(--destaque-texto); text-decoration: none;
                   font-size: 14px; font-weight: 600; font-family: inherit; }}
  .botao.desativado {{ background: var(--borda); color: var(--suave); cursor: default; }}
  .arquivos {{ display: flex; gap: 12px; font-size: 13px; }}
  .arquivos a {{ color: var(--destaque); }}
  .nenhuma {{ color: var(--suave); }}
  footer {{ color: var(--suave); font-size: 13px; padding-bottom: 32px; }}
  footer a {{ color: var(--destaque); }}
  #palco {{ position: fixed; inset: 0; background: #000; display: none; flex-direction: column; z-index: 10; }}
  #palco.ativo {{ display: flex; }}
  #palco .topo {{ display: flex; align-items: center; gap: 12px; padding: 8px 16px; background: #10151c; color: #e6ebf1; font-size: 15px; }}
  #palco .topo strong {{ flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  #palco .topo button {{ background: #2b3542; color: #e6ebf1; padding: 6px 12px; }}
  #palco iframe {{ flex: 1; border: 0; width: 100%; background: #fff; }}
</style>
</head>
<body>
<header>
  <p class="sobre">PCDIA – Storytelling de Dados · Mestrado em Administração Pública · IDP · Prof. Danny</p>
  <h1>Galeria de Dashboards · Atividade 1</h1>
</header>
<main>
  <div class="barra">
    <input id="busca" type="search" placeholder="Buscar por nome ou história..." aria-label="Buscar entregas">
    <span class="contagem" id="contagem">{total} {rotulo}</span>
    <button id="apresentar" type="button">▶ Modo apresentação</button>
  </div>
  <section class="grade" id="grade">{cards}
  </section>
</main>
<footer>
  Atualizada em {agora} · <a href="https://github.com/{html.escape(repo)}">Repositório da atividade</a>
</footer>

<div id="palco" role="dialog" aria-label="Modo apresentação">
  <div class="topo">
    <button type="button" id="anterior" aria-label="Anterior">←</button>
    <strong id="titulo-palco"></strong>
    <span id="posicao"></span>
    <button type="button" id="proximo" aria-label="Próximo">→</button>
    <button type="button" id="fechar" aria-label="Fechar">✕ Sair</button>
  </div>
  <iframe id="quadro" title="Dashboard"></iframe>
</div>

<script>
  const SLIDES = {slides};
  const busca = document.getElementById('busca');
  const cards = [...document.querySelectorAll('.card')];
  const contagem = document.getElementById('contagem');
  busca.addEventListener('input', () => {{
    const q = busca.value.trim().toLowerCase();
    let n = 0;
    cards.forEach(c => {{ const ok = c.dataset.busca.includes(q); c.hidden = !ok; if (ok) n++; }});
    contagem.textContent = n + (n === 1 ? ' entrega' : ' entregas');
  }});

  const palco = document.getElementById('palco');
  const quadro = document.getElementById('quadro');
  let atual = 0;
  function mostrar(i) {{
    if (!SLIDES.length) return;
    atual = (i + SLIDES.length) % SLIDES.length;
    quadro.src = SLIDES[atual].url;
    document.getElementById('titulo-palco').textContent = SLIDES[atual].nome;
    document.getElementById('posicao').textContent = (atual + 1) + ' / ' + SLIDES.length;
  }}
  function abrir() {{
    if (!SLIDES.length) return;
    palco.classList.add('ativo');
    mostrar(atual);
    if (palco.requestFullscreen) palco.requestFullscreen().catch(() => {{}});
  }}
  function fechar() {{
    palco.classList.remove('ativo');
    quadro.removeAttribute('src');
    if (document.fullscreenElement) document.exitFullscreen().catch(() => {{}});
  }}
  document.getElementById('apresentar').addEventListener('click', abrir);
  document.getElementById('anterior').addEventListener('click', () => mostrar(atual - 1));
  document.getElementById('proximo').addEventListener('click', () => mostrar(atual + 1));
  document.getElementById('fechar').addEventListener('click', fechar);
  document.addEventListener('keydown', e => {{
    if (!palco.classList.contains('ativo')) return;
    if (e.key === 'ArrowRight') mostrar(atual + 1);
    else if (e.key === 'ArrowLeft') mostrar(atual - 1);
    else if (e.key === 'Escape') fechar();
  }});
  document.addEventListener('fullscreenchange', () => {{
    if (!document.fullscreenElement && palco.classList.contains('ativo')) fechar();
  }});
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera a galeria de entregas.")
    parser.add_argument("--saida", default=str(RAIZ / "index.html"), help="Arquivo HTML de saída.")
    args = parser.parse_args()

    repo = os.environ.get("GITHUB_REPOSITORY", REPO_PADRAO)
    entregas = coletar(repo)
    Path(args.saida).write_text(pagina(entregas, repo), encoding="utf-8")
    print(f"Galeria gerada em {args.saida} com {len(entregas)} entrega(s).")


if __name__ == "__main__":
    main()
