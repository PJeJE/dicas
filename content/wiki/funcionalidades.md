---
title: "Lista de funcionalidades"
date: 2026-04-24T15:00:45-03:00
weight: 1
menuTitle: "Lista de Funcionalidades"
---


> ⚠️ **Atenção!** Este site esteve disponível até 19/12/2024 por meio da Wiki do PJe. O conteúdo está sendo migrado para o sítio atual integralmente - EM MANUTENÇÂO.

---

Descreveremos as funcionalidades do PJe a partir da estrutura de menus existente, que consiste nos seguintes: **Home**, **Painel**, **Processo**, **Atividades**, **Audiências e sessões** e **Configuração**


No menu **Processo**, estão as funcionalidades mais utilizadas quanto a processos (novo protocolo, reaproveitamento de rascunhos de processos, ações de solicitar habilitação, envio de processo a instância superior etc.)

No menu **Atividades**, as atividades mais comuns de cada um dos papéis que não são afetadas a nós de tarefas de fluxos.

No menu **Audiências e sessões**, as atividades mais comuns relativas a esses atos que tambẽm não são acessíveis via nós de tarefas.

No menu **Configuração**, as funcionalidades de configuração do sistema, reunindo o que existia antes em **Cadastros Auxiliares** e **Cadastros Básicos**.

As permissões para acesso às funcionalidades são determinadas pela restrição
[RN527](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn527 "Regras de negócio").

As funcionalidades vinculadas a nós de tarefas de fluxos são disponibilizadas através dos painéis do usuário.


[ Tela principal ]{#Tela_principal .mw-headline}
------------------------------------------------

A tela principal do PJe oferece quatro possibilidades:

1.  [Identificação](/wiki/funcionalidades.md#Login "Funcionalidades")
    (login)
2.  [Consultas ao andamento processual](/wiki/funcionalidades.md#Consulta_p.C3.BAblica "Funcionalidades")
3.  [Verificação de ambiente](/wiki/funcionalidades.md#Verifica.C3.A7.C3.A3o_de_ambiente "Funcionalidades")
4.  Pré-requisitos para utilização
5.  Fale conosco

A identificação, caso o usuário já não esteja cadastrado, direcionará o
usuário à confirmação de seu cadastro conforme regra
[RN412](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn412 "Regras de negócio").

As consultas ao andamento processual são consultas disponíveis sem a
necessidade de identificação.

Os pré-requisitos para utilização explicitam as condições para que o PJe funcione corretamente. Informações similares estão disponível no [Manual do
advogado](http://titanio09.cnj.jus.br/wiki/index.php/Manual_do_advogado_e_procurador#Informa.C3.A7.C3.B5es_iniciais "Manual do advogado e procurador").

A opção do **Fale conosco** exibe o conteúdo inserido no modelo de documento da instalação referenciado pelo identificador cadastrado no
[parâmetro](http://titanio09.cnj.jus.br/wiki/index.php/Par%C3%A2metros#Modelo_de_documento "Parâmetros") idModeloDocumentoFaleConosco.

[ Consulta pública ]{#Consulta_p.C3.BAblica .mw-headline}
---------------------------------------------------------

Através dessa consulta, usuários não cadastrados têm acesso à consulta
de processos que apresentam documentos de acordo com o disposto na
[Resolução Nº
121/2010](http://www.cnj.jus.br/atos-normativos?documento=92){.external
.text} do CNJ, que preconiza que a consulta aos dados básicos dos
processos judiciais será disponibilizada na rede mundial de computadores
(internet), assegurado o direito de acesso a informações processuais a
toda e qualquer pessoa, independentemente de prévio cadastramento ou de
demonstração de interesse, conforme regra
[RN381](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn381 "Regras de negócio").
A referida regra abrange outras restrições para a consulta. Os critérios
de consulta seguem a regra
[RN401](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn401 "Regras de negócio").

[ Verificação de ambiente ]{#Verifica.C3.A7.C3.A3o_de_ambiente .mw-headline}
----------------------------------------------------------------------------

Essa opção faz uma verificação do navegador utilizado a fim de
certificar que ele esteja configurado conforme o necessário para o
funcionamento do PJe. As verificações consistem em:

-   Navegador de Internet - Verificação se o navegador é o requerido

```{=html}
<!-- -->
```
-   Java e plugins - Verificação de presença do Java e de seus plugins

```{=html}
<!-- -->
```
-   Pop-ups habilitadas - Verificação se as janelas pop-ups estão
    habilitadas para o site

Para verificações bem sucedidas, o ícone
[![True.png](Funcionalidades%20-%20PJe_arquivos/True.png){width="14"
height="15"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:True.png){.image}
será exibido do lado esquerdo da opção verificada. Para verificações que
detectem que a configuração não foi feita conforme o necessário, o ícone
[![False.png](Funcionalidades%20-%20PJe_arquivos/False.png){width="12"
height="14"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:False.png){.image}
será exibido do lado esquerdo da opção verificada.

São exibidos também os
[botões](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Bot.C3.B5es "Manual de referência"):

-   Teste - testa se a leitura do certificado digital (disponível
    através de um dispositivo denonimado token, lido pela leitora do
    dispositivo na estação do usuário, denominada leitora de smart card)
    está ocorrendo sem problemas
-   Fechar - fecha a janela de verificação de ambiente

[ Login ]{#Login .mw-headline}
------------------------------

O login no PJe (ato de se identificar em um sistema para prosseguir com
sua operação) utiliza o certificado digital do usuário que está se
identificando para validá-la junto ao seu cadastro.

O certificado digital é uma identidade virtual que permite a
identificação segura e inequívoca do autor de uma mensagem ou transação
feita em meios eletrônicos, como a internet. Esse documento eletrônico é
gerado e assinado por uma terceira parte confiável, uma autoridade
certificadora que, seguindo regras da ICP-Brasil (Infraestrutura de
Chaves Públicas), associa uma pessoa a um par de chaves criptográficas.

A ICP-Brasil, por sua vez, é mantida pelo Instituto Nacional de
Tecnologia da Informação (ITI), autarquia federal vinculada à Casa Civil
da Presidência da república. O ITI é responsável por garantir a
autenticidade, a integridade e a validade jurídica de documentos em
forma eletrônica, bem como a realização de transações eletrônicas
seguras.

Sendo assim, o usuário deve estar previamente cadastrado (caso não
esteja, o sistema direcionará o usuário para a tela de cadastro,
conforme descrito na regra
[RN412](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn412 "Regras de negócio"))
e ter o certificado digital disponível através de um dispositivo. O
dispositivo pode ser um cartão, chamado de smartcard, ou um pen drive,
denonimado token. Caso seja um smartcard, deve ser instalada a leitora
de smartcard na estação do usuário. Caso seja um token, o usuário deverá
utilizar uma porta USB de sua estação. Para se identificar, com o PJe
disponível, o usuário insere o token na porta USB ou o smartcard na
leitora e pede para se autenticar. O
[sistema](/wiki/funcionalidades.md#Assinatura_digital "Funcionalidades")
lê o conteúdo da token/smartcard e pede que seja fornecida a senha para
acesso ao certificado. Ao digitar a senha, o sistema recupera os dados
da pessoa através do certificado e os
[valida](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn282 "Regras de negócio")
de acordo com os usuários cadastrados, utilizando essa identificação
para que o usuário prossiga com a operação do sistema. Esse procedimento
está de acordo com a lei
[11.419/06](http://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11419.htm){.external
.text}, que, em seu art. 1º, reconhece duas espécies de assinatura
eletrônica, entre elas a utilizada pelo PJe (assinatura digital baseada
em certificado digital, conforme normas da ICPBrasil - estrutura de
chaves públicas brasileira). A identificação presencial não é
necessária, vez que essa já é realizada pelo agente de registro no
processo de certificação.

Algumas informações sobre a utilização de certificação digital estão
disponíveis no [manual do
advogado](http://titanio09.cnj.jus.br/wiki/index.php/Manual_do_advogado_e_procurador#Certifica.C3.A7.C3.A3o_digital "Manual do advogado e procurador").

Ao realizar login, a o sistema verificará a [regra de proximidade de
expiração do certificado
digital](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn563 "Regras de negócio")
e exibirá o aviso [\"Certificado próximo de
expirar\"](/wiki/funcionalidades.md#Certificado_pr.C3.B3ximo_de_expirar "Funcionalidades")
conforme regra
[RN564](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn564 "Regras de negócio").

### [ Certificado próximo de expirar ]{#Certificado_pr.C3.B3ximo_de_expirar .mw-headline}

Quando o certificado digital do usuário identificado estiver perto de
expirar, conforme regra
[RN563](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn563 "Regras de negócio"),
será exibida, em uma nova janela, a mensagem informando o usuário da
proximidade da data de expiração, conforme exemplo a seguir:

    Atenção! 
    O seu certificado está próximo de expirar.
    Data de expiração: 15/02/2014

A janela aparecerá de acordo com a regra
[RN564](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn564 "Regras de negócio").

[ Ajuda de contexto ]{#Ajuda_de_contexto .mw-headline}
------------------------------------------------------

A ajuda no PJE é chamada de ajuda de contexto, o que significa que cada
página do PJe tem associado seu texto de ajuda. Ela está
[disponível](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Vis.C3.A3o_Geral "Manual de referência")
em todas as páginas. Os textos, inicialmente, estão vazios, e devem ser
alimentados na própria instalação. As informações podem ser inseridas
por usuários autorizados. O usuário autorizado deve estar vinculado ao
papel de identificador \"redator\", que, se não tiver sido criado, deve
ser adicionado à lista de papéis da instalação. Ao final dessa
configuração, ao se logar no sistema como usuário com permissão de
redator, a página aparecerá com a opção de edição (ícone de lápis). Ao
clicar, o usuário insere informações que estarão vinculadas à página que
está sendo acessada, ficando disponível para visualização de todos os
usuários que têm acesso à página em questão.

[ Página principal ]{#P.C3.A1gina_principal .mw-headline}
---------------------------------------------------------

### [ Mensagens ]{#Mensagens .mw-headline}

Esse agrupador aparece quando há
[avisos](/wiki/funcionalidades.md#Avisos "Funcionalidades")
cadastrados para o usuário. Ele exibirá as respectivas mensagens.

[ Painel ]{#Painel .mw-headline}
--------------------------------

O PJe tem alguns paineis definidos para papéis principais no seu
funcionamento padrão. Dentro do painel de cada papel, existem os
agrupadores, que agregam processos na mesma situação de forma a
facilitar a solução de pendências. O painel para seu papel aparece
quando o usuário se identifica no sistema ou através da seleção no menu
\"Painel\". Sendo assim, o sistema tem agrupamentos vários na forma
desses paineis, determinados pelos papéis. Os agrupadores aparecem na
medida em que o usuário tem a ele vinculados processos com as
características do agrupador.

Os processos judiciais tramitam seguindo um fluxo definido para cada
classe processual, percorrendo as tarefas e passos previamente
determinados pela área judiciária do tribunal, sem prejuízo de se
contemplar a possibilidade de o processo escapar do funcionamento normal
do fluxo em situações excepcionais. A definição de tarefas e a
associação da responsabilidade pela execução das tarefas a perfis
resultam na definição da [árvore de
tarefas](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#.C3.81rvore_de_tarefas "Manual de referência"),
onde são agrupadas as informações de forma a facilitar a execução de
tarefas pendentes para o usuário vinculado ao papel específico. Na
configuração de tarefas do fluxo, os nomes das tarefas pendentes
vinculadas às raias são utilizados para exibição na árvore de tarefas.
As raias (swimlanes) agrupam papéis que podem executar as tarefas.

Os paineis têm um padrão de apresentação que contém agrupadores
pré-definidos de acordo com o papel do usuário, sendo exibida sempre a
possibilidade de pesquisa do objeto apresentado. Uma das opções são as
[caixas](/wiki/funcionalidades.md#Caixas "Funcionalidades"),
que são uma forma de o usuário organizar os processos. As caixas estão
vinculadas aos processos através das
[tarefas](/wiki/funcionalidades.md#Tarefas "Funcionalidades")
nas quais se encontram. Pode-se, então, visualizar os processos por
tarefas vinculadas a eles e ainda por caixas em que estão localizados.
Na pesquisa das caixas, pode-se consultar o processo para verificar qual
tarefa está pendente para ele e também em qual caixa ele está, no caso
de o usuário ter definido caixas para a tarefa. Além disso, outra opção
disponível são os
[expedientes](/wiki/funcionalidades.md#Expedientes "Funcionalidades"),
que são atos relativos ao andamento do processo. Pode-se, então,
realizar pesquisa de processos por expedientes vinculados a ele, ou
seja, pelos atos processuais que já foram realizados no processo. A
visualização de expedientes dispõe os expedientes também como
agrupamentos pré-definidos.

As tarefas que um papel pode executar são configuráveis através da
definição do fluxo, mas vamos descrever aqui as tarefas usuais dos
painéis que estão definidos no PJe.

### [ Painel do advogado, procurador ou defensor ]{#Painel_do_advogado.2C_procurador_ou_defensor .mw-headline}

Dicas úteis: [roteiro de configuração de
procuradorias](http://titanio09.cnj.jus.br/wiki/index.php/Roteiro_de_configura%C3%A7%C3%A3o_de_procuradorias "Roteiro de configuração de procuradorias")

Perfil: Advogado/Procurador/Defensor

O \"Painel do usuário\" jus postulandi é similar ao painel do advogado,
procurador ou defensor.

#### [ Acervo ]{#Acervo .mw-headline}

O advogado/procurador tem acesso a todos os processos vinculados a ele.

##### [ Pendentes de manifestação ]{#Pendentes_de_manifesta.C3.A7.C3.A3o .mw-headline}

Nesse agrupador, estarão disponíveis expedientes que receberam ciência
de seus destinatários, têm prazo de manifestação definido e que ainda
não foi superado (não fechado) e aos quais ainda não foi dada resposta.
Além disso, independe do tipo de prazo do expediente.

##### [ Acervo geral ]{#Acervo_geral .mw-headline}

A aba
[listará](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI245 "Regras de interface")
todos os processos protocolados pelo advogado/ procurador/defensor.

#### [ Expedientes ]{#Expedientes .mw-headline}

O advogado/procurador/defensor verifica as intimações onde ele consta
como destinatário. Elas são agrupadas de acordo com os prazos e com suas
condições de ciência e resposta.

##### [ Pendentes de ciência ]{#Pendentes_de_ci.C3.AAncia .mw-headline}

Todos os atos de comunicação que não tenham tido ciência (ficta ou
concreta) do destinatário, independentemente do tipo de prazo ou do meio
de intimação aplicável a esse ato de comunicação. Em outras palavras,
havendo ou não prazo definido, tendo ou não data certa,
independentemente do meio de intimação, se não há ciência, aparece nessa
lista.

##### [ Ciência dada pelo destinatário e com prazo em curso ]{#Ci.C3.AAncia_dada_pelo_destinat.C3.A1rio_e_com_prazo_em_curso .mw-headline}

Todos os expedientes que têm prazo, seja ele em anos, meses, dias,
horas, minutos ou data certa, cuja ciência foi feita pelo destinatário e
cujo prazo ainda não expirou.

##### [ Ciência dada pelo sistema e com prazo em curso ]{#Ci.C3.AAncia_dada_pelo_sistema_e_com_prazo_em_curso .mw-headline}

Todos os expedientes que têm prazo, seja ele em anos, meses, dias,
horas, minutos ou data certa, cuja ciência foi feita pelo sistema e cujo
prazo ainda não expirou.

##### [ Cujo prazo findou nos últimos dez dias ]{#Cujo_prazo_findou_nos_.C3.BAltimos_dez_dias .mw-headline}

Todos os expedientes que têm prazo, seja ele em anos, meses, dias,
horas, minutos ou data certa, cujo prazo expirou nos últimos 10 dias sem
resposta do destinatário.

Neste conjunto devem ser incluídos os expedientes com o status de
fechados e os ainda não fechados. Pois, como normalmente as instalações
estão configuradas para que o status dos expedientes sejam atualizados
por um job executado na virada do dia, nos casos de prazos em horas e
minutos pode ocorrer do prazo do expediente esgotar-se no decorrer do
dia, mas o job não ter sido executado ainda.

##### [ Sem prazo ]{#Sem_prazo .mw-headline}

Todos os expedientes que não têm prazo cuja ciência aconteceu e que
ainda não estão fechados (o fechamento acontece com a resposta do
destinatário ou em 30 dias após a ciência, caso não tenha sido definido
prazo diverso nas configurações da aplicação). O parâmetro responsável
pela configuração do tempo máximo para os expedientes sem prazo ser
considerado fechado é o \"esperaMaximaSemPrazo\".

##### [ Respondidos nos últimos 10 dias ]{#Respondidos_nos_.C3.BAltimos_10_dias .mw-headline}

Todos os expedientes que foram respondidos nos últimos 10 dias
independentemente de terem ou não prazo.

#### [ Intimações de pauta ]{#Intima.C3.A7.C3.B5es_de_pauta .mw-headline}

Presente só nas instalações do segundo grau

#### [ Petições ]{#Peti.C3.A7.C3.B5es .mw-headline}

### [ Painel do magistrado ]{#Painel_do_magistrado .mw-headline}

O painel do magistrado é similar ao [painel do
usuário](/wiki/funcionalidades.md#Painel_do_usu.C3.A1rio "Funcionalidades"),
diferenciado pelas [permissões vinculadas às
tarefas](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn511 "Regras de negócio").

\

-   Mensagens de destaque

Ao usuário interno, são exibidos alertas para que ele atue conforme sua
escolha. Essa atuação retirará o destaque, para que o alerta não seja
exibido mais. São eles:

-   Pedidos de liminar ou de antecipação de tutela
-   Processos preventos
-   Habilitação nos autos
-   Mandados devolvidos

#### [ Caixas ]{#Caixas .mw-headline}

As caixas são organizadores que o usuário cria para separar os processos
na árvore de tarefas, ajudando em seu trabalho diário. O usuário pode
manualmente vincular processos às suas caixas ou pode criar regras de
filtragem que permitam que os processos sejam automaticamente
encaminhados para a caixa correta. As caixas são criadas dentro das
[tarefas](/wiki/funcionalidades.md#Tarefas "Funcionalidades"),
ou seja, o processo está primeiramente vinculado à tarefa e
posteriormente à caixa, não perdendo sua vinculação original, sendo isso
demonstrado visualmente através da hierarquia de tarefas e caixas. As
caixas ficam vinculadas à tarefa e não ao usuário que as criou. Sendo
assim, todos que estiverem na raia vinculada àquela tarefa terão acesso
às caixas.

\

##### [ Perfil de visualização ]{#Perfil_de_visualiza.C3.A7.C3.A3o .mw-headline}

Por vezes, o usuário precisa visualizar as demais tarefas dos servidores
da unidade judiciária. Essa configuração é possível para determinados
papeis, conforme
[RN572](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn572 "Regras de negócio").
A opção é disponibilizada da seguinte forma:

Perfil de visualização:
[campo](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_op.C3.A7.C3.A3o "Manual de referência")
contendo as opções:

-   Restrito - visualiza só suas tarefas
-   Completo (somente consulta) - visualiza as tarefas da sua unidade,
    apenas para consulta

##### [ Localizar caixa ]{#Localizar_caixa .mw-headline}

A funcionalidade permite que o usuário pesquise processos com o objetivo
de encontrar em qual tarefa/caixa eles estão.

A opção \"Localizar caixa\" fica logo acima da [árvore de
tarefas](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#.C3.81rvore_de_tarefas "Manual de referência").
Ao acioná-la, um [campo de
sugestão](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sugest.C3.A3o "Manual de referência")
é disponibilizado para que o usuário forneça o número do processo a ser
pesquisado ou parte dele. Ao selecionar o número do processo da lista
disponível no campo de sugestão, ele é preenchido no campo e o usuário
poderá acionar o botão \"Localizar\". O botão localizar efetuará a
pesquisa que retornará em qual(is) tarefa(s) o processo está.

Regras relacionadas:

-   [RN503](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn503 "Regras de negócio")

\

###### [ Tarefas de processos ]{#Tarefas_de_processos .mw-headline}

É exibida a [árvore de
tarefas](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#.C3.81rvore_de_tarefas "Manual de referência").
Apresentamos a descrição de algumas tarefas mais adiante.
([Tarefas](/wiki/funcionalidades.md#Tarefas "Funcionalidades"))

##### [ Mover para caixa ]{#Mover_para_caixa .mw-headline}

Opção acionada através do ícone
[![Clips.jpg](Funcionalidades%20-%20PJe_arquivos/Clips.jpg){width="19"
height="18"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Clips.jpg){.image}.

Agrupa o processo associado ao ícone selecionado para uma caixa
personalizada.

##### [ Nova caixa ]{#Nova_caixa .mw-headline}

##### [ Editar caixa ]{#Editar_caixa .mw-headline}

##### [ Remover caixa ]{#Remover_caixa .mw-headline}

#### [ Expedientes ]{#Expedientes_2 .mw-headline}

**A T E N Ç Ã O:\
Documentação da aba Expediente em MANUTENÇÃO!**

São atos de comunicação relativos ao andamento do processo judicial.
Esta aba, disponível para servidores ([**usuários
internos**](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn394 "Regras de negócio")),
permite a pesquisa de expedientes do processo através de seus
agrupamentos descritos a seguir.

##### [ Pendentes ]{#Pendentes .mw-headline}

São exibidos os expedientes cujo meio de envio é \"Enviar Via Sistema\"
(é a comunicação por meio eletrônico na forma da Lei n. 11.419/2006)
**ou**\
\"Correios\" (é a comunicação por correspondência) e as condições de
entrada e saída de expedientes neste agrupador são detalhadas a seguir.

###### [ Quando o expediente \"entra\" no agrupador \'Pendentes\'? ]{#Quando_o_expediente_.22entra.22_no_agrupador_.27Pendentes.27.3F .mw-headline}

-   Quando o expediente não possui data de ciência e tem prazo (isto é,
    a quantidade de dias para o prazo processual legal da parte é maior
    que zero).

###### [ Quando o expediente \"sai\" do agrupador \'Pendentes\'? ]{#Quando_o_expediente_.22sai.22_do_agrupador_.27Pendentes.27.3F .mw-headline}

-   Quando o advogado ou a parte tomar ciência.\
    OU
-   Quando o prazo de 10 dias se esgotar, neste caso, o envio deve ter
    sido \"Enviar Via Sistema\".\
    OU
-   Quando o servidor do tribunal registrar a ciência, neste caso, o
    envio deve ter sido \"Correios\".

Referência: Regra
[RN386](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn386 "Regras de negócio")

\

##### [ Correio(s) pendente(s) ]{#Correio.28s.29_pendente.28s.29 .mw-headline}

São exibidos os expedientes cujo meio de envio é \"Correios\" (é a
comunicação por correspondência) e as condições de entrada e saída de
expedientes neste agrupador são detalhadas a seguir.

###### [ Quando o expediente \"entra\" no agrupador \'Correio(s) Pendente(s)\'? ]{#Quando_o_expediente_.22entra.22_no_agrupador_.27Correio.28s.29_Pendente.28s.29.27.3F .mw-headline}

-   Quando o expediente não possui data de ciência e tem prazo (isto é,
    a quantidade de dias para o prazo processual legal da parte é maior
    que zero).

###### [ Quando o expediente \"sai\" do agrupador \'Correio(s) Pendente(s)\'? ]{#Quando_o_expediente_.22sai.22_do_agrupador_.27Correio.28s.29_Pendente.28s.29.27.3F .mw-headline}

-   Quando o servidor do tribunal registrar ciência.

Referência: Regra
[RN386](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn386 "Regras de negócio")

\

##### [ Mandado(s) pendente(s) ]{#Mandado.28s.29_pendente.28s.29 .mw-headline}

São exibidos os expedientes cujo meio de envio é \"Central de Mandados\"
(é a comunicação por oficial de justiça) e as condições de entrada e
saída de expedientes neste agrupador são detalhadas a seguir.

###### [ Quando o expediente \"entra\" no agrupador \'Mandado(s) Pendente(s)\'? ]{#Quando_o_expediente_.22entra.22_no_agrupador_.27Mandado.28s.29_Pendente.28s.29.27.3F .mw-headline}

-   Quando o expediente não possui data de ciência e tem prazo (isto é,
    a quantidade de dias para o prazo processual legal da parte é maior
    que zero).

###### [ Quando o expediente \"sai\" do agrupador \'Mandado(s) Pendente(s)\'? ]{#Quando_o_expediente_.22sai.22_do_agrupador_.27Mandado.28s.29_Pendente.28s.29.27.3F .mw-headline}

-   Quando o oficial de justiça registrar data de diligência cumprida.

Referência: Regra
[RN386](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn386 "Regras de negócio")

\

##### [ Expedientes físicos sem registro de intimação ]{#Expedientes_f.C3.ADsicos_sem_registro_de_intima.C3.A7.C3.A3o .mw-headline}

São exibidos os expedientes cujo meio de envio é \"Correios\" (é a
comunicação por correspondência) e as condições de entrada e saída de
expedientes neste agrupador são detalhadas a seguir.

###### [ Quando o expediente \"entra\" no agrupador \'Expedientes físicos sem registro de intimação\'? ]{#Quando_o_expediente_.22entra.22_no_agrupador_.27Expedientes_f.C3.ADsicos_sem_registro_de_intima.C3.A7.C3.A3o.27.3F .mw-headline}

-   Quando não tem registro de ciência para o expediente e, além disso,
    o expediente pode ter ou não prazo.

###### [ Quando o expediente \"sai\" do agrupador \'Expedientes físicos sem registro de intimação\'? ]{#Quando_o_expediente_.22sai.22_do_agrupador_.27Expedientes_f.C3.ADsicos_sem_registro_de_intima.C3.A7.C3.A3o.27.3F .mw-headline}

-   Quando o servidor do tribunal registrar a ciência.\
    OU
-   Quando o servidor do tribunal registrar o fechamento do expediente
    (para os expedientes com prazo), conforme regra
    [RN510](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn510 "Regras de negócio")
    .\
    OU
-   Quando decorrer o período de espera máxima (para os expedientes sem
    prazo), conforme explicado na regra
    [RN347](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn347 "Regras de negócio").

Como referência, o registro de ciência de intimação de forma geral é
determinado pela regra
[RN386](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn386 "Regras de negócio").

###### [ Registrar intimação/citação ]{#Registrar_intima.C3.A7.C3.A3o.2Fcita.C3.A7.C3.A3o .mw-headline}

Por meio dessa tarefa (ícone
[![Lapis.jpg](Funcionalidades%20-%20PJe_arquivos/Lapis.jpg){width="16"
height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Lapis.jpg){.image}
da grid \"Meus Expedientes\"), o usuário pode registrar a
[intimação](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn353 "Regras de negócio")
feita pelo meio de envio \"**Correios**\".

No campo \"Resultado\", os valores possíveis são os disponíveis na regra
[RD102](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD102 "Regras de domínio").

O registro da ciência para expedientes físicos, conforme regra
[RN510](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn510 "Regras de negócio"),
só será realizado se a intimação for efetivamente recebida, ou seja,
\"Recebido\" de acordo com as opções da regra
[RD102](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD102 "Regras de domínio").
Esse registro será realizado utilizando como data da ciência o campo
data de recebimento, que deve ser de preenchimento obrigatório apenas
para o resultado \"Recebido\", conforme a mesma regra
[RN510](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn510 "Regras de negócio").

\

##### [ Confirmadas pelo destinatário e dentro do prazo ]{#Confirmadas_pelo_destinat.C3.A1rio_e_dentro_do_prazo .mw-headline}

São exibidos os expedientes desconsiderando o meio de envio e as
condições de entrada e saída de expedientes neste agrupador são
detalhadas a seguir.

###### [ Quando o expediente \"entra\" no agrupador \'Confirmadas pelo destinatário e dentro do prazo\'? ]{#Quando_o_expediente_.22entra.22_no_agrupador_.27Confirmadas_pelo_destinat.C3.A1rio_e_dentro_do_prazo.27.3F .mw-headline}

-   Quando o expediente possui data de ciência registrada pelo
    destinatário e tem prazo (isto é, a quantidade de dias para o prazo
    processual legal da parte é maior que zero), porém somente quando o
    prazo está em curso.

###### [ Quando o expediente \"sai\" do agrupador \'Confirmadas pelo destinatário e dentro do prazo\'? ]{#Quando_o_expediente_.22sai.22_do_agrupador_.27Confirmadas_pelo_destinat.C3.A1rio_e_dentro_do_prazo.27.3F .mw-headline}

-   Quando decorrido o prazo processual.

\

##### [ Confirmadas pelo PJe e dentro do prazo ]{#Confirmadas_pelo_PJe_e_dentro_do_prazo .mw-headline}

São exibidos os expedientes desconsiderando o meio de envio e as
condições de entrada e saída de expedientes neste agrupador são
detalhadas a seguir.

###### [ Quando o expediente \"entra\" no agrupador \'Confirmadas pelo PJe e dentro do prazo\'? ]{#Quando_o_expediente_.22entra.22_no_agrupador_.27Confirmadas_pelo_PJe_e_dentro_do_prazo.27.3F .mw-headline}

-   Quando o expediente possui data de ciência registrada pelo sistema
    PJe (ou seja, o sistema deu [ciência
    automática](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn384 "Regras de negócio"))
    e ainda está com prazo (isto é, a quantidade de dias para o prazo
    processual legal da parte é maior que zero), porém somente quando o
    prazo está em curso.

###### [ Quando o expediente \"sai\" do agrupador \'Confirmadas pelo PJe e dentro do prazo\'? ]{#Quando_o_expediente_.22sai.22_do_agrupador_.27Confirmadas_pelo_PJe_e_dentro_do_prazo.27.3F .mw-headline}

-   Quando decorrido o prazo processual.

\

##### [ Prazos encerrados nos últimos 10 dias ]{#Prazos_encerrados_nos_.C3.BAltimos_10_dias .mw-headline}

São exibidos os expedientes desconsiderando o meio de envio e as
condições de entrada e saída de expedientes neste agrupador são
detalhadas a seguir.

###### [ Quando o expediente \"entra\" no agrupador \'Prazos encerrados nos últimos 10 dias\'? ]{#Quando_o_expediente_.22entra.22_no_agrupador_.27Prazos_encerrados_nos_.C3.BAltimos_10_dias.27.3F .mw-headline}

-   Quando o expediente tem prazo e o prazo foi encerrado nos últimos 10
    dias e não existe resposta para o expediente.

###### [ Quando o expediente \"sai\" do agrupador \'Prazos encerrados nos últimos 10 dias\'? ]{#Quando_o_expediente_.22sai.22_do_agrupador_.27Prazos_encerrados_nos_.C3.BAltimos_10_dias.27.3F .mw-headline}

-   Quando ultrapassar mais de 10 dias do encerramento do prazo.

\

##### [ Sem prazo ]{#Sem_prazo_2 .mw-headline}

São exibidos os expedientes cujo meio de envio é \"Enviar Via Sistema\"
(é a comunicação por meio eletrônico na forma da Lei n. 11.419/2006) e
as condições de entrada e saída de expedientes neste agrupador são
detalhadas a seguir.

###### [ Quando o expediente \"entra\" no agrupador \'Sem prazo\'? ]{#Quando_o_expediente_.22entra.22_no_agrupador_.27Sem_prazo.27.3F .mw-headline}

-   Quando o expediente não tem prazo (isto é, a quantidade de dias para
    o prazo processual legal da parte é igual a zero).

###### [ Quando o expediente \"sai\" do agrupador \'Sem prazo\'? ]{#Quando_o_expediente_.22sai.22_do_agrupador_.27Sem_prazo.27.3F .mw-headline}

-   Quando decorrer o período de espera máxima conforme explicado na
    regra
    [RN347](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn347 "Regras de negócio").

\

##### [ Mandado de prisão/ alvará de soltura/ contramandado ]{#Mandado_de_pris.C3.A3o.2F_alvar.C3.A1_de_soltura.2F_contramandado .mw-headline}

Nota: este agrupador ainda não funciona, estará disponível quando for
implantado os fluxos processuais da matéria Criminal.

#### [Agrupadores ]{#Agrupadores .mw-headline}

O painel vem com os seguintes agrupadores:

Os agrupadores são exibidos de acordo com a regra
[RN341](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn341 "Regras de negócio").

##### [ Processos com pedido de segredo de justiça não apreciado ]{#Processos_com_pedido_de_segredo_de_justi.C3.A7a_n.C3.A3o_apreciado .mw-headline}

De acordo com a marcação de segredo de justiça do processo e utilizando
a condição de apreciação do segredo marcada no protocolo da ação, esse
agrupador exibirá todos os processos daquele órgão julgador que estejam
com a marcação de apreciação registrada como \"A\", ou seja, \"a
apreciar\". Detalhamento do funcionamento do agrupador disponível no
[roteiro de
utilização](http://titanio09.cnj.jus.br/wiki/index.php/Roteiro_de_utiliza%C3%A7%C3%A3o_de_sigilo_e_segredo_de_justi%C3%A7a#Agrupador_dos_processos_sigilosos_n.C3.A3o_apreciados "Roteiro de utilização de sigilo e segredo de justiça").

##### [ Processos com pedido de sigilo nos documentos não apreciado ]{#Processos_com_pedido_de_sigilo_nos_documentos_n.C3.A3o_apreciado .mw-headline}

Detalhamento do funcionamento do agrupador disponível no [roteiro de
utilização](http://titanio09.cnj.jus.br/wiki/index.php/Roteiro_de_utiliza%C3%A7%C3%A3o_de_sigilo_e_segredo_de_justi%C3%A7a#Agrupador_dos_documentos_sigilosos_n.C3.A3o_apreciados "Roteiro de utilização de sigilo e segredo de justiça").

##### [ Processos com pedido de assistência judiciária gratuita não apreciado ]{#Processos_com_pedido_de_assist.C3.AAncia_judici.C3.A1ria_gratuita_n.C3.A3o_apreciado .mw-headline}

Todos os processos judiciais distribuídos que tenham pedido de
assistência judiciária gratuita e que ainda não foram apreciados.

##### [ Processos com pedido liminar ou com antecipação de tutela não apreciados ]{#Processos_com_pedido_liminar_ou_com_antecipa.C3.A7.C3.A3o_de_tutela_n.C3.A3o_apreciados .mw-headline}

Regras relacionadas:

-   [Regra de visualização do
    agrupador](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn502 "Regras de negócio")

##### [ Processos com habilitação nos autos não lidas ]{#Processos_com_habilita.C3.A7.C3.A3o_nos_autos_n.C3.A3o_lidas .mw-headline}

Nesse agrupador, são exibidos os pedidos de habilitação nos autos [não
lidos](http://titanio09.cnj.jus.br/wiki/index.php?title=N%C3%A3o_lidos&action=edit&redlink=1 "Não lidos (página inexistente)"){.new}.

Para cada pedido de habilitação nos autos não lido são exibidas as
seguintes informações:

-   ícone
    [![Oculos.jpg](Funcionalidades%20-%20PJe_arquivos/Oculos.jpg){width="16"
    height="21"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Oculos.jpg){.image}
    permitindo o detalhamento do processo
-   [caixa de
    seleção](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sele.C3.A7.C3.A3o "Manual de referência")
    permitindo a seleção de um ou mais pedidos para atuação
-   Processo - número do processo
-   Solicitante - Usuário que solicitou a habilitação
-   Método - Automática ou Manual
-   Data
-   Classe Processual
-   Polo Ativo
-   Polo Passivo
-   Retificar - ícone
    [![Lapis.jpg](Funcionalidades%20-%20PJe_arquivos/Lapis.jpg){width="16"
    height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Lapis.jpg){.image}
    permitindo a retificação do processo (ver regra
    [RN573](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn573 "Regras de negócio"))
-   Prioridade processual

##### [ Processos em análise de prevenção ]{#Processos_em_an.C3.A1lise_de_preven.C3.A7.C3.A3o .mw-headline}

Todos os processos que tenham processos filhos associados cujo [tipo de
associação](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD99 "Regras de domínio")
seja uma prevenção apontada anteriormente e ainda [não
validada](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn304 "Regras de negócio").
Os processos previamente avaliados pelo assessor que tiverem minuta de
documento vinculada à avaliação aparecerá com esse indicativo, de forma
a facilitar a atuação do magistrado. A assinatura do magistrado na
minuta confeccionada pelo assessor também pode ocorrer através de outra
opção do sistema onde o documento seja exibido. Para que o processo seja
considerado válido, a regra
[RN364](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn364 "Regras de negócio")
deve ser observada. Para realizar a configuração de acesso ao agrupador,
verificar a regra
[RN539](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn539 "Regras de negócio").

Para o caso do servidor, todos os processos que tenham processos filhos
associados cujo [tipo de
associação](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD99 "Regras de domínio")
seja uma prevenção apontada anteriormente e ainda [não
validadas](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn304 "Regras de negócio").
O assessor consegue confirmar ou declinar provisoriamente a situação de
prevenção, minutando o ato do magistrado, que o confirmará
posteriormente. O processo sairá do agrupador quando validado pelo
magistrado.

##### [ Processos com documentos não lidos ]{#Processos_com_documentos_n.C3.A3o_lidos .mw-headline}

Esse agrupador exibe, para cada documento incluído, processos que tenham
[documentos não
lidos](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn569 "Regras de negócio")
incluídos de acordo com a regra
[RN574](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn574 "Regras de negócio").
Estão incluídas as petições avulsas e os pedidos de habilitação.

O agrupador de pesquisa permite a filtragem dos documentos de acordo com
os seguintes parâmetros:

-   Documento elaborado por - papel que elaborou o documento
-   Processo
-   OAB (UF 000000 A)
-   CNPJ / CPF
-   Classe judicial
-   Assunto
-   Nome da Parte
-   Usuário que anexou o documento
-   Período da Anexação do Documento

Para cada peticionamento avulso ou pedido de habilitação, serão exibidas
as seguintes informações:

-   ícone
    [![Lapis.jpg](Funcionalidades%20-%20PJe_arquivos/Lapis.jpg){width="16"
    height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Lapis.jpg){.image}
    permitindo a realização da tarefa da qual o processo está pendente,
    respeitando as regras de
    [permissão](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn511 "Regras de negócio")
    para execução da tarefa
-   ícone
    [![Oculos.jpg](Funcionalidades%20-%20PJe_arquivos/Oculos.jpg){width="16"
    height="21"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Oculos.jpg){.image}
    permitindo o detalhamento do processo
-   [caixa de
    seleção](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sele.C3.A7.C3.A3o "Manual de referência")
    permitindo a seleção de um ou mais pedidos para atuação
-   Número do processo
-   Classe judicial
-   Tipo de documento
-   Data de protocolo do documento
-   Prioridade processual
-   [botão](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Bot.C3.B5es "Manual de referência")
    \"Ver tarefas\", que permite visualizar de quais tarefas o processo
    está pendente

##### [ Mandados devolvidos pelo oficial de justiça ]{#Mandados_devolvidos_pelo_oficial_de_justi.C3.A7a .mw-headline}

##### [ Processos aguardando revisão / revisados / devolvidos pelo revisor ]{#Processos_aguardando_revis.C3.A3o_.2F_revisados_.2F_devolvidos_pelo_revisor .mw-headline}

##### [ Processos aguardando encaminhamento do secretário de audiência(atas assinadas) ]{#Processos_aguardando_encaminhamento_do_secret.C3.A1rio_de_audi.C3.AAncia.28atas_assinadas.29 .mw-headline}

#### [ Últimas tarefas realizadas ]{#.C3.9Altimas_tarefas_realizadas .mw-headline}

### [ Painel do usuário ]{#Painel_do_usu.C3.A1rio .mw-headline}

Painel exibido para [usuários
internos](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn394 "Regras de negócio")
que tenham sido cadastrados como \"servidor\" e tenham sido associados a
um órgão julgador. O painel é similar ao [painel do
magistrado](/wiki/funcionalidades.md#Painel_do_magistrado "Funcionalidades"),
sendo diferenciado pelas permissões relacionadas às tarefas.

\

### [ Painel do magistrado na sessão ]{#Painel_do_magistrado_na_sess.C3.A3o .mw-headline}

A tela inicial exibirá um calendário com todas as sessões do órgão
julgador colegiado do magistrado, agrupadas por dia.

Os dias em que houver sessão (ões) já criadas estarão disponíveis para
serem selecionados. Ao selecionar, a tela do painel do magistrado será
apresentada. O PJe tem duas telas possíveis e a configuração de qual
tela será exibida é feita por meio do parâmetro
pje:painel:magistrado:sessao:novo. O valor do parâmetro poe ser \"t\" ou
\"f\", o que indicará a abertura ou não da versão mais atual do painel.
O painel exibe inicialmente os dados da sessão, se há ou não processos
apregoados, se a sessão contínua ou não, um formulário de pesquisa de
processos e os processos da sessão. Para cada processo, são apresentados
os dados básicos, a possibilidade de abertura dos autos, que obedecerá
as regras de processos com marcação de segredo de justiça, a ordem dele
na pauta e, a partir da seleção do processo, são exibidos o placar e
algumas acões dependentes da situação e do perfil e localização do
usuário que está operando:

\- Menu \"Ações como vogais\" para o caso de magistrado não relator e
(não sessão contínua or sessão iniciada) Registros disponíveis para
órgãos julgadores cadastrados como participantes da sessão e processos
em julgamento:

    Registrar pedido de vista
    Registrar/Retirar registro impedimento ou suspeição
    Redigir/Remover voto
    Incluir anotações
    Para o caso de sessão contínua, exibir opção de "Enviar para pauta presencial"

\
- Menu \"Ações do relator\" para o caso de magistrado relator

    Incluir anotações
    Editar voto
    Retirar para reexame, que
    Para o caso de sessão contínua, exibir opção de "Enviar para pauta presencial" 

\
O placar de julgamento deve exibir votos agrupados por órgão julgador,
além de agrupar também os não proferidos e os impedidos/suspeitos

Ao redigir voto, os documentos pertinentes ao órgão julgados será
apresentados para edição. Para o usuário magistrado, será possível
assinar os documentos. Conforme já ocorre na assinatura de documentos de
sessão no painel do usuário, a assinatura não atribui data de juntada, o
que só ocorrerá após assinatura do acórdão. Também conforme já ocorre
nas tarefas do painel do usuário, não é permitido anexar documentos
pela.

As opções dos menus só devem estar disponíveis para sessões em
andamento.

Para o painel do magistrado novo, se o processo tiver vinculado a um
bloco de julgamento, as ações possíveis serão referentes apenas ao bloco
de julgamento e apenas para agrupamento por relator, já que o bloco que
não foi agrupado por relator só permite julgamento unânime, ação essa
marcada pelo secretário da sessão.

A inclusão de anotações é possível mesmo que a sessão não esteja em
andamento.

### [ Painel do oficial de justiça ]{#Painel_do_oficial_de_justi.C3.A7a .mw-headline}

Perfil: oficial de justiça

\
O usuário pode filtrar os expedientes através dos seguintes filtros:

-   Nome do destinatário ([campo de texto
    livre](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_texto_livre "Manual de referência"))
-   Grupo oficial de justiça ([caixa de
    combinação](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Caixas_de_combina.C3.A7.C3.A3o "Manual de referência"))
-   Tipo de mandado ([caixa de
    combinação](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Caixas_de_combina.C3.A7.C3.A3o "Manual de referência")) -
    corresponde ao tipo de documento do expediente

Para cada mandado pendente segundo a regra
[RN555](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn555 "Regras de negócio"),
são retornadas as seguintes informações:

-   Ícone
    [![Printer.png](Funcionalidades%20-%20PJe_arquivos/Printer.png){width="16"
    height="16"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Printer.png){.image}
    para exibição do mandado para impressão
-   Ícone
    [![Lapis.jpg](Funcionalidades%20-%20PJe_arquivos/Lapis.jpg){width="16"
    height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Lapis.jpg){.image}
    para exibição da tela de [cumprimento da
    diligência](/wiki/funcionalidades.md#Controle_de_visita "Funcionalidades")
-   Ícone
    [![Oculos.jpg](Funcionalidades%20-%20PJe_arquivos/Oculos.jpg){width="16"
    height="21"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Oculos.jpg){.image}
    para exibição dos documentos do processo
-   Ato de comunicação: resumo do expediente contendo as seguintes
    informações:
    -   Órgão julgador ao qual o expediente está vinculado
    -   Ícone
        [![Indice.png](Funcionalidades%20-%20PJe_arquivos/Indice.png){width="20"
        height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Indice.png){.image}
        caso tenha sido solicitada urgência na [confecção do
        expediente](/wiki/funcionalidades.md#Preparar_comunica.C3.A7.C3.A3o "Funcionalidades")
    -   Sigla da classe judicial ao lado do número do processo ao qual
        está vinculado o expediente - tipo do documento
    -   Destinatários
    -   Expedição
    -   Distribuição
-   Endereço (s)
-   Anexos

#### [ Controle de visita ]{#Controle_de_visita .mw-headline}

Através dessa tela, o usuário pode registrar as visitas realizadas até o
encerramento da diligência.

##### [ Controle de visita ]{#Controle_de_visita_2 .mw-headline}

Através dessa aba, o usuário pode registrar a data e a hora das visitas
realizadas e suas respectivas descrições.

##### [ Resultado da diligência ]{#Resultado_da_dilig.C3.AAncia .mw-headline}

Através dessa aba, o usuário seleciona através da [caixa de
combinação](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Caixas_de_combina.C3.A7.C3.A3o "Manual de referência")
de tipo de resultado da diligência o tipo correspondente. Os tipos são
exibidos conforme regra
[RN556](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn556 "Regras de negócio").

Após o registro, a geração da movimentação fica condicionada à regra
[RN557](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn556 "Regras de negócio").

### [ Painel do oficial de justiça ]{#Painel_do_oficial_de_justi.C3.A7a_2 .mw-headline}

Perfil: oficial de justiça distribuidor

O nome do painel é o mesmo do descrito anteriormente, mas trata-se do
painel do oficial de justiça distribuidor.

São exibidos os seguintes agrupadores:

#### [ Expedientes para redistribuição ]{#Expedientes_para_redistribui.C3.A7.C3.A3o .mw-headline}

Nesse agrupador são exibidos os processos que contém mandados de justiça
pendentes de redistribuição. O agrupador contém ao lado de sua descrição
a quantidade de expedientes pendentes.

Para cada mandado pendente segundo a regra
[RN554](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn554 "Regras de negócio"),
são retornadas as seguintes informações:

-   Ícone
    [![Printer.png](Funcionalidades%20-%20PJe_arquivos/Printer.png){width="16"
    height="16"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Printer.png){.image}
    para exibição do mandado para impressão
-   Ícone
    [![Oculos.jpg](Funcionalidades%20-%20PJe_arquivos/Oculos.jpg){width="16"
    height="21"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Oculos.jpg){.image}
    para exibição dos documentos do processo
-   Processo: número do processo ao qual o mandado está vinculado
-   Expediente: tipo de comunicação utilizada na [confecção do
    mandado](/wiki/funcionalidades.md#Preparar_comunica.C3.A7.C3.A3o "Funcionalidades")
    (o mesmo que tipo de documento)
-   Urgência: exibe o ícone
    [![Indice.png](Funcionalidades%20-%20PJe_arquivos/Indice.png){width="20"
    height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Indice.png){.image}
    caso tenha sido solicitada urgência na [confecção do
    mandado](/wiki/funcionalidades.md#Preparar_comunica.C3.A7.C3.A3o "Funcionalidades")
-   Distribuído em: data em que o mandado foi distribuído originalmente
-   Destinatário
-   Endereço(s)
-   [Campo de
    seleção](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sele.C3.A7.C3.A3o "Manual de referência")
    para possibilitar ao usuário a seleção de vários mandados que terão
    a mesma distribuição

O usuário pode ordenar os mandados de forma a facilitar a organização de
sua distribuição. A ordenação é determinada pela regra
[RN560](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn560 "Regras de negócio").

Ao selecionar algum mandado através do [campo de
seleção](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sele.C3.A7.C3.A3o "Manual de referência")
disponibilizado, o
[botão](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Bot.C3.B5es "Manual de referência")
[\"Redistribuir\"](/wiki/funcionalidades.md#Redistribuir "Funcionalidades")
é habilitado.

##### [ Redistribuir ]{#Redistribuir .mw-headline}

Após selecionar o(s) mandado(s), o usuário terá a opção de selecionar o
grupo de oficiais de justiça para o qual o mandado será enviado e,
opcionalmente, o oficial de justiça a que ele será atribuído.

Na redistribuição, a regra
[RN552](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn552 "Regras de negócio")
é obedecida, ficando a geração de movimentação condicionada à regra
[RN551](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn551 "Regras de negócio").

#### [ Expedientes para distribuição ]{#Expedientes_para_distribui.C3.A7.C3.A3o .mw-headline}

Nesse agrupador são exibidos os processos que contém mandados de justiça
pendentes de distribuição. O agrupador contém ao lado de sua descrição a
quantidade de expedientes pendentes.

Para cada mandado pendente segundo a regra
[RN553](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn553 "Regras de negócio"),
são retornadas as seguintes informações:

-   Ícone
    [![Printer.png](Funcionalidades%20-%20PJe_arquivos/Printer.png){width="16"
    height="16"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Printer.png){.image}
    para exibição do mandado para impressão
-   Ícone
    [![Oculos.jpg](Funcionalidades%20-%20PJe_arquivos/Oculos.jpg){width="16"
    height="21"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Oculos.jpg){.image}
    para exibição dos documentos do processo
-   Processo: número do processo ao qual o mandado está vinculado
-   Expediente: tipo de comunicação utilizada na [confecção do
    mandado](/wiki/funcionalidades.md#Preparar_comunica.C3.A7.C3.A3o "Funcionalidades")
    (o mesmo que tipo de documento)
-   Urgência: exibe o ícone
    [![Indice.png](Funcionalidades%20-%20PJe_arquivos/Indice.png){width="20"
    height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Indice.png){.image}
    caso tenha sido solicitada urgência na [confecção do
    mandado](/wiki/funcionalidades.md#Preparar_comunica.C3.A7.C3.A3o "Funcionalidades")
-   Cadastrado em: data em que o mandado foi
    [construído](/wiki/funcionalidades.md#Preparar_comunica.C3.A7.C3.A3o "Funcionalidades")
-   Destinatário
-   Endereço(s)
-   [Campo de
    seleção](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sele.C3.A7.C3.A3o "Manual de referência")
    para possibilitar ao usuário a seleção de vários mandados que terão
    a mesma distribuição

\
O usuário pode ordenar os mandados de forma a facilitar a organização de
sua redistribuição. A ordenação é determinada pela regra
[RN560](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn560 "Regras de negócio").

Ao selecionar algum mandado através do [campo de
seleção](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sele.C3.A7.C3.A3o "Manual de referência")
disponibilizado, o
[botão](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Bot.C3.B5es "Manual de referência")
[\"Distribuir\"](/wiki/funcionalidades.md#Distribuir "Funcionalidades")
é habilitado.

##### [ Distribuir ]{#Distribuir .mw-headline}

Após selecionar o(s) mandado(s), o usuário terá a opção de selecionar o
grupo de oficiais de justiça para o qual o mandado será enviado e,
opcionalmente, o oficial de justiça a que ele será atribuído.

Na distribuição, a regra
[RN552](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn552 "Regras de negócio")
é obedecida, ficando a geração de movimentação condicionada à regra
[RN551](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn551 "Regras de negócio").

### [ Painel do perito ]{#Painel_do_perito .mw-headline}

Esse painel apresenta as perícias designadas para o perito identificado.

### [ Painel do procurador na sessão ]{#Painel_do_procurador_na_sess.C3.A3o .mw-headline}

A tela inicial exibirá um calendário com todas as sessões que tem
processos pautados com o procurador vinculado, agrupadas por dia.

### [ Painel do membro do Ministério Público na sessão ]{#Painel_do_membro_do_Minist.C3.A9rio_P.C3.BAblico_na_sess.C3.A3o .mw-headline}

A tela inicial exibirá um calendário com todas as sessões que tem
processos pautados com o membro do Ministério Público atuando, agrupadas
por dia.

### [ Painel do secretário da sessão ]{#Painel_do_secret.C3.A1rio_da_sess.C3.A3o .mw-headline}

A tela inicial exibirá um calendário com todas as sessões do órgão
julgador colegiado ao qual o secretário está vinculado, agrupadas por
dia.

### [ Quadro de avisos ]{#Quadro_de_avisos .mw-headline}

O quadro de avisos aparece quando há avisos cadastrados para aquele
perfil. Ele disponibiliza um agrupador que permite a pesquisa de avisos
por período de publicação.

[ Tarefas ]{#Tarefas .mw-headline}
----------------------------------

As tarefas são definidas através da definição de [nós de
tarefa](http://titanio09.cnj.jus.br/wiki/index.php/Configura%C3%A7%C3%A3o_inicial#N.C3.B3_de_tarefa "Configuração inicial").
A instalação padrão do PJe, que pode ser obtida a partir de
[passos](http://titanio09.cnj.jus.br/wiki/index.php/Instala%C3%A7%C3%A3o#Pacote_de_instala.C3.A7.C3.A3o_do_PJe "Instalação")
definidos no [manual de
instalação](http://titanio09.cnj.jus.br/wiki/index.php/Instala%C3%A7%C3%A3o "Instalação"),
tem uma base de dados inicial limpa, que o tribunal precisa instalar e
configurar de acordo com instruções disponíveis no [manual de
configuração](http://titanio09.cnj.jus.br/wiki/index.php/Configura%C3%A7%C3%A3o_inicial "Configuração inicial").
Após a configuração inicial, o tribunal precisa definir [fluxos
processuais](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Fluxo "Manual de referência")
e vinculá-los às [classes
judiciais](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Classe_judicial "Manual de referência")
que serão atendidas pelo PJe. Os
[fluxos](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Fluxo_processual "Manual de referência")
contêm as tarefas. Exibiremos aqui tarefas comuns utilizadas pelos
tribunais que já têm comportamentos definidos dentro do sistema. A
[árvore de
tarefas](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#.C3.81rvore_de_tarefas "Manual de referência")
é um componente do PJe que obedece a uma estrutura visual pré-definida,
sempre exibindo as tarefas agrupadas por seus nomes em conjunto com o
quantitativo de processos judiciais que se encontram na tarefa e
vinculados à localização do usuário. O comportamento do agrupamento de
tarefas é determinado por [regras de
interface](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI193 "Regras de interface").

Os processos vinculados à tarefa são exibidos do lado direito da árvore
de tarefas, conforme regra
[RI193](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI193 "Regras de interface").
O usuário [executa a
tarefa](http://titanio09.cnj.jus.br/wiki/index.php/Abrir_tarefa "Abrir tarefa")
naquele processo interagindo com os ícones, observada as regra de
[bloqueio](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn500 "Regras de negócio")
e
[desbloqueio](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn505 "Regras de negócio")
de processo.

O usuário, dentro da área de processos, poderá utilizar a filtrar ainda
mais os processos exibidos através do [agrupador de
pesquisa](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Agrupadores_de_pesquisa "Manual de referência")
disponibilizado. Conforme regra
[RN506](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn506 "Regras de negócio"),
o resultado da pesquisa no agrupador abrange apenas os processos
listados naquele agrupamento, ou seja, se processos estão em caixas e a
consulta está sendo realizado no agrupamento de processos da tarefa (não
da caixa), os processos da caixa não retornarão na lista resultante.

### [ Barra de tarefas ]{#Barra_de_tarefas .mw-headline}

A descrição do comportamentro da barra de tarefas está presente em
[Painel do
usuário](http://titanio09.cnj.jus.br/wiki/index.php/Painel_do_usu%C3%A1rio "Painel do usuário").

### [ Tarefas de audiência ]{#Tarefas_de_audi.C3.AAncia .mw-headline}

Em construção

Aqui agruparemos as informações das tarefas de fluxo relacionadas a
audiências. As tarefas relacionadas são de
[designação](/wiki/funcionalidades.md#Designar_audi.C3.AAncia "Funcionalidades")
e de
[operações](/wiki/funcionalidades.md#Opera.C3.A7.C3.B5es_da_audi.C3.AAncia "Funcionalidades").
As duas tarefas têm em comum o controle de realização das audiências por
[etapas](/wiki/funcionalidades.md#Etapas "Funcionalidades").
Durante a execução da tarefa, as audiências passam de uma
\"[etapa](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD113 "Regras de domínio")\"
para outra, conforme opções disponíveis na tela. A tela é redesenhada de
acordo com a etapa de execução da tarefa selecionada pelo usuário.

#### [ Designar audiência ]{#Designar_audi.C3.AAncia .mw-headline}

Tarefa configurada por meio de utilização do frame abaDesignarAudiencia

**Dados do processo**

No canto superior esquerdo da tela da tarefa são exibidos os \"Dados do
processo\" na forma de um quadro contendo as seguintes informações:

-   Processo - Número do processo
-   Data de autuação
-   Data da distribuição
-   Classe judicial - Nome e código da classe do processo
-   Órgão julgador - Nome do órgão julgador ao qual o processo está
    atribuído

**Documentos do processo**

No canto superior direito da tela de tarefa são exibidos os \"Documentos
do processo \<xxxxxx-xx.xxxx.x.xx.xxxx\>\" na forma de um quadro
contendo as seguintes informações:

-   Coluna contendo contendo a barra de ferramentas, que consiste no
    ícone de visualização do documento e no ícone de visualização de sua
    assinatura
-   ID - Número identificador do documento
-   Descrição
-   Anexado por - Nome do usuário que assinou o documento
-   Anexado em - Data da assinatura do documento

É também exibida uma barra de navegação e os documentos são paginados.
Cada página contém três documentos.

**Últimas audiências do processo**

São exibidas as \"Últimas audiência do processo\" na forma de um quadro
contendo as seguintes informações:

-   Sala da audiência
-   Tipo da audiência
-   Data da audiência
-   Status
    -   \"Remarcado\" para audiências redesignadas
        ([statusAudiencia](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD108 "Regras de domínio")
        = \'R\')
    -   \"Convertido em Diligência\" para audiências convertidas em
        diligência
        ([statusAudiencia](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD108 "Regras de domínio")
        = \'D\')
    -   \"Cancelado\" para audiências canceladas
        ([statusAudiencia](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD108 "Regras de domínio")
        = \'C\')
    -   \"Realizada\" para audiências realizadas
        ([statusAudiencia](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD108 "Regras de domínio")
        = \'F\')
    -   \"Não realizada\" para audiências não realizadas
        ([statusAudiencia](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD108 "Regras de domínio")
        = \'N\')
-   Ações - Barra de ferramentas de audiência, disponível disponível
    apenas para usuários internos e para audiências designadas
    ([statusAudiencia](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD108 "Regras de domínio")
    = \'M\'), exibindo as seguintes ações:
    -   Realização - quando o parâmetro
        [\"pje:audiencia:realizacaoEmFluxo\"](http://titanio09.cnj.jus.br/wiki/index.php?title=%22pje:audiencia:realizacaoEmFluxo%22&action=edit&redlink=1 ""pje:audiencia:realizacaoEmFluxo" (página inexistente)"){.new}
        não estiver configurado e não for justiça do trabalho
    -   Redesignar
    -   Cancelamento
    -   Converter em diligência

#### [ Audiência ]{#Audi.C3.AAncia .mw-headline}

##### [ Etapas ]{#Etapas .mw-headline}

**Audiências do Processo** (Inicial)

Esse agrupador é exibido apenas quando a etapa da de execução da tarefa
é a inicial ([etapaAudiencia =
\'I\'](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD113 "Regras de domínio"))

São exibidas, paginadas em grupos de 16, todas as audiências do processo
[status diferente de
\'P\'](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD108 "Regras de domínio")).

Para cada audiência, serão exibidas as seguintes informações:

-   Data de inicio
-   Tipo de audiência
-   Sala
-   Status da audiência
-   Ações:

Para usuário que não sejam advogados ou procuradores, serão exibidas as
opções de atuação na audiência já designada ([status =
\'M\'](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD108 "Regras de domínio")):

-   -   Realização (link disponível apenas se o parâmetro
        realizarAudienciaEmFluxo estiver marcado como false)

Esse link inicia a etapa de realização

\

-   -   Redesignar

Esse link inicia a etapa de remarcação

-   -   Cancelamento

Esse link inicia a etapa de cancelamento

-   -   Converter em Diligência

Esse link inicia a etapa da conversão em diligência

Para audiências com status diferente de deginada, não são exibidos os
links.

As seguintes marcações são apresentadas

-   Remarcado - statusAudiencia == \'R\'
-   Convertido em Diligência - statusAudiencia == \'D\'
-   Cancelado - statusAudiencia == \'C\'
-   Realizada - statusAudiencia == \'F\'
-   Não Realizada - statusAudiencia == \'N\'

\
**Audiência** (Marcação)

\
Exibida para audiências que estão em manutenção
(processoAudienciaHome.managed)

**Audiência reservada** (ou **Configuração atual** para etapas
diferentes de marcação)

Esse agrupador é exibido apenas quando a etapa da de execução da tarefa
é a de marcação ([etapaAudiencia =
\'M\'](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD113 "Regras de domínio"))

Ele exibe as seguintes informações:

-   Tipo de audiência
-   Sala
-   Início
-   Término
-   Situação
-   Designação

\
Pauta de audiência

(Redesignação)

Esse agrupador é exibido apenas quando a etapaAudiencia = \'L\'

**Assuntos** (Cancelamento/Conversão em diligência)

Esse agrupador é exibido apenas quando a etapaAudiencia = \'C\' ou \'D\'

**Realizar audiência** (Realização)

Esse agrupador é exibido apenas quando a etapaAudiencia = \'R\'

\
Fim do Em construção

### [ Retificar autuação ]{#Retificar_autua.C3.A7.C3.A3o .mw-headline}

São exibidos os processos pendentes da tarefa \"Retificar autuação\" e
que estejam vinculados à localização do usuário.

O comportamento dessa tarefa é similar ao comportamento da
funcionalidade de [Retificar
autuação](/wiki/funcionalidades.md#Retificar_autua.C3.A7.C3.A3o_2 "Funcionalidades").

Recomenda-se utilizar a opção de configuração da atividade em tarefa em
detrimento da utilização do item de menu.

### [ Preparar juntada ]{#Preparar_juntada .mw-headline}

São exibidos os processos pendentes da tarefa \"Preparar juntada\" e que
estejam vinculados à localização do usuário. Ao acionar a opção
\"Digitalizar documentos\" na triagem comum do fluxo principal
(exemplo:fluxo principal do CNJ), o processo será encaminhado para essa
tarefa. A configuração dessa tarefa deve ser realizada, em geral, no
subfluxo destinado a permitir a digitalização de documentos, denominado
[Digitalizar
documentos](http://titanio09.cnj.jus.br/wiki/index.php?title=Digitalizar_documentos&action=edit&redlink=1 "Digitalizar documentos (página inexistente)"){.new}.

O usuário poderá vincular documentos digitalizados a um dos documentos
principais do processo, conforme regra
[RN396](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn396 "Regras de negócio").

As restrições para inserção são:

-   [quantidade de
    arquivos](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn284 "Regras de negócio")
-   [tamanhos e
    tipos](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn285 "Regras de negócio")
-   [informações sobre os
    arquivos](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn286 "Regras de negócio")
-   [ordenação](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn287 "Regras de negócio")

Na exclusão, que é possível para documentos não assinados, aplica-se a
regra
[pertinente](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn504 "Regras de negócio").

### [ Avaliar juntada ]{#Avaliar_juntada .mw-headline}

São exibidos os processos pendentes da tarefa \"Avaliar juntada\" e que
estejam vinculados à localização do usuário. O encaminhamento de um
processo para avaliação dos documentos digitalizados é realizado na
tarefa de preparação. A avaliação consiste na verificação dos documentos
digitalizados posterior assinatura para que constem definitivamente no
processo. A configuração dessa tarefa deve ser realizada, em geral, no
subfluxo destinado a permitir a digitalização de documentos, denominado
[Digitalizar
documentos](http://titanio09.cnj.jus.br/wiki/index.php?title=Digitalizar_documentos&action=edit&redlink=1 "Digitalizar documentos (página inexistente)"){.new}.

Na exclusão de documentos digitalizados, que é possível para documentos
não assinados, aplica-se a regra
[pertinente](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn504 "Regras de negócio").

### [ Preparar comunicação ]{#Preparar_comunica.C3.A7.C3.A3o .mw-headline}

São exibidos os processos pendentes da tarefa \"Preparar comunicação\" e
que estejam vinculados à localização do usuário. Ao acionar a intimação
de uma parte através do fluxo principal, o processo será encaminhado
para essa tarefa. A configuração da tarefa de preparo de expedientes
deve ser realizada, em geral, no subfluxo destinado a permitir o preparo
de atos de comunicação, denominado [Preparar ato de comunicação
(PAC)](http://titanio09.cnj.jus.br/wiki/index.php/Preparar_ato_de_comunica%C3%A7%C3%A3o "Preparar ato de comunicação").

O usuário poderá escolher os destinatários com seus respectivos tipos e
[meios](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD95 "Regras de domínio")
de comunicação, [tipos de
prazo](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD96 "Regras de domínio"),
endereços e a vinculação do expediente em si, com possibilidade de
[vinculação de documentos do
processo](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn382 "Regras de negócio")
e posterior assinatura. A tarefa será exibida para papéis e localizações
que tenham sido configurados.

**Regras de negócio relacionadas:**

-   [RN501 - Expediente por meio
    eletrônico](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn501 "Regras de negócio")
-   [RN541 - Expediente por meio
    telefônico](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn541 "Regras de negócio")

### [ Imprimir correspondência ]{#Imprimir_correspond.C3.AAncia .mw-headline}

### [ Redistribuição ]{#Redistribui.C3.A7.C3.A3o .mw-headline}

Regras relacionadas:

-   [RN370](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn370 "Regras de negócio") -
    Redistribuição pontual
-   [RN479](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn479 "Regras de negócio") -
    Redistribuição por prevenção
-   [RN605](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn605 "Regras de negócio") -
    Regra para audiências marcadas no órgão julgador de origem

### [ Minutar ato ]{#Minutar_ato .mw-headline}

São exibidos os processos pendentes da tarefa \"Minutar ato\" e que
estejam vinculados à localização do usuário. A confecção da minuta se dá
através de editor de textos do PJe. O usuário pode utilizar tipos de
documentos e modelos de documentos diversos para a minuta, de acordo com
a
[configuração](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn348 "Regras de negócio")
relacionada a esses tipos e modelos e também pela configuração dos
modelos no próprio fluxo. A confecção da minuta deve gerar uma
movimentação processual. Essa movimentação é selecionada através do
[lançador de
movimentos](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI20 "Regras de interface"),
configurado no evento de tarefa devido. O lançador permite a
[pesquisa](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn342 "Regras de negócio")
e seleção de movimentos associados à tarefa sendo executada. A pesquisa
permite que se consulte movimentos [por código ou por
descrição](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI206 "Regras de interface").
Após selecionar o movimento no lançador de movimentos e gravar os dados,
o sistema deve apresentar a próxima ação. A tarefa de minutar ato
geralmente é configurada no subfluxo de [Preparar ato judicial
(PAJ)](http://titanio09.cnj.jus.br/wiki/index.php/Preparar_ato_judicial "Preparar ato judicial").

#### [ Minutar em lote ]{#Minutar_em_lote .mw-headline}

Para tarefas de minuta que tenham sido
[configuradas](http://titanio09.cnj.jus.br/wiki/index.php/Movimenta%C3%A7%C3%A3o,_despacho_e_assinatura_em_lote#Minutar_em_lote "Movimentação, despacho e assinatura em lote")
para poderem ser executadas em lote, acima do [agrupador de
pesquisa](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Agrupadores_de_pesquisa "Manual de referência"),
o título da tarefa é exibido acompanhado da opção de execução em lote.
Ao selecionar a opção, a lista de resultado da pesquisa será exibida com
[caixas de
seleção](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sele.C3.A7.C3.A3o "Manual de referência")
ao lado de cada processo de modo a permitir que o usuário possa
selecionar quais processos serão utilizados. É permitida também a
[seleção
agrupada](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn270 "Regras de negócio")
de processos através de opções fornecidas no cabeçalho da coluna
referente às caixas de seleção. Além disso, o
[botão](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Bot.C3.B5es "Manual de referência")
que permitirá o prosseguimento da tarefa em lote aparecerá abaixo do
agrupador de pesquisa de processos.

Ao selecionar o botão da tarefa em lote, o usuário terá a tela do
minutar exibida contendo os processos selecionados para execução de
tarefas em lote, permitindo que se visualize os
[detalhes](/wiki/funcionalidades.md#Ver_detalhes "Funcionalidades")
do processo ao clicar no número do processo, conforme [comportamento
padrão](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI193 "Regras de interface")
na árvore de tarefas. Cada processo terá também as transições de saída
na forma de uma [caixa de
combinação](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Caixas_de_combina.C3.A7.C3.A3o "Manual de referência")
posicionada à direita do descritivo de cada processo com [transições de
saída previamente
selecionadas](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn272 "Regras de negócio"),
permitindo ao usuário a [troca de
transições](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn273 "Regras de negócio")
para cada processo ou a seleção de uma [mesma
transição](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn274 "Regras de negócio")
para todos os processos.

Ao confirmar a execução da tarefa, o sistema
[executará](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn267 "Regras de negócio")
o que for definido na tela para [todos os processos
selecionados](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn269 "Regras de negócio"),
assim como os procedimentos [configurados na
tarefa](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn268 "Regras de negócio").

**Regras de Negócio relacionadas**:\
[RN537 (Minutar em
lote)](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn537 "Regras de negócio")

### [ Confirmar ato ]{#Confirmar_ato .mw-headline}

Essa tarefa exibe os processos pendentes de confirmação, e que estejam
vinculados à localização do usuário. O sistema recupera o texto inserido
no momento da minuta (dentro do editor de textos), sendo que esse texto
poderá ser alterado ou excluído. Assim como na tarefa "Minutar ato", o
usuário pode utilizar os tipos de documentos e modelos para a minuta.

### [ Redistribuir processo ]{#Redistribuir_processo .mw-headline}

São exibidos os processos pendentes da tarefa Redistribuir processo e
que estejam vinculados à localização do usuário. Um magistrado que se
considere impedido de julgar algum processo pode enviá-lo para
redistribuição. A configuração da tarefa de redistribuição deve ser
realizada no ponto do fluxo onde o magistrado toma a decisão de declarar
o impedimento. Geralmente essa configuração se dá no subfluxo destinado
a permitir o cumprimento de decisões de magistrados denominado
[Cumprimento de decisão
(CUMPRIDEC)](http://titanio09.cnj.jus.br/wiki/index.php/Cumprimento_de_decis%C3%A3o "Cumprimento de decisão").

### [ Reclassificar tipo de documento ]{#Reclassificar_tipo_de_documento .mw-headline}

São exibidos os processos pendentes da tarefa \"Reclassificar tipo de
documento\" e que estejam vinculados à localização do usuário.

A tarefa \"Reclassificar tipo de documento\" permite que usuários
autorizados possam retificar a classificação de um documento após este
ter sido anexado em um processo judicial e, além disso, prosseguir com o
processo judicial para a próxima tarefa do fluxo, de acordo com a
[configuração](http://titanio09.cnj.jus.br/wiki/index.php/Reclassificar_tipo_de_documento "Reclassificar tipo de documento").
Um papel específico foi definido para usar essa tarefa conforme regra
[RN326](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn326 "Regras de negócio").

A regra
[RI194](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI194 "Regras de interface")
explica a especificação da janela responsável por reclassificar tipo de
documento.

Esta funcionalidade possui casos de teste elaborados na ferramenta
[Testlink](http://www.cnj.jus.br/testlink){.external .text}:

-   o caso de teste **PJe:711** orienta como retificar a classificação
    de um documento após este ter sido anexado em um processo judicial;
-   o caso de teste **PJe:741** orienta como desfazer as alterações
    feitas na tarefa responsável pela reclassificação do tipo de
    documento de um processo judicial.

Outras regras relacionadas:

[RN602](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn602 "Regras de negócio")
- Regra de tipos de documentos disponíveis para reclassificação
[RN603](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn603 "Regras de negócio")
- Regra de documentos disponíveis para reclassificação

### [ Preparar remessa para o 2º grau ]{#Preparar_remessa_para_o_2.C2.BA_grau .mw-headline}

São exibidos os processos pendentes da tarefa \"Preparar remessa para o
2º grau\" e que estejam vinculados à localização do usuário.

A tarefa \"Preparar remessa para o 2º grau\" permite que a instância de
1º grau de um tribunal **elabore uma remessa de um processo judicial**
para ser oportunamente enviada para uma instância do 2º grau. Além do
envio dessa remessa, **é possível efetuar a baixa de processos** do 2º
para o 1º grau.

A configuração da tarefa \"Preparar remessa para o 2º grau\" e das
demais configurações pertinentes podem ser configuradas em algum fluxo
conforme necessidade do tribunal; essa configuração pode ser consultada
no **roteiro** publicado em [Preparar remessa para o 2º
grau](http://titanio09.cnj.jus.br/wiki/index.php/Preparar_remessa_para_o_2%C2%BA_grau "Preparar remessa para o 2º grau").

A regra
[RI4](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI4 "Regras de interface")
explica a especificação da janela responsável por preparar remessa para
o 2º grau.\
A regra
[RI104](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI104 "Regras de interface")
explica a especificação da janela responsável pela baixa de processos do
2º para o 1º grau.

Esta funcionalidade possui casos de teste elaborados na ferramenta
[Testlink](http://www.cnj.jus.br/testlink){.external .text}:

-   o caso de teste **PJe:846** orienta a preparação de remessa de uma
    manifestação processual de um processo judicial em uma instalação do
    PJe de 1º grau e o envio dessa remessa à instância de 2º grau;
-   o caso de teste **PJe:851** orienta a respeito da baixa de processos
    judiciais de 2º grau para instância de origem (1º grau).

### [ Preparar remessa de manifestação processual para envio à instância superior ]{#Preparar_remessa_de_manifesta.C3.A7.C3.A3o_processual_para_envio_.C3.A0_inst.C3.A2ncia_superior .mw-headline}

São exibidos os processos pendentes da tarefa \"Preparar remessa de
manifestação processual para envio à instância superior\" e que estejam
vinculados à localização do usuário.

A tarefa \"Preparar remessa de manifestação processual para envio à
instância superior\" permite elaborar uma remessa de uma manifestação
processual de um processo judicial para ser oportunamente enviada para
uma instância superior (**STF** ou **STJ**). Após entrega dessa
manifestação processual, fica sob a responsabilidade da instância
superior consultar mais detalhes do processo no órgão responsável pela
remessa desse processo (processo judicial que dá origem à manifestação
processual).

A configuração da tarefa \"Preparar remessa de manifestação processual
para envio à instância superior\" pode ser configurada em algum fluxo
conforme necessidade do tribunal; essa configuração se dá no subfluxo
destinado a permitir o preparo de remessa denominado [Preparar remessa
de manifestação processual para envio à instância
superior](http://titanio09.cnj.jus.br/wiki/index.php/Preparar_remessa_de_manifesta%C3%A7%C3%A3o_processual_para_envio_%C3%A0_inst%C3%A2ncia_superior "Preparar remessa de manifestação processual para envio à instância superior").
Um papel específico foi definido para usar essa tarefa conforme regra
[RN343](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn343 "Regras de negócio").

A regra
[RI195](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI195 "Regras de interface")
explica a especificação da janela responsável por preparar remessa de
manifestação processual para envio à instância superior. Esta
funcionalidade possui casos de teste elaborados na ferramenta
[Testlink](http://www.cnj.jus.br/testlink){.external .text}:

-   o caso de teste **PJe:777** orienta a preparação de remessa de uma
    manifestação processual de um processo judicial em uma instalação do
    PJe para posterior envio à instância superior STF.

Nota: a **baixa de processos do STF** ainda não foi especificada, favor
acompanhar a demanda
[PJEII-17537](http://www.cnj.jus.br/jira/browse/PJEII-17537){.external
.text}.

### [ Informação processual complementar ]{#Informa.C3.A7.C3.A3o_processual_complementar .mw-headline}

\[Este item está EM CONSTRUÇÃO, assim como os subitens relacionados\]

Uma informação processual complementar (ou IPC) serve para anexar uma
informação estruturada ao processo judicial que não esteja prevista no
núcleo do PJe. A priori, cada instalação do PJe receberá um conjunto de
informações processuais complementares (ou IPCs) pré-configuradas. No
futuro será disponibilizado um módulo configurador no qual o
administrador do PJe poderá configurar as IPCs de acordo com as
necessidades do tribunal. Toda IPC é anexada ao processo por meio uma
tarefa de fluxo denominada, normalmente, como \"Informação processual
complementar\" e, nessa tarefa são exibidos os processos judiciais que
estão pendentes e que estejam vinculados à localização do usuário. Essa
tarefa tem como proposta estruturar as IPCs que sejam relevantes ao
trâmite do processo judicial.

No que toca às questões criminais, essa tarefa permite ao usuário o
cadastramento dos diversos tipos de IPCs considerados relevantes e que
poderão ser aplicados tanto para processo de conhecimento, processo de
execução e processo cautelar. Um tipo de IPC relacionado ao contexto
criminal é configurado por meio de um nó de tarefa.

Mais detalhes sobre como configurar nós de tarefa para o cadastramento
de IPC consulte as próximas subseções.

\

#### [ Informação processual complementar do tipo prisão ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_pris.C3.A3o .mw-headline}

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo prisão" em que estejam vinculados à localização do
usuário.

A tarefa \"Informação processual complementar do tipo prisão\" permite
ao usuário o cadastramento das informações designadas ao ato de prender
ou capturar alguém. A funcionalidade recupera e apresenta para o usuário
as informações do processo judicial corrente, réus do processo,
movimentações e documentos vinculados e permite também cadastrar os
dados pertinentes da \"Informação processual complementar do tipo
prisão\" tais como: [\"tipo da
prisão\"](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD3 "Regras de domínio"),
\"data do fato\", \"local de prisão\", entre outras informações. Para
configurar essa tarefa consulte em: [nó de tarefa \"Informação
processual complementar do tipo
prisão\"](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_pris%C3%A3o "Informação processual complementar do tipo prisão").
A regra de negócio
[RN45](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn45 "Regras de negócio")
apresenta a especificação completa de IPC do tipo prisão.

#### [ Informação processual complementar do tipo fuga ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_fuga .mw-headline}

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo fuga" em que estejam vinculados à localização do
usuário.

A tarefa \"Informação processual complementar do tipo fuga\" permite ao
usuário o cadastramento das informações do ato de fuga do réu. O
cadastro da fuga será associado a uma prisão (neste caso, uma IPC do
tipo prisão) já cadastrada no sistema; os dados dessa prisão ou de um
conjunto de prisões serão apresentados em uma lista para que o usuário
selecione e vincule à informação de prisão. Também serão recuperados
outros dados do processo judicial corrente como: movimentações e
documentos vinculados ao processo. Para configurar essa tarefa consulte
em: [nó de tarefa \"Informação processual complementar do tipo
fuga\"](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_fuga "Informação processual complementar do tipo fuga").
A regra de negócio
[RN425](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn425 "Regras de negócio")
apresenta a especificação completa de IPC do tipo fuga.

#### [ Informação processual complementar do tipo soltura ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_soltura .mw-headline}

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo soltura" em que estejam vinculados à localização do
usuário.

A tarefa "Informação processual complementar do tipo soltura" permite ao
usuário registrar a soltura do réu. Para configurar essa tarefa consulte
em: [nó de tarefa \"Informação processual complementar do tipo
soltura\"](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_soltura "Informação processual complementar do tipo soltura").
A regra de negócio
[RN46](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn46 "Regras de negócio")
apresenta a especificação completa de IPC do tipo soltura.

#### [ Informação processual complementar de alguns tipos da área criminal ]{#Informa.C3.A7.C3.A3o_processual_complementar_de_alguns_tipos_da_.C3.A1rea_criminal .mw-headline}

São exibidos os processos pendentes da tarefa "Informação processual
complementar" (**para uso de alguns os tipos de IPC da área criminal**)
em que estejam vinculados à localização do usuário.

Essa tarefa permite ao usuário a escolha do tipo de IPC dentre os tipos
desejados de IPC da área criminal, no ato de realização da tarefa em
questão. Para configurar essa tarefa consulte em: [nó de tarefa
"Informação processual complementar" (**para uso de alguns os tipos de
IPC da área
criminal**)](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_de_alguns_tipos_da_%C3%A1rea_criminal "Informação processual complementar de alguns tipos da área criminal").

#### [ Informação processual complementar de todos os tipos ]{#Informa.C3.A7.C3.A3o_processual_complementar_de_todos_os_tipos .mw-headline}

São exibidos os processos pendentes da tarefa "Informação processual
complementar" (**para uso de todos os tipos de IPC existentes no
sistema**) em que estejam vinculados à localização do usuário.

Essa tarefa permite ao usuário a escolha do tipo de IPC dentre os tipos
desejados de IPC existentes no sistema, no ato de realização da tarefa
em questão. Para configurar essa tarefa consulte em: [nó de tarefa
"Informação processual complementar" (**para uso de todos os tipos de
IPC existentes no
sistema**)](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_de_todos_os_tipos "Informação processual complementar de todos os tipos").

#### [ Informação processual complementar do tipo transferência do réu ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_transfer.C3.AAncia_do_r.C3.A9u .mw-headline}

\[Este item está EM CONSTRUÇÃO\] São exibidos os processos pendentes da
tarefa "Informação processual complementar do tipo transferência do réu"
em que estejam vinculados à localização do usuário.

A tarefa "Informação processual complementar de transferência do réu"
permite ao usuário indica no PJe a transferência do réu entre os
estabelecimentos penais. Conforme previsto no Art. 86 da Lei 7.210, as
penas privativas de liberdade imputadas a um réu podem ser executadas em
outro estabelecimento penal.

Para configurar essa tarefa consulte em: [nó de tarefa \"Informação
processual complementar do tipo transferência do
réu\".](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_transfer%C3%AAncia_do_r%C3%A9u "Informação processual complementar do tipo transferência do réu")
A regra de negócio
[RN34](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn34 "Regras de negócio")
apresenta a especificação completa de IPC do tipo transferência do réu.

#### [ Informação processual complementar do tipo obrigações a pagar ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_obriga.C3.A7.C3.B5es_a_pagar .mw-headline}

\[Este item está EM CONSTRUÇÃO\]

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo obrigações a pagar" em que estejam vinculados à
localização do usuário.

A tarefa "Informação processual complementar do tipo obrigações a pagar"
permite ao usuário registrar informações a respeito das obrigações a
pagar do(s) réu(s) de um processo judicial. Para configurar essa tarefa
consulte em: [nó de tarefa \"Informação processual complementar do tipo
obrigações a
pagar\"](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_obriga%C3%A7%C3%B5es_a_pagar "Informação processual complementar do tipo obrigações a pagar").
A regra de negócio
[RN436](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn436 "Regras de negócio")
apresenta a especificação completa de IPC do tipo obrigações a pagar.

#### [ Informação processual complementar do tipo tipificação do delito ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_tipifica.C3.A7.C3.A3o_do_delito .mw-headline}

\[Este item está EM CONSTRUÇÃO\]

\

#### [ Informação processual complementar do tipo aditamento da denúncia ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_aditamento_da_den.C3.BAncia .mw-headline}

\[Este item está EM CONSTRUÇÃO\]

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo aditamento da denúncia" em que estejam vinculados à
localização do usuário.

A tarefa "Informação processual complementar de aditamento da denúncia"
permite ao usuário indica no PJe a decisão do Juiz que admitiu o
aditamento da denúncia. Para configurar essa tarefa consulte em: [nó de
tarefa \"Informação processual complementar do tipo aditamento da
denúncia\".](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_aditamento_da_den%C3%BAncia "Informação processual complementar do tipo aditamento da denúncia")
A regra de negócio
[RN448](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn448 "Regras de negócio")
apresenta a especificação completa de IPC do tipo aditamento da
denúncia.

#### [ Informação processual complementar do tipo queixa ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_queixa .mw-headline}

\[Este item está EM CONSTRUÇÃO\]

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo queixa" em que estejam vinculados à localização do
usuário.

A tarefa "Informação processual complementar de queixa" permite ao
usuário indica no PJe a decisão do Juiz que admitiu o queixa.

Para configurar essa tarefa consulte em: [nó de tarefa \"Informação
processual complementar do tipo
queixa\".](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_aditamento_da_queixa "Informação processual complementar do tipo aditamento da queixa")
A regra de negócio
[RN453](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn453 "Regras de negócio")
apresenta a especificação completa de IPC do tipo queixa.

\

#### [ Informação processual complementar do tipo aditamento da queixa ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_aditamento_da_queixa .mw-headline}

\[Este item está EM CONSTRUÇÃO\]

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo aditamento da queixa" em que estejam vinculados à
localização do usuário.

A tarefa "Informação processual complementar de aditamento da queixa"
permite ao usuário indica no PJe a decisão do Juiz que admitiu o
aditamento da queixa.

Para configurar essa tarefa consulte em: [nó de tarefa \"Informação
processual complementar do tipo aditamento da
queixa\".](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_aditamento_da_queixa "Informação processual complementar do tipo aditamento da queixa")
A regra de negócio
[RN453](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn453 "Regras de negócio")
apresenta a especificação completa de IPC do tipo aditamento da queixa.

#### [ Informação processual complementar do tipo atribuição de autoria dos fatos ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_atribui.C3.A7.C3.A3o_de_autoria_dos_fatos .mw-headline}

\[Este item está EM CONSTRUÇÃO\]

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo atribuição de autoria dos fatos" em que estejam
vinculados à localização do usuário.

A tarefa "Informação processual complementar de atribuição de autoria
dos fatos" permite ao usuário indica no PJe a decisão do Juiz que
admitiu o atribuição de autoria dos fatos.

Para configurar essa tarefa consulte em: [nó de tarefa \"Informação
processual complementar do tipo atribuição de autoria dos
fatos\".](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_atribui%C3%A7%C3%A3o_de_autoria_dos_fatos "Informação processual complementar do tipo atribuição de autoria dos fatos")
A regra de negócio
[RN456](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn456 "Regras de negócio")
apresenta a especificação completa de IPC do tipo atribuição de autoria
dos fatos.

#### [ Informação processual complementar do tipo desclassificação ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_desclassifica.C3.A7.C3.A3o .mw-headline}

\[Este item está EM CONSTRUÇÃO\]

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo desclassificação" em que estejam vinculados à
localização do usuário.

A tarefa "Informação processual complementar de desclassificação"
permite ao usuário indica no PJe a decisão do Juiz que admitiu o
desclassificação.

Para configurar essa tarefa consulte em: [nó de tarefa \"Informação
processual complementar do tipo
desclassificação\".](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_desclassifica%C3%A7%C3%A3o "Informação processual complementar do tipo desclassificação")
A regra de negócio
[RN456](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn456 "Regras de negócio")
apresenta a especificação completa de IPC do tipo desclassificação.

#### [ Informação processual complementar do tipo oferecimento da denúncia ]{#Informa.C3.A7.C3.A3o_processual_complementar_do_tipo_oferecimento_da_den.C3.BAncia .mw-headline}

\[Este item está EM CONSTRUÇÃO\]

São exibidos os processos pendentes da tarefa "Informação processual
complementar do tipo oferecimento da denúncia" em que estejam vinculados
à localização do usuário.

A tarefa "Informação processual complementar de oferecimento da
denúncia" permite ao usuário indica no PJe a decisão que ofereceu a
denúncia. Deve se referir à data em que a decisão foi proferida o
oferecimento da denúncia.

Para configurar essa tarefa consulte em: [nó de tarefa \"Informação
processual complementar do tipo oferecimento da
denúncia\".](http://titanio09.cnj.jus.br/wiki/index.php/Informa%C3%A7%C3%A3o_processual_complementar_do_tipo_oferecimento_da_den%C3%BAncia "Informação processual complementar do tipo oferecimento da denúncia")
A regra de negócio
[RN462](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn462 "Regras de negócio")
apresenta a especificação completa de IPC do tipo oferecimento da
denúncia.

[ Processo ]{#Processo .mw-headline}
------------------------------------

### [ Novo processo ]{#Novo_processo .mw-headline}

Perfil: advogado/procurador/servidor

Essa funcionalidade permite ao usuário autorizado realizar o cadastro de
processos, que consiste na petição inicial juntamente com os documentos
necessários. Ao final do cadastramento, pode-se protocolar o processo, o
que fará com que, desde que bem sucedida a distribuição, a ação seja
considerada como proposta.

Uma breve apresentação das abas da tela \"Cadastro de processo\" é
explicada a seguir e um detalhamento de como cadastrar um novo processo
é explicado
[aqui](http://titanio09.cnj.jus.br/wiki/index.php/Novo_processo "Novo processo").

#### [ Dados iniciais ]{#Dados_iniciais .mw-headline}

As jurisdições são aquelas cadastradas através do cadastro de
jurisdições e devem ser listadas conforme regra
[RN409](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn409 "Regras de negócio").

Após a seleção da jurisdição, as classes devem aparecer conforme regra
[RN402](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn402 "Regras de negócio").

#### [ Assuntos ]{#Assuntos .mw-headline}

Os assuntos vinculados à classe selecionada conforme configuração de
competência da classe respectiva serão disponibilizados para seleção.

#### [ Partes ]{#Partes .mw-headline}

Nesta aba, é permitido o [cadastro das partes do
processo](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn348 "Regras de negócio").

As partes podem estar no [polo ativo,
passivo](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn355 "Regras de negócio")
ou podem ser [outros
participantes](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn356 "Regras de negócio")
do processo. Para todas as partes, pode-se [cadastrar
procurador(es)/terceiro(s)
vinculado(s)](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn313 "Regras de negócio")
à parte de acordo com as [respectivas
validações](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn265 "Regras de negócio").

Ao adicionar uma parte no polo ativo ou passivo, pode-se selecionar se é
[uma pessoa física, jurídica ou uma
autoridade](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn357 "Regras de negócio").

Regras relacionadas:

-   Cadastro de autoridades:
    [RI246](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI246 "Regras de interface")
-   Vinculação de representantes a processos:
    [RN444](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn444 "Regras de negócio")
-   Fornecimento de CPF/CNPJ:
    [RN497](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn497 "Regras de negócio")

##### [ Informações pessoais ]{#Informa.C3.A7.C3.B5es_pessoais .mw-headline}

##### [ Documentos de identificação ]{#Documentos_de_identifica.C3.A7.C3.A3o .mw-headline}

##### [ Endereços ]{#Endere.C3.A7os .mw-headline}

Aqui são cadastrados os endereços da parte.

Deve-se incluir os
[endereços](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn354 "Regras de negócio")
através do
[CEP](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn327 "Regras de negócio").
Sem o CEP previamente cadastrado no PJe, não será possível incluir o
endereço. Pode-se também utilizar a opção de endereço desconhecido,
respeitada a [restrição para
advogados](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn354 "Regras de negócio").

A partir da identificação da parte (CPF ou CNPJ), pode-se ter acesso a
endereços previamente vinculados àquela parte em outro processo, de
acordo com a regra
[RN393](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn393 "Regras de negócio").

Regra relacionada: [exclusão de
endereço](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn359 "Regras de negócio")

##### [ Meios de contato ]{#Meios_de_contato .mw-headline}

O cadastro de meios de contato é exibido de acordo com a regra
[RI216](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI216 "Regras de interface").

##### [ Características pessoais ]{#Caracter.C3.ADsticas_pessoais .mw-headline}

O cadastro de característica pessoais estará disponível desde que a
regra
[RN508](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn508 "Regras de negócio")
tenha sido satisfeita.

O cadastro é exibido de acordo com a regra
[RI217](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI217 "Regras de interface").

#### [ Características ]{#Caracter.C3.ADsticas .mw-headline}

Nessa opção, pode-se registrar pedido de segredo de justiça para o
processo
([RN443](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn443 "Regras de negócio")),
pedido de justiça gratuita, pedido de liminar ou de antecipação de
tutela, o valor da causa e acrescentar as prioridades processuais,
conforme regra
[RN28](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn28 "Regras de negócio").

#### [ Incluir petições e documentos ]{#Incluir_peti.C3.A7.C3.B5es_e_documentos .mw-headline}

Através dessa aba, o usuário poderá escrever a petição. Instruções a
respeito dos requisitos de configuração da petição inicial estão
disponíveis no [roteiro de configuração de
documentos](http://titanio09.cnj.jus.br/wiki/index.php/Roteiro_de_configura%C3%A7%C3%A3o_de_documentos#Peti.C3.A7.C3.A3o_no_protocolo_de_processos "Roteiro de configuração de documentos").

Com a petição inicial, o usuário pode anexar outros documentos.

Podem ser adicionados documentos de acordo com a seguinte sistemática:

-   o sistema apresenta ao usuário botão para adição de arquivos;
-   o usuário seleciona e envia um ou mais arquivos para adição,
    limitando-se a lista aos arquivos de extensões específicas
    configuradas na aplicação PJe;
-   o sistema recebe os arquivos, verifica o respeito aos tipos de
    arquivos permitidos e seus respectivos tamanhos, exibindo tabela na
    qual o usuário deverá preencher os dados necessários à gravação
    definitiva; a tabela exibida também informará se o documento já está
    assinado eletronicamente;
-   o usuário complementa os dados (tipo de documento, sua descrição, se
    requer sigilo judicial a seu respeito e a ordem de inclusão) e
    seleciona o botão \[Gravar\] ou o botão \[Assinar eletronicamente e
    protocolar\]
-   o sistema informa se o protocolo foi bem sucedido.

O usuário tem a opção de remover um arquivo anteriormente adicionado até
o momento do
[protocolo](/wiki/funcionalidades.md#Protocolar "Funcionalidades").

Regras associadas:

-   [RN284](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn284 "Regras de negócio")
-   [RN285](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn285 "Regras de negócio")
-   [RN286](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn286 "Regras de negócio")
-   [RN287](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn287 "Regras de negócio")
-   [RN565](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn565 "Regras de negócio")
-   [RN566](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn566 "Regras de negócio")

#### [ Dados específicos da classe ]{#Dados_espec.C3.ADficos_da_classe .mw-headline}

Através dessa aba, o usuário poderá incluir dados complementares
configurados especificamente para a classe processual selecionada. Esta
aba só deverá ser exibida se a classe processual estiver configurada com
estes campos complementares. Os campos complementares deverão atender à
configuração especificada em [configuração de campos
complementares](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Aplica.C3.A7.C3.A3o "Manual de referência"),
relacionada à
[RN535](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn535 "Regras de negócio").

#### [ Processo ]{#Processo_2 .mw-headline}

##### [ Protocolar ]{#Protocolar .mw-headline}

Ao
[protocolar](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn392 "Regras de negócio"),
o processo será
[distribuído](http://titanio09.cnj.jus.br/wiki/index.php/Distribui%C3%A7%C3%A3o "Distribuição").
A verificação de prevenção se dá nesse momento, conforme regras
[RN303](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn303 "Regras de negócio")
e
[RN364](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn364 "Regras de negócio").

\

### [ Novo processo incidental ]{#Novo_processo_incidental .mw-headline}

Perfil: advogado/procurador/servidor

Processo incidental é aquele que, estando vinculado a um processo já em
curso, é interposto por uma das partes ou por terceiro com o objetivo de
obter tutela jurisdicional que não deve ou não pode ser obtida nos autos
ditos principais.

Regras relacionadas:

Processo incidente

-   [RN360](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn360 "Regras de negócio")
-   [RN374](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn374 "Regras de negócio")
-   [RN403](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn403 "Regras de negócio")
-   [RN464](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn464 "Regras de negócio")
-   [RN465](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn465 "Regras de negócio")
-   [RN466](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn466 "Regras de negócio")
-   [RI25](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI25 "Regras de interface")
-   [RI66](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI66 "Regras de interface")
-   [RI72](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI72 "Regras de interface")

Gerais

-   [RN277](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn277 "Regras de negócio")
-   [RN278](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn278 "Regras de negócio")
-   [RN279](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn279 "Regras de negócio")
-   [RN280](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn280 "Regras de negócio")
-   [RN281](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn281 "Regras de negócio")
-   [RN299](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn299 "Regras de negócio")
-   [RN303](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn303 "Regras de negócio")
-   [RN308](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn308 "Regras de negócio")
-   [RN313](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn313 "Regras de negócio")
-   [RN314](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn314 "Regras de negócio")
-   [RN333](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn333 "Regras de negócio")
-   [RI75](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI75 "Regras de interface")
-   [RI150](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI75 "Regras de interface")

\

### [ Novo processo com Jus Postulandi ]{#Novo_processo_com_Jus_Postulandi .mw-headline}

Perfil: jus postulandi (pessoa física validada)

Jus postulandi é a capacidade que se faculta a alguém de postular, ou se
defender, perante as instâncias judiciárias, as suas pretensões na
Justiça, sem a necessidade de ser acompanhada por advogado. O cadastro
de processo desta funcionalidade é adequado às características de
peticionamento próprias, onde os dados a serem fornecidos são distintos.
A restrição
[RN493](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn493 "Regras de negócio")
determina o comportamento do cadastro de partes no polo ativo.

\

### [ Complementação do cadastro - Processo não protocolado ]{#Complementa.C3.A7.C3.A3o_do_cadastro_-_Processo_n.C3.A3o_protocolado .mw-headline}

Perfil: advogado/procurador/servidor

Essa funcionalidade existe para permitir que o cadastro do processo seja
iniciado em um momento e terminado em outro, com a guarda dos dados já
digitados. Poderão ser visualizados todos os processos não protocolados
([em
elaboração](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD104 "Regras de domínio"))
de acordo com a [permissão do
usuário](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn483 "Regras de negócio").

A barra de paginação
[![Paginacao.png](Funcionalidades%20-%20PJe_arquivos/Paginacao.png){width="172"
height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Paginacao.png){.image}
é exibida ao final da tabela em seu canto inferior esquerdo e o total de
registros encontrados é exibido em seu canto inferior direito. Os botões
da barra de paginação serão habilitados a partir de 12 processos,
quantidade limite para exibição por página.

### [ Pesquisa ]{#Pesquisa .mw-headline}

As pesquisas relacionados aos processos estão agrupadas nessa
funcionalidade.

#### [ Processo ]{#Processo_3 .mw-headline}

Perfil: advogado/procurador/servidor

Contempla a pesquisa de processos e respectivos detalhes cadastrais do
juízo de acordo com a localização do usuário.

Os seguintes campos estão disponíveis para filtrar os resultados da
consulta:

-   CPF/CNPJ
-   Número do processo
-   Assunto
-   Classe judicial
-   Número do documento
-   OAB
-   Órgão julgador colegiado
-   Órgão julgador
-   Data de autuação
-   Valor da causa

\
Para cada processo que atende aos critérios da pesquisa são retornadas
as seguintes informações:

-   Ícone
    [![Oculos.jpg](Funcionalidades%20-%20PJe_arquivos/Oculos.jpg){width="16"
    height="21"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Oculos.jpg){.image}
    para detalhamento do processo (\"Abrir paginador\")
-   Processo
-   Prioridades
-   Órgão julgador
-   Autuado em
-   Classe judicial
-   Polo ativo
-   Polo passivo
-   Nó(s) atual(is)
-   Ícone [![Mr pje
    alerta1.jpg](Funcionalidades%20-%20PJe_arquivos/30px-Mr_pje_alerta1.jpg){width="30"
    height="25"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Mr_pje_alerta1.jpg){.image}
    para processos que têm pelo menos uma prioridade registrada

A barra de paginação
[![Paginacao.png](Funcionalidades%20-%20PJe_arquivos/Paginacao.png){width="172"
height="20"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Paginacao.png){.image}
é exibida ao final da tabela em seu canto inferior esquerdo e o total de
registros encontrados é exibido em seu canto inferior direito. Os botões
da barra de paginação serão habilitados a partir de 10 processos,
quantidade limite para exibição por página.

As seguintes regras devem ser observadas:

-   [RN469](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn469 "Regras de negócio")
-   [RN470](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn470 "Regras de negócio")
-   [RN511](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn511 "Regras de negócio") -
    regra para visualização da tarefa da qual o processo está pendente
    de execução

##### [ Ver detalhes ]{#Ver_detalhes .mw-headline}

Opção acionada através do ícone
[![Oculos.jpg](Funcionalidades%20-%20PJe_arquivos/Oculos.jpg){width="16"
height="21"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Oculos.jpg){.image}
(vulgo bob esponja) ou de link no número do processo.

###### [ Paginador ]{#Paginador .mw-headline}

Opção acionada através do ícone
[![Cpver.png](Funcionalidades%20-%20PJe_arquivos/Cpver.png){width="48"
height="48"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Cpver.png){.image}.

###### [ Cabeçalho do processo ]{#Cabe.C3.A7alho_do_processo .mw-headline}

O cabeçalho do processo é exibido no canto superior esquerdo da tela de
detalhes, ao lado do ícone do
[![Cpver.png](Funcionalidades%20-%20PJe_arquivos/Cpver.png){width="48"
height="48"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Cpver.png){.image}.

Ele é composto da seguintes informações:

-   Órgão julgador/Cargo - a descrição do órgão julgador do processo e
    do cargo judicial a ele vinculado. Para instâncias de revisão, é
    exibida primeiramente a descrição do órgão julgador colegiado.
-   abreviação da classe e número do processo -
-   polo ativo X polo passivo

###### [ Ferramentas ]{#Ferramentas .mw-headline}

Opção acionada através do ícone
[![Sigilo.png](Funcionalidades%20-%20PJe_arquivos/Sigilo.png){width="32"
height="32"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Sigilo.png){.image}.

-   Iniciar atividade de digitalização: Regra
    [RN519](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn519 "Regras de negócio")
    contém restrições para que opção esteja disponível
-   Exibir situações atuais do processo / Ocultar situações atuais do
    processo (Regra
    [RN581](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn581 "Regras de negócio"))
    (papel pje:papel:visualizaSituacoes)

Ao acionar essa opção, são exibidas, em uma lista no topo da tela de
detalhes, logo abaixo do cabeçalho do processo, as situações atuais do
processo com a data e a hora de seu início. A opção ficará, então,
disponível, como \"Ocultar situações atuais do processo\".

-   Exibir situações do processo / Ocultar situações do processo (Regra
    [RN581](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn581 "Regras de negócio"))
    (papel pje:papel:visualizaSituacoes)

Ao acionar essa opção, são exibidas, em uma lista no topo da tela de
detalhes, logo abaixo do cabeçalho do processo, as situações já
encerradas do processo com a data e a hora de seu início e data e a hora
de seu encerramento. A opção ficará, então, disponível, como \"Ocultar
situações do processo\".

-   Editar objeto do processo
-   Controle de sigilo: Detalhamento das opções de sigilo disponível no
    detalhamento do processo no [roteiro de
    utilização](http://titanio09.cnj.jus.br/wiki/index.php/Roteiro_de_utiliza%C3%A7%C3%A3o_de_sigilo_e_segredo_de_justi%C3%A7a#Detalhes_do_processo "Roteiro de utilização de sigilo e segredo de justiça").

###### [ Dados do processo ]{#Dados_do_processo .mw-headline}

###### [ Processo ]{#Processo_4 .mw-headline}

-   Detalhes do processo

Para instalações de segundo grau, é exibido o [campo de
seleção](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Campos_de_sele.C3.A7.C3.A3o "Manual de referência")
para [selecionar para
pauta](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn387 "Regras de negócio"),
que permite que o processo seja selecionado através dessa tela,
alternativamente à seleção através da opção pelo
[fluxo](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn526 "Regras de negócio").

-   Documentos

Tabela que retorna todos os documentos que foram incluídos no processo.
Para maiores detalhes, ver regra
[RI309](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI309 "Regras de interface").

-   Movimentações do Processo

Tabela que retorna todos os movimentos registrados, respeitando as
regras
[RN567](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn567 "Regras de negócio")
e
[RN559](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn559 "Regras de negócio").
A exibição dos movimentos é determinada pela regra
[RI246](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI246 "Regras de interface").

###### [ Anexar documentos ]{#Anexar_documentos .mw-headline}

Através dessa aba, o usuário poderá adicionar documentos, utilizando
também a opção de anexos de documentos já produzidos em outros
aplicativos. Podem ser adicionados documentos de acordo com a seguinte
sistemática:

-   o sistema apresenta ao usuário botão para adição de arquivos;
-   o usuário seleciona e envia um ou mais arquivos para adição,
    limitando-se a lista aos arquivos de extensões específicas
    configuradas na aplicação PJe;
-   o sistema recebe os arquivos, verifica o respeito aos tipos de
    arquivos permitidos e seus respectivos tamanhos, exibindo tabela na
    qual o usuário deverá preencher os dados necessários à gravação
    definitiva; a tabela exibida também informará se o documento já está
    assinado eletronicamente;
-   o usuário complementa os dados (tipo de documento, sua descrição, se
    requer sigilo judicial a seu respeito e a ordem de inclusão) e
    seleciona o botão \[Gravar\] ou o botão \[Assinar eletronicamente\]
-   o sistema informa se a assinatura foi bem sucedida.

O usuário tem a opção de remover um arquivo anteriormente adicionado até
o momento da assinatura.

Regras associadas:

-   [RN284](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn284 "Regras de negócio")
-   [RN285](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn285 "Regras de negócio")
-   [RN286](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn286 "Regras de negócio")
-   [RN287](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn287 "Regras de negócio")

###### [ Aba Expedientes ]{#Aba_Expedientes .mw-headline}

É por meio dessa aba que o usuário poderá
[visualizar](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI310 "Regras de interface")
todos expedientes do processo em questão, além de possuir a alternativa
de tomar a ciência do ato de comunicação quando algum expediente lhe for
designado.

###### [ Segredo ou sigilo ]{#Segredo_ou_sigilo .mw-headline}

###### [ Associados ]{#Associados .mw-headline}

Nessa aba são exibidos os processos associados ao processo objeto do
detalhamento. Os processo associados são aqueles que foi registrada
conexão por algum dos motivos [previstos no
PJe](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD99 "Regras de domínio"),
ou seja, dependência, desmembramento, prevenção ou vinculação indireta.
Os processos físicos ou que não estão na instalação do PJe não são
listados nessa opção em decorrência da regra
[RN474](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn474 "Regras de negócio").

Para cada processo encontrado, são exibidas as seguintes informações:

-   Processo - número do processo
-   Órgão julgador
-   Classe judicial
-   Assunto
-   Polo ativo
-   Polo passivo
-   Situação - o motivo da associação, conforme opções do PJe da regra
    [RD99](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_dom%C3%ADnio#RD99 "Regras de domínio")
-   Status
-   Prevenção confirmada em
-   Despacho
-   Data de registro

###### [ Petições avulsas ]{#Peti.C3.A7.C3.B5es_avulsas .mw-headline}

Nessa aba são exibidas as [petições avulsas não
apreciadas](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn571 "Regras de negócio")
de acordo com as permissões descritas na
[RN570](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn570 "Regras de negócio").

\
Para cada petição não apreciada, são exibidas as seguintes informações:

-   Documento - descrição do documento
-   Tipo de documento
-   Visualizar petição - ícone
    [![Oculos.jpg](Funcionalidades%20-%20PJe_arquivos/Oculos.jpg){width="16"
    height="21"}](http://titanio09.cnj.jus.br/wiki/index.php/Arquivo:Oculos.jpg){.image}
    que permite visualizar o documento
-   Coluna contendo registro \"Declaro, sob as penas da lei, que neste
    ato apresentei instrumento de mandato\"

###### [ Anexos ]{#Anexos .mw-headline}

Aqui são exibidos os documentos juntados após a distribuição do processo
por advogado ou procurador.

###### [ Acesso de terceiros ]{#Acesso_de_terceiros .mw-headline}

São listados os acessos registrados de terceiros interessados no
processo conforme regra
[RN452](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn452 "Regras de negócio").

#### [ Localizações ]{#Localiza.C3.A7.C3.B5es .mw-headline}

Perfil: servidor

Localizações contemplam a estrutura interna de um tribunal. Ela é
utilizada tanto para a definição da estrutura hierárquica do tribunal
quanto para a organização interna de outras "entidades" participantes do
processo, tais como os advogados, seus escritórios de advocacia, as
procuradorias e defensorias públicas. Além disso, por meio dela, é
possível definir os "setores" de um determinado órgão julgador, ou seja,
indicar que uma vara será composta por um gabinete, pela direção de
secretaria ou direção do cartório, e pelos setores de conhecimento,
expedição de atos de comunicação, execução etc. A [localização limita o
conjunto de processos visualizáveis pelos usuários]{.ul} do sistema.
Através dessa funcionalidade, o [usuário
interno](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn394 "Regras de negócio")
(diretor de secretaria, magistrado, assessor\...) pode pesquisar onde se
encontram os processos que ele tem permissão de visualizar. Ele
visualiza a localização do processo, assim como as tarefas pelas quais o
processo já passou. Além disso, ele tem acesso a um quantitativo de
processos por tarefas.

#### [ Informações de distribuição ]{#Informa.C3.A7.C3.B5es_de_distribui.C3.A7.C3.A3o .mw-headline}

Perfil: servidor

Essa funcionalidade visa dar mais transparência ao processo de
distribuição uma vez que permite que o [usuário
interno](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn394 "Regras de negócio")
pesquise e visualize o passo a passo do procedimento automático de
distribuição por processo efetivamente distribuído, contemplando todos
os valores levados em consideração para cálculo do peso e finalização do
procedimento .

#### [ Processo não distribuído ]{#Processo_n.C3.A3o_distribu.C3.ADdo .mw-headline}

Perfil: servidor

Para instalações do PJe onde o sistema está com distribuição configurada
para ser manual (acontece, via de regra, só no segundo grau), essa
consulta é muito útil para identificar os processos que ainda precisam
ser distribuídos.

#### [ Banco Nacional de Devedores Trabalhistas ]{#Banco_Nacional_de_Devedores_Trabalhistas .mw-headline}

Essa opção permite a consulta ao Banco Nacional de Devedores
Trabalhistas através de integração via web service. Ela está disponível
para usuários internos.

#### [ Consulta de processos de terceiros ]{#Consulta_de_processos_de_terceiros .mw-headline}

Perfil: advogado/procurador/servidor

Permite a consulta de processos aos quais não esteja vinculado a
advogados, procuradores e membros do Ministério Público cadastrados,
desde que demonstrado interesse, conforme regra
[RN452](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn452 "Regras de negócio").

Esse acesso está depreciado, devendo ser utilizada a [pesquisa de
processos](/wiki/funcionalidades.md#Processo_3 "Funcionalidades")
para a consulta.

#### [ Consulta de processos de outras seções ]{#Consulta_de_processos_de_outras_se.C3.A7.C3.B5es .mw-headline}

Perfil: servidor

Permite a consulta de processos de outras seções, já que a consulta
padrão leva em consideração a localização do usuário para delimitar a
consulta. Essa funcionalidade obedece à regra
[RN312](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn312 "Regras de negócio").

#### [ Consulta de prazos ]{#Consulta_de_prazos .mw-headline}

Perfil: servidor

Essa funcionalidade disponibiliza uma consulta de expedientes de forma
que se possa fechá-los em lote ou não.

A tela se constitui de um formulário de filtros e uma tela de
resultados, que exibirá os expedientes (equivalentes à entidade
ProcessoParteExpediente) com uma barra de tarefas associada que
permitirá ao usuário dar manutenção nos expedientes selecionados.

No canto superior esquerdo do formulário de filtros, é apresentada a
data de hoje. Os filtros disponíveis são os seguintes:

-   Número do processo
-   Período do prazo final - o usuário pode fornecer data de início e
    fim que será consulta conforme a seguinte regra
    -   se data de início e fim foram fornecidas, serão retornados
        expedientes cujo prazo legal (data limite para manifestação)
        esteja entre as duas datas, incluindo as data informadas.
    -   se data de início for fornecida, serão retornados expedientes
        cujo prazo legal seja maior ou igual que a data informada
    -   se data de fim for fornecida, serão retornados expedientes cujo
        prazo legal seja menor ou igual que a data informada
-   Prazo vencido? - o usuário pode pesquisar por
    -   expedientes com prazo vencido - expedientes que tenham prazo
        legal e cujo prazo seja menor que a data atual
    -   expedientes com prazo não vencido - expedientes que não tenham
        prazo legal ou tenham e o prazo seja maior ou igual que a data
        atual
    -   ou pode consultar sem levar em consideração o parâmetro
-   Expediente fechado? - o usuário pode pesquisar por expedientes
    fechados, não fechados, ou pode consultar sem levar em consideração
    o parâmetro
-   Ato - tipo de ato associado ao documento - serão retornados
    expedientes que tenham a eles associados documentos do tipo
    informado como parâmetro
-   Órgão julgador - para instalações de segundo grau, só serão
    carregados os órgão julgadores vinculados ao órgão julgador
    colegiado do usuário logado. Para usuários não vinculados a órgão
    julgador colegiado, não serão carregados órgãos julgadores.
-   Destinatário
-   Classe judicial
-   Assunto
-   Prioridades
-   Tarefas - serão carregadas tarefas configuradas na instalação de
    acordo com a view do banco de dados SituacaoProcesso. Para usuários
    cuja visualização esteja marcada como restrita (opção padrão do
    sistema), só serão retornadas tarefas vinculadas ao órgão julgador
    do usuário logado. Para usuários que não estejam vinculados a órgão
    julgador e cujo perfil de visualização seja restrito, a combo não
    será exibida, já que não teria conteúdo.

Inicialmente, a tela é carregada com todos os expedientes disponíveis na
instalação do PJe, paginados em grupos de 15.

No cabeçalho da consulta, há o ícone de pdf que permite que seja gerado
um relatório pdf a partir da consulta realizada. Também há o checkbox
que permite ao usuário selecionar todos os expedientes retornados da
consulta para posterior manutenção por meio de botão adequado descrito
mais adiante. Além disso, são retornados os nomes dos campos referentes
à cada coluna.

Para cada expediente encontrado, a tela apresenta as seguintes
informações:

-   Barra de tarefas
    -   Ícone de detalhes do processo
    -   Ícone de manutenção do expediente em exibição
-   checkbox de seleção - permite que o usuário selecione o expediente
    em exibição para posterior manutenção em lote por meio de botão
    adequado descrito mais adiante - virá desabilitado para expedientes
    fechados
-   Status
-   Processo
-   Expediente - Tipo do documento
-   Meio do expediente
-   Destinatário
-   Prazo final
-   Classe judicial
-   Tarefa atual

Os expedientes serão paginados em grupos de 15.

Caso seja selecionado algum expediente para manutenção, será exibido o
botão:

\"Fechar expedientes em lote\".

Se o usuário selecionar o botão e houver algum expediente selecionado
para fechamento cujo prazo não esteja vencido, o sistema solicitará
confirmação do usuário quanto ao fechamento.

##### [ Abrir expediente ]{#Abrir_expediente .mw-headline}

Ao acionar a opção de abrir o expediente, o sistema exibirá o
detalhamento do expediente conforme especificado abaixo:

-   Ato de comunicação
    -   Tipo de documento (número do documento)
    -   Destinatário do espediente
    -   Representante/Advogado
    -   Meio de expedição (data e hora de expedição)
    -   Prazo para ciência ou, para expedientes com ciência já
        realizada, pessoa que realização ciência e data e hora de
        registro
    -   Tipo do prazo

```{=html}
<!-- -->
```
-   Data limite prevista para ciência ou manifestação
-   Documentos
-   Fechado
    -   SIM/NÃO

Para expedientes abertos, desde que o usuário logado tenha o papel
\"ServConhe\", será exibido o botão \"Fechar expediente\", que o usuário
poderá acionar para fechar o expediente em tela.

#### [ Certidão Interna ]{#Certid.C3.A3o_Interna .mw-headline}

Perfil: administrador

Essa funcionalidade tem como objetivo realizar a pesquisa de certidões
positivas ou negativas, tendo como base a pessoa cadastrada nos polos de
um processo.

#### [ Certidão Externa ]{#Certid.C3.A3o_Externa .mw-headline}

Perfil: Usuário externo, sem necessidade de cadastramento no PJe

Essa funcionalidade tem como objetivo realizar a pesquisa de certidões
negativas, tendo como base a pessoa cadastrada nos polos de um processo.

\
TAG: certidão, certidão negativa

### [ Cadastro - Habilitação nos autos ]{#Cadastro_-_Habilita.C3.A7.C3.A3o_nos_autos .mw-headline}

Mesmo comportamento do [Solicitar
habilitação](/wiki/funcionalidades.md#Solicitar_habilita.C3.A7.C3.A3o "Funcionalidades").

### [ Outras ações ]{#Outras_a.C3.A7.C3.B5es .mw-headline}

#### [ Ajustar movimentação ]{#Ajustar_movimenta.C3.A7.C3.A3o .mw-headline}

Perfil: magistrado

Por padrão, não há ajuste em movimentação. É permitido excluir apenas as
que estão configuradas expressamente com essa característica através da
[configuração da
movimentação](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn375 "Regras de negócio").

#### [ Associar processos ]{#Associar_processos .mw-headline}

Perfil: diretor de secretaria/magistrado

Regra relacionada:
[RN464](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn464 "Regras de negócio")

A associação de processos ocorre quando se deseja que processos sejam
vinculados. A vinculação não faz com que os processos tramitem em
conjunto. A associação pode ocorrer por três motivos:

-   dependência - ocorre quando um processo é diretamente vinculado, por
    norma legal, a um principal, como os embargos à execução quanto à
    execução ou a impugnação ao valor da causa quanto ao principal (deve
    ser observada a regra
    [RN373](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn373 "Regras de negócio"));
-   prevenção - ocorre quando um processo é vinculado, por decisão
    judicial, a outro processo, nos casos em que se reconhece uma
    circunstância legal que determina a tramitação em um mesmo juízo
    (deve ser observada a regra
    [RN373](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn373 "Regras de negócio"));
-   desmembramento - ocorre quanto aos processos derivados de um
    processo originário, após a determinação do desmembramento.

#### [ Chamar à ordem ]{#Chamar_.C3.A0_ordem .mw-headline}

Perfil: administrador

Deve-se chamar o feito à ordem quando verificada a existência de erro
material e deste decorram atos que não poderiam ser determinados, em
face da decisão prolatada. Através dessa opção, faz-se o chamamento,
suspendendo o processo. Essa atividade será possível para processos de
classes judiciais cujo fluxo configurado tenha um nó de desvio. Sendo
assim, tarefas que possibilitem a chamada terão como um dos possíveis
destinos o nó de desvio.

#### [ Enviar processo ]{#Enviar_processo .mw-headline}

Funcionalidade utilizada quando se deseja remeter o processo à outra
instância.

#### [ Incluir alerta ]{#Incluir_alerta .mw-headline}

Perfil: diretor de secretaria/magistrado/administrador

Esta funcionalidade está disponível para usuários servidores. Permite
incluir alertas associados a processos para que os usuários que os
visualizem sejam notificados. Os alertas são exibidos ao serem
visualizados os detalhes do processo.

#### [ Incluir informação criminal relevante ]{#Incluir_informa.C3.A7.C3.A3o_criminal_relevante .mw-headline}

Essa opção permite vincular ao processo informações que são relevantes
para o seu andamento e análise. Por exemplo, informações sobre fuga de
uma das partes do processo que por ventura esteja presa podem implicar a
suspensão da parte.

#### [ Liberar visualização de documentos ]{#Liberar_visualiza.C3.A7.C3.A3o_de_documentos .mw-headline}

Perfil: diretor de secretaria/administrador

O magistrado poderá determinar que sejam realizados por meio eletrônico
a exibição e o envio de dados e de documentos necessários à instrução do
processo.

#### [ Retificar autuação ]{#Retificar_autua.C3.A7.C3.A3o_2 .mw-headline}

Perfil: servidor retificador

É permitida a retificação dos autos do processo para usuários
servidores, ressalvada a regra
[RN307](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn307 "Regras de negócio").
A retificação de autuação pode ser demandada por diversos motivos. Uma
das partes pode solicitar a retificação da autuação via petição anexada
ao processo. Por exemplo, para incluir um novo advogado como
representante da parte pode-se fazer através de petição, que será
analisada internamente pela vara aonde o processo foi distribuído. Caso
o pedido seja considerado válido, será realizada a retificação dos autos
do processo através dessa opção. Outra situação é a intervenção de
terceiro, que ocorre quando uma terceira parte, diante de um processo em
andamento, deseja fazer parte do processo.\
Antes de efetuar a retificação dos autos, é necessário que o
administrador do sistema inclua o(s) tipo(s) de parte desejado(s) nas
classes judiciais em uso no sistema. Essa inclusão pode ser feita por
meio da **Aba Tipo da parte** localizada em ([Configuração → Tabelas
Judiciais → Classe Judicial → Classe
Judicial](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Classe_judicial_2 "Manual de referência")).

Observação Recomenda-se utilizar a opção de configuração da atividade
[em
tarefa](/wiki/funcionalidades.md#Retificar_autua.C3.A7.C3.A3o "Funcionalidades")
em detrimento da utilização do item de menu.

#### [ Solicitar habilitação ]{#Solicitar_habilita.C3.A7.C3.A3o .mw-headline}

Perfil: advogado

\
Essa funcionalidade permite que um advogado se [habilite em um processo
(regra
RN376)](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn376 "Regras de negócio")
em andamento. Por exemplo, uma parte x (polo ativo) entra com uma ação,
representada por seu advogado, contra uma outra parte y (polo passivo).
O advogado que desejar se habilitar, de posse do nº do processo e da
procuração respectiva, poderá solicitar habilitação nos autos para
representar o seu cliente. O advogado solicita habilitação e o
magistrado examina a petição e documentos anexados na solicitação de
habilitação, mas a habilitação é realizada automaticamente. Deve ser
observada ainda, a regra
[RN300](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn300 "Regras de negócio")
quando se tratar de processo em segredo de justiça. Para perfis que não
devem ter acesso à funcionalidade, o sistema não deve disponibilizar o
menu ou deve impedir a utilização, utilizando como referência a mensagem
[MN176](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_mensagens#MN176 "Regras de mensagens").
A possibilidade de habilitação e substituição prevê a notificação do
substituído do fato. O advogado pode também realizar a habilitação por
substabelecimento, que também prevê a notificação do substabelecente do
fato. As notificações seguem a regra
[RN620](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn620 "Regras de negócio")

#### [ Peticionamento avulso ]{#Peticionamento_avulso .mw-headline}

(opção disponível a partir da versão 1.6.0 como \"Peticionar\"

Perfil: advogado/procurador/assistente de advogado/assistente de
procurador

A funcionalidade permite que:

1.  advogados atuem em processos onde as partes já representadas desejam
    destituir seus patronos;
2.  advogados solicitem permissão para atuar em processos que tramitam
    em segredo de justiça;
3.  advogados solicitem habilitação em processos onde a parte não figure
    na relação processual;
4.  advogados solicitem honorários após terem sido destituídos do
    processo;
5.  procuradores solicitem habilitação em processos nos quais necessitem
    atuar como \'custos legis\';
6.  advogados realizem peticionamentos diversos;

Regras relacionadas:

-   [Regra de vinculação do advogado ao
    processo](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn413 "Regras de negócio")
-   [Regra de permissão para utilização da funcionalidade e assinatura
    as
    petições](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn414 "Regras de negócio")

[ Atividades ]{#Atividades .mw-headline}
----------------------------------------

### [ Assinar documentos pendentes ]{#Assinar_documentos_pendentes .mw-headline}

Perfil: advogado/procurador/servidor

Permite que se
[assine](http://titanio09.cnj.jus.br/wiki/index.php/Regras_de_interface#RI244 "Regras de interface")
os documentos principais que estão [pendentes de
assinatura](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn378 "Regras de negócio"),
respeitando as regras de
[visibilidade](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn379 "Regras de negócio")
do usuário logado.

### [ Avisos ]{#Avisos .mw-headline}

Perfil: administrador

Avisos personalizados podem ser lançados funcionando como lembrete para
cada perfil de usuário que acesse o sistema. Essa funcionalidade permite
a inclusão dos avisos, que serão visualizados pelo usuário através do
agrupador de
[mensagens](/wiki/funcionalidades.md#Mensagens "Funcionalidades")
disponibilizado na [página
principal](/wiki/funcionalidades.md#P.C3.A1gina_principal "Funcionalidades").

### [ Consulta pessoa ]{#Consulta_pessoa .mw-headline}

Perfil: diretor de secretaria/oficial de justiça

É a consulta de pessoas do PJe, contemplando todos os perfis
cadastrados.

### [ Criar relação pessoal ]{#Criar_rela.C3.A7.C3.A3o_pessoal .mw-headline}

Perfil: administrador

O cadastro de relações pessoais é um cadastro liberado, ordinariamente,
apenas para o administrador. Nele, são registradas relações puramente
pessoais -- ou seja, aquelas relações entre duas pessoas que não estão
vinculadas a um processo. São exemplos desse tipo de relação a curatela,
a tutela e sucessões legalmente determinadas. Uma vez registradas tais
relações, espera-se viabilizar um melhor controle das atividades das
pessoas no sistema.

### [ Unificar pessoas ]{#Unificar_pessoas .mw-headline}

Perfil: administrador

A unificação está prevista no cadastro de pessoa física ou jurídica para
permitir que uma mesma pessoa registrada com nomes diferentes seja
referenciada pelo sistema como única. Neste caso, serão unificados os
documentos de identificação, os nomes alternativos, os expedientes e as
participações em processos.

\

### [ Desunificar pessoas ]{#Desunificar_pessoas .mw-headline}

Perfil: administrador

A funcionalidade de desunificação se presta a permitir o desfazimento de
uma prévia operação de unificação, inclusive com retorno dos processos
judiciais eventualmente afetados pela unificação ao estado anterior.

### [ Distribuição de expediente ]{#Distribui.C3.A7.C3.A3o_de_expediente .mw-headline}

Perfil: oficial de justiça distribuidor

A distribuição de expediente permite que o usuário possa realizar a
distribuição de expedientes recebidos na central de mandados aos
oficiais de justiça.

Para distribuir um expediente, acesse o PJe com o usuário oficial de
justiça distribuidor, pesquise pelo processo pela funcionalidade Menu
Atividades \> \"Distribuição de expediente\" e pesquise pelo processo,
na última coluna da tela de resultados da pesquisa, clique no check-box
de marcar processo, feito isso, clique no botão \"Distribuir\",
selecione o grupo de oficiais de justiça e selecione o oficial de
justiça ao qual será distribuído, caso o oficial de justiça não seja
selecionado o sistema selecionará um automaticamente.

### [ Emitir certidão ]{#Emitir_certid.C3.A3o .mw-headline}

Perfil: administrador/advogado/procurador/jus postulandi/magistrado

O juízo deve dar, independentemente de despacho, certidão de qualquer
ato ou termo do processo. O direito de pedir certidões dos atos
processuais é restrito às partes e a seus procuradores. O terceiro, que
demonstrar interesse jurídico, pode requerer ao juiz certidão do
dispositivo da sentença, bem como de inventário e partilha resultante do
desquite.

Veja
[aqui](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn352 "Regras de negócio")
como configurar.

### [ Pauta de perícia ]{#Pauta_de_per.C3.ADcia .mw-headline}

Perfil: diretor de secretaria

Essa funcionalidade permite a verificação das perícias agendadas, com
designação dos peritos, datas e especificidades da atividade.

### [ Recebimento de expediente físico ]{#Recebimento_de_expediente_f.C3.ADsico .mw-headline}

Perfil: oficial de justiça

Essa funcionalidade permite que o usuário registre expedientes físicos
em um processo judicial no sistema. Por exemplo, o registro de avisos de
recebimento.

### [ Redistribuição de expediente ]{#Redistribui.C3.A7.C3.A3o_de_expediente .mw-headline}

Perfil: oficial de justiça distribuidor

A redistribuição de expediente permite que o usuário possa alterar a
distribuição de expedientes já feita aos oficiais de justiça.

### [ Registrar disponibilidade de perito ]{#Registrar_disponibilidade_de_perito .mw-headline}

Perfil: perito / servidor perícia

Registra a disponibilidade do perito com os dias e os horários em que
ele pode ser convocado.

### [ Registrar indisponibilidade de perito ]{#Registrar_indisponibilidade_de_perito .mw-headline}

Perfil: perito/servidor perícia

Faz um bloqueio da agenda do perito para determinado período.

### [ Requisição de antecipação de pagamento de perito ]{#Requisi.C3.A7.C3.A3o_de_antecipa.C3.A7.C3.A3o_de_pagamento_de_perito .mw-headline}

Perfil: administrador perícia

Considerando a necessidade, em muitos processos, de produção de prova
pericial para demonstração da procedência da pretensão posta em juízo e
a regra geral vertida no art. 19 do Código de Processo Civil, de
antecipação da despesa do ato pela parte que o requer, essa
funcionalidade se destina a registrar as requisições de antecipação de
pagamento de perito.

### [ Elaborar RPV ou precatório ]{#Elaborar_RPV_ou_precat.C3.B3rio .mw-headline}

Perfil: administrador

Essa opção permite a elaboração por parte do tribunal de precatórios ou
requisições de pequeno valor a serem pagos a beneficiários em razão de
decisão transitada em julgado referente a um dado processo judicial.

### [ Imprimir RPV e precatórios ]{#Imprimir_RPV_e_precat.C3.B3rios .mw-headline}

Perfil: administrador

Essa opção permite a impressão da RPV ou do precatório emitido na opção
[Elaborar RPV ou
precatório](/wiki/funcionalidades.md#Elaborar_RPV_ou_precat.C3.B3rio "Funcionalidades")

### [ Simular valor a compensar ]{#Simular_valor_a_compensar .mw-headline}

Perfil: administrador

O beneficiário de precatório ou RPV pode utilizar o valor a ser recebido
como forma de compensar débitos que tenha perante a Fazenda Pública.
Essa opção permite a simulação do valor a ser compensado.

### [ Solicitação de antecipação de pagamento de perícia ]{#Solicita.C3.A7.C3.A3o_de_antecipa.C3.A7.C3.A3o_de_pagamento_de_per.C3.ADcia .mw-headline}

Perfil: perito

[ Audiências ]{#Audi.C3.AAncias .mw-headline}
---------------------------------------------

As funcionalidades referentes a audiências e sessões estão agrupadas no
mesmo menu no PJe. O que acontece, na verdade, é que, via de regra, a
utilização de um grupo exclui a utilização do outro grupo, já que as
sessões existem para decisões colegiadas (segunda instância) e as
audiências para as decisões monocráticas (primeira instância).
Descreveremos aqui essas funcionalidades agrupadas pelo respectivo
assunto principal, ou seja, audiências ou sessões.

### [ Pauta de audiência ]{#Pauta_de_audi.C3.AAncia .mw-headline}

Perfil: advogado/procurador

As marcações de audiências acontecem através de tarefas dentro do fluxo
do processo (verifique descrição das tarefas referentes a
[audiências](/wiki/funcionalidades.md#Tarefas_de_audi.C3.AAncias "Funcionalidades")).
Através dessa funcionalidade, tem-se acesso a uma consolidação das
marcações denominada Pauta de audiências, contendo os processos, datas e
outros detalhes das audiências marcadas.

Ver
[RN587](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn587 "Regras de negócio")

### [ Integração com AUD ]{#Integra.C3.A7.C3.A3o_com_AUD .mw-headline}

As funcionalidades dessa opção dizem respeito à integração com o sistema
AUD, que é o sistema de audiências da justiça do trabalho.

#### [ Verificar audiências importadas ]{#Verificar_audi.C3.AAncias_importadas .mw-headline}

#### [ Assinar atar de audiência ]{#Assinar_atar_de_audi.C3.AAncia .mw-headline}

[ Sessões ]{#Sess.C3.B5es .mw-headline}
---------------------------------------

As funcionalidades referentes a audiências e sessões estão agrupadas no
mesmo menu no PJe. O que acontece, na verdade, é que, via de regra, a
utilização de um grupo exclui a utilização do outro grupo, já que as
sessões existem para decisões colegiadas (segunda instância) e as
audiências para as decisões monocráticas (primeira instância).
Descreveremos aqui essas funcionalidades agrupadas pelo respectivo
assunto principal, ou seja, audiências ou sessões.

### [ Acórdão ]{#Ac.C3.B3rd.C3.A3o .mw-headline}

Perfil: assessor

Através dessa funcionalidade, pode-se acessar as minutas dos acórdãos
produzidos a partir de sessões de julgamento e assiná-los.

### [ Cadastro de sessão de julgamento ]{#Cadastro_de_sess.C3.A3o_de_julgamento .mw-headline}

Perfil: secretário da sessão

Através dessa opção, pode-se fazer o cadastramento de sessões de
julgamento, agendando-a e vinculando-a a uma sala de audiência
previamente cadastrada.

#### [ Composição da sessão ]{#Composi.C3.A7.C3.A3o_da_sess.C3.A3o .mw-headline}

### [ Pendências da sessão de julgamento ]{#Pend.C3.AAncias_da_sess.C3.A3o_de_julgamento .mw-headline}

Perfil: secretário da sessão

Essa funcionalidade permite que se verifique as pendências da sessão de
julgamento por processo. Por exemplo, um processo pode ter ficado sem
voto na sessão. Dessa forma, a atividade de finalização da sessão pode
ser facilitada.

### [ Processos pautados em sessão ]{#Processos_pautados_em_sess.C3.A3o .mw-headline}

Perfil: assistente de advogado/assistente de procuradoria/secretário da
sessão/servidor da análise de gabinete/servidor de secretaria

Essa funcionalidade permite a consulta dos processos que já estão com
dia marcado para julgamento, ou seja, já estão vinculados a um sessão.

### [ Relação de julgamento ]{#Rela.C3.A7.C3.A3o_de_julgamento .mw-headline}

Perfil: assessor/secretário da sessão

Regras relacionadas:

[RN291](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn291 "Regras de negócio")

Essa funcionalidade exibe a relação de sessões de julgamento cadastradas
através de um calendário onde pode-se selecionar uma sessão para
inclusão da pauta. Ao selecionar uma sessão, o sistema exibirá em uma
aba a relação de julgamento contendo todos os processos já incluídos,
assim como exibirá as seguinte abas:

#### [ Aptos para inclusão em pauta ]{#Aptos_para_inclus.C3.A3o_em_pauta .mw-headline}

Restrição para exibição de processos:
[RN525](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn525 "Regras de negócio")

#### [ Aptos para inclusão em mesa ]{#Aptos_para_inclus.C3.A3o_em_mesa .mw-headline}

Restrição para exibição de processos:
[RN615](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn615 "Regras de negócio")

#### [ Adiados e pautas anteriores ]{#Adiados_e_pautas_anteriores .mw-headline}

A aba "adiados e pautas anteriores" representa processos que já
estiveram em outra sessão. O sistema sinaliza isso independente de o
processo já ter sido arquivado. Só deixará de estar ali de for incluído
em nova pauta de julgamento. Isso significa que se um processo tiver
sido adiado ou retirado de pauta e o relator desistir de levar a
plenário, o processo sempre aparecerá nessa aba.

#### [ Pedido de vista ]{#Pedido_de_vista .mw-headline}

Nessa aba constarão processos que tiveram pedido de vista registrado em
sessões anteriores. Existe uma marcação \"vista elaborada\" que sinaliza
que o órgão julgador que pediu vista já construiu um documento de voto.
Se o processo for de classe que exige pauta e for liberado para pauta
por meio do fluxo, ele aparecerá em aptos para inclusão em pauta.

#### [ Aptos para publicação ]{#Aptos_para_publica.C3.A7.C3.A3o .mw-headline}

A exibição dessa aba se dará conforme regra
[RN616](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn616 "Regras de negócio").

Caso o conector com o Diário de Justiça esteja disponível, a lista com
os processos aptos para publicação (regra
[RN617](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn617 "Regras de negócio"))
será exibida para que o usuário selecione quais processos irão compor a
publicação, junto com um formulário de pesquisa para auxiliar na
verificação da lista.

\
O botão \"Publicar lista\" será apresentado para usuários detentores do
papel idSecretarioSessao.

Ao clicar em publicar lista, o sistema fará a publicação da pauta de
acordo com a regra
[RN618](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn618 "Regras de negócio").

#### [ Certidão de publicação ]{#Certid.C3.A3o_de_publica.C3.A7.C3.A3o .mw-headline}

São exibidos processos para que sejam emitidas certidões de publicação
de intimação de pauta desde que as respectivas intimações tenham sido
publicadas no DJ com sucesso. (diário retornou a data de publicação para
o PJe)

#### [ Votação antecipada ]{#Vota.C3.A7.C3.A3o_antecipada .mw-headline}

[ Configuração [(cadastros básicos)](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Cadastros_dispon.C3.ADveis "Manual de referência") ]{#Configura.C3.A7.C3.A3o_.28cadastros_b.C3.A1sicos.29 .mw-headline}
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Detalhes sobre as funcionalidades no menu \"Configurações\" estão
disponíveis no [manual de
referência](http://titanio09.cnj.jus.br/wiki/index.php/Manual_de_refer%C3%AAncia#Cadastros_dispon.C3.ADveis "Manual de referência").\
Informações detalhadas sobre as dependências geradas pelas alterações no
menu configurações podem ser encontradas nas [instruções de configuração
inicial](http://titanio09.cnj.jus.br/wiki/index.php/Configura%C3%A7%C3%A3o_inicial#teste "Configuração inicial")
do PJe.

[ Gestão ]{#Gest.C3.A3o .mw-headline}
-------------------------------------

    Justiça aberta - Corregedoria
     Estatísticas
    Monitoramento PJe

### [ Relatório de produtividade órgão julgador/magistrado ]{#Relat.C3.B3rio_de_produtividade_.C3.B3rg.C3.A3o_julgador.2Fmagistrado .mw-headline}

O relatório de produtividade deverá consultar o quantitativo de cada
evento (movimento do processo), separados por juizados (órgão julgador)
ou por magistrados.

Pendência no Jira: <http://www.cnj.jus.br/jira/browse/PJEII-4672>

[ PJe PUSH ]{#PJe_PUSH .mw-headline}
------------------------------------

PJe Push é um tipo de tecnologia utilizada para distribuição de conteúdo
informativo relativo às atualizações dos processos que estão transitando
no PJe. Os informativos são enviados para o e-mail fornecido pelo
usuário no cadastro. Pode utilizar-se desse serviço tanto advogados,
procuradores, magistrados, servidores cadastrados no PJe, quanto
qualquer cidadão comum que tenha interesse no acompanhamento de algum
processo. Informações sobre como utilizar o PJe Push consulte
[aqui](http://titanio09.cnj.jus.br/wiki/index.php/Configura%C3%A7%C3%A3o_inicial#PJe_PUSH "Configuração inicial")
.

\

### [ Minhas assinaturas ]{#Minhas_assinaturas .mw-headline}

Essa opção permite ao usuário do PJe Push cadastrar os processos que
deseja receber os informativos. É executado uma rotina diária, que envia
um e-mail com o resumo das movimentações feitas nos processos que foram
marcados para monitoramento pelo usuário.

[ Assinatura digital ]{#Assinatura_digital .mw-headline}
--------------------------------------------------------

O conceito de autenticidade de um documento está vinculado à identidade
de seu remetente. A certeza da autenticidade deve estar sempre vinculada
a uma característica unívoca da pessoa que assina um documento. Ao longo
da tramitação processual, é necessário que se tenha absoluta certeza de
que o remetente indicado seja efetivamente o signatário daquele
documento eletronicamente produzido ou transmitido. Essa garantia da
autoria do documento, conforme determina a lei
[11.419/06](http://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11419.htm){.external
.text}, pode ser obtida pelo uso de assinatura digital e é extensiva ao
envio de petições, de recursos e à prática de atos processuais em geral.
Sendo assim, sempre que necessária assinatura de documentos inseridos no
processo, o PJe se [utilizará de assinatura
digital](https://docs.pje.jus.br/configura%C3%A7%C3%B5es-do-pje/Regras%20negociais#rn283 "Regras de negócio"),
similarmente à opção de
[login](/wiki/funcionalidades.md#Login "Funcionalidades").
O usuário, de posse de seu certificado, o utiliza para atestar que o
documento produzido foi assinado por ele.

A assinatura digital no PJe é realizada através de uma applet,
aplicativo que executa na estação do cliente, junto com o navegador. A
seguir, os momentos do PJe onde o assinador é acionado:

-   login com certificado
-   assinatura de documento individual em texto do editor do PJe nos
    modos produção e teste
-   assinatura de documento individual acompanhado de anexos nos modos
    produção e teste
-   assinatura de documentos no fluxo de preparar ato de comunicação nos
    modos produção e teste

Em qualquer dos casos, o assinador pode ser utilizado usando o protocolo
https e http, assim como com a configuração de proxy fazendo o desvio de
solicitações para o servidor Jboss.
:::

::: {.printfooter}
Disponível em
\"<http://titanio09.cnj.jus.br/wiki/index.php?title=Funcionalidades&oldid=25247>\"
:::

::: {#catlinks .catlinks .catlinks-allhidden}
:::

::: {.visualClear}
:::
:::
:::

::: {#mw-head .noprint}
::: {#p-personal}
##### Ferramentas pessoais

-   [[Autenticar-se](http://titanio09.cnj.jus.br/wiki/index.php?title=Especial:Autenticar-se&returnto=Funcionalidades "Você é encorajado a autenticar-se, apesar disso não ser obrigatório. [alt-shift-o]")]{#pt-login}
:::

::: {#left-navigation}
::: {#p-namespaces .vectorTabs}
##### Espaços nominais

-   [[Página](/wiki/funcionalidades.md "Ver a página de conteúdo [alt-shift-c]")]{#ca-nstab-main}
-   [[Discussão](http://titanio09.cnj.jus.br/wiki/index.php?title=Discuss%C3%A3o:Funcionalidades&action=edit&redlink=1 "Discussão sobre o conteúdo da página [alt-shift-t]")]{#ca-talk}
:::

::: {#p-variants .vectorMenu .emptyPortlet}
#### 

##### Variantes[](#)

::: {.menu}
:::
:::
:::

::: {#right-navigation}
::: {#p-views .vectorTabs}
##### Visualizações

-   [[Ler](/wiki/funcionalidades.md)]{#ca-view}
-   [[Ver
    código-fonte](http://titanio09.cnj.jus.br/wiki/index.php?title=Funcionalidades&action=edit "Esta página está protegida.
    Você pode, no entanto, visualiar seu código-fonte. [alt-shift-e]")]{#ca-viewsource}
-   [[Ver
    histórico](http://titanio09.cnj.jus.br/wiki/index.php?title=Funcionalidades&action=history "Edições anteriores desta página. [alt-shift-h]")]{#ca-history}
-   [[Imprima como
    PDF](http://titanio09.cnj.jus.br/wiki/index.php?title=Funcionalidades&action=pdfbook&format=single)]{#ca-pdfbook}
:::

::: {#p-cactions .vectorMenu .emptyPortlet}
##### Ações[](#)

::: {.menu}
:::
:::

::: {#p-search}
##### Pesquisar

<div>

</div>
:::
:::
:::

::: {#mw-panel .noprint .collapsible-nav}
::: {#p-logo}
[](http://titanio09.cnj.jus.br/wiki/index.php/P%C3%A1gina_principal "Acessar a página principal")
:::

::: {#p-navigation .portal .first .persistent}
##### Navegação

::: {.body}
-   [[Página
    principal](http://titanio09.cnj.jus.br/wiki/index.php/P%C3%A1gina_principal "Acessar a página principal [alt-shift-z]")]{#n-mainpage-description}
:::
:::

::: {#p-Informa.C3.A7.C3.B5es_Gerais .portal .expanded}
##### [Informações Gerais](#) {#informações-gerais tabindex="2"}

::: {.body style="display: block;"}
-   [[Configuração do
    ambiente](http://titanio09.cnj.jus.br/wiki/index.php/Configura%C3%A7%C3%A3o_do_Ambiente)]{#n-Configura.C3.A7.C3.A3o-do-ambiente}
-   [[Acesso ao
    PJe](http://titanio09.cnj.jus.br/wiki/index.php/Acesso_ao_PJe)]{#n-Acesso-ao-PJe}
:::
:::

::: {#p-Aplicativos_PJe .portal .collapsed}
##### [Aplicativos PJe](#) {#aplicativos-pje tabindex="3"}

::: {.body}
-   [[PJeOffice](http://titanio09.cnj.jus.br/wiki/index.php/PJeOffice)]{#n-PJeOffice}
-   [[Navegador
    PJe](http://titanio09.cnj.jus.br/wiki/index.php/Navegador_PJe)]{#n-Navegador-PJe}
:::
:::

::: {#p-Manuais .portal .collapsed}
##### [Manuais](#) {#manuais tabindex="4"}

::: {.body}
-   [[Advogado](http://titanio09.cnj.jus.br/wiki/index.php/Manual_do_Advogado)]{#n-Advogado}
-   [[Usuário sem
    representação](http://titanio09.cnj.jus.br/wiki/index.php/Manual_do_Usu%C3%A1rio_sem_representa%C3%A7%C3%A3o)]{#n-Usu.C3.A1rio-sem-representa.C3.A7.C3.A3o}
-   [[Representantes](http://titanio09.cnj.jus.br/wiki/index.php/Manual_dos_Representantes)]{#n-Representantes}
-   [[Usuário
    interno](http://titanio09.cnj.jus.br/wiki/index.php/Manual_do_Usu%C3%A1rio_Interno)]{#n-Usu.C3.A1rio-interno}
-   [[PJe
    1.0](http://titanio09.cnj.jus.br/wiki/index.php/PJe_1.0)]{#n-PJe-1.0}
:::
:::

::: {#p-Suporte .portal .collapsed}
##### [Suporte](#) {#suporte tabindex="5"}

::: {.body}
-   [[Solução de
    Problemas](http://titanio09.cnj.jus.br/wiki/index.php/Solu%C3%A7%C3%A3o_de_Problemas)]{#n-Solu.C3.A7.C3.A3o-de-Problemas}
-   [[Centrais de Atendimento do
    PJe](http://titanio09.cnj.jus.br/wiki/index.php/Centrais_de_Atendimento_do_PJe)]{#n-Centrais-de-Atendimento-do-PJe}
:::
:::

::: {#p-tb .portal .collapsed}
##### [Ferramentas](#) {#ferramentas-1 tabindex="6"}

::: {.body}
-   [[Páginas
    afluentes](http://titanio09.cnj.jus.br/wiki/index.php/Especial:P%C3%A1ginas_afluentes/Funcionalidades "Lista de todas as páginas que possuem links para esta [alt-shift-j]")]{#t-whatlinkshere}
-   [[Alterações
    relacionadas](http://titanio09.cnj.jus.br/wiki/index.php/Especial:Mudan%C3%A7as_relacionadas/Funcionalidades "Mudanças recentes nas páginas para as quais esta possui links [alt-shift-k]")]{#t-recentchangeslinked}
-   [[Páginas
    especiais](http://titanio09.cnj.jus.br/wiki/index.php/Especial:P%C3%A1ginas_especiais "Lista de páginas especiais [alt-shift-q]")]{#t-specialpages}
-   [[Versão para
    impressão](http://titanio09.cnj.jus.br/wiki/index.php?title=Funcionalidades&printable=yes "Versão para impressão desta página [alt-shift-p]")]{#t-print}
-   [[Link
    permanente](http://titanio09.cnj.jus.br/wiki/index.php?title=Funcionalidades&oldid=25247 "Link permanente para esta versão desta página")]{#t-permalink}
-   [[Exportar para
    pdf](http://titanio09.cnj.jus.br/wiki/index.php?title=Especial:PdfPrint&page=Funcionalidades)]{#t-pdf}
:::
:::
:::

::: {#footer}
-   [Esta página foi modificada pela última vez às 11h56min de 19 de
    fevereiro de 2021.]{#footer-info-lastmod}
-   [Esta página foi acessada 1 898 503 vezes.]{#footer-info-viewcount}

```{=html}
<!-- -->
```
-   [[Política de
    privacidade](http://titanio09.cnj.jus.br/wiki/index.php/PJe:Pol%C3%ADtica_de_privacidade "PJe:Política de privacidade")]{#footer-places-privacy}
-   [[Sobre
    PJe](http://titanio09.cnj.jus.br/wiki/index.php/PJe:Sobre "PJe:Sobre")]{#footer-places-about}
-   [[Exoneração de
    responsabilidade](http://titanio09.cnj.jus.br/wiki/index.php/PJe:Aviso_geral "PJe:Aviso geral")]{#footer-places-disclaimer}

```{=html}
<!-- -->
```
-   [[![Powered by
    MediaWiki](Funcionalidades%20-%20PJe_arquivos/poweredby_mediawiki_88x31.png){width="88"
    height="31"}](http://www.mediawiki.org/)]{#footer-poweredbyico}

::: {style="clear:both"}
:::
:::

::: {.suggestions style="display: none; font-size: 13.3333px;"}
::: {.suggestions-results}
:::

::: {.suggestions-special}
:::
:::
