---
title: "Definir Revisor"
date: 2022-11-29T16:20:54-03:00
weight: 2
---

Para que o processo tenha o nome do revisor atribuído automaticamente no momento do protocolo, a [classe precisa estar configurada]({{< relref "classes/configuracao" >}}) com a opção exige revisor marcada como sim.

Desde que, na configuração do órgão julgador colegiado, os revisores estejam configurados:

![Tela para definir revisor](/imagens/revisor_1.jpg)

Em estando a classe configurada com a opção exige revisor marcada como facultativa, o processo pode ou não ter revisor, mas ele sempre será distribuído automaticamente sem revisor e o servidor precisará ir na tarefa **Definir revisor** e indicar quem é o revisor do processo.

Tal tarefa está disponível a partir da tarefa **Analisar determinação/Analisar determinação - urgentes** e possibilita a determinação do revisor para processos cujas classes tenham a revisão marcada como facultativa:

![Tela para definir revisor](/imagens/revisor_2.jpg)

O nome do revisor pode ser verificado no autos digitais, na opção exibir mais detalhes do cabeçalho.

Quando um processo está no fluxo de elaboração de decisão colegiada, na tarefa **Conferir relatório, voto e ementa,** o sistema verifica se o processo exige revisor (quando o processo é protocolado ou sua classe alterada, o sistema marca que o processo exige caso a classe esteja marcada como uma classe que exige revisão) ou se é de uma classe cuja revisão está marcada como facultativa.
Satisfeita uma das duas condições acima, aparece uma transição para que o usuário envie o processo para o revisor. Quem receberá o processo será o revisor que aparece nos autos do processo.

Quando a classe exige revisão, o processo só poderá ser pautado se o revisor tiver incluído o voto.

Para fazer alteração de um revisor já cadastrado no processo, deve-se, primeiramente, ajustar a configuração dos órgãos julgadores revisores, no órgão julgador colegiado. 

Note que tal procedimento não causará mudança nos processos que já estão com seus revisores cadastrados!

A seguir, deve-se marcar a classe com exige revisor facultativo (se estiver como obrigatório, não será possível alterar).

Por fim, é preciso colocar o processo, a partir do analisar determinação, na tarefa definir revisor. Feito isto, desmarque a opção de exige revisor e clique em Prosseguir. Retorne o processo para a tarefa Definir revisor. Agora, sim, altere as marcações exige revisor e nome do revisor, deixando selecionado o revisor correto, retornando depois o processo para analisar determinação.

Esse procedimento de retirar da tarefa e colocar novamente é necessário porque a tarefa não tem o botão Salvar.

Após finalizado o procedimento, conforme o caso, alterar novamente a configuração do colegiado ou da classe, para que novos processos protocolados não sejam afetados pela alteração.

Nos casos em que o processo tem uma classe que exige revisão, mas o julgamento será do recurso, o procedimento correto é marcar facultativo para exige revisão na classe antes de pautar o processo. Assim, quem envia o processo para a pauta é o relator, não o revisor. Depois, basta desfazer essa alteração na configuração da classe.

Se o processo já tiver sido pautado, pode-se fazer o seguinte: 
+ Tirar da sessão (para processo com pauta fechada, o sistema gerará a certidão de cancelamento de pauta);
+ Marcar a classe como facultativo, em exige revisor; 
+ Cancelar a decisão colegiada e remeter o processo para SJD (os documentos construídos de voto, relatório e ementa não serão perdidos); 
+ A partir da tarefa Analisar determinação, ir para a tarefa Definir Revisor e tirar o revisor
+ Colocar na sessão novamente (adicionar por mesa na sessão de julgamento);
+ Dessa forma, pode-se alterar a ordem de votação do processo, já que com o revisor o sistema não permite.
