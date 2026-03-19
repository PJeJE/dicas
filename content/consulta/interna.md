---
title: "Consulta interna"
date: 2022-11-29T16:19:55-03:00
menuTitle: "Interna"
weight: 5
---

A **Consulta de Processos** disponiveis para usuários logados pode ser acessada pelo menu **Processo - Pesquisar - Processo** (você também pode utilizar o acesso rápido para digitar a expressão de busca):

![Tela de consulta interna](/imagens/consulta_1.jpg)

Também é possível acessar a consulta pelo ícone da **lupa** disponível no **Painel do Usuário:**

![Tela de consulta interna](/imagens/consulta_2.jpg)

A tela da consulta exibe uma variedade de campos de pesquisa, livres e tabelados, que podem ser utilizados de maneira isolada ou em conjunto, para filtrar o processo ou grupo de processos de acordo com os critérios desejados.

{{% notice warning %}}
Os resultados da consulta são apresentados ordenados por data de autuação, sendo que dia, hora, minutos e segundos são considerados para a esta ordenação.
{{% /notice %}}

## Consulta de processos para servidor de outra instância:

No PJe 1G há um perfil de servidor chamado **Consulta de processos para servidor,** exclusivamente para consulta, não sendo possível consultar processos sigilosos. 

O cadastro dos usuários vinculados a esse perfil deve ser feito pela funcionalidade **Configuração - Pessoa - Servidor,** selecionando apenas a Localização Física (Estado) e o opção Papel (Consulta de processos para servidor):

![Tela de consulta interna](/imagens/consulta_4.jpg)

Nos TREs, os administradores locais podem criar um perfil semelhante em **Configuração - Controle de Acesso - Papéis.**

Basta Criar um novo papel com o nome Consulta de processos para servidor de outra instância, utilizando o identificador consulta. Na aba **Herdeiros** desse papel, deve ser vinculado o papel Colaborador e, na aba **Recursos**, deve ser associado o recurso Página Processo/Consulta/Consulta de Processo.

O cadastro dos usuários vinculados ao perfil é feito em **Configuração - Pessoa - Servidor,** da forma descrita acima, sendo que no PJe2G o preenchimento do campo **Órgão julgador colegiado** é facultativa:

![Tela de consulta interna](/imagens/consulta_5.jpg)

## Procuradorias

Outra forma de usuários de uma instância terem acesso ou praticarem atos em processos que estão em outra instância é mediante a criação de procuradorias.

No TSE a consulta processual para usuários dos TREs se dá por procuradores cadastrados. 
