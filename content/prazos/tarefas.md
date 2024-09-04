---
title: "Controle de prazos"
date: 2024-09-04T11:46:20-03:00
weight: 2
---

As intimações são realizadas no PJe por meio de tarefas específicas onde o usuário informa as pessoas, os meios, os prazos e o conteúdo da intimação. 

Após realizada a intimação, o sistema encaminha o processo para uma tarefa de controle de prazos, para sinalizar ao servidor que existem prazos correndo naquele processo. O nome da tarefa pode conter outros termos no final para diferenciar o controle de prazos de instâncias/situações específicas mas, via de regra, a tarefa é denominada **Processo com prazo em curso**.

O servidor pode atuar no processo por meio da transição **Verificar existência de outros pendentes**, o que fará com que um teste de expedientes abertos seja realizado. Caso não haja expediente aberto, o sistema finalizará o controle de prazos e encaminhará o processo para a respectiva tarefa de secretaria/cartório.

Caso haja alguma expediente aberto, o sistema encaminharáo processo para a tarefa **Analisar resposta do expediente**, permitindo ao servidor selecionar a transição **Ignorar demais expedientes abertos**, finalizando o controle de prazos e encaminhando o processo para a respectiva tarefa de secretaria/cartório. Esse procedimento é utilizado quando o servidor precisa realizar alguma atividade no processo enquanto os prazos estão correndo.

{{% notice note %}}
As tarefas de controle de prazos são **Processo com prazo em curso** ou **Analisar resposta do expediente**. 
{{% /notice %}}

O servidor pode proceder com sua atuação e pode também retornar o processo para o controle de prazos por meio da transição **Verificar controle de prazos**.

A partir da tarefa **Analisar resposta do expediente**, o servidor pode encaminhar o processo para **Aguardar demais manifestações**, que, havendo ainda expedientes abertos, manterá o processo na tarefa **Processo com prazo em curso**. 

Sempre que o processo estiver em um das tarefas de controle de prazos, caso o intimado responda ao expediente ou haja o decurso de prazo sem a resposta, o sistema encaminha automaticamente o processo para o teste de expedientes abertos. O processo só sairá das tarefas de controle de prazos por atuação do próprio servidor ou se, no teste de expedientes abertos, o processo não tenha mais nenhum expediente com prazo aberto. Processos em que todos os expedientes estão com prazo **Fechado** não devem constar nas tarefas de controle de prazos.

{{% notice note %}}
O sistema verifica o decurso de prazo sem resposta por meio de um procedimento automático executado todas as madrugadas. Caso haja o decurso, o sistema lança, no processo correspondente para a pessoa correspondente, o movimento **Decorrido prazo de XXX**, onde XXX é o nome da pessoa intimada. Expedientes sem prazo não provocam o decurso de prazo nem são controlados por meio de tarefas, ou seja, o sistema não encaminha o processo para tarefas de controle de prazos. 
{{% /notice %}}





