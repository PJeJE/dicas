---
title: "Certidão Automática de Redistribuição para Lavratura de Acórdão"
date: 2026-09-04T13:35:00-00:00
linkTitle: "Certidão Automática de Redistribuição para Lavratura de Acórdão"
weight: 9
draft: true
---

(disponível a partir da versão 2.2.0.4.12)

Esta funcionalidade automatiza a emissão da certidão de redistribuição para lavratura de acórdão, aplicável aos casos em que o relator originário é vencido e há a designação de um novo redator. O sistema permite que o Assessor de Plenário delibere sobre a necessidade de redistribuir os autos. Caso a opção seja pela redistribuição, o sistema registrará o respectivo movimento processual e emitirá automaticamente a certidão de redistribuição. A efetivação desse registro ocorrerá após encerrar o julgamento para o processo, ou, no fechamento da sessão, após registrar movimentação.

## Objetivos

- Identificar corretamente o julgador responsável pela redação do acórdão
- Padronizar os registros processuais
- Aumentar a transparência dos atos praticados no PJe
- Reduzir intervenções manuais
- Evitar dúvidas sobre a origem e o fundamento da redistribuição, bastante questionada pelos advogados

## Como funciona (para o Assessor de Plenário)

Durante a proclamação do julgamento, se a votação resultar em relator vencido, o sistema exibirá a pergunta: **"Deseja redistribuir o processo?"**. O Assessor de Plenário deverá obrigatoriamente selecionar **SIM** ou **NÃO**.
<img width="662" height="517" alt="image" src="https://github.com/user-attachments/assets/7c7440a9-40ed-45a4-bc72-eed947be4386" />


### Validações do sistema — Encerramento sem marcar a opção de redistribuição

**No encerramento individual do processo**

O sistema exibirá uma mensagem de bloqueio quando o processo tiver relator vencido e a marcação de redistribuição não tiver sido feita.
<img width="662" height="272" alt="image" src="https://github.com/user-attachments/assets/6d79d6fd-66d9-4698-9913-7d8f5b6316a3" />


**No encerramento da sessão plenária**

O sistema exibirá a lista de processos pendentes de redistribuição, bloqueando o fechamento da sessão até que a marcação seja realizada.
<img width="1302" height="375" alt="image" src="https://github.com/user-attachments/assets/eb585487-bbec-4ec0-8a1a-9829f2a95fc6" />


## Como a funcionalidade opera

- **Obrigatoriedade de registro:** na proclamação do julgamento, o sistema passou a apresentar a pergunta "DESEJA REDISTRIBUIR O PROCESSO?". O Assessor de Plenário deve obrigatoriamente optar por "sim" ou "não", não havendo mais a hipótese de encerrar a sessão plenária ou o julgamento individual do processo sem realizar essa marcação.
- **Ampliação de motivos:** além da opção de redistribuição por "mérito" (já existente), foram disponibilizadas as opções de redistribuição por "questão de ordem" e "preliminar".
- **Regra para feitos principais:** caso a opção de redistribuição seja "sim", o sistema gera o movimento de redistribuição e junta a certidão automática para lavratura de acórdão, na árvore processual do PJe. Essa redistribuição alcança apenas o feito principal. Os cadernos processuais vinculados não são redistribuídos.
- **Regra para recursos internos:** na hipótese de redistribuição de recurso interno, o sistema apenas atualiza o órgão julgador e a relatoria do feito, sem realizar a juntada de certidão ou o lançamento de movimento de redistribuição.

Cabe destacar que, embora a demanda tenha sido motivada por uma necessidade específica do TSE, para atender o art. 25, *caput*, do RITSE, a solução foi desenvolvida mediante a adoção de parâmetros configuráveis. Dessa forma, a funcionalidade é totalmente parametrizável e reutilizável pelos Tribunais Regionais, observadas as regras regimentais aplicáveis a cada órgão.

## Procedimentos de configuração (no tribunal regional)

O Regional que desejar utilizar a funcionalidade deverá seguir os seguintes procedimentos:

1. Configurar a certidão automática que será assinada pelo sistema, no parâmetro `idModeloCertidaoRedistribuicao`.
2. Marcar `true` no parâmetro `pje:sessao:permiteCertidaoRedistribuicaoAutomatica`.

   OBS: em caso de dúvida, consultar o suporte da ASPJE. (vide abaixo)

### Variáveis utilizadas no modelo de certidão



```#{processoTrfHome.recuperarClasseJudicial(processoTrfHome.instance)}```
```Processo #{processoTrfHome.instance.numeroProcesso}```
```#{processoTrfHome.getRedatorAcordao(processoTrfHome.instance)}```
```#{dataAtual}```.



## Importante

> [!IMPORTANT]
> **A configuração poderá ser utilizada em todos os Regionais?**
> Não. Nos Tribunais em que o fluxo foi personalizado para nunca redistribuir o processo, por adotarem esse entendimento, a melhoria não funcionará, mesmo se configurada.
>
> **Os Tribunais que já adotam o procedimento de redistribuir o feito quando o relator fica vencido poderão adotar a funcionalidade?**
> Sim. Contudo, será preciso sempre marcar a opção de redistribuir ou não.

---




