+++
title = "Erros de remessa"
date = 2023-01-20T10:29:52-03:00
weight = 6
chapter = true
+++

# Erros de remessa
A remessa é uma das tarefas em que mais ocorrem erros no sistema PJE, isso porque ela faz uma série de validações na instância de origem e na instância de destino.

A orientação é que toda remessa seja conferida, seja pela consulta interna ou pela consulta pública.

Para saber se uma remessa foi bem sucedida, o processo precisa ser verificado na instância de origem (que fez a remessa) e na de destino (para onde a remessa foi feita), devendo atender as seguintes condições:

Processo que é remetido (na instância de origem da remessa) precisa:
+ migrar para uma tarefa estacionária (manter processos expedidos, aguardando apreciação de outra instância, etc.);
+ ter movimentos de baixa e envio;
+ estar bloqueado (aquele aviso “Este processo foi remetido e por isso não pode ser movimentado”).

Processo que é recebido (na instância de destino da remessa) precisa:

**{{<marcar texto="SE FOR PRIMEIRA REMESSA">}}**
+ ser autuado/distribuído.

**{{<marcar texto="SE FOR RETORNO PARA A INSTÂNCIA">}}**
+ ter os documentos produzidos na instância de origem;
+ sair da tarefa estacionária;
+ ter movimentos de recebimento (ou recebimento e reativação, caso seja um processo que já tenha passado pela instância);
+ estar desbloqueado.

Com base nos requisitos acima, será possível definir em que instância (se na da origem da remessa ou se na de destino) se deve atuar para tentar corrigir os erros.

Se não há documentos produzidos na instância de origem, não adianta tentar atuar no destino. Por outro lado, uma vez que os documentos produzidos na origem tenham chegado (casos de retorno para a instância), não há que se falar em nova tentativa de remessa.

{{% notice note %}}
Nas situações em que a tarefa de remessa finaliza sem que o servidor consiga visualizar qual erro ocorreu, pode-se tentar usar a transição **Verifica erro de remessa**, quando disponível. Por vezes, o sistema grava o erro e recupera para exibição ao servidor na tarefa resultante dessa transição. Caso tenha havido problemas na conclusão da remessa e, por meio do uso dessa tarefa, não seja exibido o erro ou o erro não der um caminho para que o servidor consiga corrigir o problema, deve-se abrir chamado relatando o problema.
{{% /notice %}}

Vários erros estão devidamente tratados pelo sistema e retornam uma mensagem clara para o usuário, o que permite a correção pelo próprio servidor ou pelo administrador local, sem a necessidade de abertura de chamado no TSE. Na tabela abaixo, apresentamos como ajustar localmente os principais erros de remessa:

| **Descrição**                                                                                                                                             |                                                                                         **Correção**                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| CEP                                                                                                                                                       |                                                                            [Link]({{< relref "correcoes#cep" >}})                                                                           |
| Tipo de Documento                                                                                                                                         |                                                                     [Link]({{< relref "correcoes#tipo-de-documento" >}})                                                                    |
| Falta de vinculação de Ente ou Autoridade                                                                                                                 |                                                         [Link]({{< relref "correcoes#falta-de-vinculação-de-ente-ou-autoridade" >}})                                                        |
| Expedientes abertos                                                                                                                                       |                                                                    [Link]({{< relref "correcoes#expedientes-abertos" >}})                                                                   |
| Cadastro de pessoa                                                                                                                                        |                                                                    [Link]({{< relref "correcoes#cadastro-de-pessoa" >}})                                                                    |
| Documento de identificação                                                                                                                                |                                                                [Link]({{< relref "correcoes#documento-de-identificação" >}})                                                                |
| Ausência de novos documentos processuais                                                                                                                  |                                                         [Link]({{< relref "correcoes#ausência-de-novos-documentos-processuais" >}})                                                         |
| Remessa concluída, mas o processo não foi para tarefa estacionária                                                                                        |                                             [Link]({{< relref "correcoes#remessa-concluída-mas-o-processo-não-foi-para-tarefa-estacionária" >}})                                            |
| Remessa concluída, mas o processo não teve os movimentos de baixa                                                                                         |                                             [Link]({{< relref "correcoes#remessa-concluída-mas-o-processo-não-teve-os-movimentos-de-baixa" >}})                                             |
| Remessa concluída sem bloqueio do processo                                                                                                                |                                                        [Link]({{< relref "correcoes#remessa-concluída-sem-bloqueio-do-processo" >}})                                                        |
| Processo não foi atuado na instância de destino ou os documentos produzidos na instância de origem não chegaram, mas o processo ficou bloqueado na origem | [Link]({{< relref "correcoes#processo-não-foi-atuado-na-instância-de-destino-ou-os-documentos-produzidos-na-instância-de-origem-não-chegaram-mas-o-processo-ficou-bloqueado-na-origem" >}}) |
| Remessa concluída (os documentos produzidos na instância de origem chegaram) mas o processo não saiu da tarefa estacionária e/ou não foi desbloqueado     |    [Link]({{< relref "correcoes#remessa-concluída-os-documentos-produzidos-na-instância-de-origem-chegaram-mas-o-processo-não-saiu-da-tarefa-estacionária-eou-não-foi-desbloqueado" >}})    |
