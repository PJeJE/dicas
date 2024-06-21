---
title: "Devolução para a origem"
date: 2022-11-29T16:29:32-03:00
weight: 5
---

**Devolver processo à origem** é uma tarefa exclusiva do 2º e 3º graus e deve ser utilizada para devolver um processo para alguma instância em que ele já esteve anteriormente, ou seja, o processo deve existir na instância de destino (já deve ter ocorrido uma remessa entre instâncias no sistema).

A tela da tarefa permite a seleção do motivo da devolução e o acionamento do botão Retornar para a instância de origem, porém, nesse momento, o sistema verificará se há documentos não assinados, expedientes abertos ou tarefas em andamento, de modo a evitar que o processo seja encaminhado sem o devido cumprimento. Na confirmação da execução, o sistema retornará o processo para a última instância de origem (se veio do TSE, retornará para o TSE, se veio do primeiro grau, retornará para o primeiro grau).

Esta remessa lança o movimento de código 22: Baixa definitiva.

Após a confirmação, o sistema movimentará o processo para a tarefa **Manter processos expedidos** e ele ficará bloqueado para novas petições.

{{% notice tip %}}
As tarefas onde os processos permanecem após a utilização das tarefas de remessa e devolução são diferentes para que se saiba com mais facilidade qual o caminho que o processo percorreu.
{{% /notice %}}
