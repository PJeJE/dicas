+++
title = "Documentos Processuais"
date = 2022-11-23T17:49:43-03:00
weight = 1
chapter = true
+++

### Autos Digitais

# Documentos Processuais

A aba **Documentos** exibe uma lista contendo todos os documentos vinculados ao processo. A lista é exibida de forma paginada, onde cada página apresenta 16 documentos. Os campos exibidos são os seguintes:

- realizarDownload: {valueType: realizarDownload, headerType: checkSelecionarDocumentos, properties: {columnRendered: #{processoTrfHome.exibeColunaDeDownloadDeDocumentos()}}}</value>
			<value>idProcessoDocumento: {valueType: idProcessoDocumento, properties: {header: 'Id'}}</value>
			<value>idInstanciaOrigem: {properties: {header: 'Id na origem'}}</value>
			<value>numeroDocumento: {properties: {header: 'Número'}}</value>
			<value>instancia: {valueType: instancia, properties: {header: 'Origem'}}</value>
			<value>dataJuntada: { valueType: dataJuntada, properties : {header: 'Juntado em'} }</value>
			<value>usuarioInclusao: { valueType: usuarioInclusao, properties : {header: 'Juntado por'} }</value>
			<value>processoDocumento: {valueType:identificarSigilo, properties: {escape:true, header: 'Documento'}}</value>
			<value>tipoProcessoDocumento: {valueType:identificarSigilo, properties: {header: 'Tipo'}}</value>
			<value>processoDocumentoBin: {valueType: processoDocumentoBin, properties: {order: extensao, header: 'Anexos', styleClassForm: 'alinhamentoBotoesDocumento'}}</value>
			<value>motivoExclusao: {valueType: processoDocumentoRecibo, properties: {header: 'Certidão', columnRendered: #{processoTrfHome.exibirColunaCertidao()}}}</value>

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
   - se o usuário estiver vinculado ao papel visualizasigiloso ou manipulasigiloso, deve estar vinculado ao órgão julgador ou órgão julgador colegiado do processo, conforme for a vinculação do usuário atual a uma localização ou
   - se o usuário de inclusão for o usuário atual ou
   - se o usuário de inclusão for um assistente de advogado e a localização do assistente for a localização atual ou
   - se o usuário de inclusão for um assistente de procuradoria e a localização do assistente for a localização atual ou 

Os documentos são exibidos na ordem descrecente da data de juntada do documento principal. Além disso, como ordenação secundária, também é observada a ordem decrescente dos identificadores dos documentos. Ou seja, caso não existe data de juntada, essa ordenação será a principal. Como terceira regra para ordenação, é observado o campo numeroOrdem do documento. Esse campo fica disponível para o usuário editar na inclusão de anexos, quando é importante que os anexos vinculados a um documento principal sejam lidos seguindo uma sequência determinada.

As regras da aba **Documentos** não são as mesma regras da linha do tempo dos autos digitais.

A seguir, algumas informações relacionadas a documentos do processo.

{{% children  %}}
