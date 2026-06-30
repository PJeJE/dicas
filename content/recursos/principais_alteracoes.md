---
title: "Principais alterações no relacionamento entre objetos e tabelas"
date: 2022-11-29T16:28:18-03:00
linkTitle: "Principais alterações"
weight: 15
---

As principais alterações serão relatadas por tabelas alteradas:

## TB_PROCESSO
+ A tabela tem a informação da última capa registrada em tb_processo_trf (cd_processo_status = ‘D’) relativa a esse processo.

## TB_PROCESSO_TRF
+ A tabela contém o registro do processo originário (id_processo), referenciando a tabela tb_processo (sempre preenchido);
+ O registro da capa principal do processo (id_processo_trf_principal), referenciando a própria tb_processo_trf (sempre preenchido);
+ O registro da capa pai (id_processo_trf_pai), que pode existir ou não. Só existirá quando for um recurso do recurso;
+ A cadeia do recurso em forma de sigla (ds_classe_judicial_sigla). Se o campo não estiver preenchido, a recuperação é pelo campo sigla da classe da capa;
+ A cadeia do recurso por extenso (ds_classe_judicial_extenso). Se o campo não estiver preenchido, a recuperação é pelo campo de descrição da classe da capa;
+ Um identificador de recurso interno (in_recurso_interno);
+ A identificação da situação do processo (ds_nome_situacao_processual). As situações já existiam antes, mas foram replicadas aqui para deixar a consulta mais rápida

## TB_PROC_PARTE_EXPEDIENTE
+ A tabela tem o identificador da capa principal, para otimizar os joins nas consultas de intimações para usuários externos (id_processo_trf_principal); 
+ As triggers que alimentam tabelas de otimização de consultas (tb_cabecalho_processo e tb_processo_tarefa) foram alteradas para contemplar todas as alterações estruturais das tabelas de origem. As respectivas tabelas, assim como a tabela de documentos e a tabela de movimentos, foram alteradas para conter identificação da capa a que se refere o registro;
+ As tabelas tb_processo_instance e tb_proc_localizacao_ibpm foram alterados para conter a coluna id_processo_trf, correspondente ao caderno processual a que se refere o registro; 
+ Algumas interfaces para uso de publicação no diário fazem referência ao campo idProcesso. Esse campo é preenchido no PJe e recebido no diário do tribunal, que faz consultas adicionais no banco do PJe, de acordo com a necessidade. Antes dos recursos, o PJe enviava o idProcessoTrf referente ao expediente, que é igual ao idProcesso. Com os novos recursos, esses ids podem não coincidir. A implementação dos conectores com o diário deve ser revisada de acordo com essa observação.
