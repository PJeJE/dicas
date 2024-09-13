---
title: "Selecionar documentos para acórdão"
date: 2024-09-12T14:39:20-03:00
weight: 6
menuTitle: "Selecionar documentos para acórdão"
---

Na justiça eleitoral, os processos, após julgamento em sessão, são encaminhadaos para tarefas de elaboração de acórdão. Muitas vezes o processo vai a julgamento novamente sem ter tido o acórdão anterior assinado. O usuário precisa poder selecionar para qual sessão será construído o acórdão. Além disso, existem situações em que foram construídos vários documentos de relatório, voto ou ementa, e o usuário precisa definir quais serão utilizados para construção daquele acórdão. Para esse fim, temos a tarefa **Selecionar documentos para acórdão**. 

A referida tarefa permite também que se façam ajustes nos documentos de sessão relacionados à vinculação desses documentos a uma sessão ou à vinculação dos documentos a órgãos julgadores.

{{% notice note %}} 
As alterações permitidas por meio da tarefa **Selecionar documentos para acórdão** podem deixar os documentos de sessão inconsistentes e afetarem a execução de outras tarefas relacionadas a documentos de sessão. Dessa forma, antes de utilizar a tarefa, tenha certeza sobre quais campos precisam estar preenchidos para cada documento ajustado.
{{% /notice %}}

## Utilização da tarefa

A tarefa **Selecionar documentos para acórdão** é apresentada no início do fluxo de elaboração do acórdão. O fluxo é iniciado automaticamente após o encerramento do julgamento do processo ou quando o usuário seleciona a opção **iniciar novo fluxo de acórdão.**

A tarefa exibe todas as pautas onde o processo tem registro e os documentos do tipo relatório, ementa e voto vinculados ao processo. 

{{% notice note %}} 
Os votos não vinculados a documentos não são exibidos.
{{% /notice %}}

Essas informações encontram-se em abas separadas, assim o usuário pode selecionar quais desses documentos serão o relatório, a ementa, o voto do relator, o voto do vencedor e os votos de vogais do acórdão a ser montado, bem como para qual pauta será produzido o acórdão.

As abas **Ementa, Relatório, Voto Relator, Voto Vencedor** e **Acórdão** permitem a seleção de apenas uma opção de documento, mas a seleção não é obrigatória. Isso porque um processo julgador só pode conter um desses documentos. A aba de votos vogais permite a seleção de mais de um documento

Se não houver seleção para uma determinada aba, ao enviar o processo para elaboração do acórdão, a aba correspondente não terá documento previamente construído. Essa seleção refletirá na elaboração do acórdão desde que, após selecionadas todas as opções conjuntamente, o usuário utilize o botão **Salvar seleção.**. Um alerta avisará quais abas não tiveram documentos selecionados. É só um alerta. Ao serem carregadas abas com documentos em branco na tarefa de elaboração do acórdão, o usuário pode construir um documento novo, de acordo com as permissões já existentes na elaboração de acórdão para seu perfil. 

A aba que exibe as pautas contém as seguintes informações:


1.   O nome do órgão julgador que pautou o processo; 

2.   A sessão junto com o voto vencedor

3.   A situação de julgamento do processo ao final da sessão 

4.   A proclamação de julgamento do processo naquela sessão

5.   O momento de inclusão na pauta.

As abas de documentos são bem parecidas e apresentam as seguintes informações:

1.  Identificador do documento: esse número é o mesmo número pelo qual o documento pode ser visto, caso o usuário tenha permissão, na lista de documentos dos autos;
  
2.  O nome do usuário que incluiu o documento e o setor de inclusão do documento;
  
3.  Localização: as lotações que o usuário que incluiu o documento tinha no momento da inclusão;
 
4.  Sessão/Órgão julgador: a sessão à qual o documento está vinculado e o órgão julgador vinculado ao documento;
  
5.  Um ícone de visualização do documento;
  
6.  Um ícone para sinalizar que o documento já foi assinado, quando for o caso (cadeado fechado);
  
7.  Um ícone para permitir ajustar órgão julgador do documento (lápis);
  
8.  Um ícone para permitir desvincular órgão e sessão do documento (lixeira).
 
9.  Nas abas de voto é exibida indicação do voto. Por exemplo, "Nego provimento".
    
10. Na aba de acórdão, é exibida a lista de documentos vinculados a cada acórdão e um ícone de lixeira ao lado de cada documento que permite desvincular àquele documento do acórdão relacionado.  


{{% notice note %}} 
Ao utilizar o ícone da lixeira, os documentos são desvinculados do órgão julgador e da sessão. É útil quando se deseja desvincular um documento de uma sessão, mas não esqueça de vincular sempre a um órgão julgador. 
{{% /notice %}}

Caso não seja selecionado um acórdão na aba correspondente, o sistema criará um documento de acórdão em branco e o utilizará na tarefa seguinte. Ao selecionar documentos em outros abas, selecionar um acórdão na aba de sessão e selecionar **Salvar seleção**, o sistema vincula os documentos das outras abas ao acórdão selecionado.

Ao selecionar "Sim" para o **Salvar seleção**, o sistema exibirá uma mensagem notificando as divergências relacionadas à seleção. 

As possíveis divergências serão notificadas ao usuário quando:

•	O voto do relator não for do gabinete que pautou o processo;

•	O relatório não for do gabinete que pautou o processo;

•	O voto do vencedor não for do gabinete vencedor do julgamento;

•	Os votos de vogais estiverem vinculados ao gabinete que pautou o processo;

•	A ementa não for do gabinete vencedor do julgamento;

•	O acórdão não for do gabinete vencedor do julgamento;

•	Os documentos não estiverem vinculados à sessão ou estiverem vinculados à sessão distinta da sessão selecionada.

O usuário poderá selecionar "Cancelar" para desistir da seleção. Pode selecionar "Prosseguir sem ajustar informações", ou seja, as divergências informadas serão mantidas e o sistema não alterará os documentos existentes para saná-las. Em alguns casos, isso fará com que os documentos selecionados possam não ser devidamente carregados na tarefa seguinte, mas é necessário que o aviso exista para que o usuário possa apenas sinalizar que aqueles documentos serão carregados nas tarefas de acórdão, mas não serão vinculados à sessão selecionada. Ao selecionar "Prosseguir ajustando informações", o sistema vinculará todos os documentos à sessão selecionada.

As  atualizações  realizadas  podem   não  estar  disponíveis  de  imediato  nas  abas.  Atualize a  página para poder verificar, caso tenha solicitado "Prosseguir ajustando informações".

O  usuário  poderá  selecionar, pelos três pontinhos da tarefa, prosseguir por meio do "Elaborar acórdão ou resolução" ou "Iniciar novo fluxo de acórdão", caso tenha mais de
um acórdão para construir.


## Informações técnicas sobre a configuração de parâmetros

+ As abas de votos (voto relator, voto vencedor e votos vogais) exibirão sempre o mesmo conteúdo, ou seja, todos os documentos construídos na instância atual e não excluídos, cujos tipos sejam os configurados nos parâmetros: idTipoProcessoDocumentoVoto, pje:painel:magistrado:sessao:tiposVotoVogal:ids e pje:flx:votacaoVogal:tiposVoto:ids.
+ A aba de ementa trará todos os documentos do tipo, configurado no parâmetro: idTipoProcessoDocumentoEmenta.
+ A aba relatório trará todos os documentos do tipo, configurado no parâmetro: idTipoProcessoDocumentoRelatorio.
+ A aba acórdão trará todos os documentos do tipo, configurado no parâmetro: idTipoProcessoDocumentoAcordao.
