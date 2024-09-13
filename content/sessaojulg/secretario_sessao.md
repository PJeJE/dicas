---
title: "Documentos de sessão"
date: 2022-11-29T16:30:58-03:00
weight: 1
---
## Documentos de sessão

Um processo judicial se constitui, em termos básicos, da capa processual, que contém a autuação, e de seus documentos e movimentos. No PJe, os documentos processuais têm uma série de regras e comportamentos associados. O roteiro
https://www.pje.jus.br/wiki/index.php/Roteiro_de_configura%C3%A7%C3%A3o_de_documentos agrega definições sobre como são tratados documentos processuais no PJe. 

Existem alguns documentos especiais no PJe de segundo instância/especiais que são os documentos de sessão. São documentos que, além de agregarem as características dos documentos processuais, encerram também características relacionadas a uma sessão de julgamento, já que o objetivo principal deles é a vinculação a uma sessão de órgão julgador colegiado. Para construir esses documentos, o PJe precisa de editores de texto diferenciados para que consiga vincular o documento à sessão corretamente e agregar outras informações relevantes na identificação dos documentos. 

Os documentos de sessão no PJe são:
+ o relatório, quando um relator de um processo constrói o texto que norteia seu voto
+ a ementa, que contém um resumo do assunto da causa em questão a ser levada a julgamento
+ o voto do relator, que é documento que contém seu encaminhamento em relação à questão
+ o voto dos vogais, que é o documento que contém o encaminhamento que os magistrados não relatores que compõem a sessão dão à causa
+ a certidão de julgamento, que é o documento que registra, resumidamente, o que foi definido ao final da sessão de julgamento sobre a causa
+ o acórdão, que é o documento final que agrega a decisão completa relacionada à causa que foi levada à sessão

## Informações dos documentos de sessão

O PJe armazena algumas informações relevantes em cada tipo de documento de sessão. Para alguns tipos de documentos de sessão, caso a informação não esteja presente, o sistema fica inconsistente em diversos pontos. A falta da informação porde ocorrer por erro do sistema ou por ajustes em documentos realizados inadvertidamente.

Abaixo listamos os documentos e quais informações relevantes ele contém, incluindo as obrigatoriedades.

+ Relatório
Informações relevantes - órgão julgador e sessão 

O relatório precisa sempre estar vinculado ao órgão julgador, que deve ser sempre o órgão julgador relator do processo. Caso o processo vá a julgamento e o resultado do julgamento aponte um vogal (não relator) como vencedor, ainda assim o relatório é sempre do relator que levou o processo a julgamento inicialmente, mesmo que o processo seja distribuído para o vencedor do julgamento. Os editores de documentos de sessão se comportam de forma inconsistente se essa relação não for respeitada.

A sessão de julgamento é uma informação relevante, mas não obrigatória, visto que, quando o relator inicia a construção dos documentos de sessão, não sabe ainda em qual sessão estará o processo. 

A vinculação à sessão de julgamento ocorre quando o assessor de plenário inclui o processo em uma pauta de julgamento. Caso o processo vá a julgamento e seja adiado, por exemplo, o sistema desvincula o documento da sessão para que seja vinculado posteriormente na nova pauta. 

Para a construção do acórdão  vinculado ao relatório após julgado o processo, é importante que o relatório esteja vinculado à sessão para a qual será construído o acórdão.

+ Ementa
Informações relevantes - órgão julgador e sessão 

O ementa precisa sempre estar vinculado ao órgão julgador, que deve ser o órgão julgador relator do processo inicialmente. Caso o processo vá a julgamento e o resultado do julgamento aponte um vogal (não relator) como vencedor, a ementa precisa ser do vencedor. Via de regra, o vencedor constrói novo documento. O sistema está preparado, no editor de documento de sessão posterior ao julgamento do processo, para verificar quem foi o vencedor do julgamento e recuperar o documento de ementa respectivo que estiver vinculado ao órgão julgador vencedor. Caso não exista, o sistema carrega o editor com um novo documento em branco, para que o vencedor construa sua própria ementa.

A sessão de julgamento é uma informação relevante, mas não obrigatória, visto que, quando o relator inicia a construção dos documentos de sessão, não sabe ainda em qual sessão estará o processo. 

A vinculação à sessão de julgamento ocorre quando o assessor de plenário inclui o processo em uma pauta de julgamento. Caso o processo vá a julgamento e seja adiado, por exemplo, o sistema desvincula o documento da sessão para que seja vinculado posteriormente na nova pauta. 

Para a construção do acórdão  vinculado à ementa após julgado o processo, é importante que a ementa esteja vinculada à sessão para a qual será construído o acórdão.


## Construção de documentos da sessão
No PJe da Justiça Eleitoral, relatório, voto e ementa, são construídos na tarefa **Minutar relatório, voto e ementa** pelo relator do processo. Por voto, entenda-se que é o conjunto da indicação do voto e o próprio documento de voto.

Para isso, o processo estará com um servidor de gabinete vinculado ao órgão julgador do processo. Se o processo for do Ministro Ramos Tavares no TSE, por exemplo, o processo estará no perfil **Colegiado do Tribunal Superior Eleitoral/Ministro Ramos Tavares/Assessoria/Assessor Chefe**

O processo inicialmente chega ao gabinete em Realizar Triagem Ordinários

Para ir para sessão, o usuário deve selecionar **Minutar Relatório Voto e Ementa** e construir os três documentos que essa tarefa tem.

O relator do processo faz o seu voto, acompanhado dos outros documentos.

Após finalizado, ele encaminha o processo para **Conferir Relatório Voto e Ementa** e depois para **Processo liberado para julgamento sessão presencial** (poderia ser virtual também).

A partir desse momento, quem monta a sessão de julgamento incluindo esse processo é o Assessor de Plenário

{{% notice note %}} 
Se o usuário autenticado estiver em um órgão julgador diferente do órgão julgador do relator do processo, é gerada uma inconsistência só resolvida via banco de dados. Essa inconsistência - relator do processo diferente do órgão julgador que está construindo documentos de sessão - impede a utilização das tarefas de construções dos documentos de sessão. 
{{% /notice %}}

## Redistribuição de processo quando o processo já está em tarefas de construção de documentos de sessão

A tarefa **Minutar relatório voto e ementa** não deve ser executada por gabinete diferente do gabinete do relator. Caso isso ocorra, o PJe cria documentos repetidos na mesma tarefa e o usuário não percebe, já que o documento não é recarregado no editor. 

Depois que entrar na tarefa, é muito difícil corrigir essa situação porque o sistema fica sempre tentando recuperar aquele documento errado já criado e não consegue.

Para contornar esse problema, foi criada no fluxo uma tarefa chamada **Minutar relatório voto e ementa RE.** Essa tarefa faz com que o processo seja redistribuído para o gabinete atual sem que haja movimento de redistribuição. A transição está disponível pela tarefa **Minutar Relatório Voto e Ementa.**

Foi também criada uma trava no fluxo para impedir que o processo seja remetido para **Minutar relatório voto e ementa** caso o gabinete em que o processo se encontra não seja o relator do processo.

{{% notice warning %}}
Essa transição deve ser usada antes de construir documento de relatório voto e ementa pelo gabinete. Se utilizada depois, terá que ser acionada a TI para ajustar ou apagar os documentos errados produzidos. 
{{% /notice %}} 

No TSE há uma orientação passada para a COARE e gabinetes sobre essa questão. Está no SEI 2020.00.000009345-3. As alterações no fluxo foram feitas a partir de setembro de 2020. Apesar da alteração ter sido realizada para atender à necessidade de julgamento de Recurso Extraordinário, pode ser utilizada sempre que se precisar redistribuir o processo para o gabinete atual, sem gerar movimento ou pesos.

## Voto de ex-membro

Para encaminhar para o ministro que está no gabinete de ex-presidência ou ex-membro, utilize, pela judiciária, as opções disponíveis para encaminhamento em sustituição. Não utilize as opções disponíveis para recesso. Pode-se utilizar a transição **Minutar relatório voto e ementa RE.** para redistribuir o processo para o gabinete ex-membro ou ex-presidência. 

Via de regra, o que ocorre após saída de um ministro no TSE é a disponibilização de tarefas para construção/assinatura de acórdão. Para esse fim, as transições disponíveis por meio das tarefas de acórdão posteriores ao julgamento do processo, que encaminham o processo para um gabinete específico, podem ser utilizadas sem prejuízo, diferente do que ocorre com as tarefas de relatório voto e ementa que são apresentadas antes do processo ir a julgamento. 

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
