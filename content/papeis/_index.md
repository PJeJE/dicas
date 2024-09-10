+++
title = "Papéis e recursos"
date = 2024-09-03T14:07:27-03:00
weight = 13
chapter = true
pre = "<b>12. </b>"
+++

### Seção 12

# Papéis e recursos

{{% children  %}}

O controle de acesso no PJe utiliza o cadastro de pessoas, suas localizações e dois outros conceitos: o de papéis e o de recursos. Por recursos, entenda-se as funcionalidades acessíveis dentro do PJe. São, basicamente, itens de menu. Essas funcionalidades podem ser agrupadas em papéis criados pelo próprio usuário, como um conjunto de funcionalidades. Os papéis, por sua vez, podem conter outros papéis. 

A partir desses elementos, o PJe limita a visão de funcionalidades disponibilizadas ao usuário, reduzindo ou ampliando os menus e as opções disponíveis nos menus. Também limita a visualização de objetos, restringindo o acesso a essas edições. A criação de papéis e sua associação a usuários é livre ao administrador, mas esse tipo de modificação deve ser cuidadosamente planejada a fim de evitar desvios de segurança e integridade das informações. De igual modo, a criação de papéis deve ser acompanhada por uma revisão das definição das raias nos fluxos de negócio, ou seja, a definição das tarefas às quais o usuário pode acessar.

{{% notice note %}}
A redefinição de papéis sem a correspondente revisão das raias pode levar à impressão de que os processos pendentes de tarefas “desapareceram”, já que o usuário que utilizar o novo papel não verá processos pendentes na sua caixa de tarefas. 
{{% /notice %}}


**Papéis e perfis**

É mais natural enxergar os papéis como perfis. O papel **Administrador** na verdade mapeia um perfil de utilização do sistema, ou seja, um tipo de atuação que agrupa permissões diversas para uma série de funcionalidades. Da mesma forma ocorre com o papel **Servidor**. Há muitas situações onde os papéis são usados no PJe como liberação de permissões específicas, e não um agrupamento de permissões. A esses papéis, em geral, não se vincula o cadastro de pessoas. A vinculação é por meio da hierarquia de papéis, ou seja, papéis vinculados a outros papéis.

É importante avaliar a estrutura de papéis de sua aplicação para assegurar que os papéis principais do sistema não herdem funcionalidades uns dos outros. Em outras palavras, por exemplo, servidores não podem ficar "abaixo" de magistrados na hierarquia de papéis, nem tampouco isso pode acontecer com advogados etc. Na estrutura de papéis, deve-se ficar com uma árvore parecida com a seguinte: 

    Administrador (raiz)
        Magistrado
        Servidor
            Assessor
            Assessor de plenário
        Advogado
        Assistente de advogado
        Assistente de procuradoria
        Perito
        Procurador MP
            pje:procurador 
        Procurador
            pje:procurador 
        Oficial de justiça distribuidor
            Oficial de justiça 

Um caso concreto de situações que não devem ocorrer é:
 - o papel assessor-chefe é detentor do papel que permite a ele visualizar processos sigilosos
 - o papel assessor também é detentor do papel que permite a ele visualizar processos sigilosos
 - o papel assessor-chefe é detentor do papel assessor

Essa situação faz com que, ao salvar novos papéis vinculados ao papel assessor-chefe ou ao papel assessor ou ainda a alguma papel acima na sua hierarquia, o sistema tente fazer referências a todos os papéis da hierarquia e entre em uma referência cíclica, impedindo a finalização do cadastro.

Independente de cadastros equivocados, a alteração de papéis é sempre uma atividade demorada para o sistema. Em algumas vezes, pode acontecer de o sistema "desistir" de finalizar devido ao tempo máximo de espera para uma operação ter sido atingido (timeout). Não é desejável aumentar esse tempo então, caso isso ocorra, abra um chamado para que a TI realize a vinculação desejada diretamente por meio de scripts de banco de dados, reportando as evidências de impossibilidade da vinculação por meio da aplicação.

{{% notice note %}}
Ao vincular um novo papel a um papel já existente, a alteração só terá efeito após o usuário sair e entrar novamente na aplicação. Se você é **Administrador** e vinculou um novo papel ao papel **Administrador**, acione o botão **Sair** do PJe para que consiga fazer sua identificação (login) novamente e, aí sim, verificar os efeitos do novo papel adicionado.
{{% /notice %}}

**Instruções para cadastro de papéis e suas vinculações:**

O cadastro de papéis é realizado por meio da opção **Configuração - Controle de acesso - Papéis**. Na aba Formulário, o usuário informa o **Identificador** do papel e o **Nome**. Para papéis que liberam acessos específicos no PJe, o campo **Identificador** deve ser preenchido com o nome do papel exatamente como deve ser utilizado, com respeito às letras maiúsculas e minúsculas. Já o campo **Nome** servirá para facilitar a visualização do próprio usuário sobre o significado do papel ou da visualização do perfil ao qual o usuário está vinculado.

Uma vez cadastrado o papel, a tela de configuração exibe, entre outras informações, as seguintes abas que merecem atenção:

- Papéis
- Herdeiros
- Recursos

A aba **Papéis** exibe dois quadros: 
- uma lista do lado esquerdo contendo todos os papéis no sistema que não cedem permissão ao papel atual
- uma lista do lado direito contendo todos os papéis cadastrados no sistema que cedem permissão ao papel atual

A aba **Herdeiros** exibe dois quadros: 
- uma lista do lado esquerdo contendo todos os papéis no sistema para os quais o papel atual não cede permissão
- uma lista do lado direito contendo todos os papéis cadastrados no sistema para os quais o papel atual cede permissão

Com configurações realizadas nessas abas se realiza a hierarquia de papéis, ou seja, papeis cujas permissões serão aproveitadas por outros papéis. 

Caso concreto onde se deseja vincular o papel **pje:papel:administrarAutuacao** ao **Administrador**: 

    Caso o usuário esteja no cadastro do papel pje:papel:administrarAutuacao, ele deve selecionar a aba Herdeiros e vincular o papel Administrador na lista Papéis para os quais cede permissões.
        Se o usuário cadastrar o Administrador na aba Papeis, o sistema não se comportará como se deseja.
        Nesse caso, o papel pje:papel:administrarAutuacao, que não deve ser vinculado a perfil algum, será detentor de todas as permissões do Administrador, o que não é correto.
    Caso o usuário esteja no cadastro do papel Administrador, ele deve selecionar a aba Papéis e vincular o papel pje:papel:administrarAutuacao na lista Papéis dos quais recebe permissões.
        Se o usuário cadastrar o Administrador na aba Herdeiros, o sistema não se comportará como se deseja.
        Nesse caso, o papel pje:papel:administrarAutuacao, que não deve ser vinculado a perfil algum, será detentor de todas as permissões do Administrador, o que não é correto.
        
A aba **Recursos** exibe dois quadros: 
- uma lista do lado esquerdo contendo todos os recursos do sistema aos quais o papel atual não tem acesso
- uma lista do lado direito contendo todos os recursos do sistema aos quais o papel atual tem acesso

Pode-se realizar a liberação de itens de menu a perfis pela movimentação dos itens entre os dois quadros.

**Instruções para cadastro de funcionalidades e suas vinculações:**

O cadastro de recursos/funcionalidades é realizado por meio da opção **Configuração - Controle de acesso - Funcionalidades**. Por meio da aba Formulário, o usuário coloca o **Identificador** do funcionalidade e o **Nome*. O campo **Identificador** deve ser preenchido com o nome do recurso exatamente como deve ser utilizado, com respeito às letras maiúsculas e minúsculas. Já o campo **Nome** servirá para que o item de menu seja exibido conforme o cadastro, salvo alguns itens que já vêm com o nome estabelecido pela própria versão de produção do PJe.  

Uma vez cadastrado o recurso/funcionalidade, a tela de configuração exibe a aba **Papéis que acessam** que contém dois quadros:
- uma lista contendo todos os papéis do sistema que não acessam a funcionalidade
- uma lista contendo todos os papéis do sistema que acessam a funcionalidade
  
Pode-se realizar a liberação de itens de menu a perfis pela movimentação dos itens entre os dois quadros.
Para melhor identificar qual recurso se deseja acrescentar a um determinado perfil, acesse a tela como Administrador e observe no campo disponível para digitar a URL do seu navegador o que está escrito. Por exemplo, a opção **Processo - Outras ações - Incluir no push**, ao ser acessada, exibe no campo URL o seguinte:

https://pje.tre-go.jus.br/pje/Push/listView.seam

Para esse exemplo, a pesquisa pelo campo **Identificador** da opção **Configuração - Controle de acesso - Funcionalidades** deve ser feita com o termo **pages/Push/listView.seam**. O sistema retornará o recurso vinculado ao item de menu correspondente e o usuário poderá acrescentar/retirar papéis para o acesso a funcionalidade.

{{% notice note %}}
O acesso a tarefas, via de regra, é liberado por meio de alterações do fluxo, sem a necessidade do cadastro de recursos, salvo permissões específicas dentro de algumas tarefas. Além do papel vinculado às respectivas raias de fluxo, o usuário precisa, sim, ter acesso ao painel do usuário por meio do cadastro do recurso do painel, mas essa permissão já está disponível em todas as bases de produção da Justiça Eleitoral para os perfis de servidor. 
{{% /notice %}}



**Vinculação de perfis**

Alguns papéis no PJe são, como já falado mais acima, perfis de utilização, ou seja, agrupam um conjunto de recursos e permissões. Muitas vezes, o cadastro desses perfis será pela própria opção que sinaliza o nome do perfil, ou seja, se o objetivo é cadastrar um magistrado, o cadastro será por **Configuração - Pessoa - Magistrado**, se o objetivo é cadastrar um perito, o cadastro será por **Configuração - Pessoa - Perito**, se o objetivo é cadastrar um procurador, o cadastro será por **Configuração - Pessoa - Procurador**. 

Já para vincular perfis específicos de servidores, o cadastro será por meio da opção **Configuração - Pessoa - Servidor**. Por meio dessa opção, o cadastro deve ser realizado e, posteriormente, a atribuição de papéis/perfis, juntamente com a localização onde o servidor atuará, deve ser realizada pela aba **Localização**, exibida para servidores ativos. 

A exibição das opções dessa aba, ou seja, lista **Órgão julgador colegiado** (só para instâncias que não seja primeiro grau), lista **Órgão julgador**, **Localização física** e **Papel** estão relacionadas ao perfil utilizado pelo usuário cadastrador. Por exemplo, se o usuário cadastrador está vinculado a um órgão julgador colegiado específico, a lista **Órgão julgador colegiado** aparecerá desabilitada para edição com o órgão do usuário cadastrador previamente selecionado. Caso o usuário não seja vinculado a órgão julgador colegiado, o sistema recuperará os colegiados disponíveis naquela instalação que estejam abaixo da localização atual do usuário cadastrador na hierarquia de localizações. Se não houver colegiado com essa característica, a opção ficará desabilitada. 

A exibição da lista **Órgão julgador** depende, a exemplo da lista **Órgão julgador colegiado**, do perfil do usuário cadastrador e da opção selecionada em **Órgão julgador colegiado**. Segue a mesma regra acima, ou seja, obedece à hierarquia de localizações. 

A exibição da lista **Localização** depende, conforme listas descritas acima, do perfil do usuário cadastrador e da(s) opção(ões) selecionada(s) em **Órgão julgador colegiado** e em **Órgão julgador**. Segue a mesma regra acima, ou seja, obedece à hierarquia de localizações. 

A exibição do campo **Modelo de localização** depende da **Localização** selecionada. Caso a **Localização** selecionada não tenha filhos na sua estrutura modelo, essa opção virá preenchida e desabilitada. Caso tenha filhos, o usuário poderá selecionar dentre as localizações modelo disponíveis na estrutura filha da localização física preenchida. 

A exibição do campo **Papel** depende do perfil do usuário cadastrador. Toda a hierarquia de papéis será exibida caso o usuário tenha um dos perfis a seguir: **admin**, **administrador**, **pje:administrador**, **pje:papel:permissaoCadastroUsuarioTodosPapeis** ou um perfil que herde este último. Caso contrário, será exibida a hierarquia de papéis filha do papel do usuário cadastrador. 


**Papéis existentes:**

Abaixo, segue uma lista de papéis pré-definidos e têm comportamentos específicos se cadastrados no PJe
- **pje:sistema**
  - Papel utilizado para vincular ações que sejam realizadas de forma automática
   
- **pje:administrador** ou **admin** ou **administrador**
  - Papel a ser herdado pelos papéis com função de administração em uma instalação do PJe.
 
- **magistrado** ou **pje:magistrado**
  - Papel a ser herdado pelos papéis com função jurisdicional em uma instalação do PJe

- **pje:auxiliarInterno**
  - Papel a ser herdado pelos papéis que atuam como servidores ou auxiliares internos em uma instalação do PJe.
	
- **pje:advogado** ou **advogado**
  - Papel a ser herdado pelos papéis de advogado em uma instalação do PJe

- **pje:assistenteAdvogado** ou **assistAdvogado**
  - Papel a ser herdado pelos papéis de assistente de advogado em uma instalação do PJe.
 
- **pje:perito** ou **perito**
  - Papel a ser herdado pelos papéis de peritos em uma instalação do PJe.
	
- **pje:papel:podeReclassificarDocumento**:
  - Papel que permite visualizar a aba Expedientes dos autos digitais
	
- **pje:visualizaAbaAssociados**
  - Papel que permite visualizar a aba Associados dos autos digitais
 
- **pje:visualizaAbaAssociados260CE**
  - Papel que permite visualizar a aba Associados 260 dos autos digitais
	
- **pje:processoPublicarSessao**
  - Papel da JE que permite publicar decições na publicação em sessão

- **pje:processoGravarSessaoPublicacao**
  - Papel da JE para atribuir a funcionalidade de gravar decisoes para publicação em sessão
   
- **pje:relacaoJulgamento:permiteRemoverProcessoPautaFechada**
  - Papel que permite remover processo da relação de julgamento quando a pauta já está fechada

- **pje:processo:objeto:editor**
  - Papel que permite editar o objeto do processo
 
- **pje:processo:objeto:visualizador**
  - Papel que visualizar o objeto do processo
 
- **/OrgaoJulgador/abaCompetencia**
  - Papel que exibe a aba Competência na configuração do Órgão julgador

   
<!--	
	/pages/Processo/RetificacaoAutuacao/updateRetificacaoAutuacao.seam
	pje:papel:visualizaSituacoesAtuais
	pje:processo:fluxo:deflagrar:digitalizacao
	pje:papel:visualizaPartesExcluidas
	pje:papel:visualizaSituacoes
	
	pje:processo:visualizaPeticionamentoAvulso
	pje:papel:manipulaSubstituicaoMagistrado
	pje:papel:visualizaMagistradosAssociadosProcesso
	ServNucl
	procuradorMP
	procChefeMP
    pje:peso:permiteAlterarPeso
	pje:peso:permiteConsultarPeso
    pje:relacaoJulgamento:permiteOrdenarPautaSessao
	pje:processo:expedientes:permiteFechar
	pje:papel:exigeRecaptcha
	pje:papel:cadastraParteSemDocumento
	pje:websocket:placarSessaoJulgamento
	pje:papel:aproveitarAdvogados
	pje:papel:administrarAutuacao
	pdpj:marketplace:visualizar
	pje:calendario:abrangencia:nacional
	pje:calendario:abrangencia:estadual
	pje:calendario:abrangencia:municipal
	pje:calendario:abrangencia:orgaoJulgador
    pje:criminal:manipulaInformacaoCriminal
	pje:criminal:visualizaInformacaoCriminal
	pje:papel:pesquisaRecursoInterno
	pje:papel:removeRecursoInterno
	pje:papel:retornaRecursoInterno
	pje:sessao:permiteAlterarData
	pje:sessao:permiteAlterarVotos
	pje:sessao:permiteVisualizarVotos
	pje:sessao:permiteAlterarComposicao
	pje:sessao:permiteDesvincularVoto
	pje:papel:procuradorJE


	
	  Papel a ser herdado pelos papeis com função de alteração dos movimentos do processo em uma instalação do PJe.
	 
	 
	public static final String CONTROLE_VISIBILIDADE_MOVIMENTO_PROCESSO = "pje:papel:controleVisibilidadeMovimentoProcesso";
	
	
	 * Papel a ser herdado pelos papeis de assistente de procuradorias em uma instalação do PJe.
	 * 
	 
	public static final String PJE_ASSISTENTE_PROCURADOR = "pje:assistenteProcuradoria";

	public static final String PJE_ASSISTENTE_GESTOR_PROCURADOR = "pje:assistenteGestorProcuradoria";

	 
	 * Papel de Assistente de Procuradoria
	 
	public static final String ASSISTENTE_PROCURADORIA = "assistProcuradoria";
	
	public static final String ASSISTENTE_GESTOR_PROCURADORIA = "assistGestorProcuradoria";

		
	 * Papel a ser herdado pelos papeis de procuradores públicos e membros do 
	 * Ministério Público em uma instalação do PJe.
	 * 
	 
	public static final String PJE_REPRESENTANTE_PROCESSUAL = "pje:procurador";
	
	 
	 * Papel de Procurador/Defensor padrão
	 * 
	 
	public static final String REPRESENTANTE_PROCESSUAL = "procurador";

	 
	 * Papel de Procurador/Defensor Gestor
	 * 
	 
	public static final String REPRESENTANTE_PROCESSUAL_GESTOR = "procChefe";
	

	
	 * Papel a ser herdado pelos papeis de oficiais de justiça em uma instalação do PJe.
	 * 
	 
	public static final String PJE_OFICIAL_JUSTICA = "pje:oficialjustica";
	
	public static final String PJE_OFICIAL_JUSTICA_ALTERA_CONTAGEM = "pje:oficialJustica:permiteAlterarContagemPrazoResposta";
	
	public static final String OFICIAL_JUSTICA = "Ofjus";
	
	 * Papel de Oficial de Justica Distribuidor
	 
	public static final String PJE_OFICIAL_JUSTICA_DISTRIBUIDOR = "pje:oficialJusticaDistribuidor";
	
	public static final String OFICIAL_JUSTICA_DISTRIBUIDOR = "OfjusDistr";

	
	 * Papel a ser herdado pelos papeis de secretários de sessão de julgamento em uma instalação do PJe.
	 * 
	 
	public static final String SECRETARIO_SESSAO = "pje:secretariosessao";

	public static final String VISUALIZA_SIGILOSO = "pje:visualizaSigiloso";
	
	public static final String VISUALIZA_HISTORICO_PARTES = "pje:visualizaHistoricoPartes";
	
	public static final String MANIPULA_SIGILOSO = "pje:manipulaSigiloso";

	public static final String PODE_INICIAR_FLUXO_DIGITALIZACAO = "pje:processo:fluxo:deflagrar:digitalizacao";
	
	public static final String PODE_INICIAR_FLUXO_COMUNICACAO_ENTRE_INSTANCIAS = "pje:podeSolicitarComunicacaoEntreOrgaosJulgadores";

	public static final String DESENTRANHA_DOCUMENTO = "pje:desentranhaDoc";
	
	public static final String CONSULTA_MNI = "pje:consulta:mni";	

	
	 * Administrador de Cadastro de Usuário: papel com permissão de registrar usuário em qualquer papel, exceto o de Administrador.
	 *  
	 
	public static final String ADMINISTRADOR_CADASTRO_USUARIO = "pje:papel:permissaoCadastroUsuarioTodosPapeis";
	
	public static final String ADMINISTRADOR_SOCIEDADE_ADVOGADO = "pje:papel:permissaoAdministrarSociedade";
	
	
	 * Papel para Administrar os recursos de procuradorias:
	 *  
	 
	public static final String PJE_ADMINISTRADOR_PROCURADORIA = "pje:papel:administrarProcuradorias";
	
	
	 * Papel para Administrar os recursos de órgão julgador:
	 *  
	 
	public static final String PJE_ADMINISTRADOR_ORGAO_JULGADOR = "pje:papel:administrarOrgaoJulgador";
	
	
	 * Papel de Conciliador
	 
	public static final String CONCILIADOR = "conciliador";
	
	
	 * Permite responder expediente de parte sem advogado/certificado
	 
	public static final String PERMITE_RESPONDER_EXPEDIENTE = "pje:papel:servidor:permiteResponderExpediente";
	
	
	 * Papel de Analista Judiciário
	 
	public static final String ANALISTA_JUDICIARIO = "pje:papel:analistaJudiciario";
	
	
	 * Papel de Assistente Gestor Advogado
	 
	public static final String ASSISTENTE_GESTOR_ADVOGADO = "assistGestorAdvogado";
	
	
	 * Papel de Assistente Diretor de Distribuição
	 
	public static final String DIRETOR_DISTRIBUICAO = "dir_distribuicao";

	
	 * Papel de Assistente Diretor de Distribuição
	 
	public static final String PJE_SERVIDOR_MALOTE = "ServMalo";

	
	 * Papel de Servidor
	 
	public static final String SERVIDOR = "servidor";
	
	
	 * Papel de Assistente Servidor de Distribuição
	 
	public static final String SERVIDOR_DISTRIBUICAO = "serv_distrib";
	
	
	 * Papel de SERVIDOR_RET_DEST
	 
	public static final String SERVIDOR_RET_DEST = "ServRetDest";
	
	
	 * Papel de Servidor de Secretaria
	 
	public static final String SERVIDOR_SECRETARIA = "ServidorSecret";
	
	
	 * Papel de Assessor
	 
	public static final String ASSESSOR = "Asses";
	
	
	 * Papel de Visualizador de Painel Completo
	 
	public static final String VISUALIZA_PAINEL_COMPLETO = "pje:visualizaPainelCompleto";
	
	 * Papel de Visualizacao Painel Completo
	 
	public static final String PERFIL_VISUALIZACAO_PAINEL = "perfilVisualizacaoPainel";
	
	
	 * Papel de ESTAG_PREV
	 
	public static final String ESTAG_PREV = "estag_prev";
	
	
	 * Papel de ESTAG_DISTRIB
	 
	public static final String ESTAG_DISTRIB = "estag_distrib";
	
	
	 * Papel de ESTAG_ANALISE
	 
	public static final String ESTAG_ANALISE = "estag_analise";
	
	
	 * Papel de ESTAG_RETIF
	 
	public static final String ESTAG_RETIF = "estag_retif";
	
	
	 * Papel de Advogado Procurador
	 
	public static final String ADVOGADO_PROCURADOR = "advogado_procurador";
	
	
	 * Papel de Jus Postulandi
	 
	public static final String JUS_POSTULANDI = "jusPostulandi";
	
	
	 * Papel de usuário PUSH
	 
	public static final String PUSH = "UsuPush";
	
	
	 
	
	
	 * Papel de Diretor de Secretaria
	 
	public static final String DIRETOR_SECRETARIA = "dirSecretaria";
	
	
	 * Papel de ADM_CONHE
	 
	public static final String ADM_CONHE = "AdmConh";
	
	
	 * Papel de SERV_CONHE
	 
	public static final String SERV_CONHE = "ServConhe";
	
	
	 * Papel de PROTOCOLO
	 
	public static final String PROTOCOLO = "protocolo";
	
	
	 * Papel de PROTOCOLO_SECAO
	 
	public static final String PROTOCOLO_SECAO = "protocoloSecao";
	
	
	 * Papel de Redator
	 
	public static final String REDATOR = "redator";
	
	
	 * Papel de VINCULACAO_AUXILIARES
	 
	public static final String VINCULACAO_AUXILIARES = "pje:orgaojulgador:processos:vinculacaoAuxiliares:editor";
	
	
	 * Papel de OCULTAR_AGRUPADOR
	 
	public static final String OCULTAR_AGRUPADOR = "pje:painel:agrupador:ocultar";
	
	
	 * Papel de OCULTAR_AGRUPADOR_PROCESSO_SEGREDO
	 
	public static final String OCULTAR_AGRUPADOR_PROCESSO_SIGILOSO = "pje:painel:agrupador:ocultar:processoPedidoSegredo";
	
	
	 * Papel de OCULTAR_AGRUPADOR_PROCESSO_SEGREDO
	 
	public static final String OCULTAR_AGRUPADOR_DOCUMENTO_SIGILOSO = "pje:painel:agrupador:ocultar:documentoPedidoSigilo";

	
	 * Papel de OCULTAR_AGRUPADOR_PEDIDO_JUSTICA_GRATUITA
	 
	public static final String OCULTAR_AGRUPADOR_PEDIDO_JUSTICA_GRATUITA = "pje:painel:agrupador:ocultar:pedidoJusticaGratuita";

	
	 * Papel de AGRUPADOR_PEDIDO_TUTELA_LIMINAR
	 
	public static final String AGRUPADOR_PEDIDO_TUTELA_LIMINAR = "pje:painel:liminarTutela:agrupador:manipula";
	
	
	 * Papel de OCULTAR_AGRUPADOR_PEDIDO_HABILITACAO_AUTOS
	 
	public static final String OCULTAR_AGRUPADOR_PEDIDO_HABILITACAO_AUTOS = "pje:painel:agrupador:ocultar:habilitacaoAutos";
	
	
	 * Papel de OCULTAR_AGRUPADOR_ANALISE_PREVENCAO
	 
	public static final String OCULTAR_AGRUPADOR_ANALISE_PREVENCAO = "pje:painel:agrupador:ocultar:analisePrevencao";
	
	
	 * Papel de OCULTAR_AGRUPADOR_DOCUMENTOS_NAO_LIDOS
	 
	public static final String OCULTAR_AGRUPADOR_DOCUMENTOS_NAO_LIDOS = "pje:painel:agrupador:ocultar:processosDocumentosNaoLidos";
	
	
	 * Papel de OCULTAR_AGRUPADOR_MANDADO_DEVOLVIDO
	 
	pje:painel:agrupador:ocultar:mandadoDevolvido
	pje:painel:agrupador:ocultar:aguardandoRevisao
	pje:painel:agrupador:ocultar:peticoesAvulsas
	pje:lancarMovimentacaoJuntada
	pje:caracteristicasPessoais
	pje:papel:podeInserirProcessoExistente
	gestor
-->
