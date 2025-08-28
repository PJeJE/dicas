---
title: "Certidão de decurso"
date: 2025-08-20T14:12:02-03:00
menuTitle: "Certidão de decurso"
weight: 7
---

(disponível a partir da versão 2.1.8.1.68)

O sistema pode juntar automaticamente uma certidão de decurso de prazo dos expedientes que torna públicas informações como data e hora do decurso das intimações realizadas, facilitando a identificação dessa situação. Isso garante a transparência dos atos processuais e permite a análise da tempestividade com base em fatos disponíveis a todos que atuem no processo.

{{% notice note %}}
**Sigilo:** Para expedientes sigilosos ou enviados para partes sigilosas, a certidão será automaticamente marcada como sigilosa.
{{% /notice %}}

## Modelo utilizado para emissão da certidão de decurso

A certidão utiliza um modelo de documento configurado conforme as necessidades do tribunal. Para facilitar o uso inicial, o sistema já possui um modelo pré-configurado.

{{% notice warning %}}
O modelo pré-configurado é exclusivo para uso automático da certidão de decurso e não deve ser selecionado manualmente em editores de texto.
{{% /notice %}}

Para tribunais de primeiro grau, recomenda-se não criar novos modelos nem alterar o nome do modelo pré-configurado. Alterações devem ser feitas diretamente no modelo existente "Modelo de certidão automática de decurso" para facilitar o suporte da Assessoria do PJe.

{{% notice warning %}}
A alteração do modelo, caso seja necessária, precisará de auxílio da Assessoria do PJe, mas a recomendação é que o modelo seja utilizado do jeito que foi configurado inicialmente, evitando erros na sua apresentação e na tradução de variáveis.
{{% /notice %}}

### Exemplo de certidão gerada

O modelo pré-configurado gera uma certidão com conteúdo similar ao exemplo abaixo:

```
JUSTIÇA ELEITORAL

LISTA TRÍPLICE (11545) - 9999999-99.9999.9.99.9999 - JOAO PESSOA - PARAIBA
ADVOGADO(A) INDICADO(A): FATIMA FATIMA, MARIA MARIA, JOSE JOSE
INTERESSADO: TRIBUNAL REGIONAL ELEITORAL DA PARAIBA
 
DECURSO DA INTIMAÇÃO

Essa certidão registra o decurso de prazo para o expediente do tipo Notificação expedido via Pessoalmente na data 05/02/2025 para TRIBUNAL REGIONAL ELEITORAL DA PARAÍBA.

5 de fevereiro de 2025
```

### Configuração inicial

Por padrão, os tribunais regionais foram configurados com o parâmetro `pje:certidao:geraCertidaoDecurso` definido como `N` para que o uso inicial seja controlado pelo próprio TRE/TSE.

### Informações técnicas do modelo

O modelo pré-configurado possui as seguintes características:
- **Nome**: "Modelo de certidão automática de decurso"
- **Tipo**: Certidões (código 534)
- **Localização**: Raiz do tribunal (ID 1)

{{% notice warning %}}
Tenha cuidado ao alterar o modelo, pois a geração é automática e erros de tradução de variáveis não poderão ser verificados antes da juntada da certidão ao processo.
{{% /notice %}}

### Restrições importantes para variáveis

Variáveis que iniciam com `processoJudicialAction` não funcionam no processamento automático de decurso (executado durante a madrugada). 

Use esta variável **correta**:
```
#{processoJudicialManager.recuperarParteFormatada(processoTrfHome.instance, false,true,false,'A','P','T')}
```

Em vez desta **incorreta**:
```
#{processoJudicialAction.recuperarParteFormatada(true, true, 'A', 'P', 'T')}
```


## Variáveis do modelo de certidão de decurso

No modelo de documento podem ser utilizadas as seguintes variáveis para recuperação de informações:

{{<table "variaveismodelo">}}

| **Descrição** | **Variável** |
|---|---|
| Tipo de expediente (Exemplo: Intimação, Edital, Citação) | #{processoParteExpedienteHome.instance.processoExpediente.tipoProcessoDocumento} |
| Nome do intimado | #{processoParteExpedienteHome.instance.nomePessoaParte} |
| Meio de expedição (Exemplo: Correios, Mural, Expedição eletrônica) | #{processoParteExpedienteHome.instance.processoExpediente.meioExpedicaoExpediente == 'E' ? 'Expedição eletrônica' : processoParteExpedienteHome.instance.processoExpediente.meioExpedicaoExpediente.label}

{{</table>}}
  
{{% notice warning %}}
As variáveis com `processoParteExpedienteHome` são exclusivas para a certidão automática de decurso. O modelo não deve ser usado manualmente para outros documentos.
{{% /notice %}}

## Configuração de parâmetros

Configure os seguintes parâmetros para habilitar e personalizar a certidão de decurso:

- **Parâmetro `pje:certidao:geraCertidaoDecurso`**:
  - O valor desse parâmetro deve ser `S` para habilitar a utilização da funcionalidade e `N` para desabilitá-la.

- **Parâmetro `idModeloCertidaoDecurso`**:
  - O valor desse parâmetro corresponde ao ID do modelo de documento que será utilizado para a certidão com as informações alteradas pelo usuário no momento da solicitação.

- **Parâmetro `pje:fluxo:erro:certidaoDecurso`**:
  - O valor desse parâmetro corresponde ao código do fluxo para notificação de erros na emissão da certidão.

- **Parâmetro `nomeDocumentoCertidaoDecurso`**:
  - O valor desse parâmetro define o nome padrão do documento da certidão. Se não configurado, será usado o nome do tipo de documento.

- **Parâmetro `pje:certidao:decurso:concatenaParte`**:
  - O valor desse parâmetro deve ser `S` para adicionar o nome da parte intimada ao nome do documento da certidão.

{{% notice warning %}}
O ID do modelo de documento informado no parâmetro `idModeloCertidaoDecurso` deve fazer referência a um modelo de documento válido e ativo. Caso contrário, a certidão automática não será juntada ao processo.
{{% /notice %}}

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar **ativos** e devidamente configurados.
{{% /notice %}}
