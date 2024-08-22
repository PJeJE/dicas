# Tramitação processual

![Início](/imagens/fluxo1.jpg)

Um processo judicial se inicia no PJe da Justiça Eleitoral quando um [usuário externo](http://www.pje.jus.br/wiki/index.php/Regras_de_neg%C3%B3cio#RN277), que pode ser advogado, Ministério Público, Autoridade Policial ou qualquer jurisdicionado, cadastra o processo incluindo os dados e a petição inicial apresentando seu pleito. O processo pode também ser iniciado por um servidor da Justiça Eleitoral com características de [usuário interno](http://www.pje.jus.br/wiki/index.php/Regras_de_neg%C3%B3cio#RN394). Ao finalizar o que denomina-se como protocolo do processo, ocorre a [distribuição automática](http://www.pje.jus.br/wiki/index.php/Distribui%C3%A7%C3%A3o), ou seja, o processo tem o relator designado de acordo com competências e utilizando um mecanismo de sorteio.

O processo, após ser protocolado, pode ser pesquisado dentro do sistema, mas a atuação por parte dos servidores se dará sempre por meio de tarefas de fluxo. Os [fluxos](http://www.pje.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Fluxo) são agrupamentos de tarefas onde pode-se mudar a tramitação processual de acordo com os objetivos de cada organização. A [definição de fluxo](http://www.pje.jus.br/wiki/index.php/Configura%C3%A7%C3%A3o_inicial#Defini.C3.A7.C3.A3o_de_fluxos) que será utilizada para o processo depende de sua classe judicial, ou seja, o fluxo atribuído à classe em sua [configuração](http://www.pje.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Classe_judicial) será utilizado para apresentar o processo nas tarefas.

Ao ser iniciado, o processo judicial, via de regra, passa por três unidades principais dentro do tribunal: Autuação e Distribuição, Gabinete e Processamento.

![Tramitação padrão](/imagens/fluxo2.jpg)

Na Autuação e Distribuição, é realizada uma [triagem](tramitacao2grau.md#verificar-e-certificar-dados-do-processo), onde um servidor verifica os dados do processo e encaminha o pleito para [análise do relator](tramitacao2grau.md#fluxo-gabinetes), ou seja, do Gabinete. No Gabinete, o processo é analisado e são expedidos os atos judiciais. O processo é então encaminhado para a Unidade de processamento, onde são realizados [os devidos cumprimentos](tramitacao2grau.md#fluxo-cumprimento-de-determinacao). 

Por vezes, outras unidades precisam se manifestar no processo. O encaminhamento do processo para essas unidades é feito, em geral, pelo Processamento, de acordo com determinações do Gabinete. A autuação pode, em alguns momentos, remeter o processo diretamente para outras unidades. 

As unidades por onde passam um processo se traduzem internamente no PJe em papeis e localizações, de forma a limitar a autorização de execução das tarefas a determinados grupos de pessoas. 

Abaixo seguem algumas autorizações de acordo com as unidades onde são realizadas as tarefas:

## Unidade de autuação e distribuição

|  Localização  | Papel |
|:--------------|:----------|
|Secretaria Judiciária SJD | Secretário Judiciário 
|Secretaria Judiciária SJD | Servidor 
|Unidade de Autuação e Distribuição | Coordenador 
|Unidade de Autuação e Distribuição | Chefe de Seção 
|Secretaria Judiciária SJD | Colaborador 
|Unidade de Autuação e Distribuição | Servidor 
|Unidade de Autuação e Distribuição | Colaborador 

## Unidade de processamento - principal

|  Localização  | Papel |
|:--------------|:----------|
|Secretaria Judiciária SJD | Secretário Judiciário
|Secretaria Judiciária SJD | Colaborador
|Unidade de Processamento Judiciário | Coordenador
|Unidade de Processamento Judiciário | Chefe de Seção
|Unidade de Processamento Judiciário | Servidor
|Unidade de Processamento Judiciário | Colaborador

## Corregedoria Unidade de Fiscalização e Cadastro
|  Localização  | Papel |
|:--------------|:----------|
|Corregedoria Unidade de Fiscalização e Cadastro | Chefe de Seção
|Corregedoria Unidade de Fiscalização e Cadastro | Servidor
|Corregedoria Unidade de Fiscalização e Cadastro | Colaborador
|Corregedoria Unidade de Fiscalização e Cadastro | Coordenador
|Administração PJe | Administrador

## Corregedoria - Judiciária
|  Localização  | Papel |
|:--------------|:----------|
|Administração PJe | Administrador
|Corregedoria Unidade Assuntos Judiciários | Coordenador
|Corregedoria Unidade Assuntos Judiciários | Chefe de Seção


## Corregedoria - Magistrado
|  Localização  | Papel |
|:--------------|:----------|
|Ministro | Magistrado
|Assessoria | Assessor Chefe
|Corregedoria Unidade de Fiscalização e Cadastro | Coordenador
|Corregedoria Unidade de Fiscalização e Cadastro | Chefe de Seção

Raias do fluxo Processar atividades de corregedoria:

Corregedoria - Judiciária

Corregedoria Unidade Assuntos Judiciários	Assessor Chefe
Corregedoria Unidade Assuntos Judiciários	Assessor
Corregedoria Unidade Assuntos Judiciários	Coordenador
Corregedoria Unidade Assuntos Judiciários	Chefe de Seção
Corregedoria Unidade Assuntos Judiciários	Assessor-Chefe de Gabinete
Corregedoria Unidade Assuntos Judiciários	Assessor de Gabinete
Corregedoria Unidade Assuntos Judiciários	Coordenador de Assuntos Judiciários
Corregedoria Unidade Assuntos Judiciários	Chefe de Assuntos Judiciários
Corregedoria Unidade Assuntos Judiciários	Secretário da Corregedoria
Corregedoria Regional Eleitoral	Correição

Secretaria Judiciária

Secretaria Judiciária SJ	Secretário Judiciário
Unidade de Processamento Judiciário	Coordenador
Unidade de Processamento Judiciário	Chefe de Seção
Unidade de Processamento Judiciário	Servidor
Unidade de Processamento Judiciário	Coordenador de Processamento
Unidade de Processamento Judiciário	Chefe de Processamento
Unidade de Processamento Judiciário	Servidor de Processamento
Corregedoria Regional Eleitoral	Correição

O principal fluxo por onde se inicia um processo no PJe é o [Fluxo Originárias](tramitacao2grau.md#fluxo-classes-originarias).

Quando um processo é protocolado em classes de corregedoria, o fluxo é o [Fluxo principal de corregedoria](tramitacao2grau.md#fluxo-principal-corregedoria).

## Fluxo - Classes Originárias

Este fluxo define o fluxo básico de tarefas pelas quais passa um processo. É a porta de entrada no PJe para classes que não são de corregedoria.

Ao entrar nesse fluxo, caso não tenha havido no processo movimento de decisão terminativa (que é o caso de processos que acabaram de ser protocolados) o sistema encaminha o processo para a primeira tarefa, [Verificar e Certificar Dados do Processo](tramitacao2grau.md#verificar-e-certificar-dados-do-processo). Caso o processo já tenha tido movimento de decisão terminativa lançado, o sistema encaminha o processo para o [Verificar Pendências](tramitacao2grau.md#verificar-pendencias)

### Verificar e Certificar dados do processo

Responsabilidade: [Unidade de autuação e distribuição](tramitacao2grau.md#unidade-de-autuacao-e-distribuicao)

Um processo de uma classe não corregedoria entra no PJe por meio do [Fluxo Originárias](tramitacao2grau.md#fluxo-classes-originarias) na tarefa Verificar e Certificar dados do processo. 

O processo, seguindo o fluxo padrão, cairá na tarefa [Remeter Processo](tramitacao2grau.md#remeter-processo)

### Remeter Processo

Responsabilidade: [Unidade de autuação e distribuição](tramitacao2grau.md#unidade-de-autuacao-e-distribuicao)

A partir dessa tarefa, há a possibilidade de Remeter à Unidade de Fiscalização e Cadastro Corregedoria. O processo irá para o [fluxo principal de corregedoria](tramitacao2grau.md#fluxo-principal-corregedoria). Com essa transição, o fluxo originárias será encerrado e o único fluxo do processo será o da corregedoria.

### Verificar Pendências

Responsabilidade: [Unidade de processamento](tramitacao2grau.mdunidade-de-processamento-principal)

A partir da tarefa Verificar Pendências, também há a possibilidade de se acionar a corregedoria. As possibilidades são: 

- Remeter à Unidade de Assuntos Judiciários - Corregedoria 

Lança movimento 60044 e remete o processo para o fluxo [Fluxo - Processar Atividades no Processo - Corregedoria](tramitacao2grau.mdprocessar-atividades-no-processo-corregedoria)

Ao retornar, dependendo do que houve na execução. o caminho vai ser diferente. Se houve determinação para envio para o gabinete, o processo vai para [gab corregedoria]. Se não houve, o sistema verifica se houve determinação para arquivamento e envia para [realiza baixa]. Se não houve determinação para arquivamento, testa encaminhar SJD e volta pro [verificar pendências] ou então vai pro término. 

- Remeter ao Gabinete do Corregedor

Faz com que o [fluxo de gabinetes](tramitacao2grau.md#fluxo-gabinetes) seja iniciado no gabinete da corregedoria, sem redistribuir o processo. É lançado o movimento de remetidos os autos ao corregedor.

- Remeter à Unidade de Fiscalização e Cadastro Corregedoria

O processo irá para o [fluxo principal de corregedoria](tramitacao2grau.md#fluxo-principal-corregedoria). Com essa transição, o fluxo originárias será encerrado e o único fluxo do processo será o da corregedoria.


## Fluxo principal corregedoria

Este fluxo define o fluxo básico de tarefas pelas quais passa um processo de corregedoria. É a porta de entrada no PJe para classes que são de corregedoria.

Ao iniciar o fluxo, o sistema estabelece o campo pessoa relator. Esse campo aparece nos autos digitais, ao exibir os detalhes do processo. Em seguida, o processo é encaminhado para [Verificar dados - Processo Corregedoria](tramitacao2grau.mdverificar-dados-processo-corregedoria)

### Verificar dados - Processo Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.mdcorregedoria-unidade-de-fiscalizacao-e-cadastro)

É uma tarefa de triagem. Ela contém o campo objeto do processo, que deve ser preenchido. O servidor pode, verificando que o processo está OK, encaminhar para o gabinete. O encaminhamento para o gabinete pode ser diretamente para uma decisão colegiada - Elaborar decisão colegiada - inicia fluxo de [decisão colegiada](tramitacao2grau.md#fluxo-preparacao-de-decisao-colegiada) ou para decisão monocrática - Elaborar Decisão Monocrática - inicia fluxo de [preparação de ato judicial](tramitacao2grau.md#fluxo-preparacao-de-ato-judicial).  Ao retornar do gabinete, se não tiver sido realizada decisão, o sistema encaminha o processo para o [Verificar pendências](tramitacao2grau.md#verificar-pendências---processo-corregedoria). Caso contrário, o processo vai para o [cumprimento de determinações](tramitacao2grau.md#fluxo---cumprimento-de-determinação---corregedoria).

Além disso, o servidor pode encaminhar para fazer uma retificação dos dados do processo, onde ele deverá também inserir uma certidão informando as alterações. Ele faz isso por meio da transição Remeter ao Certificar e alterar dados, que deixará o processo na tarefa [Certificar e alterar dados - Processo Corregedoria](tramitacao2grau.md#certificar-e-alterar-dados---processo-corregedoria). 

O servidor tem a opção de utilizar a transição Remeter à SJD, que encerra fluxo da corregedoria e inicia [fluxo originárias](tramitacao2grau.md#fluxo-classes-originarias), lançando movimento (60005).

Remeter ao cumprimento de determinações - inicia [fluxo de cumprimento determinações corregedoria](tramitacao2grau.md#fluxo---cumprimento-de-determinação---corregedoria). Finalizado, retorna ao [verificar pendências - processo corregedoria](tramitacao2grau.mdverificar-pendências---processo-corregedoria)

Observações para ajuste:

- Tem movimentar em lote, mas a definição do objeto não é em lote, ou seja, o processo pode ser tramitado sem que o objeto seja preenchido.
- Não está configurado impedimento para tramitar quando o objeto não for preenchido

### Certificar e alterar dados - Processo Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

Nessa tarefa, o servidor pode retificar os dados do processo. O objeto também está disponível para edição.

Os tipos de documentos disponíveis para edição são: 

O servidor tem acesso a eles desde que tenha papel vinculado ao tipo de documento. 

O servidor pode utilizar a opção de editar uma certidão de retificação em lote, ou seja, construir a certidão com conteúdo semelhante para todos os processos do lote selecionado de uma só vez.  O servidor também pode assinar em lote as certidões já construídas, caso detenha papel de assinatura para o tipo de documento construído. A assinatura em lote ficará disponível na opção Assinaturas do painel do usuário. 

As transições possíveis são:

- Remeter ao verificar dados - retorna o processo para [Verificar dados - Processo Corregedoria](tramitacao2grau.md#verificar-e-certificar-dados-do-processo)

- Remeter ao Cumprimento de Determinações - inicia [fluxo de cumprimento determinações corregedoria](tramitacao2grau.md#fluxo---cumprimento-de-determinação---corregedoria). Finalizado, retorna ao [verificar pendências - processo corregedoria](tramitacao2grau.md#verificar-pendências---processo-corregedoria)

- Remeter à SJD, que encerra fluxo da corregedoria e inicia [fluxo originárias](tramitacao2grau.md#fluxo-classes-originarias), lançando movimento (60005).

- Encaminhar para o gabinete - O encaminhamento para o gabinete pode ser diretamente para uma decisão colegiada - Elaborar decisão colegiada - inicia fluxo de [decisão colegiada](tramitacao2grau.md#fluxo-preparacao-de-decisao-colegiada) ou para decisão monocrática - Elaborar Decisão Monocrática - inicia fluxo de [preparação de ato judicial](tramitacao2grau.md#fluxo-preparacao-de-ato-judicial).  Ao retornar do gabinete, se não tiver sido realizada decisão, o sistema encaminha o processo para o [Verificar pendências](tramitacao2grau.md#verificar-pendências---processo-corregedoria). Caso contrário, o processo vai para o [cumprimento de determinações](tramitacao2grau.md#fluxo---cumprimento-de-determinação---corregedoria).

O sistema permite que o usuário envie o processo para 'Remeter ao gabinete sem certificar e para Remeter ao Cumprimento de Determinações sem que a certidão seja assinada.

Caso o usuário assine uma certidão, o sistema lançará o movimento de juntada vinculado à certidão e enviará o processo para a tarefa [Verificar Pendências - Processo Corregedoria](tramitacao2grau.md#verificar-pendências---processo-corregedoria)

Observações para ajuste:
- tem movimentar em lote, mas tarefas com editor de texto não devem conter essa opção.
- tem um aviso sem conteúdo 
- Remeter ao gabinete sem certificar não existe, tinha que liberar as transições elaborar decisão monocrática e elaborar decisão colegiada sem obrigar preencher certidão

### Verificar pendências - Processo Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

Essa tarefa é de encaminhamento. Ela exibe os documentos do processo e permite realização de encaminhamento em lote. As possibilidades são:

- [Remeter ao verificar dados](tramitacao2grau.md#verificar-e-certificar-dados-do-processo)

- [Remeter ao Certificar e alterar dados](tramitacao2grau.md#certificar-e-alterar-dados---processo-corregedoria)

- [Remeter ao Cumprimento de Determinações](tramitacao2grau.md#fluxo---cumprimento-de-determinação---corregedoria)

- Remeter à SJD, que encerra fluxo da corregedoria e inicia [fluxo originárias](tramitacao2grau.mdfluxo-classes-originarias), lançando movimento (60005).

- Encaminhar para o gabinete - O encaminhamento para o gabinete pode ser diretamente para uma decisão colegiada - Elaborar decisão colegiada - inicia fluxo de [decisão colegiada](tramitacao2grau.md#fluxo-preparacao-de-decisao-colegiada) ou para decisão monocrática - Elaborar Decisão Monocrática - inicia fluxo de [preparação de ato judicial](tramitacao2grau.md#fluxo-preparacao-de-ato-judicial). Ao retornar do gabinete, se não tiver sido realizada decisão, o sistema encaminha o processo para o [Verificar pendências](tramitacao2grau.mdverificar-pendências---processo-corregedoria). Caso contrário, o processo vai para o [cumprimento de determinações](tramitacao2grau.md#fluxo---cumprimento-de-determinação---corregedoria).
 
- Remeter ao TSE desde que a aplicação seja de segundo grau, que faz com que o processo vá para o [fluxo de remessa para instância superior - Corregedoria](tramitacao2grau.md#fluxo---remessa-para-instância-superior---corregedoria). Caso o processo retorne do fluxo de remessa, será encaminhado para o [Verificar Pendências - Processo Corregedoria](tramitacao2grau.md#verificar-pendências---processo-corregedoria)

- Arquivar processo - lança movimento e envia processo para [Manter Processos Arquivados - Processo Corregedoria](tramitacao2grau.md#manter-processos-arquivados---processo-corregedoria)

- Devolver Processo Corregedoria a Origem, que coloca o processo na tarefa  [Devolver Processo Corregedoria a Origem](tramitacao2grau.md#devolver-processo-corregedoria-a-origem)

### Manter Processos Arquivados - Processo Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

Essa tarefa é o arquivo do processo. Ela exibe os documentos do processo e sua tramitação para ser realizada em lote. A partir dela, o servidor pode:

- Desarquivar processos, que lançará o movimento 893 e enviará o processo para a tarefa [Analisar processo desarquivado](tramitacao2grau.md#analisar-processo-desarquivado)

- Encaminhar o processo para a tarefa [Manter Processos Devolvidos a Origem](tramitacao2grau.md#manter-processos-devolvidos-a-origem)

### Manter Processos Devolvidos a Origem

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

Essa tarefa é uma tarefa de arquivo. Ela serve para diferenciar processos arquivados e que tramitaram normalmente na instância dos processos que foram arquivados por terem sido devolvidos à origem. Ela exibe os documentos do processo e sua tramitação para ser realizada em lote. A partir dela, o servidor pode:

- Desarquivar processos, o que enviará o processo para a tarefa [Verificar pendências da corregedoria](tramitacao2grau.md#verificar-pendências---processo-corregedoria)

- Manter Processos Arquivados - Processo Corregedoria - envia processo para [Manter Processos Arquivados - Processo Corregedoria](tramitacao2grau.md#manter-processos-arquivados---processo-corregedoria)

### Analisar processo desarquivado

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

Nessa tarefa, o servidor poderá ver os documentos processuais e poderá utilizar tramitação em lote. 

A partir dela, o servidor pode:

- [Remeter ao verificar dados](tramitacao2grau.md#verificar-e-certificar-dados-do-processo)

- [Remeter ao Certificar e alterar dados](tramitacao2grau.md#certificar-e-alterar-dados---processo-corregedoria)

- Remeter ao [Cumprimento de Determinações Corregedoria](tramitacao2grau.md#fluxo---cumprimento-de-determinação---corregedoria)

- Remeter à SJD, que encerra fluxo da corregedoria e inicia [fluxo originárias](tramitacao2grau.md#fluxo-classes-originarias), lançando movimento (60005).

- Encaminhar para o gabinete - O encaminhamento para o gabinete pode ser diretamente para uma decisão colegiada - Elaborar decisão colegiada - inicia fluxo de [decisão colegiada](tramitacao2grau.md#fluxo-preparacao-de-decisao-colegiada) ou para decisão monocrática - Elaborar Decisão Monocrática - inicia fluxo de [preparação de ato judicial](tramitacao2grau.md#fluxo-preparacao-de-ato-judicial). Ao retornar do gabinete, se não tiver sido realizada decisão, o sistema encaminha o processo para o [Verificar pendências](tramitacao2grau.md#verificar-pendências---processo-corregedoria). Caso contrário, o processo vai para o [cumprimento de determinações](tramitacao2grau.md#fluxo---cumprimento-de-determinação---corregedoria).

- Remeter ao TSE desde que a aplicação seja de segundo grau, que faz com que o processo vá para o [fluxo de remessa para instância superior - Corregedoria](tramitacao2grau.md#fluxo---remessa-para-instância-superior---corregedoria). Caso o processo retorne do fluxo de remessa, será encaminhado para o [Verificar Pendências - Processo Corregedoria](tramitacao2grau.md#verificar-pendências---processo-corregedoria)

- Arquivar processo - lança movimento e envia processo para [Manter Processos Arquivados - Processo Corregedoria](tramitacao2grau.md#manter-processos-arquivados---processo-corregedoria)

- Devolver Processo Corregedoria a Origem, que coloca o processo na tarefa  [Devolver Processo Corregedoria a Origem](tramitacao2grau.md#devolver-processo-corregedoria-a-origem)

- Encaminhar o processo para a tarefa [Manter Processos Devolvidos a Origem](tramitacao2grau.md#manter-processos-devolvidos-a-origem)

### Devolver Processo Corregedoria a Origem

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

É uma tarefa de devolução do processo a outra instância. 

Ela apresenta um aviso pedindo que o usuário, antes de devolver o processo, verifique se não há expedientes abertos ou tarefas em andamento, de modo a evitar que o processo seja encaminhado sem o devido cumprimento. A tela da tarefa permite a seleção do motivo da devolução e o acionamento do botão “Retorno do processo à origem”. O usuário pode também desistir da tarefa, retornando ao [Verificar pendências](tramitacao2grau.md#verificar-pendências---processo-corregedoria). Se selecionar o botão de retorno do processo à origem, o sistema verificará se há documentos não assinados para que o usuário possa desistir da execução da tarefa, se for o caso. Na confirmação da execução, o sistema retornará o processo para a última instância de origem (se veio do TSE, retornará para o TSE, se veio do primeiro grau, retornará para o primeiro grau, se veio do TRE, retornará ao TRE que enviou). O sistema lancará o movimento de baixa e deixará o processo bloqueado na tarefa [Manter Processos Devolvidos a Origem](tramitacao2grau.md#manter-processos-devolvidos-a-origem). 

## Fluxo - Cumprimento de determinação - Corregedoria

Este fluxo contém encaminhamentos para cumprimentos diversos. Inicialmente, ele envia o processo para a tarefa [Analisar Determinação Processo Corregedoria](tramitacao2grau.md@analisar-determinação-processo-corregedoria).

###  Analisar Determinação Processo Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro) (não habilitada para os administradores do sistema)

Essa tarefa exibe a última decisão terminativa do processo. A tramitação em lote está habilitada.

O servidor tem as seguintes possibilidades:

- Elaborar documentos - que envia o processo para a tarefa [Elaborar documentos - Processo Corregedoria](tramitacao2grau.md#elaborar-documentos-processocorregedoria)

- Verificar controle de prazos - encaminha o processo para o [Fluxo - Controle de Prazos - Corregedoria](tramitacao2grau.md#fluxo-controle-de-prazos-corregedoria). Finalizado o fluxo, o processo retorna para a tarefa atual.

- Preparar comunicação - encaminha o processo para o [Fluxo - Ato de Comunicação - Corregedoria](tramitacao2grau.md#fluxo-ato-de-comunicacao-corregedoria). Finalizado o fluxo, o processo retorna para a tarefa atual. 

- Nada mais a cumprir - Finaliza o fluxo e retorna o processo para a tarefa de onde tinha vindo.


### Elaborar documentos - Processo Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro) (não habilitada para os administradores do sistema)

Essa tarefa permite a elaboração de documentos. Os tipos de documento permitidos são Ofício, Certidão, Memorando e Ata de Audiência

O servidor tem acesso a eles desde que tenha papel vinculado ao tipo de documento. 

Na tarefa, para servidores com papel de assinatura para o tipo de documento selecionado, há a possibilidade de assinar o documento já construído em lote. Se o documento já tiver sido construído, ele ficará disponível para assinatura em lote na opção Assinaturas do painel do usuário. 

O usuário pode utilizar a transição Retornar sem que o documento tenha sido preenchido. Isso fará com que o processo vá para [Analisar Determinação Processo Corregedoria](tramitacao2grau.md#analisar-determinação-processo-corregedoria). Se assinar o documento na própria tarefa, o sistema também encaminhará o processo para o [Analisar Determinação Processo Corregedoria](tramitacao2grau.md#analisar-determinação-processo-corregedoria).

Se o usuário selecionar a transição Encaminhar para assinatura do Corregedor, o processo é encaminhado para a tarefa [Assinar documentos - Processo Corregedoria](tramitacao2grau.md#assinar-documentos-processo-corregedoria). 

Há também a possibilidade de utilizar a transição Desbloquear editor. Essa transição foi inserido para corrigir defeitos de outras tarefas de edição de documentos, que guardam o documento criado indevidamente para recuperação em unidades não pertinentes. Se isso ocorrer, o documento de outra unidade é recuperado assinado no editor da tarefa atual e o servidor não consegue construir seu próprio documento. Assim, ele pode utilizar a transição para carregar o editor sem o documento indevido, prosseguindo com a construção de seu próprio documento. 

Ao sair da tarefa, o documento criado é apagado da memória do fluxo, ou seja, tarefas seguintes não vão carregar o documento para assinatura.


Observações para ajuste:

- Ao encaminhar para assinatura do corregedor, o documento criado não é recuperado na assinatura.


### - Assinar documentos - Processo Corregedoria

Responsabilidade: [Corregedoria - Magistrado](tramitacao2grau.md#corregedoria-magistrado) 

Essa tarefa permite a elaboração de documentos. Os tipos de documento permitidos são Ofício, Certidão, Carta de ordem, Mandado, Intimação, Edital, Informação e Despacho de Ofício

Os modelos de documento permitidos são: 85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,106,113,121,131,132,136,114,142,143,144

Na tarefa, para servidores com papel de assinatura para o tipo de documento selecionado, há a possibilidade de assinar o documento já construído em lote. Se o documento já tiver sido construído, ele ficará disponível para assinatura em lote na opção Assinaturas do painel do usuário. 

O servidor pode utilizar a transição Devolver para correção que deixará o processo de volta na tarefa [Elaborar documento - Processo Corregedoria](tramitacao2grau.md#elaborar-documentos-processocorregedoria).

Caso o usuário assine o documento, o sistema lança o movimento de juntada e envia o processo para a tarefa  [Analisar Determinação Processo Corregedoria](tramitacao2grau.md@analisar-determinação-processo-corregedoria).

Observações para ajuste:

- Dispensa requeridos está em transição não existente no Criar tarefa


## Fluxo - Ato de Comunicação - Corregedoria

## Fluxo - Remessa para Instância Superior - Corregedoria

Os fluxos de remessa são configurados de forma similar, permitindo que se utiliza a tarefa de remessa para que uma instância do PJe da Justiça Eleitoral envie processos para outra instância.

O fluxo de remessa da corregedoria, ao ser iniciado, verifica se o processo é das classes Duplicidade/Pluralidade de Inscrições - Coincidências (CO 12553), Regularização de Situação do Eleitor (RS 12063) ou Direitos Políticos (DP 12064) e envia para a tarefa [Remeter ao TSE - Corregedoria](tramitacao2grau.md#remeter-ao-tse-corregedoria). Se não for dessas classes, o sistema envia o processo para a tarefa [Remeter ao TSE - Processo Corregedoria](tramitacao2grau.md#remeter-ao-tse-processo-corregedoria). São tarefas similares, mas executadas por perfis diferentes. 

O usuário pode selecionar a opção Cancelar, o que finalizará o fluxo de remessa e retornará o processo para a tarefa que tinha acionado o fluxo.

### Remeter ao TSE - Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

A tarefa permite que se protocole um novo processo no destino, com classes e assuntos específicos e também com novas configurações de partes. As classes exibidas são as classes passíveis de serem recebidas como recurso configuradas no destino. Caso a classe selecionada esteja configurada no destino com a marcação “exige numeração própria”, um novo número de processo será gerado. O novo processo conterá uma cópia dos documentos do processo originário, preservando os dados de assinatura originais.

Após a confirmação, o sistema lançará o movimento de remessa conforme o destino selecionado (TSE ou Zona eleitoral) e manterá o processo em [Aguardando apreciação pela instância Superior - Corregedoria](tramitacao2grau.md#aguardando-apreciacao-pela-instancia-superior-corregedoria) bloqueado para novas petições ou edições. 

O usuário pode selecionar a opção Cancelar, o que finalizará o fluxo de remessa e retornará o processo para a tarefa que tinha acionado o fluxo. 

### Remeter ao TSE - Processo Corregedoria

Responsabilidade: [Corregedoria - Judiciária](tramitacao2grau.md#corregedoria-judiciaria)

A tarefa permite que se protocole um novo processo no destino, com classes e assuntos específicos e também com novas configurações de partes. As classes exibidas são as classes passíveis de serem recebidas como recurso configuradas no destino. Caso a classe selecionada esteja configurada no destino com a marcação “exige numeração própria”, um novo número de processo será gerado.  O novo processo conterá uma cópia dos documentos do processo originário, preservando os dados de assinatura originais.

Após a confirmação, o sistema lançará o movimento de remessa conforme o destino selecionado (TSE ou Zona eleitoral) e manterá o processo em [Aguardando apreciação pela instância Superior - Processo Corregedoria](tramitacao2grau.md#aguardando-apreciacao-pela-instancia-superior-processo-corregedoria) bloqueado para novas petições ou edições. 

### Aguardando apreciação pela instância Superior - Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

Essa tarefa armazena os processos que foram enviados para outra instância pela Unidade de Fiscalização e Cadastro. Eles permanecem bloqueados para tramitação. Se o processo retorna da instância para onde foi enviado, o sistema automaticamente desbloqueia o processo e o tramita para a tarefa [Recebimento de instância Superior - Corregedoria](tramitacao2grau.md#recebimento-de-instancia-superior-corregedoria).

### Aguardando apreciação pela instância Superior - Processo Corregedoria

Responsabilidade: [Corregedoria - Judiciária](tramitacao2grau.md#corregedoria-judiciaria)

Essa tarefa armazena os processos que foram enviados para outra instância pela Unidade de Assuntos Judiciários. Eles permanecem bloqueados para tramitação. Se o processo retorna da instância para onde foi enviado, o sistema automaticamente desbloqueia o processo e o tramita para a tarefa [Recebimento de instância Superior - Processo Corregedoria](tramitacao2grau.md#recebimento-de-instancia-superior-processo-corregedoria).

### Recebimento de instância Superior - Corregedoria

Responsabilidade: [Corregedoria - Unidade de fiscalização e cadastro](tramitacao2grau.md#corregedoria-unidade-de-fiscalizacao-e-cadastro)

Essa tarefa notifica o servidor da unidade de fiscalização e cadastro que o processo retornou da instância para onde tinha ido. A partir dela, o servidor finaliza o fluxo de remessa e retorna o processo para a tarefa que o chamou. 

### Recebimento de instância Superior - Processo Corregedoria

Responsabilidade: [Corregedoria - Judiciária](tramitacao2grau.md#corregedoria-judiciaria)

Essa tarefa notifica o servidor da unidade de assuntos judiciários que o processo retornou da instância para onde tinha ido. A partir dela, o servidor finaliza o fluxo de remessa e retorna o processo para a tarefa que o chamou. 


## Fluxo - Processar Atividades no Processo - Corregedoria

### Analisar Processo - Corregedoria

Responsabilidade - Corregedoria - Judiciária

A partir dessa tarefa, o usuário tem, entre outras opções, o "Remeter ao gabinete Corregedoria" e o "Remeter à Presidência", ambas as transições encaminhando o processo para o [Fluxo de Gabinetes](tramitacao2grau.md#Fluxo---Gabinetes). Ao finalizar a execução do fluxo de gabinetes, o sistema verifica que o processo está com o órgão julgador corregedoria e faz o seguinte teste:

Se o parâmetro "pje:je:CumprimentoPelaCorregedoria" estiver setado como true e o movimento de código 60001 estiver presente no processo, o processo continua no fluxo atual de corregedoria, sendo encaminhado para o analisar processo ou determinação, de acordo com movimento da árvore de magistrado lançado ou não nos autos. Caso a condição não seja atendida,  o processo é encaminhado para o [cumprimento](tramitacao2grau.md#Fluxo---Cumprimento-de-determinação). Quando o cumprimento for encerrado, o processo retorna ao fluxo de processar atividades de corregedoria por meio da tarefa Verficar Pendências - Processo Corregedoria.

### Verificar Pendências - Processo Corregedoria

Responsabilidade - Secretaria Judiciária

## Fluxo - Gabinetes

## Fluxo - Cumprimento de determinação

## Fluxo - Preparação de Decisão Colegiada

## Fluxo - Preparação de ato judicial

## Fluxo - Cumprimento de determinação

