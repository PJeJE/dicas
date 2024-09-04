---
title: "Controle de prazos"
date: 2024-09-04T11:46:20-03:00
weight: 2
---

As intimações são realizadas no PJe por meio de tarefas específicas onde o usuário informa as pessoas, os meios, os prazos e o conteúdo da intimação. 

Após realizada, o sistema encaminha o processo para uma tarefa de controle de prazos, para sinalizar ao servidor que existem prazos correndo naquele processo. 
O servidor pode atuar no processo por meio da transição **Verificar existência de outros pendentes**, o que fará com que um teste de expedientes abertos seja realizado. 
Caso não haja expediente aberto, o sistema finalizará o controle de prazos e encaminhará o processo para a respectiva tarefa de secretaria/cartório.
Caso haja alguma expediente aberto, o sistema encaminharáo processo para a tarefa **Analisar resposta do expediente**, permitindo ao servidor selecionar a transição **Ignorar demais expedientes abertos**, finalizando o controle de prazos e encaminhando o processo para a a respectiva tarefa de secretaria/cartório. 
O servidor pode proceder com sua atuação e pode também retornar o processo para o controle de prazos por meio da transição **Verificar controle de prazos**.
A partir da tarefa **Analisar resposta do expediente**, o servidor pode encaminhar o processo para "Aguardar demais manifestações", que, havendo ainda expedientes abertos, manterá o processo na tarefa "Processo com prazo em curso". 

Sempre que o processo estiver em um das tarefas de controle de prazos, ou seja, **Processo com prazo em curso** ou **Analisar resposta do expediente**, caso o intimado responda ao expediente ou haja o decurso de prazo sem a resposta, o sistema encaminha automaticamente o processo para o teste de expedientes abertos. O processo só sairá das tarefas de controle de prazos por atuação do próprio servidor ou se, no teste de expedientes abertos, o processo não tenha mais nenhum expediente com prazo aberto.




