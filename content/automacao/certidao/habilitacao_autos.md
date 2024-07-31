---
title: "Certidão de habilitação nos autos"
date: 2024-07-18T16:34:02-03:00
weight: 2
---

É possível juntar automaticamente, após o pedido de habilitação nos autos, uma certidão que informa quais foram as informações alteradas pelo representante processual, por meio da configuração dos seguintes parâmetros:

- **Parâmetro `pje:habilitacao:certidaoSistema:juntarCertidao`**:
  - O valor desse parâmetro deve ser `true` para habilitar a utilização da funcionalidade e `false` para desabilitá-la.

- **Parâmetro `pje:habilitacao:certidaoSistema:modelo:id`**:
  - O valor desse parâmetro corresponde ao ID do modelo de documento que será utilizado para a certidão com as informações alteradas pelo usuário no momento da solicitação.

No modelo de documento podem ser utilizadas as seguintes variáveis para recuperação de informações:

{{<table "variaveismodelo">}}

| **Descrição** | **Variável** |
|---|---|
| Solicitante | #{habilitacaoAutosManager.getSolicitanteUltimaHabilitacao(processoTrfHome.instance)} |
| Partes | #{habilitacaoAutosManager.getPartesUltimaHabilitacao(processoTrfHome.instance)} |
| Inclusão do(a) advogado(a) | #{habilitacaoAutosManager.getUltimaInclusao(processoTrfHome.instance)} |
| Exclusão do(a) advogado(a) | #{habilitacaoAutosManager.getUltimaSubstituicao(processoTrfHome.instance)} |

{{</table>}}

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar ativos e devidamente configurados.
{{% /notice %}}