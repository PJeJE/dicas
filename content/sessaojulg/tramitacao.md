---
title: "Tramitação automática em tarefas de sessão"
date: 2024-09-27T15:58:31-03:00
weight: 4
---

## Tramitação automática após ações em telas do PJe

O PJe tem a capacidade de realizar tramitações automáticas de fluxo em algumas situações específicas. Descreveremos aqui as tramitações automáticas realizadas no contexto das sessões de julgamento.

## Tramitação após liberação do processo para julgamento

Quando o processo estiver em na tarefa **Conferir Relatório, Voto e Ementa** e o usuário selecionar uma das transições **Processo liberado para julgamento sessão presencial** ou **Processo liberado para julgamento sessão virtual**, o sistema automaticamente iniciará, caso não tenha sido iniciado ainda, os fluxos de aguardando elaboração de acórdão e os fluxos do assessor de plenário. Sobre o fluxo do assessor de plenário, temos um manual disponível neste link: https://pjeje.github.io/dicas/docs/manual_fluxo_da_asplen.pdf.

Caso o processo esteja em uma das tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** e for retirado de pauta ou for a julgamento e for adiado,  o sistema automaticamente encaminhará o processo para as tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual** respectivamente.

## Tramitação após processo incluído em pauta

Quando o processo estiver em uma das tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual** e o assessor de plenário realizar sua inclusão em alguma pauta, o sistema automaticamente encaminhará o processo para as tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** respectivamente.

Caso o processo esteja em uma das tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** e for retirado de pauta ou for a julgamento e for adiado,  o sistema automaticamente encaminhará o processo para as tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual** respectivamente.

{{% notice note %}}
Caso o processo seja colocado manualmente na tarefa de incluído em pauta antes de ter realmente sido incluído e o assessor de plenário realizar a inclusão do processo em alguma pauta, o sistema o tramitará para as tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual**. 
{{% /notice %}}

## Tramitação após encerramento do julgamento do processo

A tramitação de que trata essa seção ocorrerá após lançamento do movimento de julgamento **Deliberado em sessão**.

Quando o processo estiver em uma das tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** e o assessor de plenário registrar o movimento de julgamento do processo, o sistema tramitará o processo automaticamente. Nessa tramitação, ele verificará o resultado do julgamento.

+ se o processo foi **Julgado**, o sistema finalizará o fluxo de decisão colegiada e o processo retornará para as tarefas de cumprimento (**Analisar Processos ou **Analisar Processos - Urgentes** caso não tenha sido registrado movimento da árvore de Magistrado, conforme TPU,  **Analisar determinação** ou **Analisar determinação - Urgentes** caso exista algum movimento daquele tipo lançado pela instância atual.)
+ + caso tenha sido marcado julgamento de mérito e o órgão julgador vencedor tenha sido marcado como distinto do relator, o sistema redistribuirá o processo para o órgão julgador vencedor, lançando o movimento **Redistribuído**.
+ se o processo não tiver sido **Julgado**, o sistema o tramitará automaticamente para as tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual**, conforme o caso.
