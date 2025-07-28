---
title: "Certidão de ciência"
date: 2025-02-07T16:27:02-03:00
menuTitle: "Certidão de ciência"
weight: 6
---

(disponível a partir da versão 2.1.8.1.59)

O sistema pode juntar automaticamente uma certidão de ciência dos expedientes que torna públicas informações como data e hora de ciência das intimações realizadas. Isso garante a transparência dos atos processuais e permite a análise da tempestividade com base em fatos disponíveis a todos que atuem no processo.

{{% notice info %}}
**Importante:** A certidão é gerada automaticamente apenas para **meios de expedição** configurados no parâmetro `pje:certidao:ciencia:meios` (padrão: `E` - Sistema) e **expedientes que NÃO tenham** tipos de prazo configurados no parâmetro `pje:certidao:ciencia:excecao:tiposPrazo` (padrão: `S,C` - Sem prazo e Data Certa). Veja todos os valores possíveis na seção [Configuração de parâmetros](#configuração-de-parâmetros).
{{% /notice %}}

{{% notice note %}}
**Sigilo:** Para expedientes sigilosos ou enviados para partes sigilosas, a certidão será automaticamente marcada como sigilosa.
{{% /notice %}}

## Modelo utilizado para emissão da certidão de ciência

A certidão utiliza um modelo de documento configurado conforme as necessidades do tribunal. Para facilitar o uso inicial, o sistema já possui um modelo pré-configurado.

{{% notice warning %}}
O modelo pré-configurado é exclusivo para uso automático da certidão de ciência e não deve ser selecionado manualmente em editores de texto.
{{% /notice %}}

Para tribunais de primeiro grau, recomenda-se não criar novos modelos nem alterar o nome do modelo pré-configurado. Alterações devem ser feitas diretamente no modelo existente "Modelo de certidão automática de ciência" para facilitar o suporte da Assessoria do PJe.

### Exemplo de certidão gerada

O modelo pré-configurado gera uma certidão com conteúdo similar ao exemplo abaixo:

```
TRIBUNAL SUPERIOR ELEITORAL
SECRETARIA JUDICIÁRIA 

LISTA TRÍPLICE (11545) - 9999999-99.9999.9.99.9999 - JOAO PESSOA - PARAIBA
RELATOR(A): MINISTRO(A) ANA ANA
ADVOGADO(A) INDICADO(A): FATIMA FATIMA, MARIA MARIA, JOSE JOSE
INTERESSADO: TRIBUNAL REGIONAL ELEITORAL DA PARAIBA
 
CIÊNCIA DA INTIMAÇÃO

Esta certidão registra que foi dada ciência no expediente do tipo Notificação 
expedido via Pessoalmente na data 05/02/2025 18:28:13 ao TRIBUNAL REGIONAL 
ELEITORAL DA PARAÍBA. A ciência foi registrada pelo sistema em 05/02/2025 18:29:00.

Brasília, 5 de fevereiro de 2025.
```

### Configuração inicial

Por padrão, os tribunais regionais foram configurados com o parâmetro `pje:certidao:geraCertidaoCiencia` definido como `N` para que o uso inicial seja controlado pelo próprio TRE/TSE.

### Informações técnicas do modelo

O modelo pré-configurado possui as seguintes características:
- **Nome**: "Modelo de certidão automática de ciência"
- **Tipo**: Certidões (código 534)
- **Localização**: Raiz do tribunal (ID 1)

{{% notice warning %}}
Tenha cuidado ao alterar o modelo, pois a geração é automática e erros de tradução de variáveis não poderão ser verificados antes da juntada da certidão ao processo.
{{% /notice %}}

### Restrições importantes para variáveis

Variáveis que iniciam com `processoJudicialAction` não funcionam no processamento automático de ciência (executado durante a madrugada). 

Use esta variável **correta**:
```
#{processoJudicialManager.recuperarParteFormatada(processoTrfHome.instance, false,true,false,'A','P','T')}
```

Em vez desta **incorreta**:
```
#{processoJudicialAction.recuperarParteFormatada(true, true, 'A', 'P', 'T')}
```


## Variáveis do modelo de certidão de ciência

No modelo de documento podem ser utilizadas as seguintes variáveis para recuperação de informações:

{{<table "variaveismodelo">}}

| **Descrição** | **Variável** |
|---|---|
| Data da ciência no formato dd/MM/yyyy HH:mm:ss | #{dateUtil.dateToString(processoParteExpedienteHome.instance.dtCienciaParte, 'dd/MM/yyyy HH:mm:ss')} |
| Data de expedição da intimação no formato dd/MM/yyyy HH:mm:ss | #{dateUtil.dateToString(processoParteExpedienteHome.instance.processoExpediente.dtCriacao, 'dd/MM/yyyy HH:mm:ss')} |
| Meio de expedição (Exemplo: Correios, Mural, Expedição eletrônica) | #{processoParteExpedienteHome.instance.processoExpediente.meioExpedicaoExpediente == 'E' ? 'Expedição eletrônica' : processoParteExpedienteHome.instance.processoExpediente.meioExpedicaoExpediente.label} |
| Nome do intimado | #{processoParteExpedienteHome.instance.nomePessoaParte} |
| Responsável pela ciência (sistema ou pessoa) | #{processoParteExpedienteHome.instance.cienciaSistema != null and processoParteExpedienteHome.instance.cienciaSistema ? 'pelo sistema' : ''} #{processoParteExpedienteHome.instance.cienciaSistema != null && processoParteExpedienteHome.instance.cienciaSistema ? '' : 'por'} #{processoParteExpedienteHome.instance.cienciaSistema != null && processoParteExpedienteHome.instance.cienciaSistema ? '' : processoParteExpedienteHome.instance.nomePessoaCiencia} |
| Tipo de expediente (Exemplo: Intimação, Edital, Citação) | #{processoParteExpedienteHome.instance.processoExpediente.tipoProcessoDocumento} |

{{</table>}}
  
{{% notice warning %}}
As variáveis com `processoParteExpedienteHome` são exclusivas para a certidão automática de ciência. O modelo não deve ser usado manualmente para outros documentos.
{{% /notice %}}

## Configuração de parâmetros

Configure os seguintes parâmetros para habilitar e personalizar a certidão de ciência:

- **Parâmetro `pje:certidao:geraCertidaoCiencia`**:
  - O valor desse parâmetro deve ser `S` para habilitar a utilização da funcionalidade e `N` para desabilitá-la.

- **Parâmetro `pje:certidao:ciencia:meios`**:
  - O valor desse parâmetro define os meios de expedição para os quais a certidão será emitida. Configurado inicialmente com o valor `E` (Sistema). Os meios possíveis são: `E` (Sistema), `P` (Diário Eletrônico), `C` (Correios), `M` (Central de Mandados), `T` (Telefone), `S` (Pessoalmente), `A` (Sessão), `R` (Mural), `G` (Correios). Para múltiplos valores, separe por vírgula.

- **Parâmetro `pje:certidao:ciencia:excecao:tiposPrazo`**:
  - O valor desse parâmetro define os tipos de prazo para os quais NÃO será gerada certidão. Configurado inicialmente com `S`, `C` (Sem prazo e Data Certa). Os tipos possíveis são: `A` (anos), `M` (meses), `D` (dias), `H` (horas), `N` (minutos), `C` (data certa), `S` (sem prazo). Para múltiplos valores, separe por vírgula.

- **Parâmetro `idModeloCertidaoCiencia`**:
  - O valor desse parâmetro corresponde ao ID do modelo de documento que será utilizado para a certidão com as informações alteradas pelo usuário no momento da solicitação.

- **Parâmetro `pje:fluxo:erro:certidaoCiencia`**:
  - O valor desse parâmetro corresponde ao código do fluxo para notificação de erros na emissão da certidão.

- **Parâmetro `nomeDocumentoCertidaoCiencia`**:
  - O valor desse parâmetro define o nome padrão do documento da certidão. Se não configurado, será usado o nome do tipo de documento.

- **Parâmetro `pje:certidao:ciencia:concatenaParte`**:
  - O valor desse parâmetro deve ser `S` para adicionar o nome da parte intimada ao nome do documento da certidão.

{{% notice warning %}}
O ID do modelo de documento informado no parâmetro `idModeloCertidaoCiencia` deve fazer referência a um modelo de documento válido e ativo. Caso contrário, a certidão automática não será juntada ao processo.
{{% /notice %}}

{{% notice note %}}
Para a correta utilização da funcionalidade, todos os parâmetros devem estar **ativos** e devidamente configurados.
{{% /notice %}}