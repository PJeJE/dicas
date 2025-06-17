---
title: "Automações da PCE com o uso da SINAPSES"
date: 2024-07-18T16:34:02-03:00
menuTitle: "PCE & SINAPES"
weight: 6
---


**AUTOMAÇÃO DE ETIQUETAS**

A automação de etiquetas PCE, acionada pela transição **Remeter para automação de etiquetas PCE**, instrui o sistema PJe a verificar a presença de documentos específicos das prestações de contas eleitorais (procuração, mídia, extrato parcial, demonstrativos parciais e finais). Com base nessa verificação e na configuração do fluxo, os processos são etiquetados conforme as regras negociais para indicar omissão, apresentação parcial ou completa, ou documentos faltantes. As etiquetas otimizam a organização do trabalho, servindo como triagem inicial que, por meio de filtros, permite distinguir processos que demandam regularização daqueles aptos para as análises subsequentes.

**AUTOMAÇÃO DE MINUTAS COM USO DA SINAPSES**

No tocante à automação das minutas da PCE, esta, ao deflagrar o fluxo por meio da transição **Remeter concluso com automação**, promove o encaminhamento do processo para o escrutínio e a confrontação dos pareceres exarados pelas esferas Técnica e Ministerial, valendo-se da plataforma Sinapses, nos seguintes termos:

I - Primeiramente, procede-se a uma verificação no processo a fim de identificar se os tipos de documentos configurados no fluxo, referentes aos pareceres Técnico e Ministerial, foram devidamente juntados;

II - Em caso de validação positiva, o processo é remetido a uma fila de execução assíncrona, propiciando que o envio ao Sinapses seja processado de forma ordenada e dispense o usuário da espera pela sua conclusão para a execução de demais atividades;

III - O processo é, subsequentemente, movimentado para uma tarefa de aguardo do retorno da plataforma de Inteligência Artificial (Sinapses);

IV - Após o processamento da análise dos pareceres, uma minuta aderente ao resultado é acostada ao processo, com base nos modelos predefinidos no sistema PJe. As classificações de minuta contemplam APROVAÇÃO SEM RESSALVAS, APROVAÇÃO COM RESSALVAS, REJEIÇÃO e NÃO PRESTAÇÃO DAS CONTAS. O processo OMISSO também recebe minuta automática, mas sua análise dispensa o uso da Sinapses;

V - Concluindo, o processo é automaticamente redirecionado à etapa de revisão da minuta, na tarefa intitulada **Revisar ato**. Nesta, o magistrado disporá da prerrogativa de chancelar a minuta revisada pela equipe serventuária ou, alternativamente, de requerer seu cancelamento, retificação ou o regresso à transição de automação. Caso a análise documental pela Sinapses revele divergência entre os pareceres Técnico e Ministerial, o sistema manterá o processo na tarefa de análise em que se encontrava, além de inserir a etiqueta de DIVERGÊNCIA, para que se proceda a uma análise e elaboração de minuta individualizada.

Tal abordagem registra a movimentação do processo diretamente no histórico de movimentações e no log do PJe e a consulta ao teor dos documentos ocorre no próprio sistema PJe. Como a solução é inerente à aplicação, dispensa-se o uso de repositórios documentais externos.

Para conferir o inteiro teor das **regras negociais** das automações da PCE [Clique aqui](/docs/Guia_das_Automacoes_da_PCE_com_uso_da_SINAPSES.pdf). 

A seguir, um **vídeo** que mostra o uso da automação na prática no PJe:

{{< video src="/videos/Automacoes_da_PCE_com_uso_da_SINAPSES.mp4">}}
