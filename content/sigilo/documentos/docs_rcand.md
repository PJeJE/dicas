---
title: "Visibilidade em documentos sigilosos em processos RCAND"
date: 2022-11-29T16:31:34-03:00
menuTitle: "Documentos sigilosos em RCAND"
weight: 2
---

É possível atribuir visibilidade automática ao Ministério Público durante a juntada de documentos sigilosos de tipos específicos no PJe, em processos de Registro de Candidatura, por meio da configuração dos seguintes parâmetros:

- **Parâmetro `pje:FiscalDaLei`**:
  - O valor desse parâmetro corresponde ao ID de ente ou autoridade pública (ou fiscal da lei) ativo no PJe.

- **Parâmetro `pje:tipodocumento:acrescentavisualizadores`**:
  - O valor desse parâmetro corresponde à lista IDs dos tipos de documento, separados por vírgula, que serão monitorados (ex: Identidade, Documento de Identificação, RRC).

- **Parâmetro `pje:libera:sigilo:tipoparte`**:
  - O valor desse parâmetro corresponde ao id de um tipo de parte válido no PJe.

{{% notice warning %}}
Essa funcionalidade é aplicável apenas a processos da classe REGISTRO DE CANDIDATURA (11532).
{{% /notice %}}

{{% notice info %}}
Os tipos de documentos devem estar configurados como sigilosos.
{{% /notice %}}

A __configuração inicial__ desses parâmetros foi realizada conforme descrito a seguir:

- **Parâmetro `pje:FiscalDaLei`**:
  - Contém o ID da pessoa 'Fiscal da Lei'.
- **Parâmetro `pje:tipodocumento:acrescentavisualizadores`**:
  - Contém os IDs dos seguintes tipos de documento: RRC, Documento de Identificação e Identidade.
- **Parâmetro `pje:libera:sigilo:tipoparte`**:
  - Contém o ID do tipo de parte REQUERENTE.

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar ativos e devidamente configurados. A configuração inicial foi realizada em todas as regionais da Justiça Eleitoral.
{{% /notice %}}
