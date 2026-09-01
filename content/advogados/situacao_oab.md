---
title: "Situação da Inscrição na OAB"
date: 2022-11-23T17:26:41-03:00
linkTitle: "Situação OAB"
weight: 3
---

Como qualquer perfil no PJe, para que o advogado atue, o seu cadastro precisa estar ativado. Para cada pessoa, existe o cadastro geral do usuário e existe o cadastro dele em seu perfil de atuação. Em primeiro lugar, seu cadastro geral tem que estar **ativo** para que ele atue no PJe. Além disso, o cadastro dele no perfil também precisa estar **ativo**. De forma mais básica, a atuação do advogado no PJe deve depender de como ele é visto pela OAB, já que é a entidade de representação e regulamentação da advocacia. Dessa forma, os servidores atuam no PJe tendo como norte a situação do advogado perante sua entidade de representação.

Os cadastros dos advogados na OAB registram diferentes situações. Temos nas bases da Justiça Eleitoral algumas delas:

+ REGULAR
+ EXCLUIDO
+ FALECIDO
+ LICENCIADO
+ SUSPENSO
+ CANCELADO

Independente dessas situações, o que importa para atuação do advogado no PJe é se o seu cadastro está ativo ou inativo. 


## Utilização da situação da OAB no PJe

No cadastramento inicial, o PJe utiliza o número do CPF para consultar o Cadastro Nacional dos Advogados (CNA). São retornadas inscrições de advogados, suplementares e de estagiários, mas apenas as inscrições em situação regular são consideradas.

Caso não exista inscrição ativa, o sistema exibirá uma mensagem informando que foram recuperadas informações no CNA, mas não há inscrição ativa, permitindo que o usuário prossiga o cadastro como Jus Postulandi.

No entanto, não existe impedimento técnico no sistema para que um usuário interno do tribunal torne essa pessoa um advogado e confirme seu credenciamento, mesmo sem número de inscrição na OAB. Nesse caso, na retificação de autuação e nos autos do processo será mostrada a situação da inscrição do advogado apenas para usuários internos:

![Situação OAB](/imagens/situacao_adv_tela_retificacao.png)

Caso o advogado possua mais de uma inscrição regular, a informação acima é exibida a partir da primeira OAB encontrada no momento do cadastramento (em geral a OAB principal), ignorando-se as demais, o que pode não refletir a exata situação cadastral do advogado.

{{% notice warning %}}
É Importante ressaltar que os dados apresentados tem apenas caráter informativo, mesmo que em situação irregular.
{{% /notice %}}

IMPORTANTE: Um advogado com a situação regular no momento do cadastro no PJe e que posteriormente teve sua inscrição cancelada e/ou tornada irregular, continua como regular no sistema até que um usuário interno do PJe, a partir da funcionalidade **Confirmar credenciamento,** utilize o botão **nova validação na OAB** para atualizar os dados do advogado. Há também a execução de procedimento automático durante a madrugada que atualiza a situação de inscrição de advogados cadastrados como válidos. O processamento atualiza a situação da inscrição de acordo com a informação disponível no serviço correspondente da OAB, mas o fato da situação estar irregular não impede o advogado de atuar nos processos vinculados.

Desse modo, a situação da inscrição da OAB do advogado causa impedimento apenas no momento do cadastro inicial do usuário. Uma vez cadastrado no sistema como advogado e independentemente da situação da inscrição em momento posterior, nenhum outro impedimento é feito.

Ou seja, é permitido ao advogado protocolizar novos processos, juntar documentos e inclusive solicitar habilitação nos autos, mesmo que em situação irregular.

{{% notice info %}}
Já existem demandas (PJEVII-4416, PJEVII-3889, PJEVII-3173 e PJEVII-4536) em andamento no Conselho Nacional de Justiça (CNJ) que visam melhorias na funcionalidade e desenvolvimento de alertas para advogados penalizados.
{{% /notice %}}

<!--
## Cadastro validado (ou -não validado-)

Como dito anteriormente, o usuário interno (ou administrador) pode cadastrar uma pessoa física como advogado (assim como ocorre com o perfil jus postulandi). Esse cadastro pode ser realizado mesmo que o serviço da receita e da OAB retornem alguma irregularidade no cadastro. O objetivo principal é não impedir o cadastramento desses perfis, especialmente se os serviços estiverem indisponíveis e dada a fé pública, que todo servidor tem. O sistema tem essa opção para que o cadastro não seja impedido como um todo.

É importante ressaltar que, após realizar novas validações, o sistema não apaga a antiga. Em algumas telas do PJe, pode ocorrer de, na hora de exibir o advogado, o sistema pegar a primeira validação das que vierem. Se a validação recuperada foi justamente uma mal sucedida, o sistema exibe o alerta **Não validado**. Se vc, como servidor, sabe que aquele advogado é válido, não há problema, isso é só um alerta. Esse alerta só aparece para servidores. 

-->
## Atualização do cadastro do advogado pelo servidor

Conforme descrito mais acima, quando utilizado o cadastramento automático via recuperação de dados pelo serviço do CNA, o cadastro inicial do advogado é incluído no PJe como ativo apenas se sua situação no referido cadastro estiver como **REGULAR**.

Em muitas situações o servidor precisa que o advogado deixe de atuar no PJe. Temos posse de membros juristas, temos listas enviadas pela OAB notificando de suspensão, falecimento, exclusão e o próprio procedimento automático que executa na madrugada que recupera atualizações do cadastro na OAB. Em qualquer dessas situações, o procedimento a ser realizado pelo servidor é a inativação do seu cadastro como advogado. Com a devida permissão, o servidor deve acessar a opção pelo menu **Configuração - Pessoa - Advogado - Confirmar credenciamento**. Ao pesquisar pelo advogado, deve-se entrar em seu cadastro e marcar a opção **Situação deste perfil** como **Inativo**. Na pesquisa, se utilizado o ícone de lixeira disponível na barra de ferramentas do resultado da pesquisa, o efeito é o mesmo. 

Existe um procedimento automático que tem o objetivo de validar novamente advogados que já estão cadastrados como válidos no sistema. Esse procedimento recupera todos os advogados cujo registro de pessoa física esteja como **validado** e, a partir do CPF de cadastro, recupera consultas anteriores realizadas à OAB desse advogado. Caso não tenha sido feita consulta anterior ou caso tenha sido feita, mas a data da consulta é recente (dentro dos últimos quinze dias), o procedimento não recuperará aquele cadastro. A nova consulta, caso seja feita e recupere dados válidos, removerá o registro anterior e registrará o novo.


Um cadastro é considerado **validado** quando é realizado pelo pelo próprio usuário (assinando um termo se responsabilizando pelo cadastro) ou quando foi feito por um administrador/servidor com autorização. Um cadastro de um advogado como parte em um processo, por exemplo, não é um cadastro validado.

{{% notice info %}}
O procedimento automático que atualiza a situação da OAB dos advogados só faz atualização para cadastros que não tenham o registro da OAB recuperado ou cujo registro tenha sido recuperado a mais de quinze dias. Essa restrição dos quinze dias existe para diminuir o ônus de processamento da execução do procedimento automático. 
{{% /notice %}}

{{% notice info %}}
O procedimento automático que atualiza a situação da OAB, em algumas instalações, pode não estar habilitado. Para verificar se na sua instalação está, utilize o menu **Configuração - Ambiente - Jobs da aplicação** e procure pelo termo **validarOABProcessor**. Se os campos **Previous Fire Time** e **Next Fire Time** estiverem preenchidos, vc saberá quando o procedimento foi executado pela última vez e quando o será novamente, respectivamente. Se o termo **validarOABProcessor** nem aparecer, significa que o procedimento não está sendo executado na sua instalação.
{{% /notice %}}

Está em curso o desenvolvimento de uma funcionalidade que apresentará ao servidor a possibilidade de ser inserida uma certidão automática de modelo configurável em todos os processos em que o advogado atue, de forma que possa ficar mais claro nos autos do processo o motivo pelo qual ocorreu a inativação. 

### Nova validação OAB

Para usuários com permissão, existe um botão disponível por meio da opção **Configuração - Pessoa - Advogado - Confirmar credenciamento** que permite que o usuário faça uma **NOVA VALIDAÇÃO OAB**. O acionamento desse botão fará com que o sistema utilize o CPF de cadastro do advogado e consulte o serviço da OAB para recuperar dados daquele advogado. Caso seja recuperado algum dado, a validação anterior, se existia, é apagada, e o sistema grava a nova validação recuperada. As validações já realizadas que não foram apagadas podem ser visualizadas pelo botão **MOSTRAR DADOS OAB** disponível pelo mesmo item da menu **Confirmar credenciamento**.
