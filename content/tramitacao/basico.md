---
title: "Conceitos iniciais"
date: 2025-11-17T15:42:00-00:00
weight: 1
menuTitle: "Conceitos iniciais"
---

## Conceito de fluxo e de tarefa

Quando falamos em tramitação de um processo eletrônico dentro do Sistema PJe, as noções de fluxo e de tarefa vêm imediatamente à tona. Mas o que vem a ser fluxo e tarefa?
Para que o PJe possa funcionar corretamente, mister se faz a construção prévia de uma estrada sobre a qual os processos necessariamente terão que transitar. O ponto de partida desta estrada equivale ao protocolo da nova
ação feita pelo advogado e o ponto de chegada corresponde ao julgamento definitivo da causa. Tecnicamente, esta estrada é chamada de fluxo e tem as seguintes características:

+ Ser uma estrada de mão dupla, ou seja, o processo tanto pode ir para frente nesse trajeto quanto pode voltar em seu caminho; e
+ Ser um trajeto fixo, cujo caminho pelo qual o processo transitará foi previamente desenhado. A implementação de qualquer mudança nesse trajeto demandará do administrador do Sistema a reforma ou construção de uma nova estrada.

Se fluxo corresponde à estrada pela qual o processo necessariamente terá que transitar, o que vem a ser tarefa? Tarefa pode ser compreendida como os postos de gasolina ao longo da estrada que abastecem o processo com
combustível necessário para que ele vá para frente ou para trás nesse trajeto. Tecnicamente, tarefa corresponde a uma atividade feita no processo que faz com que os autos sejam impulsionados em direção à próxima tarefa do fluxo ou em direção à tarefa anterior do fluxo.

Em geral, o deslocamento do processo entre tarefas decorre de ação do usuário, mas em alguns casos é possível que a movimentação do processo entre tarefas seja feita de forma automática pelo Sistema, sem intervenção humana.

O diagrama abaixo ajuda a compreender como se dá a interação entre fluxo e tarefa:

![Fluxo e tarefa](/imagens/fluxotarefa.jpg)

## Painel do usuário

A tela geral do PJe (chamada de “Painel do usuário”) permite a execução das mais variadas tarefas de fluxo.

![Painel do usuário](/imagens/painelusuario.jpg)

Quando um processo chega em determinada tarefa, o nome da tarefa torna-se visível no “Painel do usuário”, seguido de um número que corresponde à quantidade de processos estacionados naquela tarefa. No exemplo abaixo, temos 7 (sete) processos
estacionados na tarefa “Processo incluído em pauta”. Caso todos os 7 processos da tarefa “Processo incluído em pauta” sejam transitados para outra tarefa, a linha “Processo incluído em pauta” desaparecerá do “Painel do usuário”. Portanto, se o nome da tarefa X não aparece no Painel do usuário, isto quer dizer que, naquele momento, aquele perfil não tem nenhum processo na tarefa X.

![Processos por tarefa](/imagens/processoportarefa.jpg)

Siga o passo a passo abaixo para ingressar na tarefa de um processo específico.

![Seleção da tarefa](/imagens/selecaotarefa.jpg)

![Seleção do processo](/imagens/selecaoprocesso.jpg)

![Execução da tarefa](/imagens/areaexecucao.jpg)

## Tramitando processos

Quando o usuário escolhe um processo para trabalhar, a tarefa é mostrada em toda esta região da tela, conforme abaixo. Em geral, é nessa área que o usuário atua.

![Área de execução](/imagens/areaexecucao2.jpg)

Existem determinadas tarefas em que o usuário somente precisa executar alguma ação nesta minúscula área da tela (para fazer o processo transitar da tarefa atual para tarefa subsequente). O botão abrigado naquela pequena região da tela
chama-se botão de transições.

![Botão de transições](/imagens/botaotransicao.jpg)

Exemplo de tarefas assim são as tarefas de notificação, que precisam apenas avisar ao usuário que algo aconteceu, seja um erro ou a finalização de um processamento. Algumas tarefas existentes no PJe da Justiça Eleitoral: **Aviso publicação mural**, **Aviso publicação**, **Aviso de expedientes abertos**, **Impedimento de remessa**, **Impedimento de devolução**, entre outras.

Já em outros tipos de tarefa, o usuário precisará executar primeiramente alguma ação nesta região maior da tela, seguida de uma segunda ação no botão de transições (para fazer o processo transitar da tarefa atual para a tarefa subsequente).

![Execução de tarefa e transição](/imagens/tarefatransicao.jpg)

A maior parte das tarefas do PJe são assim. 

Por outro lado, há tarefas em que o usuário somente precisa se preocupar em executar algo nesta região maior da tela. Concluída as ações na região maior da tela, o PJe se encarrega de transitar automaticamente o processo para a tarefa
subsequente, dispensando assim o uso do botão de transições. Esses tipos de tarefa são mais raros.

![Tarefa que será executada e tramitada automaticamente](/imagens/tarefaassinatura.jpg)

Quando se remete ou redistribui um processo, a própria finalização da redistribuição ou da remessa dentro da área de trabalho da tarefa faz com que ela seja tramitada. De forma similar, nas tarefas de assinatura de documentos, a assinatura bem sucedida faz com que o processo seja tramitado. 

Por fim, existem outras tarefas raras em que o usuário fica dispensado de executar alguma ação tanto na região maior quanto na região menor da tela. Nesses tipos de tarefa, quando uma determinada condição é implementada (chamamos
de gatilho a implementação dessa condição), o PJe se encarrega de transitar automaticamente o processo para a tarefa subsequente, sem intervenção humana.

![Tarefa que será executada por gatilho](/imagens/tarefagatilho.jpg)

**Processo com prazo em curso** é um exemplo clássico de tarefa que é tramitada por gatilho. O gatilho, no caso, é a expiração do prazo ou a resposta dos expedientes. Mais detalhes sobre esse funcionamento estão na seção [Controle de prazos](/prazos/tarefas).

## Configuração de fluxo

As configurações necessárias para definir o caminho pelo qual o processo pode passar são realizadas por administradores do sistema. 

Para realizar essas configurações, é essencial que o administrador tenha conhecimentos dos conceitos apresentandos na configuração nacional do PJe sobre definição de fluxos - [acesse aqui](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Configura%C3%A7%C3%B5es%20iniciais/#defini%C3%A7%C3%A3o-de-fluxos).

Os fluxos na Justiça Eleitoral são mantidos de forma centralizada pelo TSE. A Assessoria do PJe, via de regra, é a responsável por essas definições e alterações, mas a SESIP (área da STI - Secretaria de Tecnologia da Informação - que mantém o PJE) também realiza alterações conforme definições da Assessoria. 

As definições são mantidas de forma a que todos os estados compartilhem os mesmos fluxos. Essa uniformidade é o que permite que a Assessoria faça a manutenção de todos os regionais. 
