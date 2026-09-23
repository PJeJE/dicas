---
title: "Remessa entre instâncias"
date: 2022-11-29T16:28:40-03:00
weight: 1
---

A **Remessa para outra instância** é uma tarefa exclusiva do PJE do 2º grau e deve ser utilizada quando se objetiva enviar um processo que tenha iniciado no TRE, para o TSE. Deve ser utilizada, também, quando o processo foi iniciado físico na Zona Eleitoral, migrado no TRE, e precisa descer para o 1º grau.

Essa tarefa protocola um novo processo no destino, com classes e assuntos específicos, bem como novas configurações de partes.

As classes exibidas na tarefa são aquelas que, na instância de destino, estejam configuradas com a opção remessa entre instâncias marcada como Sim.

{{% notice warning %}}
Caso o destino seja uma instância de estado diferente, um novo número de processo será gerado. Não será assim se a remessa for para o TSE ou se vier do TSE. 
{{% /notice %}}

Essa remessa lança o movimento de código 123: Remetidos os autos, com os seus complementos cadastrados, bem como o código 22: Baixa definitiva. 

Após a confirmação, o sistema movimentará o processo para a tarefa **Aguardando apreciação de outra instância** onde ficará bloqueado para novas petições.

{{% notice info %}}
As remessas do PJe, exceto a remessa entre jurisdições (utilizada entre zonas do mesmo Estado), utilizam o MNI. Essa remessa permite a escolha de um órgão julgador específico caso o destino tenha competências que estejam configuradas com essa opção habilitada. A distribuição inicial do processo se dará de acordo com as competências previamente configuradas. Caso o processo já exista na instância, **a remessa só realiza a atualização dos documentos e o desbloqueio do processo, mas não consegue fazer com que o processo que já existe seja redistribuído para outra zona.**
{{% /notice %}}

Na tela de remessa, ao exibir a aba processo, o sistema verifica a competência do processo de acordo com suas características iniciais. Se a competência identificada permitir a seleção de órgão julgador, o sistema deve exibir os órgãos julgadores da jurisdição selecionada vinculados à competência identificada. Se houver mais de uma competência possível, a exibição ou não da lista de órgãos julgadores estará condicionada à seleção da competência, novamente respeitando a regra de que a competência deve permitir a seleção do órgão.

Sendo assim, a partir dos dados jurisdição selecionada, classe e o assunto principal do processo, o sistema faz uma consulta na instância de destino para saber quais as competências possíveis desse processo no destino. Se houver apenas uma competência, o sistema assume que a competência do processo será essa e, se for o caso de essa competência exigir a identificação de um órgão julgador para direcionamento da distribuição, deverá também fazer uma consulta à lista de órgãos julgadores competentes a fim de exibi-los para seleção do usuário. Se houver mais de uma competência possível, o sistema deverá solicitar a indicação de qual é a competência e se for selecionada uma competência que exige um órgão julgador, mostrar a lista para indicação.

{{% notice info %}}
O sistema só deve exibir na lista de órgãos julgadores para seleção órgãos disponíveis na instância de destino.
{{% /notice %}}

## Usuário da remessa

A remessa entre instâncias é uma integração que ocorre dentro da própria justiça. Apesar disso, o PJe utiliza as operações do MNI para a integração, que são operações padronizadas e que necessitam de login nos moldes definidos pelo padrão. Idealmente, a identificação do servidor que realiza a remessa deveria ser utilizada para o login necessário na remessa, mas,  para a efetivação desse procedimento, o servidor precisaria ter um cadastro no destino com as devidas permissões necessárias à remessa. Isso não é o que ocorre. Pelo contrário, via de regra, o servidor que tem cadastro no primeiro grau não tem cadastro no segundo. Para contornar essa situação, na Justiça Eleitoral foi utilizado o login de um usuário administrador que está cadastrado em todas as instâncias, de forma a não termos problemas com permissões. Assim, o usuário de juntada dos documentos recebidos por meio da remessa fica registrado como esse usuário administrador. Para recuperar o usuário de juntada do documento na origem, o servidor pode verificar as assinaturas do documento por meio do ícone de cadeado.

## Verificação de acesso ao destino

As possibilidades de envio de um processo via remessa aparecem por meio de uma caixa de opções nas tarefas de remessa. Ao selecionar o destino (campo **Instância**, conforme imagem abaixo), o usuário deve utilizar o botão **Verificar acesso** para testar antes mesmo de fornecer os dados da remessa se a conexão com o destino está ok. Se o sistema retornar a mensagem **Conexão com o endpoint OK**, o usuário pode prosseguir com o preenchimento dos dados da remessa e finalizar o procedimento.


![Destino](/imagens/remessadestino.png)

