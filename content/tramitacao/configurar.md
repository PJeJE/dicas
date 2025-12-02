---
title: "Configurações de fluxo"
date: 2025-11-28T15:42:00-00:00
weight: 2
menuTitle: "Configurações de fluxo"
---

As orientações a seguir são para administradores de sistema, especialmente aqueles que estão lotados na Assessoria do PJe e na SESIP, unidades do TSE.

## Definição do fluxo e suas configurações

Antes de qualquer iniciativa de alteração/criação de fluxos no PJe, é primordial que as instruções sobre o assunto presentes na documentaçao nacional do PJe sejam lidas com bastante atenção. A seção é a [Definiçao de fluxos](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Configura%C3%A7%C3%B5es%20iniciais/#defini%C3%A7%C3%A3o-de-fluxos). Na documentação nacional também estão presentes instruções sobre o uso da interface de configuração de fluxo no PJe. A seção é está presente no [Manual de Referêcnia](https://docs.pje.jus.br/manuais-de-uso/Manual%20de%20referencia%20PJe%201.0/#fluxo). Ambas as seções precisam ser lidas completamente pelo usuário administrador de fluxos.

É importante ressaltar que os fluxos fazem uso da camada de serviços do PJe que só o desenvolvedor tem acesso por meio do código fonte. Isso significa que a alteração/criação de fluxos é uma atividade que exige especialização específica. A pessoa que mantém fluxos no PJe precisa ter conhecimento de TI, assim como conhecimento detalhado sobre o código-fonte do PJe.

Abaixo, seguem alguns comportamentos/restrições adicionais sobre configuração de fluxo.

## Fluxos compartilhados na Justiça Eleitoral

A manutenção dos fluxos na Justiça Eleitoral é realizada de forma centralizada pelo TSE. Para o sucesso dessa empreitada, os fluxos são mantidos de forma semelhante, para que alterações solicitadas sejam replicadas com menos prejuízos, compartilhando melhorias com todos os tribunais e zonas. 

## Não copie arquivos xml para desfazer alterações

A maior parte das configurações de fluxo ficam em um xml vinculado a cada fluxo. Muitas vezes, ao tentar fazer uma alteração de fluxo sem sucesso, o administrador pode querer recuperar o fluxo anterior para colocar de volta. **NUNCA** deve-se copiar o xml de um outro regional para esse fim. Algumas tarefas, dependendo do regional, têm pequenas diferenças nos nomes (Uma tarefa tem uma palavra que começa com letra maiúscula em um regional e com letra minúscula em outro regional, por exemplo). Se a cópia for realizada em fluxos diferentes, os processos que estavam em tarefas cujos nomes estavam diferentes serão perdidos e não aparecerão mais no painel de tarefas, salvo intervenção complexa no banco de dados.

O histórico dos fluxos pode ser recuperada por ferramenta de controle de configuração mantida na TI. Mesmo a recuperação de xmls antigos por meio dessa ferramenta pode ocasionar perda de processos, já que novas versões do fluxo podem ter criado tarefas, tarefas essas que podem já ter processos vinculados. Caso seja publicada uma versão do fluxo sem essas tarefas novas, os processos serão perdidos.

## Configuração de variáveis de tarefa

Para a configuração de tarefas onde o usuário precisará executar primeiramente alguma ação na área de execução da tarefas antes de tramitar, o sistema disponibiliza variáveis de tarefa. Essas variáveis são utilizadas pelo sistema para construir a interface de usuário de modo a permitir que ele execute a atividade de interesse negocial. A definição dessas variáveis é feita diretamente na interface de definição de processo, com a indicação do tipo de variável, seu nome, um descritor e características internas. Segue abaixo um exemplo de tarefa com uma lista de variáveis:

![Variáveis de tarefa](/imagens/variaveltarefa.jpg)

### Marcação de escrita das variáveis de tarefa

Para que as tarefas que contém variáveis sejam corretamente exibidas no PJe, as variáveis devem estar sempre com a marcação de **Escrita**, conforme lista de variáveis de exemplo acima.

### Variáveis do tipo **Aviso**

Um dos tipos de variável de tarefa corriqueiramente utilizados é o **Aviso**. Essa variável é utilizada quando se precisa expor um texto na área de execução de tarefas. O aviso pode ser um texto simples e fixo, quando se pretende sinalizar algo para o usuário. Por exemplo, a tarefa **Aviso de expedientes abertos** exibe o texto **Há expedientes abertos no processo. Feche todos os expedientes antes de solicitar arquivamento.**. É uma tarefa que surge quando o usuário tenta arquivar um processo a partir do **Verificar Pendências** e o sistema detecta expedientes abertos. É uma maneira que o administrador tem de sinalizar alguma coisa para o usuário por meio de uma mensagem. 

Ao se configurar textos que serão exibidos para o usuário, o administrador utilizar o campo **Label** da variável **Aviso**. Via de regra, ao alterar esse campo **Label** e salvar o fluxo, o sistema exibe uma mensagem **Não houve alteração de fluxo**. Se tentar publicar o fluxo, o sistema exibe a mesma mensagem. Nesse caso, faça uma pequena alteração (adicione/remova uma letra ou um ponto) no campo **Descrição** da aba **Propriedades** e acione o **Salvar** novamente para que a publicação seja realizada com sucesso. 

### Movimentar em lote

A variável de tarefa do tipo **Lote - Habilitar Movimentação** permite ao usuário que executa a tarefa selecione uma lista de processos na mesma tarefa e os tramite para a próxima tarefa todos de uma só vez. É bem útil quando se deseja tramitar vários processos para a mesmo destino. 

É importante ressaltar que o sistema realizará apenas a tramitação. Se houver alguma ação a ser feita na área de execução da tarefa, nada será feito. 

Por exemplo, vamos analisar a tarefa **Verificar e Certificar dados do processo**, que contém, entre outras entradas de dados, um campo para o usuário informaar a **Causa de pedir**. Caso seja configurada a movimentação em lote e o usuário selecionar um lote de 5 processos para tramitar para a próxima tarefa selecionando a transição **Prosseguir sem certidão**, a informação da **Causa de pedir** não será informada para os processos. Ainda que o usuário a informe para o primeiro processo da lista, os outros processos que não têm essa informação continuarão sem ela.

Da mesma forma, caso o movimentar em lote seja configurado em uma tarefa que contém editor de texto, o texto não será incluído na tramitação. 

Para a execução de tarefas específicas em lote, o PJe tem algumas possibilidades. Mas nem todas as tarefas podem ser executadas em lote. O que pode ocorrer sempre é apenas a sua tramitação, ou seja, a mudança do processo de uma tarefa para outra. 

Abaixo segue a lista de possibilidades de lote disponíveis para a Justiça Eleitoral:

+ Lote - Habilitar Movimentação (opção descrita acima)
+ Lote - Habilitar Minutar
+ Lote - Habilitar Assinatura
+ Lote - Habilitar Intimação
+ Lote - Habilitar Redistribuição
+ Lote - Habilitar Lançar Movimentações
+ Lote - Habilitar Lançar Data de Trânsito

<!--
comunicarAtoLote=Lote - Habilitar Comunicação
designarAudienciaLote=Lote - Habilitar Designar Audiência
designarPericiaLote=Lote - Habilitar Designar Perícia
assinarInteiroTeorLote=Lote - Habilitar Assinatura Inteiro Teor
-->

## Variáveis de fluxo

É importante, na definição de fluxo, que o usuário administrador possa sinalizar diferentes comportamentos de acordo as necessidades de cada setor. Por exemplo, uma tarefa que contém editor de texto, ao ser exibida para um servidor da **Secretaria Judiciária**, deve exibir como tipos de documentos possíveis para utilização apenas documentos construídos e assinados no escopo da secretaria. Esse mesmo tipo de tarefa é utilizada no escopo do órgão julgador específico para construção de decisões terminativas, o que exige disponibilização de outro tipo de documento. O mecanismo utilizada para essa variação na configuração são as variáveis de fluxo. Esse tipo de variável permite que o usuário administrador sinalize informações para o PJe ou para o próprio fluxo. No exemplo citado, ou seja, em tarefas que contém editores de texto, algumas variáveis de fluxo são utilizadas para definir que tipos de documentos aparecem para seleção no editor e que modelos de documento estão disponíveis. Já outras variáveis podem ser utilizadas para sinalizar alguma ação futura, como quando a **Secretaria Judiciária** envia o processo para execução de um gabinete diverso do relator do processo. Nesse caso, a configuração do fluxo deve sinalizar para tarefas futuras que o processo deverá estar em um outro órgão julgador. 

As variáveis de fluxo são configuradas por meio de **Eventos**. Dessa forma, a sinalização que ocorre por causa dessas variáveis tem um momento correto para ocorrer de acordo com o evento selecionado. 

### Definições sobre eventos

Os eventos são utilizados para se agregar ações vinculadas a nós/tarefas específicas. As ações conterão expressões de acordo com a necessidade do usuário configurador. Por exemplo, pode-se utilizar as ações para gravar valores em variáveis de fluxo, ou recuperar valores de variáveis gravadas anteriormente. Pode-se também utilizar as ações para "falar" diretamente com o PJe, ou seja, utilizando sua camada de serviços para executar comandos específicos. O lançamento automático de movimentos é um exemplo clássico. Ao realizar a remessa de um processo, seja entre instâncias, ou para setores diferentes, via de regra é uma ação em um evento configurado no fluxo que faz o lançamento do movimento **Remetidos os autos** com seus devidos complementos. 

Cada tipo de evento disponível para configuração tem um significado em termos de momento de execução. Abaixo seguem definições sobre os tipos de eventos e seus momentos de execução:

Os tipos de eventos são executados a partir das seguintes situações:
Situação I: Quando um processo tramita e chega pela primeira vez em um nó de tarefa, são executadas as ações dos seguintes eventos de fluxo:
1. Entrar no nó
2. Criar tarefa
3. Atribuir tarefa (a tarefa é criada e se atribui à tarefa o usuário NULL)

Situação II: Quando o frame da tarefa é aberto pela primeira vez:
1. Iniciar tarefa
2. Atribuir tarefa (a tarefa é atribuída ao usuário logado) - este evento é reexecutado toda vez que o frame for aberto

Situação III: O usuário que possui permissão na tarefa, reabre a tarefa ou outra pessoa abre a tarefa:
1. Atribuir tarefa

Situação IV: O usuário encaminha o processo para a próxima tarefa, saindo da atual:
> Para a tarefa atual:
1. Finalizar Tarefa
2. Atribuir tarefa
3. Antes de sinalizar
4. Sair do nó
5. Depois de sinalizar

> Para a próxima tarefa: (repetem-se os passos a partir da Situação I)
1. Entrar no nó
2. Criar tarefa
3. Atribuir tarefa (a tarefa é criada e se atribui à tarefa o usuário NULL)

    Tipo de evento "Atribuir tarefa" é um tipo de evento que é sempre reexecutado quando o usuário abre o frame da tarefa, desta forma, deve-se tomar cuidado com esse tipo de evento e evitar indicar ações que não deveriam ser executadas múltiplas vezes para um mesmo processo. Não utilize esse evento para lançar movimentos por exemplo.

    Marcação "Reexecutar após republicar fluxo": utilizável apenas em nós de tarefa e aplicável para os tipos de evento "Entrar no nó", "Criar tarefa" e "Iniciar tarefa". Essa marcação fará com que após uma publicação de fluxo, na próxima vez que um usuário abrir o frame de tarefa as ações reexecutáveis desses eventos sejam novamente executadas para o processo específico. Isso permite que novas ações ou alterações em ações pré-existentes naquela tarefa sejam novamente executadas na abertura da tarefa, o que não aconteceria no ciclo de vida normal da tarefa no sistema. Evite indicar ações que não deveriam ser executadas múltiplas vezes para um mesmo processo com essa marcação, não utilize essa marcação para lançar movimentos por exemplo.

Para outros tipos de nó diferentes de nó de tarefa: (Nó inicial, nó de sistema, nó de decisão, nó final, nó de separação, nó de junção, nó de sub-processo), o sistema só executa dois tipos de eventos (não há possibilidade de se marcar ações desses nós como "reexecutáveis", visto que nenhum processo permanece durante a alteração do fluxo em um nó que não seja nó de tarefa):
1. Entrar no nó
2. Sair do nó

Por fim, segue a ordem geral de execução dos eventos de tarefa:
1. Entrar no nó
2. Criar tarefa
3. Atribuir tarefa (a tarefa é criada e se atribui à tarefa o usuário NULL)
4. Iniciar tarefa
5. Atribuir tarefa (a tarefa é atribuída ao usuário logado)
**Se o fluxo for republicado e houver ações marcadas como reexecutáveis, os eventos: Entrar no nó, Criar tarefa e Iniciar tarefa serão novamente executados.
6. Atribuir tarefa - este evento é reexecutado toda vez que o frame da tarefa for aberto
7. Finalizar Tarefa
8. Atribuir tarefa
9. Antes de sinalizar
10. Sair do nó
11. Depois de sinalizar



### Configuração de lançamento de movimentos

O registro de movimentações manual no PJe pode ocorrer através do uso do lançador de movimentações em tarefas, configurado através do fluxo. 

Na Justiça Eleitoral, essa configuração está presente na primeiro grau, nos TREs e no TSE. Os movimentos lançados em tarefas como essas são movimentos de **Magistrado** conforme definição do [Sistema de Gestão de Tabelas Processuais Unificadas](https://www.cnj.jus.br/sgt/consulta_publica_movimentos.php).

Para que as tarefas que permitem a seleção manual do movimento funcionem corretamente, é preciso uma configuração especial. A expressão **#{lancadorMovimentosService.setCondicaoLancamentoMovimentosTemporarioNoFluxo('#{false}')}** deve ser configurada em uma ação no evento **Iniciar tarefa**.

Além disso, há uma seção especial na configuração do fluxo que atualmente é utilizada apenas para a configuração de tarefas de lançamento manual de movimentos, que são os **Eventos de Tarefa**.

![Eventos de tarefa](/imagens/eventostarefa.jpg)

Deve-se selecionar o **Tipo do Evento** **Sair Tarefa** e selecionar a opção **INCLUIR**. Após incluído o evento, deve aparecer a aba **AGRUPAMENTO EVENTOS**. Caso não aparecã, na lista de eventos cadastrados disponíveis na aba **PESQUISA**, o usuário deve selecionar o ícone do lápis. 

![Agrupamento Eventos](/imagens/agrupamentoeventos.jpg)

Nas opções disponíveis, o usuário deve selecionar **Magistrado**. No campo **Condição para lançamento temporário*** deve estar preenchida a expressão **#{false}**. O usuário deve selecionar a opção **SALVAR**.

Ao utilizar o lançador de movimentos disponível na tarefa, o sistema tem algumas outras restrições conforme regras na documentação nacional: [RN138](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn138) [RN345](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn342) 


<!--

**Processo com prazo em curso** é um exemplo clássico de tarefa que é tramitada por gatilho. O gatilho, no caso, é a expiração do prazo ou a resposta dos expedientes. Mais detalhes sobre esse funcionamento estão na seção [Controle de prazos](/prazos/tarefas).

-->
