---
title: "Dias úteis"
date: 2025-03-18T15:19:03-03:00
---

A configuração de competência tem um atributo importante para contagem de prazos que é o **Categoria de prazo processual**. 

Para atendimento de contagem de prazos de **Cumprimento de sentença**, que deve ser feito em dias úteis, cadastramos uma nova competência com essa característica, ou seja **Categoria de prazo processual** marcada como **Dias úteis**. O nome atribuído à competência, inicialmente, foi **Geral eleitoral - Dias Úteis**, mas o usuário administrador pode alterá-lo de acordo com suas conveniências. O procedimento na Justiça Eleitoral para **Cumprimento de sentença** foi estabelecido por meio da utilização da tarefa de **Evoluir classe processual**. Para o atendimento do requisito, ou seja, a vinculação do processo na competência de contagem de prazo em dias úteis, foi criado um **Agrupamento de classes ou assuntos** de nome **Classes para contagem de prazo em dias úteis** e código **DUT**. O agrupamento foi vinculado à classe **CUMPRIMENTO DE SENTENÇA (156)**. Não houve assuntos vinculados. Dessa forma, todas as vezes que o usuário escolher **Evoluir classe processual** e selecionar a classe **CUMPRIMENTO DE SENTENÇA (156)**, ao final da realização da tarefa, o sistema vinculará automaticamente o processo à competência de dias úteis. Essa alteração foi uma melhoria realizada por meio de alterações no fluxo do processo.

A despeito de ter sido criada para atendimento da contagem de prazos de **Cumprimento de sentença**, a competência pode ser utilizada para outros casos de acordo com necessidades do usuário admininstrador.

As classes e assuntos que estiverem cadastrados nessa competência com datas válidas farão com que novos processos protocolados com essas classes e assuntos sejam encaminhados para essa competência, respeitando as outras características do processo que influenciam em competências, conforme instruções em https://docs.pje.jus.br/manuais-de-uso/Manual%20de%20referencia%20PJe%201.0/#compet%C3%AAncia. Caso haja mais de uma competência com mesma classe e assunto, o sistema apresentará a possibilidade de escolha por parte do usuário protocolador.


{{% notice note %}}
Não há mudança de pesos nem de órgão julgador quando se usa evolução de classe, mesmo que a competência tenha sido alterada.
{{% /notice %}}
