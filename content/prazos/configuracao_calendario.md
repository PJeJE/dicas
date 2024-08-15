---
title: "Configuração do calendário"
menuTitle: "Calendário"
date: 2023-08-28T22:25:20-03:00
weight: 3
---

O calendário é uma configuração muito importantes do sistema, dele depende a contagem dos prazos processuais.

Ele serve não apenas para o registro de dados de feriados, mas também para também para indicar quaisquer eventos que tenham impacto sobre a contagem de prazos, como suspensões de expedientes por greves ou desastres naturais.

Em não havendo registro de eventos no calendário, o sistema considerará, para a contagem de prazos, apenas os dias não úteis regulares – sábados e domingos. Do mesmo modo, a existência de eventos em municípios que não são sede do órgão julgador não impacta a contagem do prazo.

{{% notice note %}}
O impacto do registro de um evento no calendário será definido pelo usuário durante o cadastramento. Os eventos que afetam a contagem de prazo são aqueles do município sede da jurisdição a que está vinculado o órgão julgador.
{{% /notice %}}

No menu **Configuração - Tabelas Básicas - Calendário** é possível criar ou alterar eventos, para que a contagem de prazos automatizada do PJe funcione de maneira adequada.

Observe, na imagem abaixo, a tela de criação de evento, aba **Formulário** (A):

IMG_CALENDARIO

B - **Descrição:** campo textual para registro do nome dado ao feriado ou evento que impacta na contagem de prazos;
C - **Ato:** campo para especificação do ato normativo que criou ou regulamentou o evento;
D - **Data:** indica a data do evento (quando for pontual) ou o período deste (quando houver um intervalo);
1 - **Periodicidade:** indica se o evento é pontual (um único dia) ou um intervalo de datas, caso em que o campo data (D) será alterado para que se o dia inicial e o dia final;
2 - **Repete anualmente?:** faz com que feriados fixos sejam cadastrados de forma perene, sem precisar de inclusão ano a ano;
3 - **Suspende prazo:** indica se o evento suspende a contagem dos prazos no dia ou período de sua ocorrência, caso em que o dia/período será acrescido ao final do prazo; 

{{% notice warning %}}
A **suspensão** de prazos é uma exceção, tenha certeza de que deseja que esses dias sejam acrescidos à contagem de prazo quando optar por essa marcação!
{{% /notice %}}

4 - **Feriado judiciário:** indica que esse evento é um feriado apenas para o judiciário;
5 - **Feriado:** indica que o feriado é geral;

{{% notice info %}}
A marcação de feriado ou feriado judiciário não gera diferença prática na contagem de prazos.
{{% /notice %}}

6 - **Indisponibilidade do sistema:** utilizada quando o PJe estiver fora do ar na data ou período do evento;
7 - **Abrangência:** indica se o evento influenciará a contagem dos prazos a nível nacional, estadual, municipal ou de um único órgão julgador. Caso seja marcada abrangência inferior à nacional, serão solicitados , respectivamente, o estado, o município ou o órgão julgador. O acesso a essas opções pode ser restrito de acordo com o papel do usuário;
8 - **Situação:** indica se o registro está em uso ou não.
