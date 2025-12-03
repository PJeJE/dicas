+++
title = "Remessa"
date = 2022-11-21T15:00:17-03:00
weight = 17
chapter = true
pre = "<b>16. </b>"
+++

### Seção 16

# Remessa

A atual seção tem o objetivo de oferecer orientações gerais a respeito de remessas e devoluções para outra instância. São remessas ditas externas, ou seja, trata-se do envio dos autos para outro Tribunal ou outra Zona Eleitoral.

É importante ressaltar que as operações de remessa e devolução sempre vêm acompanhadas do respectivo bloqueio do processo para inclusão de novos movimentos e documentos na instância de origem. 

{{% notice info %}}
A remessa entre jurisdições atualmente é utilizada para redistribuições entre órgãos jurisdicionais pertecentes ao mesmo tribunal e não faz o bloqueio do processo para inclusão de novos movimentos e documentos.
{{% /notice %}}

Para evitar prejuízos após o bloqueio do processo, o sistema restringe a remessa e a devolução entre instâncias nas seguintes situações:

- Processo é um recurso interno
- Processo tem mais de uma tarefa aberta

A devolução também é impedida caso o processo seja originário da instância atual do processo.

Caso ocorram situações de impedimento, ao tentar remeter ou devolver um processo, o sistema encaminhará o usuário para uma tarefa de aviso denominada **Impedimento de remessa** ou **Impedimento de devolução**. A tarefa exibirá os detalhes do processo para que o usuário verifique em qual caso de impedimento ele se enquadra. Abaixo um exemplo de aviso:

![Impedimento de devolução](/imagens/impedimentodevolucao.jpg)

Na imagem acima, o impedimento está relacionado à devolução, já que o nome da tarefa é **Impedimento de devolução** e o texto inicial relata **O processo não pode ser devolvido**. Caso o impedimento fosse de remessa, o nome da tarefa seria **Impedimento de remessa** e o texto inicial seria **O processo não pode ser remetido**. O motivo do impedimento na imagem acima é que o processo é originário da instância atual, conforme está descrito em uma das características do processo listada em **Dados sobre o processo atual** - **Processo originário dessa instância**. Observe que o sistema também exibe a informação **Há 1 tarefa(s) aberta(s) para esse processo.** Caso fosse exibida essa mesma informação com o número de tarefas maior que 1, também seria impedimento, tanto para remessa quando para devolução. Observe também que a informação **Não é um recurso interno** é exibida. Caso fosse exibido **É um recurso interno**, também seria um impedimento para remessa e devolução. 

{{% children  %}}

