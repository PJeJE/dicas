---
title: "Configurações de fluxo"
date: 2025-11-28T15:42:00-00:00
weight: 2
menuTitle: "Configurações de fluxo"
---

As orientações a seguir são para administradores de sistema, especialmente aqueles que estão lotados na Assessoria do PJe e na SESIP, unidades do TSE.

## Definição do fluxo e suas configurações

Antes de qualquer iniciativa de alteração/criação de fluxos no PJe, é primordial que as instruções sobre o assunto presentes na documentaçao nacional do PJe sejam lidas com bastante atenção. A seção é a [Definiçao de fluxos](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Configura%C3%A7%C3%B5es%20iniciais/#defini%C3%A7%C3%A3o-de-fluxos).

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


<!--

**Processo com prazo em curso** é um exemplo clássico de tarefa que é tramitada por gatilho. O gatilho, no caso, é a expiração do prazo ou a resposta dos expedientes. Mais detalhes sobre esse funcionamento estão na seção [Controle de prazos](/prazos/tarefas).

-->
