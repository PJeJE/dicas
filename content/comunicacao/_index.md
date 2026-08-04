+++
title = "Comunicação de Atos Processuais"
date = 2022-11-21T14:58:50-03:00
weight = 8
chapter = true
pre = "<b>8. </b>"
+++

### Seção 8

# Comunicação de Atos Processuais

{{% children  %}}

## Publicações no DJe

Um dos meios mais frequentes utilizado nas comunicações de atos processuais é o Diário de Justiça Eletrônico. O DJE da Justiça Eleitoral tem algumas particularidades para atender às necessidades da Justiça Eleitoral. Definições a respeito do DJE podem ser encontradas no [STI conhecimento](https://sticonhecimento.tse.jus.br/copp/seaju/sistemas/novo-dje).

O próprio DJe trata os autos sigilosos, omitindo os dados sensíveis do processo e das partes.

Isso é feito com base no sigilo do processo: em sendo ele sigiloso, o DJe omitirá os dados na publicação.

{{% notice warning %}}
Na tarefa **Preparar ato de comunicação,** no 2º passo, existe a opção **sigiloso** ao lado do nome da parte, mas ela não tem efeito na publicação do DJe. Ou seja, se o processo não for sigiloso, os dados da parte aparecerão mesmo que esta opção esteja selecionada. A finalidade da opção Sigiloso na tarefa Preparar ato de comunicação é fazer com que o documento que será criado/selecionado em Instrumento de comunicação (após clicar no lápis) seja sigiloso. No entanto, a recomendação é NÃO utilizar essa marcação. Ela não se comporta como o esperado e depende de correção.
{{% /notice %}}


## Intimação em lote

A intimação em lote é a opção que o usuário tem, nas tarefas **Preparar comunicação**, de realizar a comunicação com vários processos de uma vez só.

O usuário tem a possibilidade de indicar a criação de documento novo para ao menos um dos expedientes, situação em que ele seleciona o modelo a ser utilizado para criação.

Após a finalização do preenchimento das informações, o sistema iniciará a construção dos expedientes, encaminhando os processos para uma tarefa de aguardo do processamento. Em caso de erro no processamento para criação de expedientes para um processo, ele é movimentado para uma tarefa de erro; em caso de sucesso na criação dos expedientes para o processo, ele é movimentado no caminho normal do fluxo para envio dos expedientes pelo meio escolhido.

No caso de seleção de documento novo para criação do expediente, é feita validação de que o tipo de documento escolhido para a comunicação tem modelos disponíveis.

No caso dos processos, é feita a verificação se existem partes no polo selecionado e, em caso de intimação por meio de sistema, se todas as partes do tipo de destinatário selecionado podem ser intimadas por esse meio.

Em caso de qualquer erro de validação, a resposta é retornada para o usuário e nenhum processo do lote é enviado para construção da intimação.

<!--
Parâmetros utilizados pela funcionalidade:


pje:tarefas:lote:tiposDocumentoProcessoPermitidos: Lista de códigos de tipo de documento separados por vírgula que indica quais tipos de documento existentes nos processos poderão ser utilizados na funcionalidade de ato de comunicação em lote. O padrão solicitado pela Assessoria foi o Edital - código 14404.

Quando não existe ou está desativado, impede a utilização deste recurso na funcionalidade.

Quando existe com valor inválido ou quando pelo menos um dos tipos listados não existe em todos os processos do lote, também impede a utilização deste recurso na funcionalidade.

pje:tarefas:lote:permiteMultiplosExpedientesPorPolo: Parâmetro que indica se a funcionalidade permitirá a criação de mais de um expediente por polo. O padrão solicitado pela Assessoria é falso. Caso o parâmetro não exista ou tenha valor diferente de boolean, também é considerado falso.

pje:tarefas:lote:qtdeMaximaProcessoAtoComunicacaoLote: Parâmetro que indica a quantidade máxima de processos que podem ser selecionados para o processamento em lote. O padrão é 50.

pje:fluxo:lote:atoComunicacao:tarefaAguardar: Parâmetro que indica o nome da tarefa utilizada pela funcionalidade de ato de comunicação em lote para manter os processos que estão aguardando o processamento para criação de seus expedientes.

pje:comunicacao:prazo:default: Parâmetro que indica o prazo numérico padrão a ser mostrado na funcionalidade. Segue a mesma regra e comportamento da funcionalidade individual.

pje:fluxo:publicacao:idDestinacaoPessoaCienciaPublica: Parâmetro que indica o id da pessoa de ciência pública. Quando configurado e referenciando uma pessoa válida no sistema, habilita a opção Ciência Pública na lista de destinatários.

pje:comunicacao:meios:impedemDocumentoProcesso: Parâmetro que lista meios que impedem a utilização de documentos existentes em processos sigilosos. Caso este parâmetro esteja configurado e o lote tenha ao menos um processo sigiloso, a funcionalidade impedirá a seleção de documento existente para todos os processos.
-->

{{< video src="/videos/intimacao-em-lote.mp4">}}

A intimação só é possível para tipos de documento configurados no parâmetro **pje:tarefas:lote:tiposDocumentoProcessoPermitidos**. Por exemplo: caso o parâmetro esteja configurado com o tipo **Edital** e nem todos os processos selecionados no lote tiver algum documento do tipo **Edital**, o campo **Tipo de documento** não apresenta nenhuma opção.

## Diário Eleitoral

Existe uma diferença entre as configurações do DJE para publicações de matérias eleitorais e a marcação “período especial” no DJE (disponível quando o ato de comunicação é feito no meio DJE.

No DJe existem duas configurações possíveis:

![diario 1](/imagens/diario_1.png)

**a) Ativar Funcionalidade Diário Eleitoral,** que permite que a marcação feita no PJe (período especial) seja válida para o DJe. Essa opção (destacada em azul na imagem acima), faz com que existam dois diários: um eleitoral, que circula direto (sábados, domingos e feriados) e outro comum (só circula nos dias úteis).

Neste caso, no momento da criação do ato no PJe, é preciso usar a opção “período especial” do PJe para separar o que vai para o diário eleitoral:

![diario 2](/imagens/diario_2.png)

Estando ativo o parâmetro e o usuário marcando período especial no PJe, o diário circula no dia seguinte, seja ele feriado, final de semana ou dia útil.

{{% notice warning %}}
Se o parâmetro Ativar Funcionalidade Diário Eleitoral for false e houver marcação no PJe de período especial, essas matérias não serão publicadas!
{{% /notice %}}

**b) Datas de Início e Término do Período Eleitoral,** que, quando marcadas, faz com que todas os diários ordinários sejam publicados no dia seguinte, independentemente de ser final de semana ou feriado. Essa opção (destacada em vermelho na primeira imagem do presente tópico), faz com que tudo o que for publicado siga a regra de circular e publicar em dias uteis e não uteis (ou seja, afeta processos não eleitorais).

{{% notice tip %}}
Estando ativos os dois parâmetros, se o usuário marcar no PJe a opção período especial, vai separar em diários diferentes e, se não marcar, vai ficar tudo junto, mas sempre em dias corridos.
{{% /notice %}}

### Calendário do PJe e reflexo no DJE

No PJe, os feriados/indisponibilidades que afetam os prazos processuais são cadastrados em ferramenta própria disponível pelo menu [**Configuração - Sistema - Tabelas Básicas - Calendário**](/prazos/configuracao_calendario). O DJE aproveita o calendário do PJe. Dessa forma, ocorre uma replicação dos feriados novos cadastrados de 30 em 30 minutos. Cada UF tem o DJE próprio, assim como o TSE. A replicação do calendário ocorre do PJe do TSE para o DJE do TSE e dos PJes das UFs para os DJEs das respectivas UF. Um cadastro realizado no calendário do PJe de primeiro grau afetará a UF relacionada àquele PJe, ou seja, se um feriado for cadastrado como estadual do PJe do primeiro grau da Bahia, as publicações do PJe do segundo grau também serão afetadas.  

Os feriados replicados a cada sincronização são os feriados cujas datas sejam posteriores ao momento da replicação e os feriados recorrentes, ou seja, feriados que se repetem anualmente. 

Um feriado será cadastrado no DJE como nacional, ou seja, afetará todo o envio de matérias daquela instância, caso seja cadastrado no PJe como feriado de abrangência nacional. 

Já um feriado estadual só será replicado se a abrangência do feriado for estadual e a UF vinculada ao feriado for a mesma do PJe. O feriado afetará todos os processos vinculados a jurisdições daquele estado. No caso do PJe do TSE, o DF é considerado o "estado" da instalação. Dessa forma, se for realizado um cadastro no PJe do TSE de feriado de abrangência estadual e a UF selecionada for o DF, o feriado será replicado no Diário do TSE como feriado estadual. 

Já feriados com abrangência de órgão julgador, ou seja, que só afetam aquele órgão julgador, serão replicados para os órgãos julgadores daquele estado.

Os feriados de abrangência municipal só serão replicados quando a UF do feriado for a mesma do PJe responsável pelo cadastro.
        
## Utilização da Central de Mandados

A utilização da central de mandados para fazer comunicação só será possível se o usuário selecionar, ao criar uma comunicação, o meio "Central de Mandados". Caso seja selecionado, o servidor terá que complementar as informações sobre a central de mandados em tarefa posterior que será apresentada ao finalizar a construção do documento a ser utilizado na comunicação. 

Da mesma forma, a tarefa para complementação das informações sobre a central de mandados só será apresentada se o usuário tiver selecionado o meio pertinente. Caso a tarefa seja apresentada e o usuário tenha selecionado o meio erroneamente, recomenda-se seguir o fluxo de complementação das informações da central e, só ao finalizar os procedimentos, fechar o expediente, certificando que a comunicação não precisa ser cumprida, conforme termos comuns da prática cartorária do regional.

{{% notice note %}}
[Clicando aqui](/docs/configuracao_da_central_de_mandados.pdf) você encontra um tutorial com o passo-a-passo para realizar a configuração da Central de Mandados (material cedido pelo TREMG). E, 
[neste link](/docs/perfil_oficial_de_justica.pdf), você encontra um Manual para o uso do perfil de Oficial de Justiça.
{{% /notice %}}

