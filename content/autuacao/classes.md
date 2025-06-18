---
title: "Classes"
date: 2025-06-16T15:32:23-03:00
weight: 1
---

As classes disponíveis para protocolo de processos obedecem à regra disponível na [documentação do PJe nacional](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn402). Da mesma forma, o sistema apresentará classes de acordo com a mesma regra na retificação da autuação, cuja possibilidade é exibida de acordo com a permissão do usuário. 

Na retificação da autuação, a alteração da classe se dará após o acionamento do botão **Salvar**. Note que, ao mudar a classe na seleção, mesmo antes da seleção do botão **Salvar**, caso não haja assuntos vinculados à nova classe selecionada disponíveis para seleção, o sistema exibe uma mensagem notificando o usuário que o processo ficará sem assunto com aquela seleção. Caso o usuário confirme a alteração por meio do botão **Salvar**, o processo ficará inconsistente. Dessa forma, salienta-se que a permissão ao usuário para realizar retificação de autuação deve ser liberada de forma bastante criteriosa. 

{{% notice info %}}
Para que o usuário possa retificar autuação por meio dos autos digitais, ele deverá ser detentor do seguinte recurso: **/pages/Processo/RetificacaoAutuacao/updateRetificacaoAutuacao.seam**. Além disso, não poderá ser usuário externo (advogado, assistente, jusPostulandi, perito, procurador, assistente de procurador) e deverá ser do mesmo juízo do processo. Para ser do mesmo juízo do processo, ou o servidor é vinculado ao órgão julgador do processo ou exclusivamente vinculado ao órgão julgador colegiado do processo. Por exclusivamente vinculado, entenda-se que o servidor não será considerado do mesmo juízo se estiver vinculado ao mesmo colegiado do processo e a um órgão julgador distinto do órgão do processo.
{{% /notice %}}

{{% notice info %}}
O servidor poderá também retificar autuação por meio de tarefas específicas do fluxo processual desenhadas com a opção de abertura da funcionalidade de retificação.
{{% /notice %}}

A retificação da autuação não altera o peso processual nem o órgão julgador do processo. Para que isso ocorra, o servidor deve utilizar a opção de redistribuição. 

Ao finalizar a retificação do processo, caso a classe tenha sido alterada, o sistema lança no processo o movimento de código 14738 conforme tabela de movimentos do [SGT](https://www.cnj.jus.br/sgt/consulta_publica_movimentos.php). 
