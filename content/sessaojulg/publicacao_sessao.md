---
title: "Publicação em sessão"
date: 2022-11-29T16:31:12-03:00
weight: 5
---

Na Justiça eleitoral, ao ser proferida decisão em processo na sessão de julgamento, a intimação do acórdão pode ser feita na própria sessão de julgamento, passando a fluir prazo a partir dali.

No PJe, essa opção pode ser realizada por meio da publicação do acórdão ou da certidão de julgamento em sessão.

A opção está disponível no papel de assessor de plenário, menu **Audiências e Sessões - Publicação de decisões em sessão.**

Ao entrar na tela, deve-se selecionar uma data de sessão e selecionar a pesquisa. As sessões que tiverem acórdão ou certidão de julgamento associados retornarão na pesquisa. 

Depois, deve-se preencher, na linha do(s) processo(s) correspondente que se quer publicar, as opções da publicação: data, tipo do prazo, prazo. Se houver dois documentos, ou seja, o acórdão e a certidão, na coluna Documento deve-se marcar qual se quer publicar. Geralmente a certidão já vem marcada.

Os processos que serão publicados devem estar selecionados por meio da caixa de seleção da primeira coluna. Os documentos só aparecerão se estiverem devidamente vinculados à sessão e se estiverem assinados. Depois de tudo pronto, deve-se selecionar o botão salvar e depois publicar. Essa ação não pode ser desfeita.

Por meio dessa mesma tela, o usuário pode publicar em sessão decisões monocráticas. O procedimento é o mesmo, mas para que as decisões apareçam na consulta, o gabinete tem que usar uma tarefa específica sinalizando que a decisão monocrática deve ser publicada em sessão.

Depois de tudo finalizado, o PJe gera uma intimação para as partes envolvidas de acordo com o que foi preenchido. Para intimação do Ministério Público como fiscal da lei, a intimação será realizada de acordo com os parâmetros abaixo:

+ pje:intimarEmSessaoColegiada:fiscalDaLei - Notifica que o fiscal da lei será intimado nas publicações em sessão de decisões colegiadas quando estiver marcado como **true**
+ pje:intimarEmSessaoMonocratica:fiscalDaLei - Notifica que o fiscal da lei será intimado nas publicações em sessão de decisões monocráticas quando estiver marcado como **true**

O Ministério Público, como fiscal da lei, pode não ser intimado caso os parâmetros estejam configurados como **false**.

{{% notice note %}}
A geração da intimação não altera a tramitação do processo, ou seja, caso o processo esteja nas tarefas **Selecionar documento para acórdão** e **Analisar determinação**, por exemplo, permanecerá nessas tarefas. Caso seja o desejo do servidor, ele pode encaminhar o processo para o controle de prazos por meio da transisão **Verificar controle de prazos**, conforme descrito na seção [Controle de prazos](/prazos/tarefas/).
{{% /notice %}}

