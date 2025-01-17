
---
title: "Certidão genérica"
date: 2024-08-27T16:33:02-03:00
menuTitle: "Certidão genérica"
weight: 3
---

É possível juntar, individualmente ou em lote, uma certidão genérica utilizando um modelo previamente definido. O modelo será selecionado de acordo com as necessidades do cartório/secretaria.

Para isso, no primeiro grau, o servidor de cada zona deverá definir qual modelo de documento será utilizado na geração da certidão.

{{% notice note %}}
Os modelos que já estão cadastrados podem ser recuperados por meio da funcionalidade **Configuração - Documento - Modelo de documento**. QUALQUER modelo disponível pode ter seu identificador utilizado para gerar a certidão (campo Id na lista de modelos da referida funcionalidade), desde que a tradução das variáveis seja possível.
{{% /notice %}}


A partir das tarefas **Analisar Novo Processo - ZE**, **Analisar Processo** ou **Analisar Determinações**, o usuário pode selecionar a transição **Gerar certidão genérica**. 

Caso nenhum modelo tenha sido definido, o sistema encaminhará o processo para a tarefa **Informar identificador do modelo de certidão**. Ele será apresentado a uma tela que conterá um campo onde ele deve informar o identificador de um modelo de documento válido. Ele deve informar um identificador, selecionar o botão **Salvar** e, após finalizado, selecionar a transição **Confirmar**. Ele pode também desistir de gerar a certidão, selecionando **Cancelar**. 

{{% notice note %}}
A seleção do identificador do modelo de documento registrará um identificador por zona eleitoral. Para selecionar, basta realizar o procedimento em um processo. A partir de então, a seleção estará valendo para todos os processos daquela zona. O usuário poderá alterar o modelo selecionado sempre que precisar.
{{% /notice %}}

Caso o usuário não informe nenhum valor ou informe um identificador de modelo que não existe na base, o sistema encaminhará o processo para a tarefa **Aviso de não seleção de modelo**. A partir dessa tarefa, ele pode tentar informar novamente selecionando **Informar identificador do modelo de certidão**. Caso o usuário já tenha cadastrado em algum momento o identificador de modelo, ele poderá selecionar a transição **Gerar certidão com identificador gravado previamente**. Ele pode também desistir de gerar a certidão, selecionando **Cancelar**. 

Caso tenha selecionado um identificador válido anteriormente, ele será encaminhado para a tarefa **Confirmar identificador do modelo de certidão**. Essa tarefa exibirá o identificador cadastrado. Ele pode selecionar a correção do identificador, selecionando a transição **Informar identificador diferente**. Ele pode também desistir de gerar a certidão, selecionando **Cancelar**. Caso o identificador esteja correto e o usuário queira realmente gerar as certidões, deverá selecionar a transição **Gerar certidão**. Após executada, será juntada uma certidão no processo com o conteúdo do modelo de documento, contendo suas respectivas variáveis traduzidas de acordo com o processo, vinculada ao movimento **Expedição de Certidão**. Se houver mais processos nessa tarefa, o usuário poderá realizar a seleção da movimentação em lote, o que fará com que todos os processos selecionados tenham a certidão juntada com seu respectivo movimento. Após execução da geração, o sistema encaminhará o processo para a tarefa **Verificar certidão**, para que o usuário finalize o procedimento. 

A partir da tarefa **Verificar certidão**, o usuário pode selecionar **Finalizar**, o que retornará o processo para a tarefa inicial, qual seja, **Analisar Novo Processo - ZE**, **Analisar Processo** ou **Analisar Determinações**. Ele pode também selecionar **Gerar outra certidão**, o que deixará o processo na tarefa **Confirmar identificador do modelo da certidão**.

**Observações para administradores (não são administradores de estado - observações são para verificação de comportamento por parte da ASPJE e SESIP):**

O identificador do modelo de documento selecionado será gravado em um parâmetro do sistema denominado 
- **pje:automacao:certidaogenerica:id:XXX**:
  - Onde XXX é o identificador do órgão julgador do processo utilizado para selecionar o modelo. O valor desse parâmetro corresponde ao identificador do modelo de documento que será utilizado para a certidão genérica.

O tipo de documento utilizado é o que está cadastrado no parâmetro **idTipoDocumentoCertidao**, que deve ser o de código **534**. Esse tipo de documento deve estar associado ao papel **Sistema**, de identificador **pje:sistema**, com exigibilidade **Suficiente**.

{{% notice note %}}
Para a correta utilização da funcionalidade, os modelos de documento devem estar configurados corretamente. Se houver problemas na tradução de variáveis, as certidões não serão geradas e a tramitação dos processos pode apresentar erros na tela. Caso isso ocorra, atualize a tela do painel de tarefas, retire o processo da tarefa, cancelando o processo e corrija o modelo de certidão utilizado. Para verificar se a tradução das variáveis ocorre sem problemas, você pode abrir os autos do processo, selecionar a opção de **Juntar documentos**, selecionar o tipo de documento **Certidão** e selecionar o modelo desejado. O sistema traduzirá as variáveis ou apresentará erro na tradução, conforme o caso. Após a confirmação, cancele a edição do documento.
{{% /notice %}}
