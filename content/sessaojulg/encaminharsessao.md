---
title: "Procedimento para julgar processo em sessão"
date: 2024-04-24T14:00:45-03:00
weight: 9
menuTitle: "Procedimento para julgar processo em sessão"
---

## Procedimento padrão

Um processo, ao ser protocolado no PJe por um usuário qualquer (pode ser procurador, advogado ou servidor), ele inicia sua vida na tarefa **Verificar e Certificar Dados do Processo**

A partir dessa tarefa, o caminho padrão é que o servidor que está na **Unidade de Autuação e Distribuição** (pode ser também o **Secretário Judiciário**, da **Secretaria Judiciária**) encaminhe o processo para **Definir procedimento**, depois para **Remeter Processo** e depois para **Remeter ao Gabinete do Relator**

Depois dessa tarefa, o processo estará com um servidor de gabinete, ou seja, vinculado ao órgão julgador do processo. Se o processo for do Ministro Ramos Tavares, por exemplo, o processo estará no perfil Colegiado do Tribunal Superior Eleitoral/Ministro Ramos Tavares/Assessoria/Assessor Chefe

Com esse perfil, ele estará em **Realizar Triagem Ordinários**

Para ir para sessão, o usuário deve selecionar **Minutar Relatório Voto e Ementa**, construir os três documentos que essa tarefa tem.

O relator do processo faz o seu voto, acompanhado dos outros documentos.

Após finalizado, dele encaminha o processo para **Conferir Relatório Voto e Ementa** e depois para **Processo liberado para julgamento sessão presencial** (poderia ser virtual também), liberado o processo para ser pautado.

Os documentos construídos podem ser liberados para visualização de outros gabinetes ou não, dependendo da vontade dele, por meio das marcações pertinentes para cada documento (**Liberar relatório**, **Liberar voto** e **Liberar ementa**).

A partir desse momento, quem monta a sessão de julgamento incluindo esse processo é o **Assessor de Plenário**

Esse perfil não tem órgão julgador vinculado, ele fica vinculado ao **Colegiado + Secretaria Judiciária**.

Ele deverá acessar, pelo menu **Audiências e Sessões - Cadastro de sessão de julgamento**, a tela para criar sessão de julgamento

O Assessor de plenário precisa criar a sessão de julgamento, que será do tipo **Contínua** ou não (contínua para virtual, não contínua para presencial) e preencher os demais campos obrigatórios. Os processos que poderão ser incluídos na sessão do tipo **Contínua** foram liberados no gabinete do relator por meio da transição **Processo liberado para julgamento sessão virtual** e os processos que poderão ser incluídos na sessão com a marcação de **Contínua** como **Não** foram liberados por meio da transição  **Processo liberado para julgamento sessão presencial**.

Se pretende utilizar blocos de julgamento (alguns regionais chamam essa opção de listas), de fazer a seleção adequada. 

Depois de criada a sessão, ele deve ir ao menu **Audiências e Sessões - Relação de julgamento**. Será apresentada uma tela com um calendário. Ele deve selecionar o dia utilizado para a sessão que ele criou.

A tela da relação de julgamento será apresentada ao usuário.

Ele deve ir na aba **Aptos para inclusão em pauta** e selecionar o processo cujo relator fez o voto, relatório e ementa pela tarefa respectiva pela qual já passamos. Ele deve selecionar tantos processos quantos forem os desejados para serem incluídos naquela sessão. 

Outros processos que já passaram por outras sessõoes podem estar disponíveis nas outras abas dessa tela. 

Após selecionar os processos para incluir em pauta, ele deve selecionar o botão **Fechar pauta** na aba **Relação de julgamento**

Após pauta fechada, ele deve selecionar o menu **Painel - Painel do secretário da sessão**

Será apresentada uma tela de calendário, onde ele deve selecionar a data da sessão criada

Ao abrir a sessão, ele deve gerar a composição da sessão de julgamento

A seleção deverá ter um presidente para a sessão mais seis gabinetes que irão compor o julgamento. O relator do processo deve ser selecionado como um desses gabinetes

Deve-se selecionar também um Procurador

Ao clicar em Continuar, o sistema abrirá o painel da sessão de julgamento para o Assessor de Plenário

O Assessor de Plenário inicia a sessão

Cada um dos gabinetes que compõem a sessão podem votar (em  geral, eles utilizam o [Painel do magistrado na sessão](/sessaojulg/painel_magistrado), mas o próprio Assessor de plenário pode realizar as marcações de voto de cada vogal).

Pelo caminho padrão, após inseridos os votos, o Assessor de plenário seleciona as deliberações de cada processo (julgado, adiado, pedido de vista, retirado de julgamento) e insere as proclamações de julgamento dos processos daquela sessão de acordo com o que foi decidido pelo colegiado e, em seguida, encerra a sessão. Após encerrada, o Assessor de plenário **Registra movimentação**, que é o momento onde o sistema gera todos os movimentos de deliberação, de acordo com a marcação de cada processo. Depois desse passo, ele gera as certidões de julgamento do processo e, se for a prática daquele tribunal, gera a ata da sessão de julgamento. Os processos seguirão nos gabinetes e na secretaria judiciária para as tarefas pertinentes de acordo com as marcações de cada processo.


## Registro de pedido de vista

Para registrar um pedido de vista, vc deverá colocar o processo em julgamento e registrar um pedido de vista em nome de um gabinete vogal qualquer e encerrar a sessão

Após o encerramento, a tarefa de **Elaborar voto vista** estará disponível para o gabinete vogal selecionado para a vista

Lá vc verá a opção de construir o voto e liberá-lo ou não para os demais órgãos julgadores

Caso o gabinete encerre o fluxo de vista por engano, um novo fluxo de vista pode ser iniciado por meio das tarefas **Aguarda Sessão de Julgamento**, **Aguarda Julgamento - incluído em pauta virtual** e	
**Aguarda Julgamento - incluído em pauta**. Isso fará com que o sistema recupere a última sessão onde o processo não foi julgado e verifique se nessa sessão houve pedido de vista. Caso tenha ocorrido, o sistema encaminhará o fluxo de vista para o vistor. Caso contrário, abrirá o fluxo no gabinete do relator. Se for necessário, o gabinete pode utilizar a opção de **Escolher órgão julgador** para encaminhar para o real vistor.


## Processo com revisor

Para processos de classes que exigem revisão ou cuja revisão for facultativa, o relator precisará enviar o processo para revisão após contruir seus documentos de sessão. A partir do **Conferir Relatório, Voto e Ementa**, o servidor poderá encaminhar o processo para o revisor por meio da transição **Remeter ao Membro Revisor**, que só aparece para processos que exijam revisão ou cuja classe judicial tenha a marcação de exigência do revisor como facultativa. O processo é então encaminhado para a tarefa **Analisar processo a ser julgado - Revisor**, disponível no gabinete do revisor. 

A partir dessa tarefa, o servidor terá as seguintes opções de transições: **Liberar para julgamento - pauta presencial** e **Liberar para julgamento - pauta virtual**. Essas opções só estarão disponíveis para instalações onde a configuração do **Órgão Julgador Colegiado** do processo tiver a marcação **Quem pede pauta nos processos que possuem revisão?** como **Revisor**. As transições citadas farão com que o revisor libere o processo para a pauta escolhida (virtual ou presencial). O sistema iniciará o fluxo de acórdão e deixará o processo na tarefa **Aguarda Sessão de Julgamento** do relator. O revisor terá também a opção de transição **Liberar revisão (relator pedirá pauta)**, que envia o processo de volta ao gabinete do relator na tarefa **Processo liberado pelo revisor**. Nessa situação, o processo não estará liberado para pauta e o relator precisará realizar a ação de liberação. O relator terá disponíveis as transições **Processo liberado para julgamento sessão presencial** e **Processo liberado para julgamento sessão virtual**, que deixam o processo liberado para pauta na tarefa **Aguarda Sessão de Julgamento**. A transição **Devolver ao Conferir Relatório, Voto e Ementa** também está presente, que deixa o processo na tarefa **Conferir Relatório, Voto e Ementa**. Também está presente a transição **Devolver ao Membro Revisor**, que retorna o processo para **Analisar processo a ser julgador - Revisor**.
