---
title: "Audiências"
date: 2023-01-18T19:20:20-03:00
weight: 2
---

Atualmente a possibilidade de realização de audiências dentro do PJe está restrita ao PJe 1G.

## Marcação de audiências
A partir das tarefas **Analisar Novo Processo – ZE, Analisar Determinação – ZE, Analisar Processo – ZE** e nas respectivas tarefas com processos urgentes, selecione a transição Audiências.

Na tarefa **Audiências** existe a opção Finalizar para retornar à tarefa anterior e diversas opções relativas à realização da audiência propriamente dita.

A marcação de nova audiência é feita no final da tela, no agrupador Audiência.

Serão exibidas as opções de designação sugerida e designação manual. Selecione designação sugerida, o tipo de audiência e selecione Procurar horário. O sistema exibirá o próximo horário disponível. Ao clicar em Reservar sala, o sistema agendará a audiência gerando a movimentação de designação nos autos. Se já houver audiência marcada anteriormente não realizada, o usuário deve selecionar a opção Designar nova audiência e prosseguir com a marcação.

Configurações necessárias para o correto funcionamento: 
+ Configurar salas para cada órgão julgador; e
+ Configurar tempo de audiência para cada tipo de audiência e cada órgão julgador; 
+ Informação para administradores: se já houver audiência marcada anteriormente e não realizada, o usuário só conseguirá agendar novas audiências se a variável de fluxo correta estiver setada na tarefa. A expressão a ser utilizada é a seguinte: #{tramitacaoProcessualService.gravaVariavelTarefa(‘pje:fluxo:audiencia:permitirDesignarMultiplas’, true)}. Ela deve ser configurada em uma ação do evento entrar no nó.

## Opções para audiências já designadas
Após agendada, as audiências marcadas aparecerão no agrupador Últimas audiências do processo. 

Na coluna Ações da tabela de audiências deste agrupador estarão disponíveis as seguintes opções:
+ Realização (1)
+ Redesignar 
+ Cancelamento 
+ Converter em Diligência

1 - Realização de audiências já marcadas

Cada audiência agendada terá a lista de opções descrita acima. O usuário deverá clicar em **Realização.**

O sistema apresentará, no final da tela, um quadro denominado **REALIZAR AUDIÊNCIA** para registrar as informações.

O usuário poderá informar se a audiência foi realizada e, em caso afirmativo, os nomes do realizador e do conciliador (podem ser iguais), assim como dados do acordo. 

Ao clicar em Próximo, a audiência ficará marcada como finalizada.

Com isso, a aba **Anexar documento** a audiência passa a ser apresentada. O documento da ata deve ser preenchido pelo editor de texto disponível na aba e depois salvo, com isso, o botão **Assinar documentos(s)** será disponibilizado.

Após assinar, deve-se acionar o botão **Concluir.**

{{% notice info %}}
Mesmo sem esta ação, o documento da ata já será apresentado nos autos digitais.
{{% /notice %}}

Após clicar no botão **Concluir,** o sistema atualizará a tela e exibirá o status da audiência em como Realizada, não apresentando mais a lista de ações. O movimento de realização e o documento assinado serão exibido nos autos. 

{{% notice warning %}}
O movimento de realização será lançado apenas após o botão **Concluir** ser acionado. Caso o botão não seja acionado, o documento eventualmente produzido aparecerá nos autos, mas sem movimento associado. Ou seja, a audiência estará finalizada, mas sem movimento de realização. 
{{% /notice %}}

Nesse caso, na tarefa **Audiências,** será apresentada a opção **Ata de audiência.** A opção exibirá, no final da tela, os dados da realização e permitirá ao usuário clicar em **Próximo.** A tela para construção do documento será exibida, mas o usuário deve clicar apenas em **Concluir.** O movimento será lançado nos autos vinculado ao documento já gerado.

Se a audiência for finalizada sem a edição da ata, ou seja, se o o usuário não finalizar a ata, mas já tiver informado os dados de realização, na tarefa **Audiências** será apresentada a opção **Ata de audiência.** A opção exibirá, no final da tela, os dados da realização e permitirá ao usuário clicar em **Próximo** para construir o documento. Para finalizar, após assinatura, o usuário deve clicar em **Concluir.**

Configurações necessárias para o correto funcionamento: 
+ o parâmetro “pje:audiencia:realizacaoEmFluxo” precisa estar marcado como false;
+ apenas conciliadores vinculados à localização da zona aparecerão na lista de conciliadores; e
+ somente Magistrados configurados no órgão julgador aparecerão na lista de realizadores.

## Informações sobre todas as audiências do processo

Para verificar audiências do processo e seu estado atual, o usuário deverá abrir os autos digitais e, no menu de opções (ícone de três barrinhas horizontais no canto superior direito dos autos) selecionar a opção **Audiência.** O sistema apresentará uma listagem com as audiências já marcadas os respectivos estados atuais.

## Movimento processual
O movimento lançado quando há designação ou realização da audiência é o mesmo, de código 970. O que muda é o complemento. O movimento segue o seguinte formato: Audiência #{tipo_de_audiencia} #{situacao_da_audiencia} conduzida por #{dirigida_por} em/para #{data_hora}, #{local} onde: tipo_de_audiencia - preenchido com o tipo de audiência respectivo.

Também é possível lançar movimento quando o processo está na tarefa Audiências (uso opcional). Essa opção permite que, em havendo alguma decisão proferida em audiência, o movimento desta possa ser registrado nos autos. 

{{% notice note %}}
[Clicando aqui](/docs/manual_audiencias.pdf) você encontra um tutorial com o passo-a-passo necessário para a realização dessa atividade (material cedido pelo TREMG).
{{% /notice %}}
