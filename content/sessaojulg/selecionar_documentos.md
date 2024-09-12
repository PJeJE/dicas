---
title: "Selecionar documentos para acórdão"
date: 2024-09-12T14:39:20-03:00
weight: 6
menuTitle: "Selecionar documentos"
---

Na justiça eleitoral, os processos, após julgamento em sessão, são encaminhadaos para tarefas de elaboração de acórdão. Muitas vezes o processo vai a julgamento novamente sem ter tido o acórdão anterior assinado. O usuário precisa poder selecionar para qual sessão será construído o acórdão. Além disso, existem situações em que foram construídos vários documentos de relatório, voto ou ementa, e o usuário precisa definir quais serão utilizados para construção daquele acórdão. Para esse fim, temos a tarefa **Selecionar documentos para acórdão**. 

A referida tarefa permite também que se façam ajustes nos documentos de sessão relacionados à vinculação desses documentos a uma sessão ou à vinculação dos documentos a órgãos julgadores.

As alterações permitidas por meio dessa tarefa podem deixar os documentos de sessão inconsistentes e afetarem a execução de outras tarefas relacionadas a documentos de sessão. Dessa forma, antes de utilizar a tarefa, tenha certeza sobre quais campos precisam estar preenchidos para cada documento ajustado.

A tarefa **Selecionar documentos para acórdão** é apresentada no início do fluxo de elaboração do acórdão. O fluxo é iniciado automaticamente após o encerramento do julgamento do processo ou quando o usuário seleciona a opção **iniciar novo fluxo de acórdão.**

Nessa tarefa, é possível fazer a vinculação manual dos documentos de um julgamento à respectiva sessão de julgamento e também selecionar quais documentos serão utilizados para a produção do acórdão.

A tarefa exibe todas as pautas onde o processo tem registro e os documentos do tipo relatório, ementa e voto vinculados ao processo. 

Essas informações encontram-se em abas separadas, assim o usuário pode selecionar quais desses documentos serão o relatório, a ementa, o voto do relator, o voto do vencedor e os votos de vogais do acórdão a ser montado, bem como para qual pauta será produzido o acórdão.

Se houver recursos internos vinculados, o sistema também exibirá os dados do recurso.

As abas **Ementa, Relatório, Voto Relator, Voto Vencedor** e **Acórdão** permitem a seleção de apenas uma opção de documento, mas a seleção não é obrigatória.

Dessa forma, se não houver seleção para uma determinada aba, ao enviar o processo para elaboração do acórdão, a aba correspondente não terá documento previamente construído. Essa seleção refletirá na elaboração do acórdão desde que, após selecionadas todas as opções conjuntamente, o usuário utilize o botão **Salvar seleção.**

## Informações técnicas sobre a configuração de parâmetros

+ As abas de votos (voto relator, voto vencedor e votos vogais) exibirão sempre o mesmo conteúdo, ou seja, todos os documentos construídos a instância atual e não excluídos, cujos tipos sejam os configurados nos parâmetros: idTipoProcessoDocumentoVoto, pje:painel:magistrado:sessao:tiposVotoVogal:ids e pje:flx:votacaoVogal:tiposVoto:ids.
+ A aba de ementa trará todos os documentos do tipo, configurado no parâmetro: idTipoProcessoDocumentoEmenta.
+ A aba relatório trará todos os documentos do tipo, configurado no parâmetro: idTipoProcessoDocumentoRelatorio.
+ A aba acórdão trará todos os documentos do tipo, configurado no parâmetro: idTipoProcessoDocumentoAcordao.

## Voto de ex-membro 

A tarefa Minutar relatório voto e ementa não deve ser executada por gabinete diferente do gabinete do relator. Caso isso ocorra, o PJe cria documentos repetidos na mesma tarefa e o usuário não percebe, já que o documento não é recarregado no editor. 

Depois que entrar na tarefa, é muito difícil corrigir essa situação porque o sistema fica sempre tentando recuperar aquele documento errado já criado e não consegue.

Para contornar esse problema, foi criada no fluxo uma tarefa chamada **Minutar relatório voto e ementa RE.** Essa tarefa faz com que o processo seja redistribuído para o gabinete atual sem que haja movimento de redistribuição.

A transição está disponível pela tarefa **Minutar Relatório Voto e Ementa.**

{{% notice warning %}}
Essa transição deve ser usada antes de construir documento de relatório voto e ementa pelo gabinete. Se utilizada depois, terá que ser acionada a TI para ajustar ou apagar os documentos errados produzidos. 
{{% /notice %}} 

No TSE há uma orientação passada para a COARE e gabinetes sobre essa questão. Está no SEI 2020.00.000009345-3. As alterações no fluxo foram feitas a partir de setembro de 2020. Apesar da alteração ter sido realizada para atender à necessidade de julgamento de Recurso Extraordinário por órgão diverso do relator, é a maneira que se tem hoje para encaminhar o processo para ex-ministro construir voto. Para encaminhar para o ministro que está no gabinete de ex-presidência ou ex-membro, utilize, pela judiciária, as opções disponíveis para encaminhamento em sustituição. Não utilize as opções disponíveis para recesso.
