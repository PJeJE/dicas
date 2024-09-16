---
title: "Indisponibilidade na OAB"
date: 2024-09-16T19:29:29-03:00
menuTitle: "Indisponibilidade na OAB"
---

O cadastro de advogados no PJe ocorre quando o advogado é inserido na autuação de um processo ou pelo próprio login do advogado. Esse cadastro sempre utiliza o serviço do **Cadastro Nacional de Advogados** mantido pelo **Conselho Federal da OAB** - https://cna.oab.org.br.

Conforme regra https://www.pje.jus.br/wiki/index.php/Regras_de_neg%C3%B3cio#RN266, caso haja indisponibilidade do serviço que consulta a situação de advogados na OAB, o servidor poderá atuar para realizar o cadastro ele mesmo, sem validações. 

Essa possibilidade pode ser utilizada quando o servidor tem certeza que o advogado possui cadastro, que é o caso, por exemplo, de um processo que foi protocolado no primeiro grau com um advogado em um momento em que o serviço da OAB estava disponível e, na ocasião da remessa do processo como recurso para o segundo grau, o serviço da OAB esteja indisponível. Caso o recurso seja protocolado em um período de um a dois meses posterior ao protocolo inicial do processo no primeiro grau, o servidor saberá que o advogado tem cadastro válido. 

Pode acontecer também de o advogado apresentar documentações que comprovem a regularidade de seu cadastro.

Para fazer esse cadastro, o servidor deve ter o CPF do advogado. Pela opção **Configuração - Pessoa - Física**, o servidor deve selecionar a aba **Pré-cadastro**, informar o CPF e selecionar **Pesquisar**. O sistema trará o nome da pessoa e o servidor deve selecionar a opção **Confirmar**. Os dados da pessoa conforme seu cadastro da Receita Federal serão recuperados. O servidor deve utilizar a opção **Tornar advogado/procurador**. O sistema apresentará uma tela de confirmação com a opção **Especializar para** selecionada com o valor **Advogado**. O servidor deve selecionar a opção **Especializar e fechar**. O sistema apresentará a mensagem **Especialização concluída. Complemente o cadastro**. O servidor deve selecionar **OK** e complementar o cadastro do advogado pela opção **Configuração - Pessoa - Advogado - Confirmar credenciamento**.

Na opção **Confirmar credenciamento**, o servidor deve utilizar o CPF do advogado para recuperar o cadastro dele que foi iniciado. Após recuperar, deve selecionar o ícone de lápis disponível na tela de resultado. Deve complementar os dados do cadastro com a OAB do advogado e selecionar **Salvar**. Após isso, deve selecionar a opção **Anexar termo**. O sistema apresentará um documento modelo contendo o termo de compromisso que, usualmente, deve ser assinado pelo advogado. Nesse caso, o servidor assinará o termo, acionando a opção **Assinar termo de compromisso** disponível ao final do texto do termo. O cadastro do advogado estará finalizado. 

Se for o caso de remessas, o servidor terá que retirar o advogado da autuação na origem. O servidor pode remover a parte com os advogados na tela **Partes** da remessa, o que não altera a retificação do processo na origem. O sistema permitirá a remessa. No destino, o servidor deve adicionar o advogado, que deve ter sido previamente cadastrado conforme orientações acima. Caso o servidor tenha optado por retificar a autuação do processo na origem antes da remessa, não pode esquecer de retificar novamente após realizar a remessa. Para realizar esse procedimento, ele terá que desbloquear o processo, **Iniciar digitalização**. O sistema abrirá uma tarefa **Processo destravado** que deve ser finalizada. O servidor realizada a retificação da autuação e depois precisa utilizar a transição **Bloquear processo que está em outra instância**, disponível nas tarefas de análise, para deixar o processo corretamente bloqueado em tarefa estacionário, conforme esperado após uma remessa.

{{% notice warning %}} 
Para o caso de remessas em que for necessário retirar o advogado antes do envio, é essencial que se faça uma certidão notificando a exclusão para que, no destino, o processo seja alterado para ficar com a autuação correta. **CERTIFIQUE SEMPRE** antes do envio.
{{% /notice %}}

