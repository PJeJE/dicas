
---
title: "Certidão de ciência"
date: 2025-02-07T16:27:02-03:00
menuTitle: "Certidão de ciência"
weight: 6
---

(disponível a partir da versão 2.1.8.1.59)

É possível que o sistema junte automaticamente uma certidão de ciência dos expedientes que torne públicos, entre outras informações, a data e hora de ciência nas intimações feitas, garantindo a transparência dos atos processuais e permitindo a análise da tempestividade com base em fatos disponíveis a todos que atuem ou venham a atuar no feito.

{{% notice note %}}
A certidão deve ser emitida para expedientes enviados para meios conforme parâmetro **pje:certidao:ciencia:meios**. Esse parâmetro virá configurado previamente com o valor **E**, que remete ao meio **Sistema**. Caso seja necessário, o usuário administrador pode configurar e emissão de certidão para outros meios, acrescentando a letra referente ao meio no parâmetro, separado por vírgula. Os meios possíveis são: E(**Sistema**), P(**Diário Eletrônico**),  C(**Correios**), M(**Central de Mandados**), T(**Telefone**), S(**Pessoalmente**), A(**Sessão**), R(**Mural**), G(**Correios**). 
{{% /notice %}}

{{% notice note %}}
Não haverá certidão para expedientes cujos tipos de prazo tenham sido configurados no parâmetro “pje:certidao:ciencia:excecao:tiposPrazo”, o qual virá configurado inicialmente com o valor **S**, **C**, ou seja, expedientes com tipo de prazo **Sem prazo** e **Data Certa** não terão certidão gerada. Isso porque a configuração desse tipo de parâmetro deve ser realizada com letras separadas por vírgula, letras essas que remetem aos seguintes tipos de prazo: A(“anos”), M(“meses”), D(“dias”), H(“horas”), N(“minutos”), C(“data certa”), S(“sem prazo”). 
{{% /notice %}}

Para expedientes sigilosos, a emissão da certidão será como um documento sigiloso. Da mesma forma, o sistema se comportará se o expediente for enviado para uma parte sigilosa.

## Modelo utilizado para emissão da certidão de ciência

A certidão emitida utilizará o modelo configurado de acordo com as necessidades do usuário administrador. Para facilitar a utilização inicial da funcionalidade, foi inserido um modelo previamente configurado que emitirá uma certidão com o conteúdo similar ao descrito abaixo:

TRIBUNAL SUPERIOR ELEITORAL
SECRETARIA JUDICIÁRIA 

LISTA TRÍPLICE (11545) - 9999999-99.9999.9.99.9999 - JOAO PESSOA - PARAIBA
RELATOR(A): MINISTRO(A) ANA ANA
ADVOGADO(A) INDICADO(A): FATIMA FATIMA, MARIA MARIA, JOSE JOSE
INTERESSADO: TRIBUNAL REGIONAL ELEITORAL DA PARAIBA
 
CIÊNCIA DA INTIMAÇÃO

Essa certidão registra que foi dada ciência no expediente do tipo Notificação expedido via Pessoalmente na data 05/02/2025 18:28:13 a(o) TRIBUNAL REGIONAL ELEITORAL DA PARAIBA. A ciência foi registrada pelo sistema em 05/02/2025 18:29:00.

Brasília, 5 de fevereiro de 2025.

{{% notice note %}}
Os regionais foram configurados inicialmente para não gerarem a certidão para que o uso inicial seja controlado pelo próprio TRE/TSE. (parâmetro **pje:certidao:geraCertidaoCiencia** inicialmente configurado com o valor **N**)
{{% /notice %}}

{{% notice note %}}
As informações a seguir são importantes para que o regional tenha acesso ao modelo de documento configurado inicialmente, caso queira consultá-lo/modificá-lo: o modelo de documento criado tem o nome **Modelo de certidão automática de ciência** e foi vinculado ao tipo de modelo de documento de nome **Certidões**, ao tipo de documento de código **534** e vinculado à localização de identificador **1** - localização raiz do tribunal (Tribunal Superior Eleitoral ou Tribunal Regional Eleitoral ou Tribunal). Caso haja necessidade que usuários vinculados a outras localizações alterem o modelo, a vinculação à localização deve ser alterada por um usuário que esteja vinculado à localização. **É importante ter cuidado na alteração para que não sejam utilizadas variáveis que não possam ser traduzidas no ato da emissão, já que ela ocorrerá de forma automática e o usuário não poderá verificar erros de tradução antes da efetiva juntada da certidão**.
{{% /notice %}}

## Variáveis do modelo de certidão de ciência

O modelo de documento para a certidão de ciência pode ser alterado conforme necessidades do tribunal utilizando variáveis diversas disponíveis no PJe. 

Algumas variáveis foram utilizadas na inclusão do modelo padrão a ser utilizado na funcionalidade quando ela foi disponibilizada na produção:

- **#{processoParteExpedienteHome.instance.processoExpediente.tipoProcessoDocumento}**
  - Exibe o tipo de expediente. Exemplo: Intimação, Edital, Citação
- **#{processoParteExpedienteHome.instance.processoExpediente.meioExpedicaoExpediente == 'E' ? 'Expedição eletrônica' : processoParteExpedienteHome.instance.processoExpediente.meioExpedicaoExpediente.label}**
  - Exibe o meio de expedição. Exemplo: Correios, Mural, Expedição eletrônica
- **#{dateUtil.dateToString(processoParteExpedienteHome.instance.processoExpediente.dtCriacao, 'dd/MM/yyyy HH:mm:ss')}**
  - Exibe a data de expedição da intimação no formato **dd/MM/yyyy HH:mm:ss**
- **#{processoParteExpedienteHome.instance.nomePessoaParte}**
  - Exibe o nome do intimado
- **#{processoParteExpedienteHome.instance.cienciaSistema != null and processoParteExpedienteHome.instance.cienciaSistema ? 'pelo sistema' : ''} #{processoParteExpedienteHome.instance.cienciaSistema != null && processoParteExpedienteHome.instance.cienciaSistema ? '' : 'por'} #{processoParteExpedienteHome.instance.cienciaSistema != null && processoParteExpedienteHome.instance.cienciaSistema ? '' : processoParteExpedienteHome.instance.nomePessoaCiencia}**
  - Exibe quem foi o responsável pela ciência. Caso a ciência tenha sido registrada pelo sistema, será exibido **pelo sistema**
- **#{dateUtil.dateToString(processoParteExpedienteHome.instance.dtCienciaParte, 'dd/MM/yyyy HH:mm:ss')}**
  - Exibe a data da ciência no formato **dd/MM/yyyy HH:mm:ss**
  
As variáveis utilizadas no modelo de documento que iniciam com o termo processoParteExpedienteHome, se utilizadas em outros contextos que não o da emissão da certidão da atual pendência, vão apresentar erros. Sendo assim, o modelo não deve ser utilizado na construção de documentos pelo usuário. 

## Orientações de configuração para o usuário administrador

A emissão da certidão está condicionada à configuração do parãmetro "pje:certidao:geraCertidaoCiencia" com o valor "S". Além disso, deve estar corretamente configurado o identificador do modelo a ser utilizado na emissão por meio do registro de seu identificador no parâmetro "idModeloCertidaoCiencia". Caso o identificador não corresponda a um modelo ativo no PJe, o sistema notificará o erro na emissão por meio do fluxo cujo código esteja registrado no parâmetro "pje:fluxo:erro:certidaoCiencia" e isso só ocorrerá se o código corresponder a um fluxo válido. O nome do documento gerado pode seguir um padrão de acordo com configurações. Caso as configurações não sejam realizadas, o nome adotado será o nome do tipo de documento. Caso o parâmetro "nomeDocumentoCertidaoCiencia" tenha sido configurado e tenha alguma valor que não vazio, o sistema utilizará esse nome para atribuir ao nome do documento. Caso esse parâmetro seja corretamento configurado, o usuário administrador pode também optar por adicionar ao nome do documento o nome da parte intimada a cuja ciência está vinculada a certidão por meio da marcação "S" do parâmetro "pje:certidao:ciencia:concatenaParte".
 

