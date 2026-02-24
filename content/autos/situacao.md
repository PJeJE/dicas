---
title: "Situações processuais"
date: 2023-05-08T20:00:45-03:00
weight: 5
---

## Introdução

As situações processuais foram criadas no PJe para possibilitar a implementação da redistribuição por sucessão, mas elas têm reflexos e utilidades múltiplas.

Elas são "etapas" do ciclo de vida do processo cadastradas pelo próprio tribunal e utilizadas no fluxo de tramitação para que se possa recuperar os processos de acordo com esse parâmetro.

{{% notice info %}}
As situações são cumulativas, salvo se forem encerradas. 
{{% /notice %}}

A utilização de situações processuais permite identificar a etapa em que o processo se encontra sem que seja necessário recorrer ao histórico de tramitação do processo.
Sem a situação processual a realização de algumas consultas, mesmo que por meio do banco de dados, é uma tarefa complexa, pois varia muito de acordo com as maneiras de trabalhar de cada tribunal. Em muitos casos se faz necessário um conjunto de movimentos e tarefas para chegar ao resultado desejado. 

{{% notice info %}}
Quando um processo é arquivado, a situação em andamento também é finalizada.
{{% /notice %}}

As **Situações do processo** podem ser visualizadas por meio de um ícone de relógio localizado no canto superior direito dos autos do processo para quem tem os papeis **pje:papel:visualizaSituacoesAtuais**, que permite visualizar as situações atuais do processo, e **pje:papel:visualizaSituacoes**, que permite visualizar as atuais e as já finalizadas. 

{{% notice info %}}
As situações processuais são registradas por capa, ou seja, o processo principal pode estar **Em andamento**, e o recurso, quando houver, pode estar **Arquivado**.
{{% /notice %}}

Abaixo estão listadas as situações processuais definidas até o momento para o TSE e para os TREs. Cada situação é identificada por um código e pode ser acessada por meio do link correspondente.

| Código | Descrição |
| --- | --- |
| [jus:suspenso](#jussuspenso) | Situação de processos suspensos. |
| [jus:andamento](#jusandamento) | Situação de processos em andamento. |
| [jus:arquivado](#jusarquivado) | Situação de processos arquivados. |
| [jus:arquivoprov](#jusarquivoprov) | Situação de processos arquivados provisoriamente. |
| [jus:remetido](#jusremetido) | Situação de processos expedidos e devolvidos a origem. |
| [jus:remetidostf](#jusremetidostf) | Situação de processos aguardando retorno do STF. |
| [jus:aguardasessao](#jusaguardasessao) | Situação de processos aguardando sessão de julgamento. |
| [jus:emjulgamento](#jusemjulgamento) | Situação de processos aguardando julgamento. |
| [jus:acordao](#jusacordao) | Situação de processos com julgamento finalizado. |
| [jus:acordaofinalizado](#jusacordaofinalizado) | Situação de processos com acórdão assinado e finalizado. |
| [jus:corregedoria](#juscorregedoria) | Situação de processos administrativos de corregedoria (DP, RSE, CO). |
| [jus:prazovista](#jusprazovista) | Situação de processos com prorrogação de prazo para retorno dos autos após pedido de vista |
| [jus:transitojulgado](#justransitojulgado) | Situação de processos que tiveram o registro de trânsito em julgador realizado |
| [jus:julgado](#jusjulgado) | Situação de processos que tiveram algum movimento da árvore de julgamento (193) lançado naquela instância |

{{% notice warning %}}
As situações acima foram documentadas com base no fluxo do TSE, sendo aplicadas, no que cabe, para as instâncias de segundo grau dos Regionais.
{{% /notice %}}

## Cenários

### jus:suspenso

1. Quando o processo entra na tarefa **Manter Processos Suspensos ou Sobrestados**. Ao sair da tarefa por meio da transição **Reativar processo suspenso ou sobrestado**, a situação é finalizada e é acrescentada a situação **jus:andamento**.
2. Quando o processo entra na tarefa **Manter Processos Suspensos ou Sobrestados - Cor**. Ao sair da tarefa por meio da transição **Reativar processo suspenso ou sobrestado - Cor**, a situação é finalizada e é acrescentada a situação **jus:andamento**.
3. Quando o processo entra na tarefa **Manter Processo Suspenso ou Sobrestado**. Ao sair da tarefa por meio da transição **Reativar processo suspenso ou sobrestado**, a situação é finalizada e é acrescentada a situação **jus:andamento**.

### jus:andamento

1. Quando um processo é protocolado e entra nas tarefas de triagem (Verificar e certificar dados do processo e similares urgentes)
2. Quando um recurso é protocolado e entra em umas das tarefas de análise (analisar determinação, analisar processo e similares urgentes)
3. Quando um processo é reativado após arquivamento.

{{% notice note %}}
No TSE e nos TREs, sempre que essa situação for registrada, as situações **jus:suspenso**, **jus:arquivado**, **jus:remetido**, **jus:remetidostf** e **jus:arquivoprov** são encerradas. 
{{% /notice %}}

{{% notice note %}}
No TSE e nos TREs, a situação **jus:andamento** é finalizada quando as situações **jus:suspenso**, **jus:arquivado**, **jus:remetido**, **jus:remetidostf** e **jus:arquivoprov** são registradas.
{{% /notice %}}


### jus:arquivado

1. Quando um processo entra na tarefa **Manter Processos Arquivados - Processo Corregedoria**. Ao sair da tarefa por meio da transição **Desarquivar processo**, a situação é finalizada e é acrescentada a situação **jus:andamento**.
2. Quando um processo sai do **Verificar Pendências** por meio da transição **Realiza Baixa para arquivamento**. Ao sair da tarefa **Manter recurso arquivado** ou **Manter processo arquivado** por meio da transição **Reativa recurso** ou **Reativa Processo**, a situação é finalizada e é acrescentada a situação **jus:andamento**.
3. Quando um processo sai do **Manter Processos Expedidos** por meio da transição **Enviar para arquivo**. Ao sair da tarefa **Manter recurso arquivado** ou **Manter processo arquivado** por meio da transição **Reativa recurso** ou **Reativa Processo**, a situação é finalizada e é acrescentada a situação **jus:andamento**.
4. Quando um processo sai das tarefas **Verficar Pendências - Processo Corregedoria**, **Analisar Determinações - Corregedoria** ou **Analisar Processo - Corregedoria** por meio da transição **Remeter para arquivamento**. Ao sair da tarefa **Manter recurso arquivado** ou **Manter processo arquivado** por meio da transição **Reativa recurso** ou **Reativa Processo**, a situação é finalizada e é acrescentada a situação **jus:andamento**.
5. Quando um processo sai da tarefa **Devolver Processo Corregedoria a origem** após devolução (por meio da transição oculta **Prosseguir**). Ao sair da tarefa **Manter recurso arquivado** ou **Manter processo arquivado** por meio da transição **Reativa recurso** ou **Reativa Processo**, a situação é finalizada e é acrescentada a situação **jus:andamento**. 

### jus:arquivoprov

1. Quando um processo entra na tarefa  **Manter processos arquivados provisoriamente** ou na tarefa **Manter Processo Arquivamento Provisório**. Ao sair da tarefa por meio da transição **Desarquivar Processo**, a situação é finalizada e é acrescentada a situação **jus:andamento**.
2. Quando um processo sair da tarefa  **Registrar arquivamento provisório** por meio da transição **Arquivar Provisoriamente**. Ao sair da tarefa **Manter processo arquivamento provisório** por meio da transição **Desarquivar Processo**, a situação é finalizada. 

### jus:remetido

1. Quando um processo entra na tarefa **Manter Processos Expedidos**. A situação é finalizada quando o processo sair da tarefa por meio das transições **Retornar para análise**, **Retornar para análise com registro de movimento** e **Retornar para análise sem registro de movimento**
2. Quando um processo entra nas tarefas **Aguardando apreciação de outra instância - Corregedoria** e **Aguardando apreciação de outra instância - Processo Corregedoria**. A situação é finalizada quando o processo entra nas tarefas **Recebimento de outra instância - Corregedoria** e **Recebimento de outra instância - Processo Corregedoria**, quando também é acrescentada a situação jus:andamento.
3. Quando um processo entra na tarefa **Manter Processos Devolvidos a Origem**. A situação é finalizada quando o processo sair da tarefa por meio das transições **Prosseguir** e **Desarquivar processo**. 
4. Quando um processo entra em uma das seguintes tarefas do segundo grau: **Aguardando apreciação de outra instância**, **Processos remetidos ao TSE** e **Processos remetidos à zona**. A situação é finalizada quando o processo sair da tarefa por meio da transição **Reativar com registro de movimento**.
5. Quando um processo entra na tarefa **Aguardando Apreciação do TRE**. A situação é finalizada quando o processo entrar na tarefa **Recebimento do TRE** ou ao sair da tarefa **Aguardando apreciação do TRE** (o **a** de **apreciação** minúsculo).
6. Quando um processo entra na tarefa **Manter Processos Devolvidos**. A situação é finalizada quando o processo entrar na tarefa **Recebimento de Processos**.


### jus:remetidostf

1. Quando um processo entra na tarefa **Aguardando retorno do STF**. A situação é finalizada quando o processo entrar na tarefa **Recebimento do STF**, quando também é acrescentada a situação jus:andamento.

### jus:aguardasessao

1. Quando um processo entra nas tarefas **Aguarda Sessão de Julgamento** e **Aguarda Sessão de Julgamento Virtual**. A situação é finalizada quando o processo sair das tarefas.

### jus:emjulgamento

1. Quando um processo entra nas tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual**. A situação é finalizada quando o processo sair das tarefas.

### jus:acordao

1. Quando um processo sai das tarefas **Aguarda Julgamento - incluído em pauta** e **Aguarda Julgamento - incluído em pauta virtual** após o julgamento ser finalizado. A transição que aciona o teste para essa condição é a **Testa existência de julgamento**. Em caso positivo, a situação jus:acordao será registrada.

### jus:acordaofinalizado

1. Quando um processo entra na tarefa **Analisar Acórdão Assinado - SJD**. Nesse momento, a situação jus:acordao é finalizada.

### jus:corregedoria

1. Quando um processo entra na tarefa **Verificar dados - Processo Corregedoria**. 

### jus:prazovista

1. Quando um processo sai de uma das tarefas **Pedido de providência - vistor**, **Revisar pedido de providência - vistor** ou **Assinar pedido de providência - vistor** por meio de assinatura do ato judicial.

{{% notice note %}}
A situação **jus:prazovista** nunca se encerra.
{{% /notice %}}

### jus:transitojulgado

1. Quando um processo sai da tarefa **Elaborar certidão de trânsito em julgado** por meio de assinatura da certidão. 

### jus:julgado

1. Nos TREs e TSE, quando um processo sai de uma das seguintes tarefas **Lançar movimentos de Julgamento Colegiado**, **Lançar movimentos de julgamento colegiado**, **Lançar movimento** ou  **Lançar movimento - Corregedoria** após ser lançado um movimento da árvore de julgamento (código 193). Nos ambientes de primeiro grau, quando um processo sai da tarefa **Lançar movimentação** por meio da transição **Audiências - ZE** após ser lançado um movimento da árvore de julgamento (código 193) ou após sair da tarefa **Lançar Movimentação Processual**, também após ser lançado um movimento da árvore de julgamento (código 193). A situação é finalizada por meio do acionamento da transição **Encerrar situação processual Julgado**. Essa transição aparece nas tarefas de análise (**Analisar Processos - Urgentes**, **Analisar Processos**, **Analisar determinação - Urgentes**, **Analisar determinação**, **Analisar Determinações**, **Analisar Determinações - Urgentes**, **Analisar Processo**, **Analisar Processo - Urgentes**) e só aparecerá caso o processo tenha a situação jus:julgado e não tenha movimento ativo da árvore de julgamento lançado após a data de autuação. Esse procedimento é útil quando houver um lançamento de movimento da árvore e uma posterior inativação/exclusão do movimento por qualquer meio. 
