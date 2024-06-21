---
title: "Remessa para o TRE"
date: 2022-11-29T16:29:01-03:00
weight: 2
---

**Remeter processo para o TRE** é uma tarefa exclusiva do 1º grau e deve ser utilizada para realizar a remessa de um processo da Zona Eleitoral para o TRE, independente de se o processo já esteve ou não na instância de destino (2º grau).

No ambiente de zona, para remeter a outra instância, só existe hoje a possibilidade de utilizar a tarefa **Remeter processo para o TRE,** mesmo quando for devolução. Entretanto, o sistema sempre consulta o processo na instância de origem, ao fazer a remessa. Encontrando-o lá, ele automaticamente fará a devolução, e não uma nova remessa.

Esta remessa lança o movimento de código 123: Remetidos os autos, com os seus complementos cadastrados, bem como o código 22: Baixa definitiva.

Ao utilizar tarefa Remeter processo para o TRE, o processo fica na tarefa **Aguardando apreciação do TRE** e bloqueado para novas petições.

Quando devolvido pelo TRE, deve ir automaticamente para as tarefas **Analisar processo – ZE** ou **Analisar determinações – ZE** e também deve ser retirado o bloqueio para novas petições.


{{% notice warning %}}
A transição Retornar processo não tem relação com a remessa, ela só retorna o processo de volta para as tarefas **Analisar determinação** ou **Analisar processo.**
{{% /notice %}}
