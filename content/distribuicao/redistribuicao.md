---
title: "Redistribuições"
date: 2024-12-04T12:09:20-03:00
weight: 6
menuTitle: "Redistribuições"
---
As redistribuições no PJe em muitos casos seguem as mesmas regras da distribuição inicial realizada no protocolo do processo. 

Abordaremos algumas particularidades das redistribuições nesta seção.

## Redistribuição por prevenção

Conforme descrito no sítio https://www.pje.jus.br/wiki/index.php/Distribui%C3%A7%C3%A3o, existem situações de prevenção abordadas na distribuição de processos. Temos na Justiça Eleitoral, inclusive, uma caso de prevenção específico, conforme detalhamos na seção do Artigo 260 do código eleitoral. 

Para redistribuições, existe a posssibilidade do servidor selecionar, como motivo da redistribuição, a opção **Prevenção**. Para esses casos, o sistema registrará, nas conexões do processo (aba **Processos associados** dos autos digitais), uma ligação com o processo informado como **Processo paradigma** e encaminhará o processo sendo redistribuído para o mesmo órgão julgador do processo paradigma informado. 


{{% notice warning %}}
Informação para administradores: A conexão registrada, para o caso de tarefas de fluxo configuradas com a variável do tipo **frame** de nome **Processo_Fluxo_prevencao_analiseProcessosPreventos** será exibida na referida tarefa do processo. Caso a conexão seja confirmada, a conexão deixará de ser exibida na tarefa. O usuário administrador pode também remover a variável da configuração da tarefa no fluxo e a pendência de confirmação deixará de ser exibida. Essa exibição não afeta em nada a tramitação do processo. 
{{% /notice %}}


