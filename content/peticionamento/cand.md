---
title: "Registro de candidaturas"
date: 2026-04-17T15:00:45-03:00
weight: 1
menuTitle: "Registro de candidaturas"
---
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

Ao peticionar, são juntados os documentos iniciais e são realizadas as associações entre processos existentes. As associações de processos seguem as regras a seguir:

▪ Prevenção entre DRAPs (mesmo CNPJ do partido e da federação independente do cargo – majoritário e proporcional)
▪ Prevenção entre RRC e RRCI aos DRAPs (RRCI vai pelo CNPJ do partido/da coligação/federação)
▪ Prevenção de RRC de vaga remanescente vai para o DRAP prevento (O CAND repassa, via integração, o número do processo do DRAP prevento)
▪ Associar RRCs de cargos majoritários da mesma chapa (mesmo CNPJ do partido/da coligação/federação da mesma abrangência)
▪ Associar processos de substituto e substituído (O CAND informa, via integração, o número do processo do substituído)

{{% notice note %}}
Partidos e federações sem CNPJ serão inseridos como Ente e Autoridade no PJe associados a uma pessoa jurídica com o CNPJ Nacional
{{% /notice %}}

Documentos que são utilizados nesse peticionamento inicial:

- Petição (DRAP, RRC e RRCI com dados anonimizados)
  - Original, substituto e remanescente
- Anexos:
  - RRC/RRCI sigiloso com dados anonimizados
  - Comprovantes:
    - Desincompatibilização (anonimizado) (Código: 285)
    - Dissidência (Código: 21)
    - Identificação (RG ou CNH) (Código: 65) (sigiloso)
    - Escolaridade (anonimizado) (Código: 286)
    - Proposta de governo (Código: 41)
    - Certidões (Código: 6000014)
    - Declaração de bens (Código: 14649)
    - Atas de convenção (Código: 14643)
    - Certidões criminais (anonimizado)
    - Certidão criminal da Justiça Federal de 1º grau (Código: 14646)
    - Certidão criminal da Justiça Federal de 2º grau (Código: 14645)
    - Certidão criminal da Justiça Estadual de 1º grau (Código: 14644)
    - Certidão criminal da Justiça Estadual de 2º grau (Código: 14647)
    - Certidão criminal de foro por prerrogativa de função (Código: 14648)

Ao finalizar o peticionamento no PJe, as informações de número do processo e de nome do relator são retornadas ao CAND.

## Enviar documentos (pós-peticionamento)

Após o peticionamento do processo no PJe, podem ocorrer atualizações de documentos no CAND que devem ser refletidas no PJe. Os documentos que são juntados no PJe ao serem atualizados no CAND são os seguintes:

• Edital de pedido de registro (Código: 569)
• Edital de pedido de registro individual (Código: 569)
• Edital de vaga remanescente (Código: 569)
• Edital de intimação de contrarrazões de recurso (Código: 569)
• Edital de intimação de despacho (Código: 569)
• Edital de substituição (Código: 569)
• Informação de candidato(a) (Código: 587)
• Informação de coligação (Código: 588)
• Informação de partido (Código: 589)
• Informação de federação (Código: C6000101)
• Mapa de documentação de federação (Código: C6000099)
• Mapa documentação de coligação (Código: 648)
• Mapa documentação de partido (Código: 649)
• Nome Social (Código: 669)
• Renúncia de candidatura (Código: C6000100)
• Declaração de Bens (Código: 14649)
• Atas de convenção (Código: 14643)
• Requerimento para o registro analítico (Código: 670)
• Requisitos para o registro – Dados do Cadastro Eleitoral e FILIA (Código: 670)
• Intimação de diligência do(a) candidato(a) (Intimação de diligência) (Código: 805)
• Intimação de diligência do partido (Intimação de diligência) (Código: 805)
• Intimação de diligência da coligação (Intimação de diligência) (Código: 805)
• Intimação de diligência da federação (Intimação de diligência) (Código: 805)


## Enviar documentos/informações para o CAND

Existem também documentos que, se forem inseridos diretamente no processo judicial no PJe, devem ser refletidos no CAND. Os documentos que são atualizados no CAND ao serem juntados no PJe são os seguintes:

- Proposta de governo (Código: 41)
- Certidões criminais:
  - Certidão criminal da Justiça Federal de 1º grau (Código: 14646)
  - Certidão criminal da Justiça Federal de 2º grau (Código: 14645)
  - Certidão criminal da Justiça Estadual de 1º grau (Código: 14644)
  - Certidão criminal da Justiça Estadual de 2º grau (Código: 14647)
  - Certidão criminal de foro por prerrogativa de função (Código: 14648)
 
O PJe também atualiza no CAND a informação do(a) relator(a) do processo caso seja alterada no PJe.

## Movimentos/Informações CAND para PJe

Alguns procedimentos no CAND resultam em atualizações no PJe. Essas atualizações são realizadas por meio do registro de movimentos processuais. Os movimentos lançados no PJe em decorrência de alterações no CAND são os seguintes:
• Identificada possível dissidência partidária (Código: 12655)
• Partido movimentado (Código: 12657)
• Determinada a movimentação de partido/federação (Código: 12664)
• Reaberto o sistema de candidaturas ** (Código: 14212)
• Fechado o sistema de candidaturas ** (Código: 12658)
• Alteração de candidato(a)** (alteração de dados do(a) candidato(a): nome para urna (Código: 15097)**, foto (Código: 15098), número (Código: 15099), data de nascimento (Código: 15100)
• Registrado o falecimento no sistema de registro de candidaturas** (Código: 15157)
• Registrada a renúncia no sistema de registro de candidaturas** (Código: 15158) 

Nas operações marcadas com *, o movimento é lançado independentemente da instância do processo.

Além do movimento, há também a atualização da prioridade eleito(a)/não eleito(a), que afeta a tramitação processual do processo no PJe

## Recebimento de informação de ICN

O programa de Identificação Civil Nacional [ICN](https://www.justicaeleitoral.jus.br/identificacao-civil-nacional/) criou a a Base de Dados da Identificação Civil Nacional. A informação de óbito de candidato, caso ocorra, é attualizada no PJe.  


## Envio de Documentos para o PJe (Classe RCAND)

• Outros documentos (Código: 106)
• Notícia de inelegibilidade (Código: 33)
• Foto (Código: 92)
• Comprovante de escolaridade (Código: 286)
• Comprovante de desincompatibilização (Código: 285)
• Declaração de bens (Código: 14649)
• Proposta de governo (Código: 41)
• Identidade (Código: 65)
• Certidão criminal da Justiça Federal de 1º grau (Código: 14646)
• Certidão criminal da Justiça Federal de 2º grau (Código: 14645)
• Certidão criminal da Justiça Estadual de 1º grau (Código: 14644)
• Certidão criminal da Justiça Estadual de 2º grau (Código: 14647)
• Certidão criminal de foro por prerrogativa de função (Código: 14648)
• Renúncia de candidatura (Código: C6000100)

## Detalhamento gráfico das integrações
![Integração CAND PJE](/imagens/integracaocandpje.jpg)



