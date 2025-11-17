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

## Configuração de fluxo

As configurações necessárias para definir o caminho pelo qual o processo pode passar são realizadas por administradores do sistema. 

Para realizar essas configurações, é essencial que o administrador tenha conhecimentos dos conceitos apresentandos na configuração nacional do PJe sobre definição de fluxos - [acesse aqui](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Configura%C3%A7%C3%B5es%20iniciais/#defini%C3%A7%C3%A3o-de-fluxos).

Os fluxos na Justiça Eleitoral são mantidos de forma centralizada pelo TSE. A Assessoria do PJe, via de regra, é a responsável por essas definições e alterações, mas a SESIP (área da STI - Secretaria de Tecnologia da Informação - que mantém o PJE) também realiza alterações conforme definições da Assessoria. 

As definições são mantidas de forma a que todos os estados compartilhem os mesmos fluxos. Essa uniformidade é o que permite que a Assessoria faça a manutenção de todos os regionais. 
