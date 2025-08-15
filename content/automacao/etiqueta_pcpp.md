---
title: "Automação de etiquetas para PC-PP"
date: 2025-08-05T14:16:02-03:00
menuTitle: "Automação de etiquetas PC-PP"
weight: 3
---


A automação de etiquetas no sistema PJe, destinada aos processos de PRESTAÇÃO DE CONTAS ANUAL (PC-PP), visa verificar a presença de documentos específicos para essa classe judicial. O fluxo é disparado quando o usuário encaminha o(s) processo(s) para a transição designada, **Remeter para automação de etiquetas PCA**, a partir das tarefas de análise. Em seguida, o sistema realiza uma varredura para identificar os tipos de documentos previamente configurados. Caso um ou mais desses tipos sejam encontrados, a etiqueta correspondente é aplicada automaticamente. Após essa verificação, o processo é automaticamente movido para a tarefa de "elaborar documento".

As etiquetas geradas seguem o padrão "PJE_IA_OK – [Nome do Tipo de Documento]". Os tipos de documentos configurados são aqueles listados na pasta 14601, localizada na aba “Documentos Processuais” da SGT/CNJ.

Se um processo for encaminhado indevidamente para a transição "Remeter para automação de etiquetas PCA" e a etiquetagem não for desejada, basta excluir as etiquetas aplicadas. Da mesma forma, caso as etiquetas sejam apagadas por engano, é possível refazer o encaminhamento do processo pela mesma transição para que a automação ocorra novamente.
