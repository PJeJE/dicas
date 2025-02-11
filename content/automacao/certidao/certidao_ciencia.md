
---
title: "Certidão de ciência"
date: 2025-02-07T16:27:02-03:00
menuTitle: "Certidão de ciência"
weight: 6
---

(disponível a partir da versão 2.1.8.1.58)

É possível que o sistema junte automaticamente uma certidão de ciência dos expedientes que torne públicos, entre outras informações, a data e hora de ciência nas intimações feitas, garantindo a transparência dos atos processuais e permitindo a análise da tempestividade com base em fatos disponíveis a todos que atuem ou venham a atuar no feito.

{{% notice note %}}
A certidão deve ser emitida para expedientes enviados via **Sistema**, **Correios**, **Mural**, **Diário**, **Pessoalmente**, **Telefone** e **Central de Mandados**. Todas as ciências serão objeto de emissão de certidão, inclusive as geradas pelo processamento automático do sistema que ocorre durante a madrugada. Não haverá certidão para expedientes com tipo de prazo **Sem prazo** nem para expedientes **Data Certa**. Ao ser gerada a certidão, o sistema vincula o documento ao movimento "Juntada de certidão" (código 581)
{{% /notice %}}

Para expedientes sigilosos, a emissão da certidão será como um documento sigiloso. Da mesma forma, o sistema se comportará se o processo relacionado ao expediente tiver partes sigilosas.

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
Os regionais forem configurado inicialmente para não gerarem a certidão para que o uso inicial seja controlado pelo próprio TRE. (parâmetro **pje:certidao:geraCertidaoCiencia** com o valor **N**)
{{% /notice %}}

## Variáveis do modelo de certidão de ciência

O modelo de documento para a certidão de ciência pode ser alterado conforme necessidades do tribunal utilizando variáveis diversas disponíveis no PJe. 

Algumas variáveis foram utilizadas na inclusão do modelo padrão a ser utilizado na funcionalidade quando ela foi disponibilizada na produção:

+ #{processoParteExpedienteHome.instance.processoExpediente.tipoProcessoDocumento}
  ++ Exibe o tipo de expediente. Exemplo: Intimação, Edital, Citação
+ #{processoParteExpedienteHome.instance.processoExpediente.meioExpedicaoExpediente == 'E' ? 'Expedição eletrônica' : processoParteExpedienteHome.instance.processoExpediente.meioExpedicaoExpediente.label}
  ++ Exibe o meio de expedição. Exemplo: Correios, Mural, Expedição eletrônica
+ #{dateUtil.dateToString(processoParteExpedienteHome.instance.processoExpediente.dtCriacao, 'dd/MM/yyyy HH:mm:ss')}
  ++ Exibe a data de expedição da intimação no formato **dd/MM/yyyy HH:mm:ss**
+ #{processoParteExpedienteHome.instance.nomePessoaParte}
  ++ Exibe o nome do intimado  
+ #{processoParteExpedienteHome.instance.cienciaSistema != null and processoParteExpedienteHome.instance.cienciaSistema ? 'pelo sistema' : ''} #{processoParteExpedienteHome.instance.cienciaSistema != null && processoParteExpedienteHome.instance.cienciaSistema ? '' : 'por'} #{processoParteExpedienteHome.instance.cienciaSistema != null && processoParteExpedienteHome.instance.cienciaSistema ? '' : processoParteExpedienteHome.instance.nomePessoaCiencia}
  ++ Exibe quem foi o responsável pela ciência. Caso a ciência tenha sido registrada pelo sistema, será exibido **pelo sistema**.
+ #{dateUtil.dateToString(processoParteExpedienteHome.instance.dtCienciaParte, 'dd/MM/yyyy HH:mm:ss')}
  ++ Exibe a data da ciência no formato **dd/MM/yyyy HH:mm:ss**
  
As variáveis utilizadas no modelo de documento que iniciam com o termo processoParteExpedienteHome, se utilizadas em outros contextos que não o da emissão da certidão da atual pendência, em geral, não terão o funcionamento correto, já que dependem que um expediente específico esteja carregado no contexto do PJe no momento do uso.

## Orientações de configuração para o usuário administrador

A emissão da certidão está condicionada à configuração do parãmetro "pje:certidao:geraCertidaoCiencia" com o valor "S". Além disso, deve estar corretamente configurado o identificador do modelo a ser utilizado na emissão por meio do registro de seu identificador no parâmetro "idModeloCertidaoCiencia". Caso o identificador não corresponda a um modelo ativo no PJe, o sistema notificará o erro na emissão por meio do fluxo cujo código esteja registrado no parâmetro "pje:fluxo:erro:certidaoCiencia" e isso só ocorrerá se o código corresponder a um fluxo válido. O nome do documento gerado pode seguir um padrão de acordo com configurações. Caso as configurações não sejam realizadas, o nome adotado será o nome do tipo de documento. Caso o parâmetro "nomeDocumentoCertidaoCiencia" tenha sido configurado e tenha alguma valor que não vazio, o sistema utilizará esse nome para atribuir ao nome do documento. Caso esse parâmetro seja corretamento configurado, o usuário administrador pode também optar por adicionar ao nome do documento o nome da parte intimada a cuja ciência está vinculada a certidão por meio da marcação "S" do parâmetro "pje:certidao:ciencia:concatenaParte".
 

