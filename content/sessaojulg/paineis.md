---
title: "Condução da sessão"
date: 2024-09-16T16:39:58-03:00
weight: 4
---

Após montada a pauta de julgamento, o assessor de plenário precisará montar a composição da sessão de julgamento. Pelo **Painel do secretário da sessão**, ele selecionará a sessão por meio do dia respectivo exibido no calendário. A composição do julgamento inclui órgãos julgadores (gabinetes) e seus magistrados. Os votos são sempre vinculados a gabinetes, mas os magistrados são exibidos nos placares das sessões, dando maior visibilidade aos participantes do julgamento sobre quem é o responsável pelo voto.

{{% notice note %}}
É importante ressaltar que existe a composição da sessão de julgamento e a composição do processo. A diferença entre os dois conceitos é que o primeiro diz respeito ao conjunto de membros que está presente na sessão e a composição do processo são os magistrados que votam naquele processo específico. Ocorre, muitas vezes, de um magistrado da composição da sessão estar impedido de votar em um processo. O assessor de plenário, para aquele processo, marca o gabinete como não presente e insere um outro para substituir. A substituição pode ocorrer dentro do próprio gabinete, só com a marcação do magistrado, não afetando, nesse caso, a titularidade do voto. Outra situação onde a composição da sessão é diferente da composição do processo é quando um processo foi trazido de outra sessão que já tinha votos proferidos. Se o gabinete que votou não estiver presente na sessão atual, o voto dele estará no processo, já que foi proferido em sessão anterior, mas ele não estará presente na sessão. Dessa forma, ele fará parte apenas da composição do processo.
{{% /notice %}}

Ao abrir a tela do **Painel do secretário da sessão** antes de ter gerado a composição, o sistema exibe uma tela com o botão **Gerar composição inicial dos participantes**. Ao acionar o botão, o sistema recuperará todos os gabinetes ativos (data inicial menor ou igual ao dia de hoje, data final vazia ou maior ou igual ao dia de hoje) vinculados ao colegiado daquele sessão. A exibição dos gabinetes obedece ao campo **Ordem** conforme composição da configuração do **Órgão julgador colegiado**, primeiramente, e à ordem alfabética, secundariamente. 

O sistema gerará a composição marcando o presidente da sessão e os presentes de acordo com configurações do órgão julgador colegiado. Os magistrados titulares já serão vinculados à composição. Essa montagem pode ser alterada pelo Assessor de plenário de acordo com suas necessidades. 

{{% notice note %}}
Caso existam órgãos julgadores sem marcação de titulares, o sistema exibirá um aviso perguntando se o usuário deseja gerar a composição inicial ainda assim. Como a composição é gerada a partir de todos os órgãos vinculados ao colegiado, o sistema não impede a geração, já que não serão todos os que irão compor a sessão. É IMPORTANTE QUE TODOS OS ÓRGÃOS JULGADORES PRESENTES TENHAM TITULARES VINCULADOS. Caso o usuário queira revisar a configuração dos gabinetes antes da geração da composição, ele poderá responder ao aviso cancelando a geração da composição. De toda maneira, a composição sempre pode ser ajustada, ou seja, não há maiores prejuízos se o usuário marcar *Sim*. 
{{% /notice %}}

Na composição da sessão, o assessor de plenário também marcará quem será o procurador do ministério público na sessão. Para essa seleção, o sistema apresentará todos os procuradores ativos cadastrados que tenham a marcação **Acompanha a Sessão de Julgamento** selecionada.

{{% notice note %}}
Ao gerar a composição da sessão, o sistema gera também a composição dos processos pautados na sessão utilizando a mesma composição marcada. Posteriormente, o usuário poderá selecionar marcações diferentes por processo.
{{% /notice %}}

Só após gerada a composição inicial da sessão, com os respectivos presentes, presidente e procurador da sessão, o sistema permitirá que o usuário selecione **Continuar** para prosseguir com a condução da sessão. 

{{% notice note %}}
Após criada a composição inicial, o usuário pode selecionar a opção **Recriar a composião da sessão**. É uma opção útil quando há a alteração das configurações do órgão julgador colegiado e o usuário deseja que essas novas configurações reflitam na composição. Caso o usuário queira, a nova composição poderá ser refletida nos processos também. Para isso, ele deverá utilizar a opção **Aplicar composição para processos pendentes de julgamento**. O sistema não alterará composição de processos que não estejam pendentes de julgamento.
{{% /notice %}}

O usuário sempre pode alterar o procurador da sessão. Essa alteração não reflete na composição dos processos, mas só esse procurador conseguirá acompanhar as sessões não contínuas por meio do **Painel do membro do ministério público na sessão**. 

## Opções do painel do secretário

Após criada a composição, o sistema exibe o painel do secretário da sessão. Sempre que a sessão não estiver aberta ainda e o usuário selecionar alguma data de sessão com composição criada no calendário, o sistema abrirá a tela de composição montada antes de apresentar a lista de processos na sessão. O usuário deve selecionar o botão **Continuar** para que a lista de processos seja exibida.

O sistema apresenta informações básicas sobre a sessão no cabeçalho da tela e menu de ferramentas por meio do ícone de três barrinhas no canto superior direito. 

Ações na sessão - opções disponíveis que afetam a configuração da sessão
+ Atualizar todos os processos
+ Atualizar resultado sessão
+ Anotações da sessão
+ Incluir processos em mesa
+ Lista de presença na sessão
+ Iniciar (Pausar e Encerrar também são é apresentados quando a sessão está aberta)
+ Visualizar ata de sessão de julgamento

Ações em lote - opções disponíveis que afetam uma lista de processos selecionados

+ Adicionar a um bloco de julgamento
+ Marcar preferência
+ Retirar preferência
+ Tornar pendente de julgamento
+ Redistrar votação em lote
+ Adiar para próxima sessão
+ Colocar em julgamento (só apresentada com sessão aberta)
+ Retirar de julgamento (só apresentada com sessão aberta)
+ Registrar julgamento (só apresentada com sessão aberta)
+ Registrar pedido de vista (só apresentada com sessão aberta)

O sistema apresenta também a lista de processos da sessão. A lista separa em um agrupador inicialmente fechado (sem exibição do conteúdo) os processos já proclamados, ou seja, onde já houve atuação do Assessor de plenário para resultado seu resultado de julgamento. Caso o usuário queira visualizar os detalhes desses processos deve clicar no ícone correspondente para abertura do agrupador. 

Em seguida, são apresentados os processos que ainda não foram proclamados. Para cada capa processual (pode estar em julgamento a capa principal e/ou o(s) recurso(s)), são exibidos: uma opção para selecionar o processo (utilizada para as ações em lote do menu de ferramentas da sessão), um ícone que exibe a situação de julgamento do processo e, caso o processo esteja em julgamento (ícone apresentado é o da balança), um ícone de liberação do processo para ser visualizado no **Púlpito de sustentação oral**, painel que pode ser utilizado pelos advogados em sessões presenciais. 

Além disso, são apresentados os dados principais do cabeçalho da capa, uma caixinha de texto para informar a proclamação de julgamento, o placar de julgamento daquele processo e uma barra de ferramentas. 

## Visualização de documentos da sessão

A visualização de documentos da sessão não assinados só é possível se as respectivas marcações **Liberar voto**, **Liberar relatório** e **Liberar ementa** forem realizadas. Essa marcações são realizadas pelo magistrado relator, por meio das tarefas de contrução dos documentos da sessão.

Os pontos do sistema onde poderão ser visualizados são:

+ Painel do secretário da sessão; 
+ Painel do magistrado na sessão; 
+ Painel do membro da OAB na sessão; 
+ Painel do membro do ministério público na sessão; 
+ Púlpito de sustentação oral;
+ Internet - opção Pautas de julgamento (http://www.tse.jus.br/servicosjudiciais/sessoes-de-julgamento/pautas-de-julgamento/pje); 
+ Tarefas de vogais. 

Depois que inicia a sessão, quando o Assessor de plenário colocar o processo em julgamento, vai aparecer na Internet, sem necessidade de usuário e senha, o tipo de voto (concedo, nego, etc.) mas não aparece o documento do voto. Na Internet, sem login e senha, só aparece o documento de voto depois de assinado. 

Já no painel do membro da OAB, assim como no painel do membro do ministério público na sessão, basta iniciar a sessão e o documento já aparece. Em todos os casos, é sempre necessária liberação por meio da tarefa do gabinete

## Visualização de Documentos em outros painéis

Se o magistrado tiver liberado seu documento para visualização por meio da opção respectiva na tarefa e o parâmetro **pje:sessao:ocultarVotosAntecipadosNaoMagistrado** estiver marcado como false o voto/documentos serão exibidos para o Assessor de plenário no **Painel do secretário da sessão**.

Nas sessões contínuas, os processos são colocados em julgamento automaticamente na data escolhida para a sessão após o início, que também é automático, e ocorre entre 0h00 e 2h00, do horário de Brasília, independente do horário informado na configuração da sessão. No TSE, as sessões contínuas se iniciam às 0h00 no dia da sessão. Nas sessões não contínuas o Assessor de plenário pode liberar os processos para que sejam visualizados na Internet - opção **Pautas de julgamento**, quando inicia a sessão. Antes de iniciada a sessão, os processos não são exibidos.

O Assessor de plenário pode liberar o voto/documentos para que sejam visualizados na Internet - opção **Pautas de julgamento** quando finaliza a sessão. No gabinete, o magistrado pode liberar os documentos de sessão clicando nas respectivas opções **Liberar voto**, **Liberar relatório** e **Liberar ementa**. Ao clicar na opção **Liberar relatório**, somente este será liberado. Ao clicar na opção **Liberar voto**, os três documentos serão liberados. Se o magistrado tiver liberado seu documento para visualização por meio da opção respectiva na tarefa, os votos serão exibidos na opção **Pautas de julgamento** desde que:

+ O parâmetro pje:sessao:plenarioVirtual:documentoAssinado esteja configurado como false;
+ O gabinete tenha liberado o voto;
+ O processo tenha sido julgado;
+ A sessão esteja encerrada.

Se o parâmetro **pje:sessao:plenarioVirtual:documentoAssinado** estiver com o valor true, o documento só aparecerá em **Pautas de julgamento** após assinatura do acórdão.

Os processos e votos/documentos serão visualizados no menu **Painel do membro da OAB na sessão** em sessões contínuas, quando iniciada a sessão.

Se o parâmetro **pje:sessao:ocultarVotosAntecipadosNaoMagistrado** estiver marcado como **false** e o magistrado tiver liberado o documento para visualização por meio da opção respectiva na tarefa, voto/documentos serão exibidos no **Painel do membro da OAB na sessão.**

O Assessor de plenário pode liberar os processos e votos/documentos para que sejam visualizados no menu **Painel do membro do ministério público na sessão** do procurador que está cadastrado naquela sessão, em sessões não contínuas, quando inicia a sessão. Caso a sessão não tenha sido iniciada, a visualização não é liberada.

Se o parâmetro **pje:sessao:ocultarVotosAntecipadosNaoMagistrado** estiver marcado como **false**, e o magistrado tiver liberado seu documento para visualização por meio da opção respectiva na tarefa, voto/documentos serão exibidos no **Painel do membro do ministério público na sessão.**

O Assessor de plenário pode liberar o processo para ser visualizado no menu **Púlpito de sustentação oral** em julgamentos de sessões não contínuas quando colocar o processo **Em julgamento** (ícone balancinha sendo exibido).

O Assessor de plenário pode liberar o voto/documentos para que sejam visualizados por meio do menu **Púlpito de sustentação oral** em julgamentos de sessões não contínuas, quando clicar no ícone de olho, disponível nos processos que estão **Em julgamento** (ícone balancinha sendo exibido).

Se o magistrado tiver liberado seu documento para visualização por meio da opção respectiva na tarefa, voto/documentos serão exibidos no **Púlpito de sustentação oral.**

## Orientação passada para o TSE quando foram disponilizados os painéis:

De ordem da assessora-chefe da Assessoria do PJe, informamos que a versão disponibilizada hoje no TSE, 18 de maio de 2020, contempla um painel aos advogados e ao ministério público para acompanhamento das sessões virtuais e por videoconferência. Para as sessões iniciadas, virtuais ou não, o painel da OAB e do MP exibe documentos de relatório, voto e ementa produzidos pelos gabinetes, desde que liberados para visualização.

Conforme já ocorria antes dessa melhoria, a liberação de visualização dos documentos é realizada pelo gabinete, a partir das opções já existentes “Liberar relatório”, “Liberar ementa” e Liberar voto”, disponíveis nas tarefas de conferência dos documentos.

A liberação é por documento, ou seja, o gabinete pode escolher liberar apenas o relatório, assim como pode escolher não liberar documento algum.

## Orientação passada para os TREs quando foram disponilizados os painéis:

A versão 2.0.0.0.49.3 do PJe nos regionais e no TSE traz uma melhoria solicitada pela OAB e pelo ministério público para que advogados e MP possam enxergar os documentos de voto, relatório e ementa, desde que liberados pelo gabinete, a partir das opções já existentes “Liberar relatório”, “Liberar ementa” e Liberar voto”, disponíveis nas tarefas de “Aguarda sessão de julgamento” inclusive para julgamento virtual. 

Caso liberados os documentos, os processos que estejam em sessão aberta terão a opção do placar, que exibe os votos dos magistrados. As permissões para esse painel podem ser encontradas no menu Configuração - Controle de acesso - Funcionalidades, pesquisando pelo identificador pages/Painel/ProcuradorMP/sessaoAbertaProcuradorMP.seam.

Às permissões que já existem, pode ser acrescentada a permissão para o perfil de advogado. Ou ainda, se for o caso, retirar permissões.

Além da melhoria nessa funcionalidade, foi disponibilizada uma nova, que só permite acesso aos documentos liberados pelo gabinete de processos em julgamento de sessões abertas não contínuas e que tenham visualização liberada pelo Assessor de plenário. A liberação ocorre por meio de um novo ícone em forma de olho no painel do secretário da sessão que aparece para cada processo. Ao clicar nesse ícone, a visualização dos documentos está liberada para esse novo painel.

Além disso, a permissão para o painel deve ser também configurada por meio do controle de acesso - funcionalidades, identificador /pages/Painel/painel_usuario/painelPulpito.seam juntamente com a associação do papel: pje:papel:pulpitoSustentacaoOral ao perfil desejado.

Sobre essas duas funcionalidades, a liberação do assessor de plenário só é necessária quando se usa o painel do púlpito.

{{% notice note %}}
Há um erro conhecido em processos migrados. Os documentos não aparecem na aba para selecionar documentos para acórdão, e a orientação para a TI é ajustar o nr_instancia do client.tb_processo_trf para o mesmo ds_instancia do core.tb_processo_documento. A migração tem que ser também ajustada para preencher esse campo e o problema deixar de ocorrer (a solução, nestes casos, depende de abertura de chamado).
{{% /notice %}}

