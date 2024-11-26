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

{{% notice note %}}
Sempre que o processo tiver algum prazo aberto e não estiver em tarefas de controle de prazos, caso seja o desejo do servidor, pode-se encaminhar o processo para tarefas de controle de prazos por meio da transição **Verificar controle de prazos**.
{{% /notice %}}

A partir da tarefa **Analisar resposta do expediente**, o servidor pode encaminhar o processo para **Aguardar demais manifestações**, que, havendo ainda expedientes abertos, manterá o processo na tarefa **Processo com prazo em curso**. 

Sempre que o processo estiver em um das tarefas de controle de prazos, caso o intimado responda ao expediente ou haja o decurso de prazo sem a resposta, o sistema encaminha automaticamente o processo para o teste de expedientes abertos. O processo só sairá das tarefas de controle de prazos por atuação do próprio servidor ou se, no teste de expedientes abertos, o processo não tenha mais nenhum expediente com prazo aberto. Processos em que todos os expedientes estão com prazo **Fechado** não devem constar nas tarefas de controle de prazos.

{{% notice note %}}
O sistema verifica o decurso de prazo sem resposta por meio de um procedimento automático executado todas as madrugadas denominado **Verificador periódico**. Caso haja o decurso, o sistema lança, no processo correspondente para a pessoa correspondente, o movimento **Decorrido prazo de XXX**, onde XXX é o nome da pessoa intimada. Expedientes sem prazo não provocam o decurso de prazo nem são controlados por meio de tarefas, ou seja, o sistema não encaminha o processo para tarefas de controle de prazos. 
{{% /notice %}}

## Verificador periódico

O Verificador Periódico é uma rotina da aplicação PJe que é executada automaticamente com periodicidade diária em hora previamente programada (na Justiça Eleitoral, em geral o procedimento é executado às 2 da madrugada). Essa rotina é responsável pela realização de diversas tarefas executadas na seguinte ordem:

+ Obtém o identificador do usuário do sistema conforme cadastrado no parâmetro "idUsuarioSistema".
+ Recupera os feriados que afetam o órgão julgador dado, ou seja, àqueles que pertencem ao próprio órgão, ao seu município sede (municipais), à unidade federativa em que está o município (estaduais ou distritais) e a todo o país (nacionais).
+ Registra a ciência automática de expedientes com prazo processual de graça expirado.
+ Registra a movimentação de decurso de prazo para os expedientes com prazo processual expirado.

O processamento automático para atestar o decurso de prazo sempre executa nas máquinas do TSE, que ficam em Brasília. O fuso horário utilizado, portanto, é o de Brasília. Dessa forma, a rotina é sempre executada após as duas da manhã para que em locais com fuso horário diferente não seja lançado decurso antes de o dia terminar. 

{{% notice note %}}
Quando o servidor informar prazos com um horário específico do dia para serem encerrados, não será possível a verificação automática do encerramento no horário estabelecido, visto que o procedimento automático executa apenas em horário específico. A rotina é por demais custosa e não é desejável que seja executada mais de uma vez por dia, principalmente em horários que atrapalhem a utilização do sistema por seus usuários em decorrência da sobrecarga do procedimento. 
{{% /notice %}}
  
## Novos feriados com prazos abertos

Existem casos em que um prazo está correndo e o servidor registra um novo feriado, mas o prazo final não reflete o registro.

Por exemplo, em uma intimação, houve registro de ciência no dia 19/04/2024 e o prazo final de resposta à intimação está registrado como 23/04/2024. O servidor verifica que dia 22/04/2024 é feriado e registra no calendário do PJe, mas nos autos do processo, o prazo final continua exibindo dia 23, quando o servidor espera que esteja registrado 24. Esse é o comportamento esperando e não haverá o decurso no dia 23. O que ocorre no sistema é que quando há o registro da ciência, o sistema faz a conta do prazo verificando os feriados e registra o dia do prazo final utilizando essa conta apenas como uma expectativa. Todos os dias que a rotina executa, o sistema recupera os expedientes que finalizam naquele dia. Ou seja, enquanto não chegar dia 23, ele não recupera esse expediente.

Quando chegar o dia 23, ele recupera o expediente e, por isso, recalcula o prazo. Nesse momento, o sistema verifica que houve mudança no prazo final por causa do feriado novo cadastrado e não lança o decurso. Ao mesmo tempo, ele atualiza o prazo final para o dia 24/04. 

{{% notice note %}}
Novos feriados não afetarão prazos já encerrados, ou seja, não adianta registrar feriados de dias passados. 
{{% /notice %}}





