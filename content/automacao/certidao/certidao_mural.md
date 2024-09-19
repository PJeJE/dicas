---
title: "Certidão de publicação no Mural"
date: 2024-07-18T16:34:02-03:00
menuTitle: "Certidão do mural"
weight: 4
---


É possível juntar automaticamente, após a publicação de expediente no Mural, uma certidão com os dados da publicação, por meio da configuração dos seguintes parâmetros:

- **Parâmetro `pje:publicacao:mural:geraCertidaoPublicacao`**:
  - O valor desse parâmetro deve ser `S` para habilitar a utilização da funcionalidade e `N` para desabilitá-la.

- **Parâmetro `idModeloCertidaoPublicacaoMural`**:
  - O valor desse parâmetro corresponde ao ID do modelo de documento que será utilizado para a certidão com as informações alteradas pelo usuário no momento da solicitação.

{{% notice warning %}}
O ID do modelo de documento informado no parâmetro `idModeloCertidaoPublicacaoMural` deve fazer referência a um modelo de documento válido e ativo. Caso contrário, a certidão automática não será juntada ao processo.
{{% /notice %}}

No modelo de documento podem ser utilizadas as seguintes variáveis para recuperação de informações:

{{<table "variaveismodelo">}}

| **Descrição** | **Variável** |
|---|---|
| Tipo do documento | #{certidaoPublicacaoMuralService.getTipoAto()}  |
| Id do documento | #{certidaoPublicacaoMuralService.getIdAto()} |
| URL para o documento | #{certidaoPublicacaoMuralService.getUrlVisualizarDocumento()} |
| Data da publicação | #{certidaoPublicacaoMuralService.getDataPublicacao()} |

{{</table>}}

<!-- A seguir, um exemplo de modelo de certidão que utiliza as variáveis anteriormente descritas:
{{< video src="/videos/exemplo_modelo_certidao_mural.mp4">}} -->

{{% notice note %}}
Cada Regional é responsável por criar o próprio modelo de acordo com suas necessidades. Após a criação, o ID do modelo
deve ser configurado no parâmetro `idModeloCertidaoPublicacaoMural`.
{{% /notice %}}

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar ativos e devidamente configurados.
{{% /notice %}}