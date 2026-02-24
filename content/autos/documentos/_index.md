+++
title = "Documentos Processuais"
date = 2022-11-23T17:49:43-03:00
weight = 2
chapter = true
+++

### Autos Digitais

# Documentos Processuais

A aba **Documentos** dos autos digitais exibe uma lista contendo todos os documentos vinculados ao processo. A lista é exibida de forma paginada, onde cada página apresenta 16 documentos. Os campos exibidos são os seguintes:

<!-- realizarDownload: {valueType: realizarDownload, headerType: checkSelecionarDocumentos, properties: {columnRendered: #{processoTrfHome.exibeColunaDeDownloadDeDocumentos()}}}</value>-->
- Id - Identificador do documento [Verifique detalhes a respeito desse campo](/autos/documentos/identificadores).
- Id na origem - Identificado do documento na origem, caso tenha sido incluído na instância atual via remessa
- Número - Número do documento, que vem a ser um identificador negocial do documento [Verifique detalhes a respeito desse campo](/autos/documentos/identificadores).
- Origem - exibe qual o grau de jurisdição onde foi criado o documento
- Juntado em - exibe a data de juntada do documento
- Juntado por - exibe o usuário responsável pela juntada do documento. Via de regra, é quem o assinou. 
- Documento - exibe a descrição atribuída ao documento
- Tipo - exibe o tipo de documento vinculado
- Anexos - a coluna agrega informações por meio de ícones que são exibidos conforme a situação do documento e as permissões do usuário
  - Ícone de folha - o usuário pode clicar e será exibido o conteúdo do documento
  - Ícone de edição - o usuário pode clicar e editar o documento
  - Ícone de cadeado fechado - indica que o documento foi assinado. O usuário pode clicar e verificar os dados da assinatura
  - Ícone de cadeado aberto - indica que o documento não foi assinado. O usuário pode clicar e assinar o documento
  - Ícone de exclusão/inativação - o usuário pode clicar e excluir (documento não juntado) ou inativar (documento juntado)
  - Ícone de histórico de desentranhamento - caso o documento tenha sido inativado e ativado novamente, exibe o histórico
  - Ícone de reativação - caso o documento tenha sido inativado, permite a reativação
  - Ícone de pendente de ciência - indica que o documento não poderá ser visualizado pelo usuário atual, já que está pendente de ciência.
  - Ícone de exibição de lembretes vinculados ao documento
  - Ícone de cadastramento de lembretes vinculados ao documento (disponível para usuário interno e para documentos juntados que não tenham lembrete registrado ainda)
<!-- Certidão -  columnRendered: #{processoTrfHome.exibirColunaCertidao()}-->

A lista é exibida respeitando algumas restrições:
- Os documentos vinculados a expedientes construídos a partir de documentos existentes não serão exibidos, visto que são apenas cópias de documentos já produzidos
- Caso a data de juntada não exista ou não existam assinadores para o documento, ele só será exibido 
  - se o usuário de inclusão for o usuário atual ou
  - se o usuário de inclusão for um assistente de advogado e a localização do assistente for a localização atual ou
  - se o usuário de inclusão for um assistente de procuradoria e a localização do assistente for a localização atual ou
  - se a localização de inclusão do documento seja a localização atual
- Caso a data de juntada exista e existam assinadores para o documento, ele será exibido, exceto de acordo com as seguintes situações:
  - se o documento é sigiloso ou o documento principal a ele vinculado é sigiloso
   - o usuário deve estar cadastrado como visualizador do documento ou deve estar vinculado à procuradoria cadastrada como visualizadora ou
   - se o usuário estiver vinculado ao papel pje:visualizaSigiloso ou pje:manipulaSigiloso, deve estar vinculado ao órgão julgador ou órgão julgador colegiado do processo, conforme for a vinculação do usuário atual a uma localização ou
   - se o usuário de inclusão for o usuário atual ou
   - se o usuário de inclusão for um assistente de advogado e a localização do assistente for a localização atual ou
   - se o usuário de inclusão for um assistente de procuradoria e a localização do assistente for a localização atual ou 

Os documentos são exibidos na ordem descrecente da data de juntada do documento principal. Além disso, como ordenação secundária, também é observada a ordem decrescente dos identificadores dos documentos. Ou seja, caso não exista data de juntada, essa ordenação será a principal. Como terceira regra para ordenação, é observado o campo numeroOrdem do documento. Esse campo fica disponível para o usuário editar na inclusão de anexos, quando é importante que os anexos vinculados a um documento principal sejam lidos seguindo uma sequência determinada.


{{% notice note %}}
As regras da aba **Documentos** não são as mesma regras da linha do tempo dos autos digitais.
{{% /notice %}}

A seguir, algumas informações relacionadas a documentos do processo.

{{% children  %}}
