---
title: "Certidão de publicação do acórdão em Sessão"
date: 2024-11-07
linkTitle: "Certidão de publicação em Sessão"
weight: 8
---

{{% notice warning %}}
Esta funcionalidade está em fase final de homologação. Portanto, **ainda não disponível nos ambientes de produção**.
{{% /notice %}}

É possível juntar automaticamente, após a publicação do acórdão em Sessão, uma certidão com os dados da publicação, por meio da configuração dos seguintes parâmetros:

- **Parâmetro `idModeloCertidaoPublicacaoAcordaoEmSessao`**:
  - O valor desse parâmetro corresponde ao ID do modelo de documento que será utilizado para a certidão com as informações alteradas pelo usuário no momento da solicitação.

- **Parâmetro `pje:publicacao:acordaoEmSessao:geraCertidao`**:
  - O valor desse parâmetro deve ser `S` para habilitar a utilização da funcionalidade e `N` para desabilitá-la.

{{% notice warning %}}
O ID do modelo de documento informado no parâmetro `idModeloCertidaoPublicacaoAcordaoEmSessao` deve fazer referência a um modelo de documento válido e ativo. Caso contrário, a certidão automática não será juntada ao processo.
{{% /notice %}}

No modelo de documento podem ser utilizadas as seguintes variáveis para recuperação de informações:

{{<table "variaveismodelo">}}

| **Descrição** | **Variável** |
|---|---|
| Assuntos do processo | #{certidaoPublicacaoAcordaoService.processo.assuntoTrfListStr} |
| Classe do processo | #{certidaoPublicacaoAcordaoService.processo.classeJudicial} |
| Data da publicação | #{certidaoPublicacaoAcordaoService.getData()} |
| Estado | #{certidaoPublicacaoAcordaoService.processo.complementoJE.estadoEleicao.estado} |
| Id do documento | #{certidaoPublicacaoAcordaoService.getIdAto()} |
| Município | #{certidaoPublicacaoAcordaoService.processo.complementoJE.municipioEleicao.municipio} |
| Número do processo | #{certidaoPublicacaoAcordaoService.processo.numeroProcesso} |
| Relator do processo | #{certidaoPublicacaoAcordaoService.processo.pessoaRelator != null ? certidaoPublicacaoAcordaoService.processo.pessoaRelator.pessoa.nome : ''} |
| Tipo do documento | #{certidaoPublicacaoAcordaoService.getTipoAto()}  |
| URL para o documento | #{certidaoPublicacaoAcordaoService.getUrlVisualizarDocumento()} |

{{</table>}}

{{% notice note %}}
Cada Regional é responsável por criar o próprio modelo de acordo com suas necessidades. Após a criação, o ID do modelo
deve ser configurado no parâmetro `idModeloCertidaoPublicacaoAcordaoEmSessao`.
{{% /notice %}}

{{% notice note %}}
Para utilizar a variável de URL (`#{certidaoPublicacaoAcordaoService.getUrlVisualizarDocumento()}`), que permite acessar o documento diretamente por meio de um clique, consulte o vídeo explicativo disponível na documentação da [funcionalidade de certidão de publicação no Mural]({{< ref "certidao_mural.md" >}}#video-certidao-mural).
{{% /notice %}}

{{% notice warning %}}
Esse modelo é de uso exclusivo da funcionalidade de certidão automática de publicação do acórdão em Sessão e **NÃO** deve ser selecionado *manualmente* em nenhum editor de texto.
{{% /notice %}}

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar **ativos** e devidamente configurados.
{{% /notice %}}
