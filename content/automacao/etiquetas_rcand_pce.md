---
title: "Automação de etiquetas para RCAND e PCE"
date: 2024-08-05T14:16:02-03:00
menuTitle: "Automação de etiquetas"
weight: 3
---


Em conjunto com o TRE-SP, foram desenvolvidos ajustes no fluxo do PJe de primeiro grau para, de acordo com a tramitação e com a presença ou ausência de alguns documentos no processo, permitir que o sistema vincule etiquetas automaticamente de forma a sinalizar ao servidor a situação de processos RCAND e PCE quanto à necessidade de documentos obrigatórios para o prosseguimento da tramitação do processo.

**Protocolo para compartilhamento da ferramenta**

A solução está em todos os ambientes de produção do PJe da Justiça Eleitoral de primeiro grau. Outras iniciativas para automatizar a vinculação de etiquetas podem ser desenvolvidas. Para solicitação de novas iniciativas, deve-se detalhar os requisitos e enviar a solicitação via oficio à presidência do TSE aos cuidados da Assessoria do PJe


**Unidade(s) responsável(eis) para esclarecimentos técnicos e negociais**

Contato: Assessoria do PJe - aspje@tse.jus.br

**Instruções sobre funcionamento**

Na liberação da funcionalidade de automação de etiquetas, foram divulgadas algumas instruções sobre o funcionamento que replicamos abaixo.

Nos ambientes do primeiro grau, ao ser utilizada as transições **Remeter para automação de etiquetas PCE** (processos da classe PCE) ou **Remeter para automação de etiquetas RCand** (processos da classe RCAND), o sistema vinculará, de forma automática, algumas etiquetas para sinalizar presença ou falta de alguns documentos. As transições estão disponíveis a partir das tarefas de análise, conforme classe processual. Sempre que acionadas, o sistema apagará as etiquetas com o prefixo PJE_IA e aplicará novas etiquetas de acordo com a ausência ou presença dos documentos. 

Tipos de Documentos relativos à Prestação de Contas Eleitorais

+ Extrato de Prestação de Contas
+ Declaração de Juntada dos Demonstrativos
+ Certidão de inadimplência
+ Declaração da Apresentação das Contas Finais
+ Procuração

Etiquetas abaixo serão apresentadas na falta dos documentos respectivos

+ PJE_IA_OMISSO – Qualquer documento da lista abaixo que não esteja presente, a etiqueta também será apresentada, assim como o documento se faltar o documento Certidão de inadimplência
+ PJE_IA_PENDENTE – Parcial  - Extrato de Prestação de Contas e/ou Declaração de Juntada dos Demonstrativos
+ PJE_IA_PENDENTE – Mídia -  Declaração da Apresentação das Contas Finais  
+ PJE_IA_PENDENTE – Procuração -  Procuração 


Caso nenhum dos documentos acima estiver ausente, serão vinculadas as seguintes etiquetas:

+ PJE_IA_DOCUMENTAÇÃO_COMPLETA 
+ PJE_IA_REVISAR_AUTUAÇÃO


Tipos de Documentos relativos à Registro de Candidatura 

+ Declaração de bens 
+ Certidão Criminal da Justiça Estadual de 1º grau 
+ Certidão Criminal da Justiça Estadual de 2º grau 
+ Certidão Criminal da Justiça Federal de 1º grau 
+ Certidão Criminal da Justiça Federal de 2º grau 
+ Comprovante de escolaridade 
+ Documento de identificação ou Identifidade
+ Proposta de governo (validação apenas para processos que não sejam relacionados ao cargo Vereador

Etiquetas abaixo serão apresentadas na falta ou ausência dos documentos respectivos

+ PJE_IA_Sem Documentação – Qualquer documento da lista abaixo que não esteja presente, a etiqueta também será apresentada
+ PJE_IA_OK - Declaração de bens
+ PJE_IA_OK - Certidão Criminal da Justiça Estadual de 1º grau 
+ PJE_IA_OK - Certidão Criminal da Justiça Estadual de 2º grau
+ PJE_IA_OK - Certidão Criminal da Justiça Federal 1º de grau 
+ PJE_IA_OK - Certidão Criminal da Justiça Federal de 2º grau
+ PJE_IA_OK - Comprovante de escolaridade 
+ PJE_IA_OK - Documento de identificação 
+ PJE_IA_OK - Proposta de governo 
+ PJE_IA_Pendente - Declaração de bens 
+ PJE_IA_Pendente - Certidão Criminal da Justiça Estadual de 1º grau 
+ PJE_IA_Pendente - Certidão Criminal da Justiça Estadual de 2º grau 
+ PJE_IA_Pendente - Certidão Criminal da Justiça Federal 1º de grau 
+ PJE_IA_Pendente - Certidão Criminal da Justiça Federal de 2º grau 
+ PJE_IA_Pendente - Comprovante de escolaridade 
+ PJE_IA_Pendente - Documento de identificação 
+ PJE_IA_Pendente - Proposta de governo
