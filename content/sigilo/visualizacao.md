---
title: "Visualização de processos sigilosos"
date: 2022-01-15T10:32:00-03:00
weight: 3
---

## Regras gerais

No protocolo inicial do processo, de acordo com a classe e os assuntos cadastrados, o sistema utilizará os níveis de sigilo para estabelecer os visualizadores do processo.

É importante ressaltar a diferença entre servidores/magistrados e partes do processo/usuários externos:

+ Para servidores/magistrados, a visualização é determinada pelo nível de sigilo do processo. Se o servidor/magistrado não tiver permissão para visualizar pelo nível do processo, terá que ser incluído como visualizador.
+ Para partes do processo/usuários externos, a visualização sempre se dará de acordo com o cadastro na lista de visualizadores.

Deste modo, o servidor somente consegue enxergar nas tarefas os processos cujos níveis de sigilo são compatíveis com seu respectivo nível de acesso ou aqueles em que seja cadastrado como visualizador. Além disso, para fins de abertura dos autos digitais, o usuário precisará ser visualizador do processo ou:
+ ter o mesmo nível do processo ou maior; e
+ ser do mesmo órgão julgador do processo ou, caso não tenha órgão julgador,
+ ser do mesmo órgão julgador colegiado; e
+ se estiver vinculado a um cargo (magistrados são sempre vinculados ao cargo), deve ser o cargo responsável pelo processo ou ter a visibilidade “Todos” no cadastro do órgão julgador.

{{% notice warning %}}
Cuidado! Partes posteriormente incluídas no processo tem a visualização liberada automaticamente.
{{% /notice %}}

No ato de comunicação a parte citada/intimada é automaticamente adicionada como visualizadora.

A alteração do nível de sigilo não modifica as permissões de visualização já concedidas no processo. 

A marcação de uma parte como sigilosa faz com que essa parte não fique mais visível pelo polo contrário, mas não a impede de visualizar o processo sigiloso.

## Regra das procuradorias

Ao cadastrar uma procuradoria como visualizadora do processo sigiloso, os participantes dessa procuradoria estarão aptos a visualizarem o processo, salvo se detiverem o papel pje:papel:administrarProcuradorias.

Esse papel existe para que procuradorias possam atribuir a servidores a função administrativa de cadastrar novos procuradores e novos assistentes de procuradoria, com a restrição de não visualizarem processos. Dessa forma, o papel de procurador ou de procurador gestor não pode conter em sua hierarquia o papel de administrador de procuradoria, sob pena de não visualizarem os processos sigilosos aos quais a procuradoria tem acesso.

A visualização dos procuradores depende do correto cadatramento da porcuradoria como visualizador do processo. Observe a imagem abaixo:

![Visualização Procuradorias](/imagens/visualizacao_procuradorias.jpg)

IMG_VISUALIZACAO_PROCURADORIAS

No destaque em amarelo (número 1) o cadastramento está correto e todos os usuários da procuradoria, respeitadas as regras de visualização dentro das caixas, terão acesso aos autos. 

Já no exemplo em azul (número 2), está incorreto. Apenas quando o símbolo de procuradoria aparece ao lado do nome é que os usuários vão ver o processo.

Caso precise ajustar os visualizadores, clique em **Opções** e escolha a opção **Liberar Vizualização para todas as partes.** Dessa forma as procuradorias serão cadastradas de maneira correta. Após isso, se for necessário, exclua visualizadores que não deveriam ter sido incluídos. 

## Como atribuir visualizadores

Na tarefa em que o magistrado indica qual servidor poderá visualizar o processo, ele também pode, a qualquer tempo, atribuir visualização para o polo passivo e/ou outra parte que tenha ingressado posteriormente na relação jurídica processual (terceiros interessados, por exemplo).

Para isso, o magistrado deverá entrar no processo, nos **Autos digitais – Segredo ou sigilo – Opções – Acrescentar visualizador – Autorizar pessoa a visualizar processo,** basta digitar nome ou CPF e clicar em concluído.

Regras importantes:
+ A atribuição de visualizador é apenas por processo e a indicação uma por vez;
+ É possível atribuir a visualização a mais de uma pessoa;
  
## Como não expor nomes de parte em processos sigilosos

Para que o nome da parte de processos sigilosos não seja exposto em movimentos que utilizam esse complemento, há uma configuração que deve ser feita.

Como administrador, pesquise pela opção **Tipo de complemento (Configurações –  Tabelas Judiciais – Movimentações –  Complementos – Tipos).** A tela de configuração dos tipos de complementos será exibida, pesquise, no campo Nome, por nome_da_parte. 

Clique no ícone de edição (lápis) e verifique como está o campo Expressão de busca.

O valor correto é #{processoParteUtils.obterPartesProcesso(tramitacaoProcessualService.recuperaProcesso())}.
+ Para retirar a visualização, basta clicar na lixeira.

+ O usuário que peticiona não escolhe o nível de segredo do processo, isso é configurado pelo administrador do sistema, no tópico [Como atribuir níveis de sigilo aos processos]({{< relref "niveis" >}}). 

