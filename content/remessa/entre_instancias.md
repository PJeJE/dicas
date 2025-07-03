---
title: "Remessa entre instâncias"
date: 2022-11-29T16:28:40-03:00
weight: 1
---

A **Remessa para outra instância** é uma tarefa exclusiva do PJE do 2º grau e deve ser utilizada quando se objetiva enviar um processo que tenha iniciado no TRE, para o TSE. Deve ser utilizada, também, quando o processo foi iniciado físico na Zona Eleitoral, migrado no TRE, e precisa descer para o 1º grau.

Essa tarefa protocola um novo processo no destino, com classes e assuntos específicos bem como novas configurações de partes.

As classes exibidas na tarefa são aquelas que, na instância de destino, estejam configuradas com a opção remessa entre instâncias marcada como Sim.

{{% notice warning %}}
Caso a classe selecionada esteja configurada no destino com a marcação exige numeração própria, um novo número de processo será gerado. 
{{% /notice %}}

Essa remessa lança o movimento de código 123: Remetidos os autos, com os seus complementos cadastrados, bem como o código 22: Baixa definitiva. 

Após a confirmação, o sistema movimentará o processo para a tarefa **Aguardando apreciação de outra instância** onde ficará bloqueado para novas petições.

{{% notice info %}}
As remessas do PJe, exceto a remessa entre jurisdições (utilizada entre zonas do mesmo Estado), utilizam o MNI. Essa remessa **não permite a escolha de um órgão julgador específico,** a definição do órgão julgador se dará pela distribuição inicial do processo, de acordo com as competências previamente configuradas. Caso o processo já exista na instância, **a remessa só realiza a atualização dos documentos e o desbloqueio do processo, mas não consegue fazer com que o processo que já existe seja redistribuído para outra zona.**
{{% /notice %}}

Usuário da remessa

A remessa entre instâncias é uma integração que ocorre dentro da própria justiça. Apesar disso, o PJe utiliza as operações do MNI para a integração, que são operações padronizadas e que necessitam de login nos moldes definidos pelo padrão. Idealmente, a identificação do servidor que realiza a remessa deveria ser utilizada para o login necessário na remessa, mas,  para a efetivação desse procedimento, o servidor precisaria ter um cadastro no destino com as devidas permissões necessárias à remessa. Isso não é o que ocorre, pelo contrário, via de regra, o servidor que tem cadastro no primeiro grau não tem cadastro no segundo. Para contornar essa situação, na Justiça Eleitoral foi utilizado o login de um usuário administrador que está cadastrado em todas as instâncias, de forma a não termos problemas com permissões. Assim, o usuário de juntada dos documentos recebidos por meio da remessa fica registrado como esse usuário administrador. Para recuperar o usuário de juntada do documento na origem, o servidor pode verificar as assinaturas do documento por meio do ícone de cadeado.
