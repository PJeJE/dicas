---
title: "Registro de candidaturas"
date: 2026-04-17T15:00:45-03:00
weight: 1
menuTitle: "Registro de candidaturas"
---
# Registro de candidaturas

O processo de negócio do **Registro de candidaturas** envolve diversos passos e sistemas da Justiça Eleitoral. 

Uma característica inerente a essa questão é que pedidos de **Registro de candidaturas** e pedidos de **Demonstrativo de regularidade de atos partidários** serão sempre representados no PJe por processos judiciais. 

Para a existência desses processos judiciais, uma série de integrações se tornam necessárias entre os sistemas envolvidos com o **Registro de candidaturas** e o PJe.

O registro de candidaturas tem regras próprias de funcionamento que são eventualmente atualizadas com normativos próprios. As regulamentações atualizadas podem ser encontradas no sítio https://www.tse.jus.br/eleicoes/

A partir do(s) sistema(s) pertinentes disponibilizados no sítio acima, são iniciados os procedimentos relacionados ao registro. 

Atualmente, o CAND é o sistema responsável pelo início das ações que envolvem o PJE.

Descreveremos nesta seção as principais regras relacionadas a essas integrações.

## Enviar informações das candidaturas

Após as ações pertinentes no CAND, o servidor aciona o PJe por meio de opção própria no CAND para o envio das informações das candidaturas. 

Dentro do PJe, são protocolados os processos judiciais por meio de uma fila de integrações. 

Após o peticionamento, são juntados os documentos iniciais e são realizadas as associações entre processos existentes. As associações de processos seguem as regras a seguir:

▪ Prevenção entre DRAPs (mesmo CNPJ do partido e da federação independente do cargo – majoritário e proporcional)
▪ Prevenção entre RRC e RRCI aos DRAPs (RRCI vai pelo CNPJ do partido/da coligação/federação)
▪ Prevenção de RRC de vaga remanescente vai para o DRAP prevento (O CAND repassa, via integração, o número do processo do DRAP prevento)
▪ Associar RRCs de cargos majoritários da mesma chapa (mesmo CNPJ do partido/da coligação/federação da mesma abrangência)
▪ Associar processos de substituto e substituído (O CAND informa, via integração, o número do processo do substituído)

{{% notice note %}}
Partidos e federações sem CNPJ serão inseridos como Ente e Autoridade no PJe associados a uma pessoa jurídica com o CNPJ Nacional
{{% /notice %}}

## Detalhamento gráfico das integrações
![Integração CAND PJE](/imagens/integracaocandpje.jpg)



