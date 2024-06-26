---
title: "Pauta de Julgamentos"
date: 2022-11-29T16:30:31-03:00
weight: 1
---

## Intimação de pauta na publicação da lista e no fechamento da pauta:

A publicação de pauta (última aba na Relação de julgamento) no diário, utiliza a pessoa Destinatário para ciência pública. A intimação não é gerada para pessoas individuais, já que aquele é um aviso geral da sessão que acontecerá. As intimações individuais são geradas no fechamento mesmo (primeira aba da Relação de julgamento), ou via fluxo, em **Preparar ato de comunicação.**

Para inibir as intimações gerais, tem que usar a configuração do Órgão julgador colegiado, onde há um campo indicando a intimação automática da pauta.

+ Campos na intimação de pauta:

No documento de intimação de pauta só funcionam as variáveis listadas na Regra de Negócio 618 (https://www.pje.jus.br/wiki/index.php/Regras_de_neg%C3%B3cio#RN618). A inserção de outras informações pode gerar inconsistência técnica.

Como regra, a publicação da pauta utiliza os processos selecionados pelo usuário na aba Aptos para publicação e monta um documento de acordo com os seguintes parâmetros:

a) Pessoa que será utilizada para registrar ciência, quando a publicação ocorrer no DJE, conforme configuração do  parâmetro: pje:fluxo:publicacao:idDestinacaoPessoaCienciaPublica.

b) Tipo de processo documento, conforme configuração do parâmetro: idTipoProcessoDocumentoIntimacaoPauta.

c) Modelo de documento, conforme configuração do parâmetro: idModeloIntimacaoPauta (deve ser usado tanto para o fechamento da pauta quanto para sua publicação). 

Para cada processo selecionado, o sistema construirá um documento de acordo com o modelo referenciado, e o utilizará para registrar o ato de comunicação eletronicamente via diário, sem prazo para resposta.

Por fim, o movimento de código 60, conforme tabela unificada de movimentos do SGT no CNJ, com complemento código 4 e com elemento do tipo domínio de código 80, é lançado no processo associado ao documento gerado.

Essas configurações de movimento dizem respeito ao registro final no processo “Expedição de outros documentos”. No modelo de documento utilizado nessa funcionalidade, as seguintes variáveis, e apenas elas, estão disponíveis para uso (tem que sempre usar gradinha e abre e fecha chaves):
+ processoJudicial, contendo o número do processo;
+ classeJudicial; 
+ orgaoJulgador;
+ poloAtivo, contendo a lista de partes do polo ativo com seus respectivos tipos e a lista de advogados que representam partes do polo ativo com seus respectivos números de OAB;
+ poloPassivo, contendo a lista de partes do polo passivo com seus respectivos tipos e a lista de advogados que representam partes do polo passivo com seus respectivos números de OAB;
+ localSessao;
+ dataSessao;
+ horaSessao;
+ tipoSessao;
+ Estado; 
+ Municipio. 


## Adiados e pautas anteriores

A aba Adiados e pautas anteriores da Relação de julgamento apresenta processos que já estiveram em outra sessão. O sistema sinaliza isso independente de o processo já ter sido arquivado. Quando for incluído em nova pauta de julgamento, ele deixa de estar nessa aba.

A partir da versão 2.1.8.0, o processo que tiver sido adiado ou retirado de pauta e o relator desistir de levar a plenário, pode ser removido dessa aba pela atuação do gabinete do relator, que deve utilizar a transição **Retirar processo apto para julgamento.** 

Se o processo não estiver mais no gabiente, volte o processo para a tarefa de **Aguarda sessão de julgamento** (faça as tramitações necessárias para enviar o processo para o gabinete e coloque nessa tarefa por meio do elaborar decisão colegiada). Nessa tarefa, clique na opção **Retirar processo apto para julgamento** e o processo some do painel do assessor de plenário.

Depois, basta retornar o processo para a tarefa em que estava e seguir com a tramitação do feito.

Outra opção para retirada da aptidão de julgamento é a utilização da transição **Retirar da aba Adiados do Assessor de Plenário,** disponível a partir das tarefas de análise, na unidade de processamento. 
