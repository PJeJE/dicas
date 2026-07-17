---
title: "Editor anotações da sessão"
date: 2026-07-17T12:09:20-03:00
weight: 4
---

## Anotações da sessão

Está disponível para o **Assessor de Plenário** um editor de textos de uso geral no escopo da **Sessão de Julgamento** denominado **Anotações da sessão**. Esse editor carrega um documento que fica vinculado à respectiva sessão vinculada à tela onde ele pode ser acessado. Dessa forma, as informações ali gravadas vão ser sempre recuperadas quando o editor for aberto novamente naquela sessão. 

Usualmente, ao ser acionado, ele carrega um documento cujo modelo foi previamente configurado pelo usuário administrador. O modelo traz informações sobre todos os processos pautados naquela sessão. 

Pode-se fazer uso de outras variáveis no modelo de documento, mas deve-se sempre lembrar que o escopo do editor é o da sessão de julgamento, ou seja, se uma variável recupera informações sobre um processo específico, ela não funcionará nesse editor já que o editor não sabe à qual processo se refere à variável. No escopo de uma sessão, muitos processos podem ser referenciados.

Muito tribunais utilizam esse editor como uma alternativa para gerar um documento de pauta e até o utilizam para envio para publicação. 

O editor está disponível por meio da **Relação de julgamento**.

![Editor na Relação de julgamento](/imagens/editorsessaopauta.png)

Também está disponível pelo **Painel do secretário da sessão**.

![Editor no Painel do secretário](/imagens/editorsessaopainel.png)



{{% notice note %}}
O modelo de documento carregado no editor é o modelo cujo identificador está cadastrado no parâmetro **pje:sessao:modeloDocumento:minutaPregao**
{{% /notice %}}


Abaixo estão algumas variáveis que funcionam no escopo da sessão de julgamento e, consequentemente, podem ser utilizadas no modelo do editor **Anotações da sessão**:


#{sessaoManager.recuperarProcessosPautadosPublicacao(null)}.
