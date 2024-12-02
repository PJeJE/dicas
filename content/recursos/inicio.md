---
title: "Registrando um recurso"
date: 2022-11-29T16:25:39-03:00
weight: 2
---

O recurso é interposto quando o usuário externo (advogado, procurador, parte) inclui um novo documento expondo seu pleito. O documento, se classificado corretamente pelo usuário, terá o tipo correspondente à classe recursal interna.

Feito isso, é iniciada a tarefa **Registrar recurso** para que o servidor faça o devido registro. 

Como o início dessa tarefa é resultado de uma configuração no tipo de documento, caso o usuário externo não classifique corretamente sua petição ou o tipo de documento não esteja corretamente configurado, a tarefa não será iniciada automaticamente. 

{{% notice warning %}}
Para configurar corretamente a tarefa a ser iniciada quando da juntada pelo usuário externo (advogado/procurador) de documento recursal, o tipo de documento deve ter como **Fluxo associado** o fluxo que contém a tarefa de registro de recurso. O sistema entende, desse forma, que ao ser inserido um documento desse tipo, será iniciada uma tarefa de registro de recurso.
{{% /notice %}}

Quando, ao analisar os autos do processo, o servidor percebe que o documento de petição inserido pelo advogado é um recurso que foi indevidamente classificado, basta que este inicie a tarefa de registro de recurso. Está possibilidade se dá a partir da tarefa **Analisar determinação:**

![Informações do recurso](/imagens/recurso_2.jpg)

## Classificação

O primeiro passo no registro do recurso é a classificação. Nessa etapa, serão informados o documento principal do registro e também se o recurso foi interposto para o processo originário ou para um outro recurso (caso já tenham sido registrados recursos para esse processo anteriormente).

A lista de **Recursos já registrados (1)** exibe todos os recursos já registrados para o processo. Cada item corresponde a uma capa processual a mais já gerada para o processo originário.

{{% notice warning %}}
Para que a cadeia recursal se forme sobre um recurso já registrado, este precisa ser selecionado. Caso contrário, a cadeia recursal conterá apenas a classe do recurso novo e do processo originário.
{{% /notice %}}

A lista de **Recursos não registrados (2)** exibe todos os documentos vinculados a classes recursais classificadas como recurso interno e que não estão ainda vinculados a uma capa processual recursal.

Caso a classificação da peça recursal tenha sido feita errada, o documento estará na lista **Outros documentos do processo (3)** e a reclassificação acontece nessa mesma tela, por meio do ícone de lápis (4) disponível na coluna **Ações**, do documento correspondente:

![Informações do recurso](/imagens/recurso_3.jpg)

Ao selecionar salvar, o sistema moverá o documento, agora reclassificado, da lista Outros documentos do processo para a lista Recursos não registrados.

Para o registro do recurso, é obrigatório que um item da lista Recursos não registrados esteja selecionado. Se o usuário tentar prosseguir sem a seleção, o sistema não permitirá, notificando que a seleção deve ser realizada.

## Cadeia recursal

O segundo passo no registro do recurso permite ao usuário confirmar como ficou a cadeia recursal e alterar o órgão julgador de distribuição do recurso.

A **Cadeia recursal** identifica, na forma de siglas ou nomes de classe encadeadas no cabeçalho da capa do processo, se o recurso tem como base uma decisão proferida no processo ou uma decisão proferida em outro recurso:

![Informações do recurso](/imagens/recurso_4.jpg)

Por padrão, os cabeçalhos das capas processuais exibirão sempre a cadeia recursal com as siglas da classe, assim como já ocorre com o processo originário.

## Alteração do órgão julgador

Em alguns casos, o julgamento do recurso terá como relator um órgão julgador diferente do relator originário do processo. No TSE, por exemplo, em Recursos Extraordinários, a competência para julgamento do recurso é da presidência.

Para esses casos, o sistema permite a seleção de um órgão julgador de distribuição do recurso diferente do órgão julgador originário do processo:

![Informações do recurso](/imagens/recurso_5.jpg)

A possibilidade de ajuste da relatoria no momento do registro do recurso não impede ajustes posteriores, já que o recurso pode ser redistribuído a qualquer tempo, sem que isso resulte na redistribuição do processo originário ou de eventuais outros recursos vinculados.

{{% notice info %}}
A distribuição de recursos não impacta nos pesos dos cargos.
{{% /notice %}}

## Seleção das partes

O terceiro passo permite ao usuário informar as partes do recurso:

![Informações do recurso](/imagens/recurso_6.jpg)

Os tipos de parte do recurso são os tipos de parte vinculados à classe processual do recurso, conforme configurado em **Configuração – Tabelas Judiciais - Classe Judicial - Classe Judicial.**

O sistema fará a conversão automática das partes do processo nos tipos de parte principais vinculados à classe do recurso, mas o usuário poderá alterar os tipos, assim como acrescentar ou remover partes e seus representantes.

## Finalização do registro

No quarto e último passo, o usuário pode verificar o resumo das informações do recurso e selecionar a finalização do registro:

![Informações do recurso](/imagens/recurso_7.jpg)

Ao selecionar a opção Cadastrar recurso, o sistema envia o recurso cadastrado para a primeira tarefa do fluxo vinculado à classe recursal.

{{% notice warning %}}
Observe que, a qualquer tempo, a tarefa pode ser finalizada sem que o registro do recurso tenha sido concluído. Não há prejuízo algum. Se a finalização da tarefa for selecionada erroneamente, pode-se iniciar um novo registro.
{{% /notice %}}



