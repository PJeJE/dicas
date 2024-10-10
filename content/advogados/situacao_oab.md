---
title: "Situação da Inscrição na OAB"
date: 2022-11-23T17:26:41-03:00
menuTitle: "Situação OAB"
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

No entanto, não existe impedimento técnico no sistema para que um usuário interno do tribunal torne essa pessoa um advogado e confirme seu credenciamento, mesmo sem número de inscrição na OAB. Nesse caso, somente na retificação de autuação será mostrada a situação da inscrição do advogado, e apenas para usuários internos:

![Situação OAB](/imagens/situacao_adv_tela_retificacao.png)

Caso o advogado possua mais de uma inscrição regular, a informação acima é baseada apenas na primeira OAB encontrada no momento do cadastramento (em geral a OAB principal), ignorando-se as demais, o que pode não refletir a exata situação cadastral do advogado.

{{% notice warning %}}
É Importante ressaltar que os dados apresentados tem apenas caráter informativo, mesmo que em situação irregular.
{{% /notice %}}

IMPORTANTE: Um advogado com a situação regular no momento do cadastro no PJe e que posteriormente teve sua inscrição cancelada e/ou tornada irregular, continua como regular no sistema até que um usuário interno do PJe, a partir da funcionalidade **Confirmar credenciamento,** utilize o botão **nova validação na OAB** para atualizar os dados do advogado.

Desse modo, a situação da inscrição da OAB do advogado causa impedimento apenas no momento do cadastro inicial do usuário. Uma vez cadastrado no sistema como advogado e independentemente da situação da inscrição em momento posterior, nenhum outro impedimento é feito.

Ou seja, é permitido ao advogado protocolizar novos processos, juntar documentos e inclusive solicitar habilitação nos autos, mesmo que em situação irregular.

{{% notice info %}}
Já existem demandas (PJEVII-4416, PJEVII-3889, PJEVII-3173 e PJEVII-4536) em andamento no Conselho Nacional de Justiça (CNJ) que visam melhorias na funcionalidade e desenvolvimento de alertas para advogados penalizados.
{{% /notice %}}

## Atualização do cadastro do advogado pelo servidor

Conforme descrito mais acima, quando utilizado o cadastramento automático via recuperação de dados pelo serviço do CNA, o cadastro inicial do advogado é incluído no PJe como ativo apenas se sua situação no referido cadastro estiver como **REGULAR**.

Em muitas situações o servidor precisa que o advogado deixa de atuar no PJe. Temos posse de membros juristas, temos listas enviadas pela OAB notificando de suspensão, falecimento, exclusão... Em qualquer dessas situações, o procedimento a ser realizado pelo servidor é a inativação do seu cadastro como advogado. Com a devida permissão, o servidor deve acessar a opção pelo menu **Configuração - Pessoa - Advogado - Confirmar credenciamento**. Ao pesquisar pelo advogado, deve-se entrar em seu cadastro e marcar a opção **Situação deste perfil** como **Inativo**. Na pesquisa, se utilizado o ícone de lixeira disponível na barra de ferramentas do resultado da pesquisa, o efeito é o mesmo. 

Está em curso o desenvolvimento de uma funcionalidade que apresentará ao servidor a possibilidade de ser inserida uma certidão automática de modelo configurável em todos os processos em que o advogado atue, de forma que possa ficar mais claro nos autos do processo o motivo pelo qual ocorreu a inativação. 
