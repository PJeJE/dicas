---
title: "Certidão de publicação no DJe"
date: 2024-11-07
menuTitle: "Certidão de publicação do DJe"
weight: 5
---

{{% notice warning %}}
Esta funcionalidade está em fase final de homologação. Portanto, **ainda não disponível nos ambientes de produção**.
{{% /notice %}}

É possível juntar automaticamente, após a publicação de expediente no DJe, uma certidão com os dados da publicação, por meio da configuração dos seguintes parâmetros:

- **Parâmetro `idModeloCertidaoPublicacaoDJE`**:
  - O valor desse parâmetro corresponde ao ID do modelo de documento que será utilizado para a certidão com as informações alteradas pelo usuário no momento da solicitação.

- **Parâmetro `pje:publicacao:dje:geraCertidao`**:
  - O valor desse parâmetro deve ser `S` para habilitar a utilização da funcionalidade e `N` para desabilitá-la.

{{% notice warning %}}
O ID do modelo de documento informado no parâmetro `idModeloCertidaoPublicacaoDJE` deve fazer referência a um modelo de documento válido e ativo. Caso contrário, a certidão automática não será juntada ao processo.
{{% /notice %}}

No modelo de documento podem ser utilizadas as seguintes variáveis para recuperação de informações:

{{<table "variaveismodelo">}}

| **Descrição** | **Variável** |
|---|---|
| Assuntos do processo | #{certidaoPublicacaoDJEService.processo.assuntoTrfListStr} |
| Classe do processo | #{certidaoPublicacaoDJEService.processo.classeJudicial} |
| Data da publicação | #{certidaoPublicacaoDJEService.getData()} |
| Estado | #{certidaoPublicacaoDJEService.processo.complementoJE.estadoEleicao.estado} |
| Id do documento | #{certidaoPublicacaoDJEService.getIdAto()} |
| Município | #{certidaoPublicacaoDJEService.processo.complementoJE.municipioEleicao.municipio} |
| Número do processo | #{certidaoPublicacaoDJEService.processo.numeroProcesso} |
| Relator do processo | #{certidaoPublicacaoDJEService.processo.pessoaRelator != null ? certidaoPublicacaoDJEService.processo.pessoaRelator.pessoa.nome : ''} |
| Tipo do documento | #{certidaoPublicacaoDJEService.getTipoAto()}  |
| URL para o documento | #{certidaoPublicacaoDJEService.getUrlVisualizarDocumento()} |

{{</table>}}

{{% notice note %}}
Cada Regional é responsável por criar o próprio modelo de acordo com suas necessidades. Após a criação, o ID do modelo
deve ser configurado no parâmetro `idModeloCertidaoPublicacaoDJE`.
{{% /notice %}}

{{% notice warning %}}
Esse modelo é de uso exclusivo da funcionalidade de certidão automática de publicação no DJe e **NÃO** deve ser selecionado *manualmente* em nenhum editor de texto.
{{% /notice %}}

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar **ativos** e devidamente configurados.
{{% /notice %}}
