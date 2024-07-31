---
title: "Atribuição automática de visibilidade em documentos em RCAND"
date: 2022-11-29T16:31:34-03:00
menuTitle: "Visualização de documentos em RCAND"
weight: 4
---

É possível atribuir visibilidade automática ao Ministério Público durante a juntada de documentos sigilosos de tipos específicos no PJe, em processos de Registro de Candidatura, por meio da configuração dos seguintes parâmetros:

- **Parâmetro `pje:FiscalDaLei`**:
  - Cadastre ou verifique a existência do parâmetro.
  - Certifique-se de que o valor desse parâmetro corresponde ao ID de uma pessoa válida no PJe.

- **Parâmetro `pje:tipodocumento:acrescentavisualizadores`**:
  - Cadastre ou atualize este parâmetro com os IDs dos tipos de documento que deverão ser monitorados (ex: Identidade, Documento de Identificação, RRC).

- **Parâmetro `pje:libera:sigilo:tipoparte`**:
  - Cadastre ou verifique o parâmetro, garantindo que ele contenha o ID correspondente a um tipo de parte válido no PJe, como REQUERENTE.

{{% notice warning %}}
Essa funcionalidade é aplicável apenas a processos da classe REGISTRO DE CANDIDATURA (11532).
{{% /notice %}}

{{% notice info %}}
Os tipos de documentos devem estar configurados como sigilosos.
{{% /notice %}}

A __configuração inicial__ desses parâmetros deve ser a seguinte:

- **Parâmetro `pje:FiscalDaLei`**:
  - Contém o ID da pessoa 'Fiscal da Lei'.
- **Parâmetro `pje:tipodocumento:acrescentavisualizadores`**:
  - Contém os IDs dos seguintes tipos de documento: RRC, Documento de Identificação e Identidade.
- **Parâmetro `pje:libera:sigilo:tipoparte`**:
  - Contém o ID do tipo de parte REQUERENTE.

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar ativos e devidamente configurados.
{{% /notice %}}
