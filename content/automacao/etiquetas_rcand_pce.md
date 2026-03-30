---
title: "Automação de etiquetas para RCAND e PCE"
date: 2024-08-05T14:16:02-03:00
menuTitle: "Automação de etiquetas RCAND e PCE"
weight: 3
---

**Automação de Etiquetas: Registro de Candidatura (RCAND)**

**1. Objetivo**

A funcionalidade de automação de etiquetas foi desenvolvida para otimizar a análise de processos de Registro de Candidatura (RCAND). Ao ser acionada, ela verifica automaticamente a presença ou ausência de documentos obrigatórios, aplicando etiquetas que sinalizam o status de cada processo.
Isso permite que o servidor identifique rapidamente as pendências documentais, garantindo maior agilidade na tramitação.

**2. Como Funciona**

A automação é iniciada pela transição *"Remeter para automação de etiquetas RCand"*. Ao ser acionada, o sistema executa duas ações principais:
	Limpeza: Remove todas as etiquetas anteriores que começam com o prefixo PJE_IA_. Isso garante que a análise seja sempre baseada no estado atual do processo.
	Aplicação: Realiza uma nova varredura dos documentos e aplica as etiquetas atualizadas (PJE_IA_OK para documentos presentes e PJE_IA_Pendente para ausentes).

**3. Regras de Disponibilidade**

A transição para automação de etiquetas está disponível conforme as seguintes condições:
  •	Classe Processual: Exclusivamente para a classe Registro de Candidatura (RCAND).
  •	Fluxo: Disponível em todas as instâncias (1º, 2º e 3º Graus).
  •	Tarefas:
      o	1º Grau: Disponível a partir das tarefas de análise do processo.
      o	2º e 3º Graus: Unidade de Autuação: Disponível na tarefa "Verificar e Certificar Dados". A automação deve ser executada através do menu esquerdo, na funcionalidade "Movimentar em Lote". Unidade de Processamento:    Disponível a partir das tarefas de análise do processo.

**4. Documentos Verificados**

O sistema busca pelos seguintes tipos de documentos no processo:

•	Declaração de bens

•	Certidão Criminal da Justiça Estadual de 1º grau

•	Certidão Criminal da Justiça Estadual de 2º grau

•	Certidão Criminal da Justiça Federal de 1º grau

•	Certidão Criminal da Justiça Federal de 2º grau

•	Comprovante de escolaridade

•	Documento de identificação (Identidade)

•	Proposta de governo

Observação: A validação da Proposta de Governo é realizada em todos os cargos, exceto: Vereador, Senador e Deputado Federal/Estadual/Distrital.

**5. Etiquetas Geradas**
As etiquetas indicam o status de cada documento verificado.

**Etiquetas de Conformidade (Documento Encontrado)**

•	PJE_IA_OK - Declaração de bens

•	PJE_IA_OK - Certidão Criminal da Justiça Estadual de 1º grau

•	PJE_IA_OK - Certidão Criminal da Justiça Estadual de 2º grau

•	PJE_IA_OK - Certidão Criminal da Justiça Federal 1º de grau

•	PJE_IA_OK - Certidão Criminal da Justiça Federal de 2º grau

•	PJE_IA_OK - Comprovante de escolaridade

•	PJE_IA_OK - Documento de identificação

•	PJE_IA_OK - Proposta de governo

**Etiquetas de Pendência (Documento Ausente)**

•	PJE_IA_Pendente - Declaração de bens

•	PJE_IA_Pendente - Certidão Criminal da Justiça Estadual de 1º grau

•	PJE_IA_Pendente - Certidão Criminal da Justiça Estadual de 2º grau

•	PJE_IA_Pendente - Certidão Criminal da Justiça Federal 1º de grau

•	PJE_IA_Pendente - Certidão Criminal da Justiça Federal de 2º grau

•	PJE_IA_Pendente - Comprovante de escolaridade

•	PJE_IA_Pendente - Documento de identificação

•	PJE_IA_Pendente - Proposta de governo

**Etiqueta de Status Geral**

•	PJE_IA_Sem Documentação: Esta etiqueta é aplicada como um alerta geral sempre que pelo menos um dos documentos obrigatórios da lista estiver ausente no processo.









**Automação de Etiquetas: Prestações de contas**


**Instruções sobre funcionamento**

Na liberação da funcionalidade de automação de etiquetas, foram divulgadas algumas instruções sobre o funcionamento que replicamos abaixo. Alternativamente, [clique aqui](https://pjeje.github.io/dicas/automacao/pce_com_sinapses/) para saber mais sobre as regras gerais das etiquetas da PCE e suas automações.

Nos ambientes do primeiro grau, ao ser utilizada a transição **Remeter para automação de etiquetas PCE** (processos da classe PCE) o sistema vinculará, de forma automática, algumas etiquetas para sinalizar presença ou falta de alguns documentos. A transição está disponível a partir das tarefas de análise. Sempre que acionadas, o sistema apagará as etiquetas com o prefixo PJE_IA e aplicará novas etiquetas de acordo com a ausência ou presença dos documentos. 

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







**Automação de etiquetas (PC-PP)**

A automação de etiquetas no sistema PJe, destinada aos processos de PRESTAÇÃO DE CONTAS ANUAL (PC-PP), visa verificar a presença de documentos específicos para essa classe judicial. O fluxo é disparado quando o usuário encaminha o(s) processo(s) para a transição designada, "Remeter para automação de etiquetas PCA", a partir das tarefas de análise. Em seguida, o sistema realiza uma varredura para identificar os tipos de documentos previamente configurados. Caso um ou mais desses tipos sejam encontrados, a etiqueta correspondente é aplicada automaticamente. Após essa verificação, o processo é automaticamente movido para a tarefa de "elaborar documento".

As etiquetas geradas seguem o padrão "PJE_IA_OK – [Nome do Tipo de Documento]". Os tipos de documentos configurados são aqueles listados na pasta 14601, localizada na aba “Documentos Processuais” da SGT/CNJ.

Se um processo for encaminhado indevidamente para a transição "Remeter para automação de etiquetas PCA" e a etiquetagem não for desejada, basta excluir as etiquetas aplicadas. Da mesma forma, caso as etiquetas sejam apagadas por engano, é possível refazer o encaminhamento do processo pela mesma transição para que a automação ocorra novamente.
