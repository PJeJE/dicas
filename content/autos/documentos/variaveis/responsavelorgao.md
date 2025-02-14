---
title: "Recuperar magistrado responsável"
date: 2023-01-20T17:57:39-03:00
weight: 7
hidden: true
---

Utilização: `#{orgaoJulgadorManager.recuperaResponsavel(processoTrfHome.orgaoJulgador, null)}` 

Essa variável vai recuperar o nome do juiz, na seguinte ordem de prioridades:

1ª prioridade: juiz que esteja marcado como recebe distribuição e que seja titular;

2ª prioridade: juiz que recebe distribuição (mesmo não sendo titular);

3ª prioridade: juiz que é titular (mesmo não recebendo distribuição); e 

4ª prioridade: qualquer magistrado lotado na localização.
