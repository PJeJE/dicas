<img width="1676" height="727" alt="image" src="https://github.com/user-attachments/assets/60767dc4-6603-4788-899f-04b1de3e3f5a" />---
title: "Pauta de Julgamentos"
date: 2022-11-29T16:30:31-03:00
weight: 3
---

Quem monta a sessão de julgamento é o Assessor de Plenário. Esse perfil não tem órgão julgador vinculado, ele fica vinculado ao Colegiado + Secretaria Judiciária.

Após construção de documentos da sessão e liberação do processo para inclusão em pauta, o Assessor de plenário precisa criar a sessão de julgamento, que será do tipo **Contínua** ou não, dependendo da seleção feita por meio do passo **Processo liberado para julgamento sessão presencial** ou **Processo liberado para julgamento sessão virtual** realizado pelo gabinete relator do processo.

Para criar a sessão, ele deverá acessar, pelo menu **Audiências e Sessões - Cadastro de sessão de julgamento**, a tela da sessão de julgamento. Atividades de manutenção da sessão podem ser realizadas por essa tela também, como por exemplo, a alteração da data da sessão, descrita [nas instruções para alterar data da sessão](/sessaojulg/alterar_data)

Ele deve criar a sessão de julgamento com a marcação de **Contínua** ou não de acordo com sua necessidade, ou seja, contínua para virtual, não contínua para presencial, e preencher os demais campos obrigatórios. Os processos disponíveis para inclusão em pauta respeitarão essa diferença, ou seja, se o gabinete liberou para sessão presencial, o processo estará disponível para sessões não contínuas, se o gabinete liberou para sessão virtual, o processo estará disponível para sessões contínuas.

{{% notice note %}} 
As sessões de julgamento podem ser criadas antes mesmo de liberação de processos por parte do gabinete, já que o calendário de sessões do ano, via de regra, já é conhecido pelo **Assessor de plenário**.
{{% /notice %}}

Depois de criada a sessão, ele deve ir ao menu “Audiências e Sessões - Relação de julgamento”. Será apresentada uma tela com um calendário. Ele deve selecionar o dia utilizado para a sessão que ele criou e a tela da relação de julgamento abrirá.

Ele deve ir na aba “Aptos para inclusão em pauta” e selecionar os processos que comporão a pauta daquela sessão. 

Ele pode selecionar processos por outras abas também. A aba **Aptos para inclusão em mesa** exibe processos liberados pelo gabinete cujas classes não têm a marcação de **Exige inclusão em pauta** e exibe também uma consulta para que o assessor possa buscar processos que não consegue encontrar em outras abas e exibirá processos que não estejam em outra sessão em andamento e que já tenham tido eventos de conclusão registrado (código 51).

A aba **Adiados e pautas anteriores** exibe processos que já estiveram em outras pautas e ainda não foram julgados.

A aba **Pedido de vista** exibe processos que tiveram pedido de vista registrado em outras pautas e ainda não foram julgados.

Após selecionar o processo para incluir em pauta, ele deve selecionar o botão **Fechar pauta** na aba **Relação de julgamento**. Essa ação não pode ser revertida.

{{% notice note %}} 
Após incluído em uma pauta, mesmo que a pauta onde ele tenha sido incluído não tenha sido fechada, o processo não deve estar mais disponível para inclusão em outras pautas.
{{% /notice %}}


## Intimação de pauta na publicação da lista e no fechamento da pauta:

A publicação de pauta (última aba na Relação de julgamento) no diário, utiliza a pessoa Destinatário para ciência pública. A intimação não é gerada para pessoas individuais, já que aquele é um aviso geral da sessão que acontecerá. Há intimações individuais que são geradas no fechamento da pauta (primeira aba da Relação de julgamento), que dispara intimações para todas as partes do processo que possam receber intimações via sistema. Para inibir essas intimações, deve-se usar a configuração do Órgão julgador colegiado, onde há um campo indicando a intimação automática da pauta. As intimações de pauta são sempre **Sem prazo** e não haverá decurso registrado.

{{% notice warning %}}
Só serão intimadas as partes quando a inclusão em pauta se der pela aba Aptos para inclusão em Pauta ou Adiados. Inclusões em Mesa ou Pedido de Vista não geram intimações individuais. 
{{% /notice %}}

Pode-ser também realizar intimação de pauta via fluxo, por meio da tarefa **Preparar ato de comunicação**, caso o tipo da intimação esteja apropriadamente configurado no fluxo.

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
+ periodoSessao, onde o sistema trará a data da sessão no formato "DATA DA SESSÃO: [data]", para o caso de sessões não contínuas (presenciais) ou o período da sessão no formato"PERÍODO DA SESSÃO: [data] a [data]", para o caso de sessões contínuas;
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

## Lista de pautas

O usuário detentor do papel **pje:papel:pesquisaRecursoInterno** nas instalações do PJe que não sejam de primeiro grau têm acesso, por meio dos autos digitais, a aba **Recursos e sessões**. Por meio dessa aba, pode-se visualizar todos os recursos associados àquela capa e também verificar todas as sessões onde o capa foi pautada.

O sistema lista, para cada pauta onde a capa foi incluída, o nome da sessão, a situação de julgamento (**Em julgamento** ou **Aguardando julgamento** ou **Julgado** ou **Não julgado** ou **Inclusão em pauta cancelada**), a data da inclusão naquela sessão, a data de exclusão (se houver), a situação de **Adiado/Vista** (**Adiado** ou **Pedido de Vista** ou **Pauta Presencial**), caso o processo tenha sido **Não julgado**, o órgão julgador do pedido de vista, caso exista, o relator na hora em que o processo foi incluído naquela sessão e o vencedor, caso o processo tenha sido **Julgado**.

As informações sobre as pautas são úteis para que o usuário consiga identificar situações onde o usuário relata alguma inconsistência. Por exemplo, o magistrado é relator do processo, mas não consegue inserir voto de relator na sessão. Pode ter sido o caso de o relator na pauta ser diferente do relator atual. O processo foi julgado mas não tem órgão julgador vencedor, e isso ocasiona erro nas tarefas de elaboração de acórdão. 

{{% notice note %}} 
A alteração do órgão julgador relator do processo após ele ter sido pautado pode causar inconsistências na condução da sessão de julgamento e na construção de documentos de sessão.
{{% /notice %}}

Além de lista de pautas, para detentores do papel **pje:sessao:permiteVisualizarVotos**, o sistema apresentará um ícone - Ícone de visualização de votos - ao lado de cada pauta da capa processual. Ao clicar no ícone, o sistema exibirá a lista de votos já lançados vinculados àquela pauta. 

Para votos com documento associado, o sistema também apresentará um ícone que permitirá ao usuário visualizar o conteúdo do documento, mesmo quando ainda estiver em construção. Dessa forma, esse papel só deve ser liberado para administradores do sistema.
