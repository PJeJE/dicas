---
title: "Paineis da sessão de julgamento"
date: 2022-11-29T16:30:58-03:00
weight: 3
---
## Construção de documentos da sessão
No PJe da Justiça Eleitoral, relatório, voto e ementa, são construídos na tarefa **Minutar relatório, voto e ementa** pelo relator do processo.

Se o usuário autenticado estiver em um órgão julgador diferente do órgão julgador do relator do processo, é gerada uma inconsistência só resolvida via banco de dados.

Por voto, entenda-se que é o conjunto da indicação do voto e o próprio documento de voto.

## Visualização de documentos da sessão

A visualização de documentos da sessão não assinados só é possível se as respectivas marcações **Liberar voto**, **Liberar relatório** e **Liberar ementa** forem realizadas.

Os pontos do sistema onde poderão ser visualizadas são:

+ Painel do secretário da sessão; 
+ Painel do magistrado na sessão; 
+ Painel do membro da OAB na sessão; 
+ Painel do membro do ministério público na sessão; 
+ Púlpito de sustentação oral;
+ Internet - opção Pautas de julgamento (http://www.tse.jus.br/servicosjudiciais/sessoes-de-julgamento/pautas-de-julgamento/pje); 
+ Tarefas de vogais. 

Depois que inicia a sessão, quando o Assessor de plenário colocar o processo em julgamento, vai aparecer na Internet, sem necessidade de usuário e senha, o tipo de voto (concedo, nego, etc.) mas não aparece o documento do voto. Na Internet, sem login e senha, só aparece o documento de voto depois de assinado. 

Já no painel do membro da OAB, basta iniciar a sessão e o documento já aparece. Em todos os casos, é sempre necessária liberação por meio da tarefa do gabinete

## Visualização de Documentos em outros painéis

Se o magistrado tiver liberado seu documento para visualização por meio da opção respectiva na tarefa e o parâmetro **pje:sessao:ocultarVotosAntecipadosNaoMagistrado** estiver marcado como false o voto/documentos serão exibidos para o Assessor de plenário no **Painel do secretário da sessão**.

Nas sessões contínuas, os processos são colocados em julgamento automaticamente após o início da sessão, de acordo com o horário planejado. Nas sessões não contínuas o Assessor de plenário pode liberar os processos para que sejam visualizados na Internet - opção **Pautas de julgamento**, quando inicia a sessão. Antes de iniciada a sessão, os processos não são exibidos.

O Assessor de plenário pode liberar o voto/documentos para que sejam visualizados na Internet - opção **Pautas de julgamento** quando finaliza a sessão. Se o magistrado tiver liberado seu documento para visualização por meio da opção respectiva na tarefa, os votos serão exibidos na opção Pautas de julgamento desde que:

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

{{% notice warning %}}
Há um erro conhecido em processos migrados. Os documentos não aparecem na aba para selecionar documentos para acórdão, e a orientação para a TI é ajustar o nr_instancia do client.tb_processo_trf para o mesmo ds_instancia do core.tb_processo_documento. A migração tem que ser também ajustada para preencher esse campo e o problema deixar de ocorrer (a solução, nestes casos, depende de abertura de chamado).{{% /notice %}}
