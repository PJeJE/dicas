---
title: "Configuração"
date: 2022-11-29T16:19:03-03:00
---

No menu **Configuração - Tabelas Judiciais - Classe Judicial** é possível configurar as classes, para que o PJe funcione de maneira adequada.

Para que uma determinada classe "exista" no PJe ela precisa estar ativa e ter um fluxo associado (E). Observe, na imagem abaixo, a tela de configuração da classe, aba **Formulário** (A):

![configuracao_classe_formulario](/imagens/configuracao_classe_formulario.jpg)


B - **Natureza:** campo de textual para registro de diferenciação entre classes.

C - **Classe superior:** indica a classe hierarquicamente superior da classe selecionada, com base na TPU/CNJ.

D - **Tipo de Documento Inicial:** indica o tipo de documento exigido para a classe.

E - **Fluxo:** especifica o fluxo ao qual estarão associados os processos que utilizam a classe. 

1 - **Inicial:** - determina se a classe pode ser utilizada para cadastro de novos processos (tanto para usuários internos quanto externos).

2 - **Incidental:** determina se a classe pode ser utilizada para o cadastro do processos incidentais.

3 - **Exige polo passivo:** determina se a presença de partes no polo passivo é obrigatória.

4 - **Ignorar prevenção:** determina se processos associados a classes com essa marcação não deverão ser preventos com outros processos. De acordo com a documentação do CNJ, atualmente, essa configuração não está em uso no sistema.

5 - **Possui custas** de acordo com a documentação do CNJ, caso esteja configurada, essa opção habilita um link, na página de cadastro de processos, para uma outra página, onde poderão ser calculadas as custas do processo. O endereço para a página de cálculo de custas é definido pelo órgão, por meio do parâmetro “calcularCustasUrl”. Considerando que, na Justiça Eleitoral não existem custas, a opção deve estar sempre desmarcada e tal parâmetro não deve ser configurado.

6 - **Exige inclusão em pauta:** determina a exigibilidade de inclusão em pauta de processos associados à classe. Quando marcada, tais processos não poderão ser julgados sem terem sido previamente pautados.

7 - **Ativo:** indica a possibilidade de utilização dessa classe no sistema, desde que haja um fluxo associado (E) e tenha sido feita a configuração de Classe x Assunto dentro da competência.

8 - **Processo referência:** configuração utilizada para exigir, facultar ou suprimir o número de processo de referência durante o cadastro de processos.

9 - **Aplicável a sessões contínuas:** determina que os processos da classe podem ser incluído em sessoes continuas (virtuais).

10 - **Recursal:** - determina se a visibilidade da classe será restrita aos usuários internos, quando desmarcada, possibilita também o peticionamento por usuários externos.

11 - **Complementar:** de acordo com a documentação do CNJ, atualmente essa configuração não está sendo utilizada pelo sistema.

12 - **Exige ente ou autoridade:** define se é obrigatória a presença de autoridades ou entes como parte do processo. Quando marcada a opção, no cadastro de partes do protocolo do processo, o usuário distribuidor deverá selecionar uma autoridade ou ente conforme regra RN357 ou cadastrar um(a) novo(a). Para processos dessa classe, o protocolo não será permitido se não houver pelo menos uma autoridade ou ente.

13 - **Exigir documento de identificação:** a marcação desse campo impede a possibilidade, em regra disponível para usuários internos, de autuar processos mesmo quando não existem documentos de identificação das partes. 

14 - **Exige Revisor:** determina se a classe exige a atuação de revisor. Quando marcado sim, no momento da distribuição, o processo receberá um revisor (conforme configuração estabelecida no Orgão Julgador Colegiado). Se marcado facultativo, após a distribuição do processo, será necessário utilizar a transição Atribuir Revisor. Havendo revisor no processo, este não poderá ir à julgamento sem passar pela revisão.

15 - **Exige numeração própria:** define se processos vinculados à classe sempre receberão número próprio na remessa entre instâncias. O correto é deixar a opção desmarcarda, para que a numeração originária do processo seja utilizada. ATENÇÃO: essa opção não pode estar marcada pois, nas remessas, fará com que os processos recebam novo número, em desacordo com a Resolução CNJ n. 69, que trata da Numeração Única.

16 - **Exige Fiscal da Lei:** quando marcado, coloca o Ministério Público como Fiscal da Lei no campo Outros Interessados.

17 - **Habilitar máscara:** quando marcado sim, este campo serve para que, sendo indicado o processo de referência (opção do campo 8), ao digitar o número do processo referência, o sistema coloque uma máscara, exibindo pontos e traços no lugar certo, para facilitar a digitação.

18 - **Designar audiência em fluxo:** campo utilizado para designação automática de audiências, indicativo do tipo de audiência cadastrado que deverá ser utilizado para marcação automatizada.

19 - **Remessa entre instâncias?:** quando marcado, esse campo permite que a classe fique disponível na remessa. Ou seja, outras instâncias vão poder remeter processos para a instância atual na classe que está sendo configurada.

20 - **Permite jus postulandi:** define se a classe estará disponível para peticionamento por pessoas sem representação de advogado.

21 - **Sigilosa:** determina se a classe judicial é sigilosa. Nesses casos, processos associados a classes com essa configuração, são tratados como sigilosos

22 - **Realiza compensação:** marca indicativa de que o processo dessa classe deve provocar compensação. De acordo com a documentação do CNJ, essa configuração não está em uso no sistema.

23 - **Composição de Julgamento:** permite definir a composição de julgamento, como sendo Integral, Reduzido ou Facultativo.

24 - **Permite numeração manual:** possibilita a criação de um novo processo com a numeração informada manualmente pelo usuário cadastrador. Tal usuário precisa herdar um papel específico para que essa opção possa ser utilizada. Como seu uso não é autorizado na Justiça Eleitoral, pois temos uma ferramenta própria para migração de processos, o papel necessário não está habilitado.

25 - **Público:** essa marcação faz com que, na consulta pública, haja livre acesso aos documentos não sigilosos, não obstante a marcação de publicidade atribuída aos tipos de documentos individualmente. IMPORTANTE: considerando que a Justiça Eleitoral adota uma ferramenta própria de consulta pública (a Consulta Pública Unificada), essa regra da configuração de classe não se aplica aos processos eleitorais. 


{{% notice note %}}
A ordenação na exibição da lista de classes para protocolo de processos obedece a ordem alfabética dos nomes das classes, desde que as classes estejam gravadas no banco de dados em caixa alta. O PJe sempre grava em caixa alta, mas algumas vezes, a classe pode ter sido inserida via script de banco de dados e o script pode não ter inserido em caixa alta. Caso tenha problema na ordenação das classes no protocolo de processos, salve novamente a classe que não está ordenada por meio de seu formulário de cadastro. Essa gravação fará com que o nome fique corretamente grafado no banco de dados e corrigirá o problema na ordenação.
{{% /notice %}}
