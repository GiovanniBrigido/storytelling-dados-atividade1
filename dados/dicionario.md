# Dicionário de dados — eleitos.csv

## Estrutura e cobertura

O arquivo `eleitos.csv` é uma tabela única, com **11.106 linhas, 72 colunas e 5.553 municípios**. Cada linha representa uma pessoa: prefeito ou vice-prefeito. Cada município tem duas linhas ligadas pelo mesmo `id_chapa`. Há 5.553 prefeitos e 5.553 vices, em 26 UFs e nas cinco regiões do Brasil; 51 municípios têm turno decisivo igual a 2.

O recorte contém apenas as eleições municipais **ordinárias de 2024** confirmadas pelos critérios desta consolidação. Das 5.569 cidades com eleição municipal em 2024, **16 municípios ficaram fora por falta de confirmação suficiente**.

**Referência da extração: 01/10/2026.** As bases do TSE são atualizadas e incorporam alterações judiciais. Este arquivo descreve candidaturas e resultados de 2024 conforme as evidências disponíveis; não é uma relação dos ocupantes em exercício em 2026.

## Critérios de confirmação

“Confirmado” significa inclusão segundo a evidência especificada abaixo. Os critérios têm níveis de evidência distintos e não equivalem todos a uma confirmação jurídica atual de exercício do mandato.

| classificacao_validacao | Pessoas | Municípios | Evidência e interpretação |
| --- | ---: | ---: | --- |
| `ELEITO_ATUAL_TSE` | 11.060 | 5.530 | Candidaturas e arquivos estaduais de eleitos concordam, incluindo a vinculação do vice. Representa o status ELEITO na extração do TSE. |
| `CHAPA_CASSADA_TSE` | 18 | 9 | Chapa mais votada com cassação registrada na candidatura pelo TSE, mantida para o recorte histórico. A eleição passada não implica mandato vigente. |
| `ELEICAO_HISTORICA_DOCUMENTADA` | 28 | 14 | Fonte histórica identificada documenta a eleição, embora o cadastro atual não marque a chapa como eleita. A evidência pode ser reportagem, e não decisão judicial. |

Para um recorte exclusivamente com candidaturas marcadas como ELEITO na extração atual do TSE, use `classificacao_validacao = ELEITO_ATUAL_TSE`: 11.060 pessoas e 5.530 municípios.

## Leitura e interpretação

- **Formato:** CSV com separador `;`, codificação UTF-8 com BOM e vírgula decimal. Um CSV tem uma única tabela; ao importar no Excel, ela pode ser carregada em uma única aba.
- **Identificadores:** importe códigos e números eleitorais como texto para preservar zeros à esquerda. Use `id_candidato_tse` como chave da pessoa neste pleito e `id_chapa` como chave da dupla.
- **Valores ausentes:** células vazias indicam dados não disponíveis, não aplicáveis ou não divulgáveis. Não preencher com zero ou “Não”. Quando a fonte publica “NÃO INFORMADA”, essa indicação é preservada.
- **Perfil pessoal:** características são declarações publicadas pelo TSE; não houve inferência por nome ou imagem. Etnia indígena não equivale a raça/cor nem a pertencimento quilombola. Identidade de gênero, orientação sexual, religião e deficiência não foram inferidas.
- **Reeleição:** a variável é a declaração eleitoral `ST_REELEICAO`, vinculada à eleição confirmada. Não houve auditoria individual do exercício do mandato anterior; sucessões e eleições suplementares podem dificultar comparações com 2020.
- **Contagens de pessoas:** filtre `cargo` para comparar somente prefeitos ou somente vices. Conte municípios por `codigo_municipio_tse` e chapas por `id_chapa`.
- **Votos:** o vice é eleito na mesma chapa e não recebe votação individual separada. Os votos e percentuais da chapa aparecem nas duas linhas. Para somar votos, filtre apenas `cargo = Prefeito` ou mantenha uma linha por `id_chapa`, evitando duplicação.
- **Temporalidade:** idade, partido, ocupação e bens referem-se à candidatura e às datas definidas nos campos. Votos válidos e situações judiciais refletem a extração atual, com possíveis alterações posteriores à eleição.

## Campos

As colunas aparecem na mesma ordem do CSV. “Ausentes” conta somente células vazias, não outras indicações textuais de ausência publicadas pela fonte.

| Campo | Tipo de leitura | Descrição | Ausentes |
| --- | --- | --- | ---: |
| `ano_eleicao` | Inteiro | Ano do pleito ordinário: 2024. | 0 |
| `codigo_municipio_tse` | Texto (código) | Código de cinco dígitos do município na Justiça Eleitoral. Preservar zeros à esquerda. | 0 |
| `municipio` | Texto | Nome do município no cadastro do TSE. | 0 |
| `uf` | Categoria | Sigla da unidade da Federação onde ocorreu a eleição. | 0 |
| `codigo_ibge` | Texto (código) | Código de sete dígitos do município no IBGE. Pareado com o TSE por UF e nome, com 13 correspondências de grafia/denominação explicitamente resolvidas. | 0 |
| `municipio_ibge` | Texto | Nome oficial do município na API de localidades do IBGE consultada na extração. | 0 |
| `uf_nome` | Texto | Nome da unidade da Federação segundo o IBGE. | 0 |
| `regiao` | Categoria | Grande região do IBGE: Norte, Nordeste, Centro-Oeste, Sudeste ou Sul. | 0 |
| `regiao_imediata` | Texto | Região geográfica imediata à qual pertence o município, segundo o IBGE. | 0 |
| `regiao_intermediaria` | Texto | Região geográfica intermediária à qual pertence o município, segundo o IBGE. | 0 |
| `cargo` | Categoria | Cargo da pessoa: Prefeito ou Vice-prefeito. | 0 |
| `codigo_cargo_tse` | Texto (código) | Código do cargo no TSE: 11 = prefeito; 12 = vice-prefeito. | 0 |
| `id_chapa` | Texto | Identificador construído com ano, UF, município TSE e identificador do prefeito. Une as duas pessoas da mesma chapa. | 0 |
| `id_prefeito_tse` | Texto (código) | Identificador SQ_CANDIDATO do prefeito da chapa, repetido nas duas pessoas. | 0 |
| `id_vice_tse` | Texto (código) | Identificador SQ_CANDIDATO do vice da chapa, repetido nas duas pessoas. | 0 |
| `turno_decisivo` | Inteiro | Turno em que a chapa venceu: 1 ou 2. O vice recebe o turno da chapa. | 0 |
| `data_eleicao` | Data (DD/MM/AAAA) | Data do turno decisivo: 06/10/2024 ou 27/10/2024. | 0 |
| `codigo_eleicao_tse` | Texto (código) | Identificador da eleição: 619 = primeiro turno; 620 = segundo turno. Eleições suplementares foram excluídas deste arquivo. | 0 |
| `classificacao_validacao` | Categoria | Critério de inclusão da pessoa. Ver a tabela de critérios de confirmação abaixo. | 0 |
| `eleicao_historica_confirmada` | Categoria | Indicador de inclusão pelos critérios históricos documentados. Todas as linhas deste arquivo apresentam Sim. | 0 |
| `id_candidato_tse` | Texto (código) | SQ_CANDIDATO: identificador da candidatura da pessoa neste pleito. É a chave única de cada linha; não é identificador permanente para cruzar anos diferentes. | 0 |
| `numero_urna` | Texto (código) | Número eleitoral da candidatura. O número do vice corresponde à chapa e não indica votação individual. | 0 |
| `nome_completo` | Texto | Nome completo registrado na candidatura. | 0 |
| `nome_urna` | Texto | Nome usado na urna na eleição de 2024. | 0 |
| `nome_social` | Texto | Nome social publicado pelo TSE, quando disponível. | 11105 |
| `partido` | Categoria | Sigla do partido pelo qual a pessoa concorreu em 2024. Prefeito e vice podem ter partidos diferentes. | 0 |
| `partido_nome` | Texto | Nome completo do partido da candidatura. | 0 |
| `numero_partido` | Texto (código) | Número do partido da pessoa no TSE. Pode diferir do número de urna da chapa, especialmente para o vice. | 0 |
| `tipo_agremiacao` | Categoria | Forma de participação eleitoral declarada: partido isolado, coligação ou federação, conforme o TSE. | 0 |
| `coligacao` | Texto | Nome da coligação; pode apresentar PARTIDO ISOLADO ou FEDERAÇÃO conforme o cadastro. | 0 |
| `composicao_coligacao` | Texto | Partidos e federações que integram a coligação da candidatura. | 0 |
| `federacao` | Texto | Nome da federação partidária da candidatura, quando aplicável. | 9835 |
| `sigla_federacao` | Texto | Sigla ou composição abreviada da federação. | 9835 |
| `genero_tse` | Categoria | Gênero cadastrado no campo DS_GENERO do TSE. Não equivale a um campo de identidade de gênero ou orientação sexual. | 0 |
| `raca_cor_autodeclarada` | Categoria | Raça/cor autodeclarada no registro: branca, parda, preta, amarela ou indígena, conforme publicação do TSE. | 42 |
| `escolaridade` | Categoria | Grau de instrução declarado no registro da candidatura. | 0 |
| `ocupacao_declarada` | Categoria | Ocupação declarada no TSE. Valores como PREFEITO e OUTROS não informam necessariamente a formação profissional. | 0 |
| `estado_civil` | Categoria | Estado civil declarado no registro da candidatura. | 0 |
| `data_nascimento` | Data (DD/MM/AAAA) | Data de nascimento publicada pelo TSE. | 0 |
| `uf_nascimento` | Texto | UF de nascimento publicada no cadastro. | 0 |
| `situacao_totalizacao_atual_tse` | Categoria | Situação da candidatura na extração atual do TSE. Pode ser ELEITO, NÃO ELEITO ou estar vazia em casos históricos, mesmo com inclusão por outra evidência. | 16 |
| `nacionalidade` | Categoria | Nacionalidade declarada no TSE. | 0 |
| `municipio_nascimento` | Texto | Nome do município de nascimento declarado; é diferente do município pelo qual a pessoa concorreu. | 0 |
| `etnia_indigena_autodeclarada` | Texto | Etnia indígena declarada no campo DS_ETNIA_INDIGENA. É uma informação específica de pertencimento indígena, não uma classificação étnica de todas as pessoas. NÃO INFORMADA ou vazio não significa ausência de pertencimento indígena. | 6260 |
| `situacao_julgamento_atual_tse` | Categoria | Situação do julgamento do registro de candidatura na extração atual, incluindo eventual indeferimento posterior. | 0 |
| `situacao_julgamento_pleito` | Categoria | Situação do julgamento do registro no pleito, conforme campo específico do TSE. | 0 |
| `situacao_cassacao_atual_tse` | Categoria | Registro de cassação da candidatura na extração atual. Vazio indica informação não disponível/não aplicável, sem atestar ausência de processos. | 11063 |
| `situacao_diploma_tse` | Categoria | Situação do diploma publicada no campo DS_SITUACAO_DIPLOMA. A ausência não comprova que a pessoa deixou de ser diplomada. | 11106 |
| `situacao_candidatura_totalizacao` | Categoria | Situação da candidatura considerada na totalização, conforme DS_SITUACAO_CANDIDATO_TOT. | 0 |
| `genero_fefc` | Categoria | Classificação publicada em DS_GENERO_FEFC, relativa ao Fundo Especial de Financiamento de Campanha. Manter distinta de genero_tse. | 11106 |
| `raca_cor_fefc` | Categoria | Classificação publicada em DS_COR_RACA_FEFC, relativa ao Fundo Especial de Financiamento de Campanha. Manter distinta de raca_cor_autodeclarada. | 11106 |
| `idade_primeiro_turno` | Inteiro | Idade em anos completos em 06/10/2024, calculada a partir da data de nascimento. | 0 |
| `idade_turno_decisivo` | Inteiro | Idade em anos completos na data do turno decisivo, calculada a partir da data de nascimento. | 0 |
| `idade_posse_2025` | Inteiro | Idade na data de posse prevista (01/01/2025), publicada em NR_IDADE_DATA_POSSE. Não confirma que a pessoa tomou posse. | 0 |
| `candidato_a_reeleicao_tse` | Categoria | Sim/Não da declaração ST_REELEICAO do registro da candidatura. | 0 |
| `reeleito_declaracao_tse` | Categoria | Sim/Não obtido pela combinação de eleição confirmada e declaração ST_REELEICAO. Como o arquivo contém apenas confirmados, coincide com candidato_a_reeleicao_tse. Não representa auditoria individual do mandato anterior. | 0 |
| `quilombola_autodeclarado` | Categoria | Sim/Não de pertencimento quilombola declarado, conforme ST_QUILOMBOLA. | 0 |
| `declarou_bens_tse` | Categoria | Sim/Não de declaração de bens, conforme ST_DECLARAR_BENS. | 0 |
| `bens_declarados_total_reais` | Decimal | Soma dos valores dos bens declarados pela pessoa nesta candidatura, em reais nominais. Zero por ausência de bens somente quando ST_DECLARAR_BENS = N. Não representa patrimônio atual auditado. | 569 |
| `quantidade_bens_declarados` | Inteiro | Número de itens na declaração de bens, após eliminação de duplicatas por eleição, candidatura e ordem do item. | 569 |
| `votos_nominais_chapa` | Inteiro | Soma dos votos nominais por zona eleitoral da chapa, incluindo votos que possam ter sido anulados posteriormente. Valor repetido para prefeito e vice. | 16 |
| `votos_validos_chapa_atual_tse` | Inteiro | Soma dos votos nominais válidos da chapa na extração atual. Valor repetido para prefeito e vice. | 16 |
| `votos_validos_municipio_turno_atual_tse` | Inteiro | Soma dos votos nominais válidos de todas as candidaturas a prefeito no município e turno na extração atual. Valor repetido para prefeito e vice. | 0 |
| `percentual_validos_chapa_atual_tse` | Decimal | 100 × votos válidos da chapa ÷ votos válidos para prefeito no município e turno. Escala de 0 a 100; vazio quando denominador zero. Reflete reprocessamentos atuais e pode diferir do percentual divulgado em 2024. | 18 |
| `data_geracao_candidatos_tse` | Data (DD/MM/AAAA) | Data de geração do arquivo de candidaturas usado na extração. | 0 |
| `hora_geracao_candidatos_tse` | Hora (HH:MM:SS) | Hora de geração do arquivo de candidaturas, conforme publicada pelo TSE. | 0 |
| `data_consulta` | Data (DD/MM/AAAA) | Data de consulta e consolidação da fonte: 01/10/2026. | 0 |
| `fonte_candidatura` | Texto (URL) | URL do ZIP oficial de candidaturas de 2024. | 0 |
| `fonte_complementar` | Texto (URL) | URL do ZIP oficial de informações complementares de candidaturas. | 0 |
| `fonte_resultado` | Texto (URL) | URL do arquivo oficial de resultado utilizado na conferência da chapa. | 0 |
| `fonte_validacao_historica` | Texto (URL) | URL da evidência usada para inclusão. Pode ser arquivo oficial de eleitos, resultado municipal ou reportagem histórica identificada. | 0 |
| `observacao` | Texto | Nota sobre o critério de validação da chapa e as limitações de interpretação. | 0 