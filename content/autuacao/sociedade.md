---
title: "Sociedade de advogados"
date: 2025-07-24T15:32:23-03:00
weight: 6
---

Conforme previsto no § 1º do art. 272 do CPC/2015, "Os advogados poderão requerer que, na intimação a eles dirigida, figure apenas o nome da sociedade a que pertençam, desde que devidamente registrada na Ordem dos Advogados do Brasil".

Dessa forma, o PJe da Justiça Eleitoral foi alterado para atender à previsão legal, assim como fornecer algumas facilidades para o usuário quando usadas Sociedade de advogados na autuação de processos.

## Cadastro de sociedades em processos

De forma similar ao que ocorre com o cadastro de advogados, o cadastro de uma sociedade de advogados deve ocorrer pelo cadastro de processos, por meio da vinculação da sociedade representando uma parte. O cadastro poderá ser realizado pelo número da OAB ou pelo número do CNPJ.

O tipo de parte será apresentado ao usuário caso esteja devidamente configurado na classe processual. Instruções sobre essa configuração estão na documentação do PJe nacional:

[Configuração de tipo de parte vinculado à classe judicial](https://docs.pje.jus.br/manuais-de-uso/Manual%20de%20referencia%20PJe%201.0#tipo-da-parte)

## Restrições 

Só serão cadastradas sociedades com CNPJ. Se a OAB da sociedade não estiver associada a um CNPJ no [Cadastro Nacional de Sociedade de Advogados](https://cnsa.oab.org.br/), o cadastro não será efetuado.

Da mesma forma, não será possível cadastrar sociedade que não tenha associado ao seu CNPJ um CPF do responsável.

O cadastro da sociedade recupera também os sócios. Ao cadastrar uma sociedade, o sistema cadastra automaticamente os sócios como advogados vinculados, fazendo com que esses advogados tenham acesso ao acervo e às intimações vinculadas à sociedade. 

Só serão recuperados sócios na OAB que estiverem com situação regular. Na recuperação do cadastro da sociedade na OAB, ela precisará de pelo menos um sócio com situação regular. Se a sociedade for individual e o único sócio não estiver regular, a sociedade não será recuperada. 

Ao inativar um advogado no PJe, ele não estará automaticamente desvinculado da sociedade. O que ocorre é que, e isso é uma regra já existente no PJe, a inativação o impedirá de fazer login e, consequentemente, de atuar conforme sua vinculação.

{{% notice info %}}
Usuários com permissões específicas podem administrar a sociedade, vinculando e desvinculando sócios.
{{% /notice %}}

## Utilização em expedientes 

Após cadastrada, a sociedade será utilizada na intimação da mesma forma que ocorre com a representação por parte de advogados. O sistema deve permitir aos advogados vinculados à sociedade a resposta das intimações e o acesso aos processos como parte de seu acervo, assim como o acesso à lista de intimações. 

No caso de intimação de partes no diário e no mural representadas por sociedade de advogados, as sociedades devem aparecer como representantes nas publicações, da mesma forma que ocorre com os advogados. Os advogados atuarão em nome da sociedade quando a sociedade representar uma parte no processo. 

Já se a sociedade for ela mesma uma parte cadastrada como pessoa jurídica, a atuação dessa parte no processo se dará por meio de procuradorias ou de representantes cadastrados, ou seja, um advogado ou uma sociedade representando a parte pessoa jurídica que, no caso, é também uma sociedade.

## Verificação dos sócios 

O sistema permite que se saiba quais são os sócios de uma sociedade por meio do menu **Configuração - Órgãos de representação - Sociedade de advogados**. 

Além disso, ao exibir os autos do processo, caso tenha permissão, o usuário pode clicar na parte sociedade que, na tela de detalhes da parte, serão exibidos os nomes dos sócios vinculados.


## Observações sobre comportamentos já existentes no PJe relacionados a advogados

### Intimação via sistema

A intimação via sistema só é permitida para usuários cuja representação já tenha feito login no sistema. Para o caso de sociedades, pelo menos um dos sócios deve já ter realizado o login.

### Restrições no protocolo

No protocolo de ações por parte do advogado o sistema vincula automaticamente o advogado como representante no polo ativo e não permite a exclusão. 

Caso seja incluída alguma sociedade como representante no polo ativo que tenha como um dos sócios o advogado logado, o sistema permitirá a exclusão do advogado como representante. 

Da mesma forma, se só houver uma sociedade vinculada ao advogado logado representando o polo ativo e não houver advogados representantes, o sistema não permitirá a exclusão daquela sociedade, a menos que se inclua uma sociedade com o advogado logado ou o próprio advogado como representante do polo ativo.

Para o usuário externo, o tipo de parte **Advogado** não é apresentado no polo passivo. Da mesma forma, o tipo de parte **Sociedade** também não é.

### Remessa/MNI

O protocolo de processo via remessa/mni não admite envio de sócios, apenas da identificação da sociedade por meio do seu CNPJ. Dessa forma, o cadastro da sociedade no destino recuperará os sócios que estão vinculados na OAB no momento do protocolo do processo.

### Processos não protocolados

A tela de processos não protocolados utiliza como regra atualmente as localizações físicas dos processos iniciados como restrição para exibição dos processos. Com a entrada das sociedades, o sistema verificará se o processo é da localização física do usuário logado (regra atual) ou se o processo tem como parte no polo ativo uma sociedade do advogado logado .

### Push

A inclusão de advogados sócios da sociedade no push ocorrerá nos mesmos momentos em que o advogado é incluído no processo no PJe versão atual. Serão incluídos os sócios vinculados à sociedade no momento da inclusão automática no push. Caso um advogado seja vinculado à sociedade posteriormente, o processo só será vinculado à lista de processos do seu push caso ele atue manualmente para esse fim.

### Segredo de justiça e documentos sigilosos

Os processos em segredo de justiça, caso tenham cadastrados sociedades como visualizadores, estarão disponíveis para sócios das sociedades. 

Quando um advogado que faz parte da sociedade junta um documento sigiloso no processo, conforme comportamento atual do sistema, o advogado fica automatimente cadastrado como visualizador. Para que outros advogados da sociedade visualizem o documento sigiloso, a sociedade deve ser cadastrada como visualizadora.

### Impedimento/suspeição

Ao cadastrar Impedimentos/suspeição  do tipo advogado para um magistrado, os pontos de verificação de impedimento deverão verificar se há sociedade daquele advogado vinculado ao processo do magistrado, de forma a exibir os alertas que o sistema já emite hoje para processos com advogados cadastrados.
