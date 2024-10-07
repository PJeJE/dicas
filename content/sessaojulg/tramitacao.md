---
title: "Tramitação automática em tarefas de sessão"
date: 2024-09-27T15:58:31-03:00
weight: 4
---

## Tramitação automática após ações em telas do PJe

O PJe tem a capacidade de realizar tramitações automáticas de fluxo em algumas situações específicas. Esse procedimento é muito útil na sinalização para o servidor que houve alguma mudança no processo realizada por outro unidade.  Descreveremos aqui as tramitações automáticas realizadas no contexto das sessões de julgamento.

## Tramitação após liberação do processo para julgamento

Em geral, quem constrói os documentos de sessão e os disponibiliza para julgamento é o **gabinete do relator**. Já quem monta a sessão de julgamento é o **Assessor de plenário**. Quem constrói o acórdão, em alguns TREs, é o próprio **gabinete que assinará** o acórdão. Em outros é a **Secretaria Judiciária**. Dessa forma, é importante a notificação de finalização de cada passo nesse processo para que as diferentes unidades possam realizar seu trabalho de forma tempestiva. 

No **gabinete do relator**, quando o processo estiver na tarefa **Conferir Relatório, Voto e Ementa** e o usuário selecionar uma das transições **Processo liberado para julgamento sessão presencial** ou **Processo liberado para julgamento sessão virtual**, o sistema automaticamente iniciará a tarefa **Aguardar Julgamento do Processo**, para o caso do TSE, ou **Iniciar Acórdão - SJD**, para os TREs que têm a **Secretaria Judiciária** como responsável pela elaboração do acórdão. Para os TREs onde o gabinete elabora o acórdão, a tarefa **Selecionar documentos para acórdão - Gabinete** será iniciada. Essas tarefas serão iniciadas caso não existam ainda. 
Também nesse momento, o fluxo do **Assessor de plenário** será iniciado. Sobre o fluxo do assessor de plenário, temos um manual disponível neste link: https://pjeje.github.io/dicas/docs/manual_fluxo_da_asplen.pdf.

{{% notice note %}}
Para trocar do gabinete para a Secretaria Judiciária como responsável pela elaboração do acórdão ou vice-versa, o parâmetro a ser utilizado é **pje:je:elaboraAcordaoGabinete**, ou seja, caso esteja marcado como **true**, o gabinete é o responsável, caso esteja marcado como **false**, a secretaria é a responsável.
{{% /notice %}}

Caso o processo esteja em uma das tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** e for retirado de pauta ou for a julgamento e for adiado,  o sistema automaticamente encaminhará o processo para as tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual** respectivamente, de forma que o gabinete poderá, a seu tempo, novamente liberá-lo para julgamento.

## Tramitação após processo incluído em pauta

Quando o processo estiver em uma das tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual** e o assessor de plenário realizar sua inclusão em alguma pauta, o sistema automaticamente encaminhará o processo para as tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** respectivamente.

Caso o processo esteja em uma das tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** e for retirado de pauta ou for a julgamento e for adiado,  o sistema automaticamente encaminhará o processo para as tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual** respectivamente.

{{% notice note %}}
Caso o processo seja colocado manualmente na tarefa de incluído em pauta antes de ter realmente sido incluído e o assessor de plenário realizar a inclusão do processo em alguma pauta, o sistema o tramitará para as tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual**. 
{{% /notice %}}

## Tramitação após encerramento do julgamento do processo

A tramitação de que trata essa seção ocorrerá após lançamento do movimento de julgamento **Deliberado em sessão**.

Quando o processo estiver em uma das tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** e o assessor de plenário registrar o movimento de julgamento do processo, o sistema tramitará o processo automaticamente. Nessa tramitação, ele verificará o resultado do julgamento.

+ se o processo foi **Julgado**, o sistema finalizará o fluxo de decisão colegiada e o processo retornará para as tarefas de cumprimento (**Analisar Processos** ou **Analisar Processos - Urgentes** caso não tenha sido registrado movimento da árvore de Magistrado, conforme TPU,  **Analisar determinação** ou **Analisar determinação - Urgentes** caso exista algum movimento daquele tipo lançado pela instância atual naquele processo.)
+ caso tenha sido julgado e tenha sido marcado julgamento de mérito e o órgão julgador vencedor tenha sido marcado como distinto do relator, o sistema redistribuirá o processo para o órgão julgador vencedor, lançando o movimento **Redistribuído por Determinação Judicial em razão de lavratura de acórdão**.
+ se o processo não tiver sido **Julgado**, o sistema o tramitará automaticamente para as tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual**, conforme o caso.
 
{{% notice note %}}
Para tribunais que tenham o parâmetro **pje:je:redistribuiMerito** configurado com o valor **false**, o sistema não fará a redistribuição automática para o caso de órgão julgador vencedor diferente do órgão julgador relator. 
{{% /notice %}}

Caso o processo tenha sido julgado e estiver em uma das tarefas **Minutar Relatório Voto e Ementa**, **Conferir Relatório Voto e Ementa**, **Revisar Relatório Voto e Ementa**, **Aguarda Sessão de Julgamento**, **Aguarda Sessão de Julgamento Virtual**, a fim de impedir que o usuário utilize essas tarefas para edição de documentos da sessão após processo julgado, o sistema tramitará o processo automaticamente para a tarefa **Processo julgado**. Esse impedimento existe para evitar inconsistências na construção de documentos de sessão. 

A tarefa **Processo julgado** notifica o usuário que **Esse processo foi julgado e seus documentos não podem ser editados pela tarefa anterior.** O usuário terá duas opções: **Finalizar procedimentos pós julgamento** e **Finalizar fluxo de decisão colegiada**.

{{% notice note %}}
A tramitação automática para a tarefa **Processo julgado** só ocorrerá se o processo tiver sido tramitado em uma das tarefas do fluxo de decisão colegiada após a atualização realizada em outubro de 2024. 
{{% /notice %}}

A transição **Finalizar procedimentos pós julgamento** fará com que o processo seja redistribuído, se for o caso, e que seja acrescentada a situação processual **Confecção do acórdão**. Também iniciará o fluxo de acórdão, caso não esteja ainda aberto, além de finalizar o fluxo de colegiado, retornando o processo para cumprimento. A transição **Finalizar fluxo de decisão colegiada** só finalizará o fluxo de colegiada, retornando o processo para cumprimento.

 Se o processo for julgado e ainda estiver em uma das tarefas de construção de documentos da sessão, realize a tramitação do processo entre as tarefas até que seja possível utilizar a transição **Verificar julgamento do processo**, o que finalizará o fluxo da mesma forma que a opção **Finalizar procedimentos pós julgamento** mencionada acima. A tramitação segue as instruções disponibilizadas na seção [Documentos de sessão](/sessaojulg/secretario_sessao/#construção-de-documentos-da-sessão-relatório-voto-e-ementa).
