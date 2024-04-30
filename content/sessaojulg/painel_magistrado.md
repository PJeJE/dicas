---
title: "Painel do magistrado"
date: 2022-11-29T16:30:45-03:00
weight: 2
---

## Orientações gerais sobre o painel do Magistrado na Sessão

No menu principal do PJe (ícone com três barrinhas horizontais no canto superior esquerdo), deve-se clicar na opção **Painel - Painel do magistrado na sessão.**

A tela inicial exibirá um calendário com todas as sessões do órgão julgador colegiado do magistrado, agrupadas por dia.

Os dias em que houver sessão(ões) já criadas estarão disponíveis para serem selecionados. Ao selecionar, a tela do painel do magistrado será apresentada. 

O painel exibe inicialmente os dados da sessão, se há ou não processos apregoados, se a sessão é contínua ou não, um formulário de pesquisa de processos e os processos da sessão.

Para cada processo, são apresentados os dados básicos, a possibilidade de abertura dos autos (resguardadas as regras de processos em segredo de justiça), a ordem dele na pauta e, a partir da seleção do processo, é exibido o placar contendo os votos já proferidos e as opções de voto.

Após selecionar a opção de voto, o sistema disponibiliza a opção **Redigir voto,** que apresentará o editor de texto permitindo inserir voto escrito.

Além das opções de voto, também estão disponíveis **Enviar para pauta presencial, Registrar pedido de vista** e **Registrar impedimento ou suspeição.** Com exceção da última, estas opções, após acionadas, só poderão ser desfeitas com auxílio do Assessor de plenário, que deverá colocar o processo em julgamento novamente, se precisar desfazê-las.

É válido ressaltar que, após o registro de um pedido de vista, os outros gabinetes não têm mais disponíveis as opções para retirada de julgamento ou envio para a pauta presencial. Caso a vista tenha sido lançada de forma equivocada, o Assessor de plenário deverá atuar colocando o processo em julgamento novamente.

{{% notice warning %}}
Para poder utilizar o Painel do Magistrado na Sessão antes de iniciar a sessão de julgamento, o parâmetro pje:sessao:habilitarAcoesEmVotacaoAntecipada precisa estar ativo.
{{% /notice %}}

## Visualização de Documentos da Sessão

No PJe da Justiça Eleitoral, relatório, voto e ementa, são construídos na tarefa **Minutar relatório, voto e ementa** pelo relator do processo.

Se o usuário autenticado estiver em um órgão julgador diferente do órgão julgador do relator do processo, é gerada uma inconsistência só resolvida via banco de dados.

Por voto, entenda-se que é o conjunto da indicação do voto e o próprio documento de voto. A visualização desses itens/documentos não assinados só é possível se as respectivas marcações **Liberar voto, Liberar relatório** e **Liberar ementa forem realizadas.**

Os pontos do sistema onde poderão ser visualizadas são:

+ Painel do secretário da sessão; 
+ Painel do magistrado na sessão; 
+ Painel do membro da OAB na sessão; 
+ Painel do membro do ministério público na sessão; 
+ Púlpito de sustentação oral;
+ Internet - opção Pautas de julgamento (http://www.tse.jus.br/servicosjudiciais/sessoes-de-julgamento/pautas-de-julgamento/pje); 
+ Tarefas de vogais. 

Depois que inicia a sessão, quando o Assessor de plenário colocar em julgamento, vai aparecer na Internet, sem necessidade de usuário e senha, o tipo de voto (concedo, nego, etc.) mas não aparece o documento do voto. Na Internet, sem login e senha, só aparece o documento depois de assinado. 

Já no painel do membro da OAB, basta iniciar a sessão, o documento já aparece. Em todos os casos, é sempre necessária liberação por meio da tarefa do gabinete
