---
title: "Certidão de disponibilização no DJe"
date: 2024-11-07
menuTitle: "Certidão do DJe"
weight: 5

---

{{% notice warning %}}
Esta funcionalidade está em fase final de homologação. Portanto, **ainda não disponível nos ambientes de produção**.
{{% /notice %}}


É possível juntar automaticamente, após a disponibilização de expediente no DJe, uma certidão com os dados da disponibilização, por meio da configuração dos seguintes parâmetros:

- **Parâmetro `idModeloCertidaoDisponibilizacao`**:
  - O valor desse parâmetro corresponde ao ID do modelo de documento que será utilizado para a certidão com as informações alteradas pelo usuário no momento da solicitação.
  
- **Parâmetro `pje:disponibilizacao:dje:geraCertidaoDisponibilizacao`**:
  - O valor desse parâmetro deve ser `S` para habilitar a utilização da funcionalidade e `N` para desabilitá-la.

{{% notice warning %}}
O ID do modelo de documento informado no parâmetro `idModeloCertidaoDisponibilizacao` deve fazer referência a um modelo de documento válido e ativo. Caso contrário, a certidão automática não será juntada ao processo.
{{% /notice %}}

No modelo de documento podem ser utilizadas as seguintes variáveis para recuperação de informações:

{{<table "variaveismodelo">}}

| **Descrição** | **Variável** |
|---|---|
| Tipo do documento | #{certidaoDisponibilizacaoDJEService.getTipoAto()}  |
| Id do documento | #{certidaoDisponibilizacaoDJEService.getIdAto()} |
| URL para o documento | #{certidaoDisponibilizacaoDJEService.getUrlVisualizarDocumento()} |
| Data da publicação | #{certidaoDisponibilizacaoDJEService.getDataDisponibilizacao()} |

{{</table>}}

A seguir, um exemplo de modelo de certidão que utiliza as variáveis anteriormente descritas:
{{< video src="/videos/exemplo_modelo_certidao_mural.mp4">}}

{{% notice note %}}
Cada Regional é responsável por criar o próprio modelo de acordo com suas necessidades. Após a criação, o ID do modelo
deve ser configurado no parâmetro `idModeloCertidaoDisponibilizacao`.
{{% /notice %}}

{{% notice warning %}}
Esse modelo é de uso exclusivo da funcionalidade de certidão automática de disponibilização no DJe e **NÃO** deve ser selecionado *manualmente* em nenhum editor de texto.
{{% /notice %}}

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar **ativos** e devidamente configurados.
{{% /notice %}}