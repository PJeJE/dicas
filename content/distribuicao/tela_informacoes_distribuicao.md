---
title: "Informações da Distribuição"
date: 2026-04-24T13:04:05-03:00
weight: 7
---

A funcionalidade **Informações da Distribuição** permite consultar, para qualquer processo já distribuído, o passo a passo completo do algoritmo de distribuição — quais órgãos foram avaliados, quais filtros foram aplicados, qual cargo foi sorteado e como o acumulador foi atualizado. É a principal ferramenta para entender por que um processo foi para um determinado órgão julgador.

## Como acessar

{{% notice info %}}
**Caminho no sistema:** Processo → Pesquisar → Informações de distribuição
{{% /notice %}}

Ao entrar, o sistema exibe a tela de pesquisa com alguns filtros e a listagem de todas as distribuições registradas.

## A tela de listagem

Cada linha representa **uma distribuição** (ou redistribuição) do processo. Se o processo já passou por mais de uma distribuição, aparecerão várias linhas — da mais antiga para a mais recente.

### Filtros disponíveis

| Campo | Para que serve |
|-------|----------------|
| Número do Processo | Filtra pelo número exato de um processo específico. |
| Órgão Julgador Colegiado | Disponível apenas em 2º grau/TSE. |
| Órgão Julgador | Filtra pelo órgão julgador que recebeu o processo. |
| Tipo de Distribuição | Filtra pelo motivo da distribuição (ver tabela abaixo). |

### Colunas da listagem

| Coluna | Descrição |
|--------|-----------|
| Número do Processo | O número do processo cuja distribuição foi registrada. |
| Data do Log | Data e hora em que a distribuição aconteceu (formato `dd/MM/yy HH:mm`). |
| Órgão Julgador Colegiado | Órgão colegiado associado (só em 2º grau/TSE). |
| Órgão Julgador | Órgão julgador definido como destino do processo. |
| Órgão Julgador Cargo | Cargo específico dentro do órgão julgador (ex.: Juiz Titular, Juiz Auxiliar). |
| Tipo de Distribuição | Código que resume o motivo do evento (ver tabela abaixo). |

### Tipos de Distribuição

A coluna *Tipo de Distribuição* responde, sem precisar abrir o log, por que aquela distribuição aconteceu. Os tipos mais comuns na Justiça Eleitoral são:

| Código | Significado |
|:------:|-------------|
| **S**  | Por sorteio (caso comum) |
| **I**  | Incidental (o processo herdou o órgão julgador do processo principal) |
| **PP** | Por prevenção — Art. 260 do Código Eleitoral |
| **PD** | Por dependência |
| **EN** | Por encaminhamento (redistribuição) |
| **CE** | Por competência exclusiva |
| **Z**  | Por sucessão |
| **A**  | Automática (outros casos) |

## A aba "Itens do Log"

Ao clicar no ícone **Selecionar** em uma linha, a aba **Itens do Log** é exibida. Ela mostra, em ordem cronológica, cada etapa do algoritmo naquele evento de distribuição.

| Coluna | Descrição |
|--------|-----------|
| Item | Texto escrito pelo algoritmo: jurisdição, filtros aplicados, cargos elegíveis, cargo sorteado, pesos calculados. |
| Data | Momento em que o item foi gravado. |
| Criticidade | No fluxo de distribuição, aparece sempre como *Informação* (**I**). |

## O algoritmo simplificado

O PJe executa a distribuição em oito etapas. As duas primeiras trabalham sobre o **órgão julgador**; da terceira em diante, o algoritmo passa a operar no nível do **cargo** (um mesmo órgão pode ter mais de um cargo configurado para receber distribuição, como Juiz Titular e Juiz Auxiliar — e o acumulador, a flag *ativo* e a flag *recebe distribuição* ficam no cargo).

![Fluxo simplificado da distribuição no PJe](fluxo_distribuicao.svg)

{{% notice tip %}}
**Fator de 25%** — No passo 6, cada cargo que **não passou** no filtro da distância máxima (passo 5) ainda tem **25% de chance** de ser repescado e participar do sorteio. Esse mecanismo aumenta a imprevisibilidade da distribuição. A lista de *Cargos elegíveis* que aparece no log **já contempla** os cargos repescados — se aparecer um cargo com acumulador bem acima dos demais, foi esse fator que o trouxe.
{{% /notice %}}

## Mapeamento entre os passos do algoritmo e as mensagens do log

A pergunta mais comum de quem abre o log é: *"qual linha corresponde a qual passo?"*. A correspondência é direta nos passos 1, 2, 5-6, 7 e 8. Os passos 3 e 4 são internos (não geram linha própria); seus resultados alimentam o passo 5-6.

### Etapas principais

| Passo | Descrição no algoritmo | Mensagem(ns) correspondente(s) no log |
|:----:|------------------------|---------------------------------------|
| **1** | Recuperar órgãos da jurisdição. | *Dimensão espacial — Jurisdição: … — Órgãos judiciais selecionados: …*<br>(em 2º grau/TSE, acrescenta uma linha análoga com os órgãos colegiados.) |
| **2** | Filtrar órgãos competentes. | *Dimensão material e procedimental — Órgãos judiciais selecionados: …*<br>Pode acrescentar blocos complementares (Dimensão alçada, funcional ou pessoal) quando o cadastro das competências exigir. |
| **3 e 4** | Filtrar cargos ativos e recuperar acumuladores. | *Sem mensagem própria.* Os valores recuperados alimentam o passo seguinte. |
| **5 e 6** | Aplicar a distância máxima e formar a lista de cargos elegíveis (incluindo os repescados pelos 25%). | *Distância máxima de distribuição: …*<br>*Cargos elegíveis (após aplicação da distância máxima…): …*<br>A lista registrada já contempla tanto os cargos que passaram pela distância máxima quanto os repescados pelos 25%. |
| **7** | Sortear um cargo entre os elegíveis. | *Órgão julgador sorteado: …*<br>*Cargo sorteado: …*<br>Em processo incidental, *sorteado* aparece como *originário*. Em prevenção do Art. 260, esse bloco é substituído por *Processo paradigma*, *Órgão julgador prevento* e *Cargo prevento*. |
| **8** | Atualizar acumulador do cargo sorteado. | *Peso processual: …*<br>*Peso de distribuição: …*<br>Recurso interno não gera estas linhas. |

### Situações que adicionam linhas extras

As situações abaixo não correspondem a um passo do algoritmo-padrão, mas acrescentam blocos próprios no log sempre que ocorrem.

| Situação | Mensagem(ns) adicional(is) no log |
|----------|-----------------------------------|
| Redistribuição | *Redistribuído por &lt;motivo&gt;. Órgãos judiciais selecionados após exclusão dos impedidos: …*<br>Aparece como primeira linha do log quando o evento é uma redistribuição. O `<motivo>` vem do tipo de redistribuição (impedimento, suspeição, prevenção, encaminhamento etc.). |
| Conflito de competência | *Conflito de competência — Competência selecionada pelo usuário: … — Órgãos judiciais selecionados: …*<br>*Competência definida: …*<br>Aparecem quando a distribuição foi iniciada com mais de uma competência candidata. |
| Colegiado (2º grau/TSE) | *Órgão julgador colegiado sorteado: …*<br>*Quantidade de participantes no sorteio: X. Mínimo permitido: Y*<br>Linhas específicas de 2º grau/TSE; acompanham o passo 7. |

## Dicas para ler um log

- **Comece pelo final** (o sorteio) e suba o log: o encolhimento das listas entre blocos de *Dimensão …* mostra qual filtro removeu qual órgão.
- Se na lista *Cargos elegíveis* aparecer um cargo com acumulador bem acima dos demais, foi o **fator de 25%** que o trouxe.
- Em prevenção do Art. 260, não há sorteio — as linhas que aparecem são *Distribuição por prevenção conforme Art. 260*, *Processo paradigma*, *Órgão julgador prevento* e *Cargo prevento*.
- Em redistribuição, a **primeira linha** já indica o motivo (*Redistribuído por …*). Abrir o log mais antigo primeiro dá o contexto original; o mais recente traz o motivo da redistribuição.
- Recursos internos normalmente não exibem as linhas de *Peso processual* e *Peso de distribuição*, porque a atualização do acumulador não acontece nesses casos.

## Perguntas frequentes

{{% expand "Por que o mesmo processo aparece em várias linhas?" %}}
Cada linha é uma **distribuição** ou **redistribuição** distinta. Se o processo foi redistribuído uma ou mais vezes, cada evento é registrado separadamente.
{{% /expand %}}

{{% expand "Por que não aparece o cargo na lista de elegíveis apesar de ele atender à competência?" %}}
Verifique as linhas *Dimensão …* no log: algum filtro pode tê-lo removido (alçada, dimensão funcional, dimensão pessoal). Se o cargo passou pelos filtros mas não aparece em *Cargos elegíveis*, o acumulador dele provavelmente está acima do limite da distância máxima **e** ele não foi repescado pelos 25%.
{{% /expand %}}

{{% expand "O que significa 'Cargos elegíveis (após aplicação da distância máxima)'?" %}}
É a lista final que foi ao sorteio. Inclui tanto os cargos cujo acumulador estava dentro do limite da distância máxima quanto os que foram repescados pelo fator de 25%.
{{% /expand %}}

{{% expand "Qual a diferença entre 'Órgão julgador sorteado', 'originário' e 'prevento'?" %}}
*Sorteado* é o caso padrão (passou pelo sorteio). *Originário* aparece em processos incidentais — o órgão é herdado do processo principal, sem sorteio. *Prevento* aparece em prevenção do Art. 260 do Código Eleitoral — o órgão é herdado do processo paradigma.
{{% /expand %}}

{{% expand "Posso alterar o peso do cargo para mudar a distribuição?" %}}
Tecnicamente sim. Na Justiça Eleitoral, a diretriz é que todos os cargos tenham o **mesmo peso** — e é essa uniformidade que neutraliza o efeito do *P*_cargo na fórmula de *P*_dist. Se algum cargo for configurado com peso diferente, a distribuição passa a ser afetada: cargos com peso maior recebem *P*_dist menor e tendem a ser sorteados mais vezes até equilibrar o acumulador. Alterações devem seguir as diretrizes do órgão.
{{% /expand %}}
