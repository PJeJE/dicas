---
title: "Documentos de sessão"
date: 2022-11-29T16:30:58-03:00
weight: 1
---
## Documentos de sessão

Um processo judicial se constitui, em termos básicos, da capa processual, que contém a autuação, e de seus documentos e movimentos. No PJe, os documentos processuais têm uma série de regras e comportamentos associados. O roteiro
https://www.pje.jus.br/wiki/index.php/Roteiro_de_configura%C3%A7%C3%A3o_de_documentos agrega definições sobre como são tratados documentos processuais no PJe. 

Existem alguns documentos especiais no PJe de segunda instância/especiais que são os documentos de sessão. São documentos que, além de agregarem as características dos documentos processuais, encerram também características relacionadas a uma sessão de julgamento, já que o objetivo principal deles é a vinculação a uma sessão de órgão julgador colegiado. Para construir esses documentos, o PJe precisa de editores de texto diferenciados para que se consiga vincular o documento à sessão corretamente e agregar outras informações relevantes na identificação dos documentos. 

Os documentos de sessão no PJe são:
+ o relatório, quando um relator de um processo constrói o texto que norteia seu voto, tomando por base os fatos descritos e o direito que está sendo discutido
+ a ementa, que contém um resumo do assunto da causa em questão a ser levada a julgamento
+ o voto do relator, que é documento que contém seu encaminhamento em relação à questão
+ o voto do vogal, que é o documento que contém o encaminhamento que o magistrado não relator que compõe a sessão dá à causa 
+ a certidão de julgamento, que é o documento que registra, resumidamente, o que foi definido ao final da sessão de julgamento sobre a causa
+ o acórdão, que é o documento final que agrega a decisão colegiada completa relacionada à causa que foi levada à sessão

## Informações dos documentos de sessão

O PJe armazena algumas informações relevantes em cada tipo de documento de sessão. Para alguns tipos de documentos de sessão, caso a informação não esteja presente, o sistema fica inconsistente em diversos pontos. A falta da informação porde ocorrer por erro do sistema ou por ajustes em documentos realizados inadvertidamente.

Abaixo listamos os documentos e quais informações relevantes ele contém, incluindo as obrigatoriedades.

### Relatório
Informações relevantes - órgão julgador e sessão 

O relatório precisa sempre estar vinculado ao órgão julgador, que deve ser sempre o órgão julgador relator do processo. Caso o processo vá a julgamento e o resultado do julgamento aponte um vogal (não relator) como vencedor, ainda assim o relatório é sempre do relator que levou o processo a julgamento inicialmente, mesmo que o processo seja distribuído para o vencedor do julgamento. Os editores de documentos de sessão se comportam de forma inconsistente se essa relação não for respeitada.

A sessão de julgamento é uma informação relevante, mas não obrigatória, visto que, quando o relator inicia a construção dos documentos de sessão, não sabe ainda em qual sessão estará o processo. 

A vinculação à sessão de julgamento ocorre quando o assessor de plenário inclui o processo em uma pauta de julgamento. Caso o processo vá a julgamento e seja adiado, por exemplo, o sistema desvincula o documento da sessão para que seja vinculado posteriormente na nova pauta. 

Para a construção do acórdão vinculado ao relatório após julgado o processo, é importante que o relatório esteja vinculado à sessão para a qual será construído o acórdão.

Ajustes na vinculação de documentos à sessão e ao órgão julgador podem ser feitos pela tarefa [Selecionar documentos para acórdão](/sessaljulg/selecionar_documentos).

### Ementa
Informações relevantes - órgão julgador e sessão 

O ementa precisa sempre estar vinculado ao órgão julgador, que deve ser o órgão julgador relator do processo inicialmente. Caso o processo vá a julgamento e o resultado do julgamento aponte um vogal (não relator) como vencedor, a ementa precisa ser do vencedor. Via de regra, o vencedor constrói novo documento. O sistema está preparado, no editor de documento de sessão posterior ao julgamento do processo, para verificar quem foi o vencedor do julgamento e recuperar o documento de ementa respectivo que estiver vinculado ao órgão julgador vencedor. Caso não exista, o sistema carrega o editor com um novo documento em branco, para que o vencedor construa sua própria ementa.

A sessão de julgamento é uma informação relevante, mas não obrigatória, visto que, quando o relator inicia a construção dos documentos de sessão, não sabe ainda em qual sessão estará o processo. 

A vinculação à sessão de julgamento ocorre quando o assessor de plenário inclui o processo em uma pauta de julgamento. Caso o processo vá a julgamento e seja adiado, por exemplo, o sistema desvincula o documento da sessão para que seja vinculado posteriormente na nova pauta. 

Para a construção do acórdão vinculado à ementa após julgado o processo, é importante que a ementa esteja vinculada à sessão para a qual será construído o acórdão. 

Ajustes na vinculação de documentos à sessão e ao órgão julgador podem ser feitos pela tarefa [Selecionar documentos para acórdão](/sessaljulg/selecionar_documentos).

### Voto do relator
Informações relevantes - tipo de voto, órgão julgador, órgão julgador acompanhado e sessão 

O documento de voto precisa sempre ter um tipo de voto associado. Se não tiver, o sistema apresenta incosistências nas telas que exibem/tratam o voto do relator.

O voto do relator precisa sempre estar vinculado ao órgão julgador, que deve ser o órgão julgador relator do processo quando o processo foi pautado. 

A informação de órgão julgador acompanhado é onde o PJe registra se um órgão julgador acompanha outro órgão julgador no seu voto. Para o relator, essa informação armazena o mesmo órgão julgador relator do processo. Caso haja redistribuição do processo, mesmo que o órgão julgador dono do voto seja alterado para o novo relator do processo, o órgão julgador acompanhado continuará apontando para o relator anterior. Essa dado causa uma inconsistência na exibição dos placares da sessão, já que placar é o principal componente do sistema que leva a informação do órgão julgador acompanhado em consideração. Essa informação nunca é exibida nas telas do PJe, por mais que seja relevante para o correto funcionamento. Existe uma opção disponível na aba **Recursos e sessões** dos autos digitais que exibe essa informação de cada voto do processo em uma sessão para ajudar a elucidar casos que estejam gerando inconsistência nas telas do PJe. A exibição dos votos está condicionada ao papel **pje:sessao:permiteVisualizarVotos**.

{{% notice note %}}
Pela aba **Recursos e sessões**, para votos com documento associado, o sistema também apresentará um ícone que permitirá ao usuário visualizar o conteúdo do documento, mesmo quando ainda estiver em construção. Dessa forma, esse papel só deve ser liberado para administradores do sistema.
{{% /notice %}}

A sessão de julgamento é uma informação relevante, mas não obrigatória, visto que, quando o relator inicia a construção dos documentos de sessão, não sabe ainda em qual sessão estará o processo. 

A vinculação à sessão de julgamento ocorre quando o assessor de plenário inclui o processo em uma pauta de julgamento. Caso o processo vá a julgamento e seja adiado, por exemplo, o sistema desvincula o documento da sessão para que seja vinculado posteriormente na nova pauta. 

Para a construção do acórdão vinculado ao voto do relator após julgado o processo, é importante que o voto do relator esteja vinculado à sessão para a qual será construído o acórdão. 

Ajustes na vinculação de documentos à sessão podem ser feitos pela tarefa [Selecionar documentos para acórdão](/sessaljulg/selecionar_documentos).

### Voto do vogal
Informações relevantes - tipo de voto, órgão julgador, órgão julgador acompanhado e sessão 

O documento de voto precisa sempre ter um tipo de voto associado. Se não tiver, o sistema apresenta incosistências nas telas que exibem/tratam o voto do vogal.

O voto do vogal precisa sempre estar vinculado ao órgão julgador, que deve ser o órgão julgador dono do voto. 

A informação de órgão julgador acompanhado é onde o PJe registra se um órgão julgador acompanha outro órgão julgador no seu voto. Para os vogais, o voto pode acompanhar o relator, pode acompanhar ele mesmo ou pode acompanhar outro vogal que já votou. Essa informação nunca é exibida nas telas do PJe, por mais que seja relevante para o correto funcionamento. Existe uma opção disponível na aba **Recursos e sessões** dos autos digitais que exibe essa informação de cada voto do processo em uma sessão para ajudar a elucidar casos que estejam gerando inconsistência nas telas do PJe. A exibição dos votos está condicionada ao papel **pje:sessao:permiteVisualizarVotos**.

{{% notice note %}}
Pela aba **Recursos e sessões**, para votos com documento associado, o sistema também apresentará um ícone que permitirá ao usuário visualizar o conteúdo do documento, mesmo quando ainda estiver em construção. Dessa forma, esse papel só deve ser liberado para administradores do sistema.
{{% /notice %}}

A sessão de julgamento é uma informação relevante, mas não obrigatória, visto que, quando um processo tem um pedido de vista, o vogal inicia a construção de seu voto e não sabe ainda em qual sessão estará o processo. 

A vinculação à sessão de julgamento ocorre quando o assessor de plenário inclui o processo em uma pauta de julgamento. Caso o processo vá a julgamento e seja adiado, por exemplo, o sistema desvincula o documento da sessão para que seja vinculado posteriormente na nova pauta. 

Para a construção do acórdão vinculado ao voto do vogal após julgado o processo, é importante que o voto do vogal esteja vinculado à sessão para a qual será construído o acórdão. 

Ajustes na vinculação de documentos à sessão podem ser feitos pela tarefa [Selecionar documentos para acórdão](/sessaljulg/selecionar_documentos).

### Certidão de julgamento
Informações relevantes - sessão 

A certidão de julgamento pode ser um documento processual usual, construído por um editor comum. Quando ela é construída pelo **Painel do secretário da sessão**, o sistema a vincula à sessão correspondente. Se já há documento de sessão do tipo certidão de julgamento vinculado àquela sessão, o sistema impedirá que se faça um novo por meio do referido painel.

Pode-se construir documento de certidão de julgamento pelos autos digitais. Nesse caso, o sistema apresenta uma caixa de combinação (combo box) contendo as sessões em que o processo já esteve para que o usuário selecione e vincule a certidão corretamente à sessão correspondente. 

### Acórdão
Informações relevantes - órgão julgador e sessão 

O acórdão precisa sempre estar vinculado ao órgão julgador, que deve ser sempre o órgão julgador redator para o acórdão. Algumas vezes são criados vários documentos de acórdão para uma mesma sessão, mas o usuário às vezes não consegue apagá-los já que o sistema tem impedimentos para apagar documentos de sessão, ao contrário dos documentos processuais usuais. Dessa forma, é importante que os acórdãos que não são relevantes e não serão assinados sejam desvinculados da sessão. A vinculação a órgão julgador também é relevante para que o sistema não apresente inconsistências em algumas telas que trabalham, em seu processamento, com essa informação. Sendo assim, caso o acórdão não vá ser utilizado e esteja sem órgão julgador vinculado, o sistema apresenta erros do tipo **Há elementos de julgamento não vinculados a órgão julgador e a tela não poderá ser carregada.** Caso isso aconteça, vincule o acórdão a um órgão julgador qualquer, não relevante para o julgamento, e o sistema não apresentará inconsistências relacionadas a isso.

{{% notice note %}}
Ajustes na vinculação de documentos à sessão e ao órgão julgador podem ser feitos pela tarefa [Selecionar documentos para acórdão](/sessaljulg/selecionar_documentos).
{{% /notice %}}

A sessão de julgamento é uma informação sempre relevante para o acórdão. Os documentos de sessão que devem ser vinculados ao acórdão precisam sempre estar com a mesma sessão que o acórdão. Além disso, os documentos precisam ser anexos do acórdão, ou seja, o acórdão é o documento principal ao qual eles ficam vinculados. A vinculação de documentos de sessão ao acórdão pode ser realizada pela tarefa [Selecionar documentos para acórdão](/sessaljulg/selecionar_documentos).

O tarefa de construção do acórdão tem uma validação para ser corretamente carregada que é a existência de sessão de julgamento onde o processo foi julgado e o acórdão não foi construído ainda. Caso essa situação não ocorra, o sistema apresenta a mensagem **Processo pendente de vinculação a sessão de julgamento.** 

O fluxo para construção do acórdão foi desenhado de forma a permitir que se inicie a construção do acórdão antes mesmo da sessão ocorrer. Quando o processo é liberado para julgamento (tarefas **Aguarda sessão de julgamento** ou **Aguarda sessão de julgamento virtual**. Para o TSE, o processo vai iniciar uma tarefa paralelamento denominada **Aguardar Julgamento do Processo**, que pode ser tramitada para iniciar o fluxo de acórdão. Já para os TREs, caso o parâmetro **pje_je_ElaboraAcordaoAntesDaSessao** estiver configurado com o valor **true**, o sistema apresentará a transição para o usuário **Iniciar fluxo de elaboração de acórdão**, quando o gabinete que elabora o acórdão no regional, ou **Iniciar Elaboração de Acórdão**, quando a SJD elabora acórdão no regional. Caso o processo permaneça nessa tarefa, ao ser julgado, será automaticamente tramitado para a tarefa de elaboração de acórdão.

{{% notice note %}}
Se as tarefas **Iniciar Acórdão - SJD** ou **Iniciar Acórdão** ou **Aguardar Julgamento do Processo** forem finalizadas, ao ser julgado o processo, o fluxo de acórdão não iniciará automaticamente. O usuário terá que iniciar manualmente por meio das tarefas disponíveis nas tarefas de cumprimento na Unidade de Processamento Judiciário.
{{% /notice %}}


## Construção de documentos da sessão relatório, voto e ementa
No PJe da Justiça Eleitoral, relatório, voto e ementa, são construídos na tarefa **Minutar relatório, voto e ementa** pelo relator do processo. Por voto, entenda-se que é o conjunto da indicação do voto e o próprio documento de voto.

Para isso, o processo estará com um servidor de gabinete vinculado ao órgão julgador do processo. Se o processo for do Ministro Ramos Tavares no TSE, por exemplo, o processo estará no perfil **Colegiado do Tribunal Superior Eleitoral/Ministro Ramos Tavares/Assessoria/Assessor Chefe**

O processo inicialmente chega ao gabinete em Realizar Triagem Ordinários

Para ir para sessão, o usuário deve selecionar **Minutar Relatório Voto e Ementa** e construir os três documentos que essa tarefa tem.

O relator do processo faz o seu voto, acompanhado dos outros documentos.

{{% notice note %}} 
Se o usuário autenticado estiver em um órgão julgador diferente do órgão julgador do relator do processo, é gerada uma inconsistência só resolvida via banco de dados. Essa inconsistência - relator do processo diferente do órgão julgador que está construindo documentos de sessão - impede a utilização das tarefas de construções dos documentos de sessão. 
{{% /notice %}}

Após finalizado, ele encaminha o processo para **Conferir Relatório Voto e Ementa** e depois para **Processo liberado para julgamento sessão presencial** (poderia ser virtual também). O processo ficará na tarefa **Aguarda Sessão de Julgamento** ou **Aguarda Sessão de Julgamento Virtual**. Nesse ponto, é também iniciado o fluxo de acórdão.

A partir desse momento, quem monta a sessão de julgamento incluindo esse processo é o Assessor de Plenário, conforme descrito nos [procedimentos de pauta de julgamento](/sessaojulg/pauta).

Caso o Assessor de Plenário inclua o processo em uma pauta, o sistema automaticamente moverá o processo para a tarefa **Aguarda Julgamento - incluído em pauta** ou **Aguarda Julgamento - incluído em pauta virtual**. Se o processo for julgado em sessão, o fluxo do colegiado é encerrado. Caso a sessão ocorra e o processo tenha sido retirado de julgamento, adiado ou tenha pedido de vista registrado, o sistema tramita o processo novamente para **Aguarda Sessão de Julgamento** ou **Aguarda Sessão de Julgamento Virtual**.

{{% notice note %}} 
Caso o usuário retire manualmente os processos das tarefas **Aguarda Sessão de Julgamento** ou **Aguarda Sessão de Julgamento Virtual** ou **Aguarda Julgamento - incluído em pauta** ou **Aguarda Julgamento - incluído em pauta virtual**, deve sempre retornar para a mesma tarefa de acordo com a situação do processo. Caso isso não ocorra, os procedimentos automáticos na inclusão do processo em pauta, na retirada ou no julgamento não serão realizados corretamente. 
{{% /notice %}}

Para processos julgados em que o Assessor de plenário marcou um órgão julgador vencedor diferente do relator e que foi um julgamento de mérito, para instalações do PJe que tenha marcado o parâmetro **pje:je:redistribuiMerito** como **true**, ao tramitar o processo automaticamente para encerrar o fluxo de colegiado, o sistema redistribui o processo para o vencedor do pleito, lançando movimento respectivo de redistribuição em razão de lavratura de acórdão. 

Em casos que, no final do julgamento, o processo não esteja na tarefa correta, a redistribuição para o vencedor diferente do relator não ocorrerá, assim como não ocorrera a finalização do fluxo de colegiado. Se desejar forçar essa redistribuição com o fluxo de colegiado ainda em andamento, a partir das tarefas **Aguarda Sessão de Julgamento** ou **Aguarda Sessão de Julgamento Virtual** ou **Aguarda Julgamento - incluído em pauta** ou **Aguarda Julgamento - incluído em pauta virtual**, deve-se selecionar a transição **Verificar julgamento do processo**. Essa transição, quando disponível, verifica se o processo foi julgado na última sessão para finalizar o fluxo de colegiado e realizar os procedimentos automáticas já descritos, de acordo com o resultado do julgamento.

Caso tenha sido registrado um pedido de vista no julgamento, o sistema iniciará a tarefa de **Elaborar voto vista** para o gabinete vogal que pediu vista.

Ele poderá construir o voto e liberar o processo para julgamento. 

Caso o gabinete encerre o fluxo de vista por engano, um novo fluxo de vista pode ser iniciado por meio das tarefas **Aguarda Sessão de Julgamento**, **Aguarda Sessão de Julgamento Virtual**, **Aguarda Julgamento - incluído em pauta virtual** e **Aguarda Julgamento - incluído em pauta**. Isso fará com que o sistema recupere a última sessão onde o processo não foi julgado e verifique se nessa sessão houve pedido de vista. Caso tenha ocorrido, o sistema encaminhará o fluxo de vista para o vistor. Caso contrário, abrirá o fluxo no gabinete do relator. Se for necessário, o gabinete pode utilizar a opção de **Escolher órgão julgador** para encaminhar para o real vistor.

## Redistribuição de processo quando o processo já está em tarefas de construção de documentos de sessão

A tarefa **Minutar relatório voto e ementa** não deve ser executada por gabinete diferente do gabinete do relator. Caso isso ocorra, o PJe cria documentos repetidos na mesma tarefa e o usuário não percebe, já que o documento não é recarregado no editor. 

Depois que entrar na tarefa, é muito difícil corrigir essa situação porque o sistema fica sempre tentando recuperar aquele documento errado já criado e não consegue.

Para contornar esse problema, foi criada no fluxo uma tarefa chamada **Minutar relatório voto e ementa RE.** Essa tarefa faz com que o processo seja redistribuído para o gabinete atual sem que haja movimento de redistribuição. A transição está disponível pela tarefa **Minutar Relatório Voto e Ementa.**

Foi também criada uma trava no fluxo para impedir que o processo seja remetido para **Minutar relatório voto e ementa** caso o gabinete em que o processo se encontra não seja o relator do processo.

{{% notice note %}}
Essa transição deve ser usada antes de construir documento de relatório voto e ementa pelo gabinete. Se utilizada depois, terá que ser acionada a TI para ajustar ou apagar os documentos errados produzidos. 
{{% /notice %}} 

No TSE há uma orientação passada para a COARE e gabinetes sobre essa questão. Está no SEI 2020.00.000009345-3. As alterações no fluxo foram feitas a partir de setembro de 2020. Apesar da alteração ter sido realizada para atender à necessidade de julgamento de Recurso Extraordinário, pode ser utilizada sempre que se precisar redistribuir o processo para o gabinete atual, sem gerar movimento ou pesos.

## Voto de ex-membro

Para encaminhar para o ministro que está no gabinete de ex-presidência ou ex-membro, utilize, pela judiciária, as opções disponíveis para encaminhamento em sustituição. Não utilize as opções disponíveis para recesso. Pode-se utilizar a transição **Minutar relatório voto e ementa RE.** para redistribuir o processo para o gabinete ex-membro ou ex-presidência. 

Via de regra, o que ocorre após saída de um ministro no TSE é a disponibilização de tarefas para construção/assinatura de acórdão. Para esse fim, as transições disponíveis por meio das tarefas de acórdão posteriores ao julgamento do processo, que encaminham o processo para um gabinete específico, podem ser utilizadas sem prejuízo, diferente do que ocorre com as tarefas de relatório voto e ementa que são apresentadas antes do processo ir a julgamento. 
