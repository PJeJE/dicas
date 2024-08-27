
---
title: "Certidão genérica"
date: 2024-08-27T16:33:02-03:00
menuTitle: "Certidão genérica"
weight: 1
---

É possível juntar, individualmente ou em lote, uma certidão genérica de acordo com as necessidades do cartório utilizando um modelo previamente definido. 

Para isso, o servidor de cada zona deverá definir qual modelo de documento será utilizado na geração da certidão.

A partir das tarefas "Analisar Novo Processo - ZE", "Analisar Processo" ou "Analisar Determinações", o usuário pode selecionar a transição "Gerar certidão genérica". 

Caso nenhum modelo tenha sido definido, o sistema encaminhará o processo para a tarefa "Informar identificador do modelo de certidão". Ele será apresentado a uma tela que conterá um campo onde ele deve informar o identificador de um modelo de documento válido. Ele deve informar um identificador e selecionar "Confirmar". Ele pode também desistir de gerar a certidão, selecionando "Cancelar". 

Caso o usuário não informe nenhum valor ou informe um identificador de modelo que não existe na base, o sistema encaminhará o processo para a tarefa "Aviso de não seleção de modelo". A partir dessa tarefa, ele pode tentar informar novamente selecionando "Informar identificador do modelo de certidão". Caso o usuário já tenha cadastrado em algum momento o identificador de modelo, ele poderá selecionar a transição "Gerar certidão com identificador gravado previamente". Ele pode também desistir de gerar a certidão, selecionando "Cancelar". 

Caso tenha selecionado um identificador válido anteriormente, ele será encaminhado para a tarefa "Confirmar identificador do modelo de certidão". Essa tarefa exibirá o identificador cadastrado. Ele pode selecionar a correção do identificador, selecionando a transição "Informar identificador diferente". Ele pode também desistir de gerar a certidão, selecionando "Cancelar". Caso o identificador esteja correto e o usuário queira realmente gerar as certidões, deverá selecionar a transição "Gerar certidão". Após executada, será juntada uma certidão no processo com o conteúdo do modelo de documento, contendo suas respectivas variáveis traduzidas, de acordo com o processo, vinculado ao movimento "Expedição de Certidão". Se houver mais processos nessa tarefa, o usuário poderá realizar a seleção da movimentação em lote, o que fará com que todos os processos selecionados tenham a certidão juntada com seu respectivo movimento. Após execução da geração, o sistema encaminhará o processo para a tarefa "Verificar certidão", para que o usuário finalize o procedimento. 

A partir da tarefa "Verificar certidão", o usuário pode selecionar "Finalizar", o que retornará o processo para a tarefa inicial, qual seja, "Analisar Novo Processo - ZE", "Analisar Processo" ou "Analisar Determinações". Ele pode também selecionar "Gerar outra certidão", o que deixará o processo na tarefa "Informar identificador do modelo de certidão".

Observações para administradores:

O identificador do modelo de documento selecionado será gravado em um parâmetro do sistema denominado 
- **pje:automacao:certidaogenerica:id:XXX`**:
  - Onde XXX é o identificador do órgão julgador do processo utilizado para selecionar o modelo. O valor desse parâmetro corresponde ao ID do modelo de documento que será utilizado para a certidão genérica.

{{% notice note %}}
Para a correta utilização da funcionalidade, os modelos de documento devem estar configurados corretamente. Se houver problemas na tradução de variáveis, as certidões não serão geradas e a tramitação dos processos pode apresentar erros na tela. Caso isso ocorra, atualize a tela do painel de tarefas, retire o processo da tarefa, cancelando o processo e corrija o modelo de certidão utilizado. Para verificar se a tradução das variáveis ocorre sem problemas, você pode abrir os autos do processo, selecionar a opção de "Juntar documentos", selecionar o tipo de documento "Certidão" e selecionar o modelo desejado. O sistema traduzirá as variáveis ou apresentará erro na tradução, conforme o caso. Após a confirmação, cancele a edição do documento.
{{% /notice %}}
