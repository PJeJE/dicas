---
title: "Remessa para outra jurisdição"
date: 2022-11-29T16:29:16-03:00
weight: 4
---

Tarefa disponível apenas no PJe Zona, a **Remessa para outra jurisdição** permite que se remeta o processo para outro órgão jurisdicional.

O processo, após remetido a outra jurisdição, não fica na mesma tarefa:
+ Se gera novo número (quando a remessa é de um Estado para outro), é para ficar o número originário na tarefa **Manter processo arquivado** na Zona Eleitoral inicial, e o novo número em **Analisar novo processo,** na ZE de destino;
+ Se não gera novo número (remessa entre zonas do mesmo Estado), fica apenas um processo em **Analisar novo processo,** na ZE de destino.


A remessa entre jurisdições pode ser realizada por encaminhamento ou por competência. A remessa por encaminhamento enviará o processo para um órgão específico. A remessa por competência, via de regra, utilizará sorteio para encaminhar o processo, salvo quando a competência permitir a escolha do órgão julgador.

A remessa por competência exibirá, para seleção, as competências possíveis de acordo com a jurisdição selecionada, a classe e os assuntos do processo. Quando essa opção é selecionada, a aba órgão julgador só permite a seleção do órgão julgador quando a competência selecionada permitir a escolha de órgão julgador.

Na remessa por encaminhamento, o servidor escolhe qual órgão julgador receberá o processo. A remessa não será possível caso não exista nenhuma competência configurada naquela jurisdição para a classe e os assuntos do processo.

Ao final da remessa, para distribuição por competência, o sistema lança movimento de redistribuído por competência exclusiva em razão de incompetência, se for por encaminhamento, o movimento registra apenas redistribuído por competência exclusiva.
