---
title: "PCE"
date: 2026-04-17T15:00:45-03:00
weight: 2
menuTitle: "PCE"
---

Em construção

As prestações de contas eleitorais fazem parte de um processo de negócio que envolve diversos passos e sistemas da Justiça Eleitoral.

Uma característica inerente a essa questão é que as prestações serão sempre representados no PJe por processos judiciais.

Para a existência desses processos judiciais, uma série de integrações se tornam necessárias entre os sistemas envolvidos com o as Prestações de contas e o PJe.

As prestações de contas eleitorais têm regras próprias de funcionamento que são eventualmente atualizadas com normativos próprios. As regulamentações atualizadas podem ser encontradas no sítio https://www.tse.jus.br/eleicoes/

A partir do(s) sistema(s) pertinentes disponibilizados no sítio acima, são iniciados os procedimentos relacionados às prestações.

Atualmente, o SPCE é o sistema responsável pelo início das ações que envolvem o PJe.

Descreveremos nesta seção as principais regras relacionadas a essas integrações.

## Enviar informações das prestações

Após as ações pertinentes no SPCE, o servidor aciona o PJe por meio de opção própria no sistema para o envio das informações das prestações. 

Dentro do PJe, são protocolados os processos judiciais por meio de uma fila de integrações. 

Ao peticionar, são juntados os documentos iniciais:

- Petição Inicial
- Certidão de Pendência na Autuação
- Extrato da PC Final Oficial

O PJe envia de volta o número do processo protocolado que é atualizado no SPCE. 

## Enviar documentos (pós-peticionamento) - Final

Após o peticionamento do processo no PJe, há atualizações no processo que podem vir do SPCE. Os documentos que são refletidos no PJe são:

- Certidão de Juntada de Apresentação das Contas Finais
- Extrato da PC Final

## Enviar Mídia 

SITDOC - Sistema de Inteiro Teor de Documentos - Responsável pela gerenciamento de acervo digitalizado e mídias - controla o acesso ao acervo e faz integraçao com outros sistemas

software de controle de transferências de arquivos utilizados pelo TSE, com vigência até 24/11/2020.

Em outubro de 2019, visando a manutenção dos serviços mencionados acima, foi iniciado o procedimento de nova contratação (SEI 2019.00.000011595-8).

EDI - software de controle de transferências de arquivos utilizados pelo TSE - envia mídia
SITDOC - Sistema de Inteiro Teor de Documentos-  Leitura da Mídia e Envio de arquivos para o PJe e Juntada de Mídia
Juntar documentos ao processo

- Certidão de Juntada de Mídia
- Documentos de comprovação PC Final Intempestiva


 Movimentos SPCE para PJe - Juntada de Mídia

  
## Óbito - Recebimento de informação de ICN

O programa de Identificação Civil Nacional [ICN](https://www.justicaeleitoral.jus.br/identificacao-civil-nacional/) criou a **Base de Dados da Identificação Civil Nacional**. A informação de óbito, caso ocorra, é atualizada com base nos processos existentes no PJe. O processamento verifica se há óbitos no ICN relacionados às partes dos processos das classes processuais de código 12193 (Prestação de Contas Eleitorais) e 12633 (Requerimento de regularização de omissão de prestação de contas eleitorais) e repassa a informação ao PJe nos processos (processamento semelhante ocorre com processos de registro de candidaturas). Na ocorrência, o processo no PJe recebe uma certidão com as informações relacionadas e o movimento de código 15157 (Registrado o falecimento no sistema de registro de candidaturas) é lançado vinculado à certidão.
