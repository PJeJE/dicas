
---
title: "Atuação de magistrados em caso de impedimento/suspeição"
date: 2023-01-20T16:20:20-03:00
weight: 5
menuTitle: "Impedimentos e suspeições"
---
## Impedimento e suspeição por município, estado, nome de parte ou nome de advogado

Conforme §4º. art. 5º da Resolução 185 do CNJ, não é permitida exclusão automática de magistrado por impedimento/suspeição. Há, por outro lado, previsão de funcionalidade que faça indicação prévia de possível suspeição ou impedimento, que não influenciará na distribuição, cabendo ao magistrado analisar a existência, ou não, da suspeição ou do impedimento.

O cadastro prévio do impedimento ou suspeição fará com que, em determinados pontos do sistema, o usuário veja os impedimentos e possa redistribuir o processo ou excluir magistrados da composição da sessão com base na informação cadastrada. Em tarefas, a informação aparecerá mediante configuração de variável de fluxo. Na relação de julgamento e na composição de julgamento do processo, ao abrir as respectivas telas, o sistema disponibiliza um botão "Verificar impedimento/suspeição", que pesquisa, pelos magistrados presentes, se já algum impedimento de acordo com as características do processo e aponta os resultados para o servidor.

Para realizar o cadastro do impedimento/suspeição, na configuração do magistrado em Configuração - Pessoa - Magistrado, por meio da aba Impedimento/suspeição disponível para o papel "pje:papel:administrarAutuacao", o usuário poderá registrar o impedimento/suspeição previamente comunicada pelo magistrado.

Na aba mencionada, os servidores da unidade competente incluirão as regras que poderão ser relacionadas à parte, ao advogado, ao Estado, ao município ou ao ano de eleição. As regras serão executadas seguindo a ordem da sua inclusão no sistema. Sendo pela parte, deve-se indicar o CPF da parte que provoca o impedimento/suspeição e o polo ao qual está vinculada (Se em ambos os polos, o identificador deve ser "Ambos"). Sendo pelo advogado, deve-se indicar o CPF ou número da OAB do advogado que provoca o impedimento/suspeição e o polo ao qual está vinculado. Sendo pelo estado ou município, deve-se indicá-lo. Sendo pelo ano de eleição, deve-se indicar uma eleição previamente cadastrada. No campo motivo, o usuário deve descrever, em campo livre, o que determinou o impedimento/suspeição.

Quando for cadastrada regra “pelo advogado”, caso o usuário informe o número da OAB, não é necessário informar a letra. O número da OAB do advogado é formado pelo número + letra + sigla da UF, ou seja, a informação da letra não é obrigatória.
Exemplo: 
111111- A – DF
111111- DF

Após salvar a regra, o sistema poderá recuperar a informação gravada após distribuído o processo, mediante configuração em tarefa de fluxo com a variável Processo_Fluxo_visualizarImpedimentoSuspeicao, que é um "frame". Quando a tarefa contiver essa variável em sua configuração, para processos cujo magistrado relator tenha o impedimento registrado, a lista de impedimentos aparecerá. Da mesma forma, a lista de impedimentos será exibida pelo acionamento do botão "Verificar impedimento/suspeição" na composição do processo e na relação de julgamento.

## Impedimento e suspeição em autos específicos

Um magistrado pode se declarar impedido por motivo de foro íntimo, sem necessidade de declarar suas razões, nos termos do que autoriza o art. 145, §1º do NCPC:

 "§ 1º Poderá o juiz declarar-se suspeito por motivo de foro íntimo, sem necessidade de declarar suas razões."

Para auxiliar na realização do controle pela unidade de autuação e distribuição de forma a evitar redistribuição dos autos ao ministro impedido e também ajudar na atuação da Assessoria de Plenário na configuração da composição da sessão, existe a funcionalidade de registro de impedimento/suspeição em autos específicos, de forma a gerar os mesmos efeitos da anotação de impedimento por município, estado, nome de parte ou nome de advogado, mas com foco especial ao cenário de o magistrado impedido/suspeito não ser o relator do processo.

O registro de impedimento para um processo específico é feito pela aba **Impedimento/Suspeição** localizada no menu de três barras horizontais no canto superior direito dos autos digitais, onde estão todos os magistrados vinculados ao órgão julgador ativo na ZE/TRE/TSE.

Para registrar o impedimento deve-se selecionar o magistrado e vincular um documento assinado do processo. Nesse momento, o sistema pede confirmação do registro do impedimento e do documento selecionado.

Feito isto, a lista de magistrados impedidos - exibida por meio de ícone correspondente, na barra de ícones superiores do cabeçalho dos autos, ao lado do ícone de etiquetas -, é atualizada:

![Magistrados impedidos](/imagens/impedimento_1.jpg)

Importante ressaltar que os impedimentos/suspeições identificados a partir das características dos processos (município, estado, advogado, parte etc.), não atualizam esta lista.

A remoção do impedimento registrado é feito na mesma aba.

{{< tabs groupId="impedimento_suspeicao" >}}

{{% tab name="ZONAS" %}}

No PJe 1G, quando um juiz eleitoral se declara suspeito ou impedido e novo juiz é designado para o processo, além do registro de impedimento, há outras atividades que precisam ser realizadas.

Para que o juiz eleitoral substituto visualize apenas o processo para o qual foi designado, sem ter acesso a todos os outros processos da Zona Eleitoral, inclusive os sigilosos, é preciso que o processo em questão seja redistribuído para o substituto (no PJe, como regra, apenas juízes titulares recebem distribuição) e que este magistrado receba visibilidade apenas para o cargo de juiz substituto na zona em questão.

Para tanto, em **órgão julgador,** na aba **visibilidade,** deve-se configurar a visibilidade apenas para o cargo juiz substituto e, caso o processo seja sigiloso, adicioná-lo como visualizador do processo.

Note que, caso a visibilidade do juiz titular do órgão julgador permaneça como todos (que é o padrão), ele seguirá tendo acesso ao processo para o qual se declarou suspeito/impedido. Se isso for um problema, a solução a ser adotada é a alteração da visibilidade do juiz titular para apenas titular.

{{% /tab %}}

{{% tab name="TREs/TSE" %}}

No PJe 2G e 3G o voto de impedimento proferido também atualiza a lista de magistrados impedidos, sendo todos exibidos nos autos do processo.

Para atualização da lista de impedidos para os autos é fundamental realizar um dos registros de impedimento (via menu ou via voto).

Na tarefa que exibe impedimento do relator (SJD), serão considerados também esses registros para apontá-los em conjunto com os outros existentes vinculados a regras específicas pelas características do processo, conforme o caso. 

Nas telas de sessão, no local onde são exibidos os impedimentos dos magistrados do colegiado da sessão vinculados a regras específicas pelas características do processo, também serão exibidos os impedimentos por processo (botão **Verificar impedimento/suspeição**).

{{% /tab %}}
{{< /tabs >}}


{{% notice warning %}}
Informação importante para os administradores do PJe: para registrar magistrados impedidos/suspeitos nos autos de um processo é necessário ter o papel pje:papel:administrarAutuacao. A visualização também está vinculada a esse papel. 
{{% /notice %}}


