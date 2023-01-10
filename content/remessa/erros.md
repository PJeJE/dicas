---
title: "Correção de erros"
date: 2022-11-29T16:29:52-03:00
---

A remessa é uma das tarefas em que mais ocorrem erros no sistema PJE, isso porque ela faz uma série de validações na instância de origem e na instância de destino.

Vários erros estão devidamente tratados pelo sistema e retornam uma mensagem clara para o usuário, o que permite a correção pelo próprio servidor ou pelo administrador local, sem a necessidade de abertura de chamado no TSE. Na sequência, vamos apresentar os principais erros e as soluções.

+ CEP

Esse erro aparece quando alguma das partes do processo está com o CEP inválido ou em branco.
Para correção, basta ir ao menu dos autos processuais, na opção retificar autuação, aba partes, dentro das partes verificar a aba endereço e conferir o CEP de todas as partes e advogados, procedendo às correções necessárias.
Feito isso, é preciso deletar a remessa (na aba processo) e fazer nova tentativa de envio.

+ Tipo de Documento

Esse erro acontece quando existe, no processo a ser remetido, um documento cujo tipo é inexistente na instância de destino. 
Para correção, deve-se, primeiro, verificar qual tipo de documento apresenta erro, pesquisando o número do id do documento na árvore processual. 
Delete a remessa e tramite o processo para a tarefa Reclassificar documentos, depois altere o tipo de documento para uma opção diferente. 
Feito isso, faça nova tentativa de remessa.

+ Falta de vinculação de Ente ou Autoridade

Esse erro acontece porque o ente ou autoridade, quando criado, foi vinculado a uma pessoa jurídica cadastrada no sistema sem CNPJ.
Para correção vá em **Configuração/Pessoa/Ente ou autoridade** do PJE da instância de origem e, após localizar a autoridade informada no erro, faça a devida vinculação na aba Formulário. Escolha uma pessoa jurídica que possua CNPJ.
Outra opção, é corrigir o cadastro da pessoa jurídica vinculada ao ente ou autoridade, incluindo o CNPJ. Isto pode ser feito em **Configuração/Pessoa/Pessoa Jurídica.**
Feito isso, é preciso deletar a remessa (na aba processo) e fazer nova tentativa de envio.

+ Expedientes abertos

Esse erro acontece quando o processo que está sendo remetido possui algum expediente em aberto. Normalmente o expediente que ainda está aberto é sem prazo.
Para correção, delete a remessa e tramite o processo para a tarefa Fechar expediente manualmente. Nela, os expedientes abertos deverão ser fechados.
Caso, ao realizar o procedimento descrito acima, não apareça nenhum expediente em aberto, vá no menu **Processo/Pesquisar/Consulta de prazos** e pesquise pelo número do processo e mais algum critério. 
Feito isso, faça nova tentativa de remessa.

+ Cadastro de pessoa

Esse erro acontece quando, na hora da remessa, por alguma instabilidade da integração com o sistema da Receita Federal, uma parte ou pessoa que assinou algum documento no processo, não consegue ser cadastrada automaticamente na instância de destino.
Para correção, basta que o Administrador do Sistema do PJE da instância de destino faça este cadastramento no menu **Configuração/Pessoa/Física** ou **Jurídica,** conforme o caso. Na opção pré-cadastro, faça o cadastro manual do CPF ou CNPJ que constar no erro e faça nova tentativa de remessa.

+ Documento de identificação

Esse erro acontece quando algum documento de identificação de uma das partes do processo está em branco. 
Para correção, retifique a atuação (aba partes), selecionando cada uma das partes e verificando, na aba documentos de identificação, os documentos constantes, procedendo às correções necessárias (verificar inclusive advogados).
Feito isso, é preciso deletar a remessa (na aba processo) e fazer nova tentativa de envio.

+ Ausência de novos documentos processuais:

Quando se tenta remeter um processo sem que tenha sido elaborado ou juntado algum documento na instância, o erro “Não foram encontrados novos documentos processuais” impede o envio. A solução consiste na elaboração de algum documento. Como sugestão, pode ser incluída uma certidão de remessa.
Feito isso, é preciso deletar a remessa (na aba processo) e fazer nova tentativa de envio.

{{% notice tip %}}
Além destes erros tratados, existem casos em que a remessa é concluída com falhas, ou ainda, situações em que aparentemente a remessa foi feita, mas o processo não chegou ao destino. Na maior parte das vezes uma nova tentativa de remessa resolve o problema, na sequência, vamos abordar as formas de correção para estes casos.{{% /notice %}}

Para saber se uma remessa foi bem sucedida, o processo precisa ser verificado na instância de origem (que fez a remessa) e na de destino (para onde a remessa foi feita), devendo atender as seguintes condições:

Processo que é remetido (na instância de origem da remessa) precisa:
+ migrar para uma tarefa estacionária (manter processos expedidos, aguardando apreciação de outra instância, etc.);
+ ter movimentos de baixa e envio;
+ estar bloqueado (aquele aviso “Este processo foi remetido e por isso não pode ser movimentado”).
+
Processo que é recebido (na instância de destino da remessa) precisa: 
SE FOR PRIMEIRA REMESSA
+ ser autuado/distribuído.

SE FOR RETORNO PARA A INSTÂNCIA
+ ter os documentos produzidos na instância de origem;
+ sair da tarefa estacionária;
+ ter movimentos de recebimento (ou recebimento e reativação, caso seja um processo que já tenha passado pela instância); e
+ estar desbloqueado.

Com base nos requisitos acima, será possível definir em que instância (se na da origem da remessa ou se na de destino) se deve atuar para tentar corrigir os erros.

Se não há documentos produzidos na instância de origem, não adianta tentar atuar no destino. Por outro lado, uma vez que os documentos produzidos na origem tenham chegado (casos de retorno para a instância), não há que se falar em nova tentativa de remessa.

Nos próximos tópicos vamos ensinar como ajustar localmente cada um dos pontos acima.

+ Remessa concluída, mas o processo não foi para tarefa estacionária

Se o processo estiver bloqueado (com o aviso “Este processo foi remetido e por isso não pode ser movimentado”)

+ Remessa concluída, mas o processo não teve os movimentos de baixa

Algumas vezes pode ocorrer de o processo ser remetido à outra instância, mas os movimentos de baixa não serem lançados na origem. Nesse caso, o servidor pode fazer o lançamento dos movimentos.

Para que os movimentos sejam lançados corretamente, na tarefa de envio, devem ser selecionados o motivo da remessa e a instância de destino. Se não selecionar o motivo da remessa, a transição apresentará erro e não será concluída. Se não selecionar a instância de destino, o sistema poderá atribuir um valor errado ao movimento e este não poderá ser posteriormente ajustado.

Estando o processo na tarefa de remessa, deve-se selecionar a transição **Registrar movimento baixa (selecione instância e motivo).** O processo será tramitado para uma tarefa intermediária denominada **Conferir processo remetido.** Essa tarefa é importante para identificarmos os casos em que se tenha tramitado manualmente o processo sem que ele tenha chegado ao destino, facilitando o trabalho da investigação de problemas.

A partir desta tarefa, deve-se selecionar **Aguardando apreciação do TRE** ou a tarefa estacionária equivalente no segundo grau para que o processo fique na tarefa de finalização do envio.

+ Remessa concluída sem bloqueio do processo

Algumas vezes, apesar de a remessa ser concluída com sucesso (ou usuário vai saber isto verificando na Consulta interna ou pública da instância de destino), o sistema não bloqueia o processo na origem para tramitação e inclusão de documentos. Esse bloqueio é fundamental para que novas informações processuais sejam inseridas apenas na instância onde está ocorrendo a tramitação atual do processo.

Ocorrendo esta situação, se o processo estiver na tarefa de finalização do envio, deve-se escolher a opção **Retornar para análise sem registro de movimento.**

Para realizar o bloqueio, há uma transição chamada **Bloquear processo que está em outra instância,** disponível a partir das tarefas de análise (para o primeiro grau: **Analisar processos, Analisar novo processo e Analisar determinação,** urgentes ou não. Para as instâncias colegiadas: **Verificar pendências).**

Isso fará com que o processo seja tramitado para a tarefa de finalização do envio (tarefa estacionária) e seja bloqueado para tramitação de petições.

Importante: em alguns casos as transições mencionadas não estarão disponíveis (nos fluxos de corregedoria, por exemplo, ou quando os processos são mais antigos e estão em fluxos desatualizados) entre em contato com a ASPJe para maiores orientações sobre como proceder em tais situações.

+ Processo não foi atuado na instância de destino ou os documentos produzidos na instância de origem não chegaram, mas o processo ficou bloqueado na origem

Nesse caso não houve a remessa. Ainda que, ao analisar o processo apenas na instância de origem, tudo indique que o procedimento foi executado com sucesso.

Quando a remessa não ocorre de maneira efetiva, a primeira coisa que o usuário precisa fazer é uma nova tentativa. 

Em estando o processo bloqueado (com o aviso “Este processo foi remetido e por isso não pode ser movimentado”), abra os autos e clique na opção **Iniciar atividade de digitalização.**

No primeiro grau a tarefa está disponível para o perfil de administrador estado e nos TREs foi originalmente configurado para os Administradores.

O acionamento desta opção retirará o bloqueio do processo e abrirá uma nova tarefa, denominada **Processo destravado.** O servidor deve finalizar a tarefa (antes de fazer a nova tentativa de envio). 

{{% notice warning %}}
Para solução de problemas técnicos pela equipe de suporte, podem existir outras opções nessa tarefa (como novo fluxo originárias), jamais as utilize quando estiver tentando desbloquear um processo.{{% /notice %}}

Depois, é só tramitar o processo na tarefa principal em que ele se encontra já desbloqueado.

Em geral o processo estará na tarefa de finalização do envio (tarefa estacionária). A opção **Reativar com registro de movimento** lança o movimento processo reativado, a opção **Retornar para análise sem registro de movimento,** não.

{{% notice tip %}}
Em alguns casos as transições para retirada da tarefa estacionária mencionadas acima não estarão disponíveis (nos fluxos de corregedoria, por exemplo, ou quando os processos são mais antigos e estão em fluxos desatualizados, nestes casos você pode chamar o processo à ordem para tirá-lo da tarefa ou entrar em contato com a ASPJe para maiores orientações sobre como proceder).
{{% /notice %}}

+ Remessa concluída (os documentos produzidos na instância de origem chegaram) mas o processo não saiu da tarefa estacionária e/ou não foi desbloqueado

Pode acontecer de um processo retornar de uma outra instância via remessa e os movimentos de reativação não terem sido lançados. Neste caso, a partir da tarefa de finalização do envio, o servidor pode acionar a transição **Reativar com registro de movimento.** O processo será encaminhado para a tarefa de análise e nos autos o movimento de reativação será lançado.

