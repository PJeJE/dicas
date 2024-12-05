---
title: "Redistribuições"
date: 2024-12-04T12:09:20-03:00
weight: 6
menuTitle: "Redistribuições"
---
As redistribuições no PJe, em muitos casos, seguem as mesmas regras da distribuição inicial realizada no protocolo do processo. 

Abordaremos algumas particularidades das redistribuições nesta seção.

## Redistribuição por prevenção

Conforme descrito no sítio https://www.pje.jus.br/wiki/index.php/Distribui%C3%A7%C3%A3o, existem situações de prevenção abordadas na distribuição de processos. Temos na Justiça Eleitoral, inclusive, um caso de prevenção específico, conforme detalhamos na seção do [Artigo 260 do código eleitoral](distribuicao/260). Os indicativos de prevenção tratadas pelas regras de negócio descritas na seção Distribuição da wiki do PJe não são utilizados na Justiça Eleitoral, mas para as instalações do PJe que os utilizam, sempre fica registrada uma pendência de confirmação. Esta pendência faz com que, mediante uso de configurações de fluxo específicas, o sistema exiba para o servidor que encontrou um indicativo de prevenção para que possa ser analisado e eventualmente confirmado. Mesmo na situação de confirmação, o servidor terá que redistribuir o processo para o relator do processo paradigma. 

Para redistribuições, existe a posssibilidade do servidor selecionar, como motivo da redistribuição, a opção **Prevenção**. Após essa seleção, ele deve informar qual processo está relacionado ao atual que está sendo redistribuído. Para esse cenário, caso não tenha sido registrada ainda prevenção entre os processos, o sistema registrará, nas conexões do processo (aba **Processos associados** dos autos digitais), uma ligação com o processo informado como **Processo paradigma** como pendente de confirmação e encaminhará o processo sendo redistribuído para o mesmo órgão julgador do processo paradigma informado. Rotineiramente, o registro não terá efeito prático, já que o servidor já realizou a redistribuição e não precisará revisar o processo para confirmar que a prevenção existe.

{{% notice warning %}}
Informação apenas para administradores: A conexão registrada, para o caso de tarefas de fluxo configuradas com a variável do tipo **frame** de nome **Processo_Fluxo_prevencao_analiseProcessosPreventos**, será exibida na referida tarefa do processo. Caso a conexão seja confirmada ou negada (na coluna **Prevento** da tarefa, selecionar **Prevento** ou **Não prevento** e depois selecionar **Continuar**), a conexão deixará de ser exibida na tarefa. A opção **Continuar** só estará disponível se a variável de fluxo **pje:fluxo:confirmaPrevencao** estiver configurada nas ações de eventos do fluxo. O usuário administrador pode também remover a variável **Processo_Fluxo_prevencao_analiseProcessosPreventos** da configuração da tarefa no fluxo e a pendência de confirmação deixará de ser exibida(botão de lixeira na lista **Variável** da tarefa no fluxo). Essa exibição não afeta em nada a tramitação do processo. 
{{% /notice %}}


