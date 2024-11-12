---
title: "Variáveis"
date: 2022-11-23T17:57:39-03:00
weight: 6
---

{{% notice note %}} 
É importante ressaltar que, ao utilizar variáveis, se for utilizada a opção de copiar e colar a variável desta atual seção do Dicas ou até mesmo de um outro modelo de documento, ao colar a mesma variável em um novo modelo, via de regra, são inseridos indevidamente caracteres especiais relevantes para formatação em páginas web ou editores html. Esses caracteres prejudicam a interpretação da variável, causando erros no carregamento do documento que utiliza o modelo. Recomendamos que para utilizar o copiar e colar, que se copie a variável em um bloco de notas e depois se copie desse bloco de notas a referida variável e cole-a em seu modelo.
{{% /notice %}}

{{<table "variaveismodelo">}}

| **Descrição** | **Variável** | **Outras informações** |
|---|---|:---:|
| Assuntos do Processo | #{processoTrfHome.instance.assuntoTrfListStr} |  |
| Cabeçalho do processo com cadeia recursal em siglas | #{processoTrfHome.instance} |  |
| Cabeçalho do processo com cadeia recursal em siglas dentro da sessão | #{sessaoProcessoDocumentoHome.sessaoPautaProcessoTrf.processoTrf} |  |
| Cabeçalho do processo com cadeia recursal por extenso, exceto classe do principal | #{processoTrfHome.instance.extensoClasse != null ? processoTrfHome.instance.extensoClasse : processoTrfHome.instance.classeJudicial} |  |
| Cabeçalho do processo com cadeia recursal por extenso, exceto classe do principal dentro da sessão | #{sessaoProcessoDocumentoHome.sessaoPautaProcessoTrf.processoTrf.extensoClasse != null ? <br>sessaoProcessoDocumentoHome.sessaoPautaProcessoTrf.processoTrf.extensoClasse : sessaoProcessoDocumentoHome.sessaoPautaProcessoTrf.processoTrf.classeJudicial} |  |
| Cargo do órgão julgador do processo | #{processoTrfHome.instance.orgaoJulgadorCargo} |  |
| Cidade Órgão Julgador Processo | #{processoTrfHome.instance.orgaoJulgador.localizacao.endereco.cep.municipio} |  |
| Classe do Processo | #{processoTrfHome.instance.classeJudicial} |  |
| Classe do processo para uso em modelos de oficial de justiça | #{processoExpedienteCentralMandadoHome.instance.processoExpediente.processoTrf.classeJudicial} |  |
| Competência da Distribuição |  #{processoTrfHome.instance.getCompetencia().competencia} |  |
| Data Atual | #{currentDate} |  |
| Data Atual Abreviada | #{dataAtualAbreviada} |  |
| Data Atual Extenso | #{dataAtual} |  |
| Data atual Formatada | #{dataAtual} |  |
| Data da Audiência | #{processoTrfHome.dataAudiencia} |  |
| Data da Distribuição | #{processoTrfHome.dataDistribuicao} |  |
| Data e Hora Atual | #{currentDatetime} |  |
| Data Semana Hoje Extenso | #{dataAtualExtenso} |  |
| Endereço Advogado Polo Ativo | #{processoTrfHome.advogadoEnderecoPoloAtivoStr} |  |
| Endereço Advogado Polo Passivo | #{processoTrfHome.advogadoEnderecoPoloPassivoStr} |  |
| Endereço da Sala de Audiência | #{processoTrfHome.enderecoSalaAudiencia} |  |
| Endereço Órgão Julgador | #{processoTrfHome.instance.orgaoJulgador.localizacao.endereco.enderecoCompleto} |  |
| Endereço s Polo Ativo | #{processoTrfHome.processoEnderecoPoloAtivoStr} |  |
| Endereço s Polo Passivo | #{processoTrfHome.processoEnderecoPoloPassivoStr} |  |
| Escreve título Juiz ou Juíza de acordo com a informação sexo do cadastro do magistrado relator | #{processoTrfHome.getRelator(processoTrfHome.instance) != null and processoTrfHome.getRelator(processoTrfHome.instance).sexo == 'F'? 'Juíza': 'Juiz'} |  |
| Escreve título Procurador ou Procuradora de acordo com a informação sexo do cadastro do procurador na sessão | #{sessaoHome.instance.getPessoaProcurador() != null and sessaoHome.instance.getPessoaProcurador().sexo == 'F'? 'Procurador': 'Procuradora'} |  |
| Para pessoas cadastradas com a marcação do sexo como **Feminino**, escreve título Servidora para papéis que tenham em seu texto o nome "Servidor". Para pessoas com o cadastro do sexo como **Masculino** ou que não tenha o texto "Servidor" no nome do papel, escreve o nome original do papel | #{authenticator.getPessoaLogada().sexo == 'F' and usuarioLogadoLocalizacaoAtual.papel.toString().contains('Servidor') ? 'Servidora' :usuarioLogadoLocalizacaoAtual.papel} |  |
| Estado da autuação do Processo | #{processoTrfHome.instance.complementoJE.estadoEleicao.estado} |  |
| Hora Atual | #{currentTime} |  |
| Juiz Órgão Julgador - retorna o nome do último usuário da localização do processo que tenha o papel magistrado (se houver mais de um magistrado no OJ, vai mostrar o último, não necessariamente o atual, não necessariamente o relator do processo | #{processoTrfHome.instance.nomeJuizOrgaoJulgador} |  |
| Lista Nome Autor | #{processoTrfHome.nomeCpfAutorList} |  |
| Lista Tipo Nome Advogado Autor | #{processoTrfHome.instance.tipoNomeAdvogadoAutorList} |  |
| Lista Tipo Nome Advogado Réu | #{processoTrfHome.instance.tipoNomeAdvogadoReuList} |  |
| Login Usuário Logado | #{usuarioLogado.login} |  |
| Município da autuação do Processo | #{processoTrfHome.instance.complementoJE.municipioEleicao.municipio} |  |
| Nome Autor Ativo Processo | #{processoTrfHome.instance.nomeAutorAtivoProcesso} |  |
| Nome Autor Processo | #{processoTrfHome.instance.tipoNomeAutorProcesso} |  |
| Nome do Usuário Logado | #{usuarioLogado.nome} |  |
| Nome Outros Interessados | #{processoParteHome.processoParteTerceiroSemVinculacaoList} |  |
| Nome Réu Processo | #{processoTrfHome.instance.nomeReuProcesso} |  |
| Número do Processo | #{processoTrfHome.instance.numeroProcesso} |  |
| Número do processo para uso em modelos de oficial de justiça | #{processoExpedienteCentralMandadoHome.instance.processoExpediente.processoTrf.processo.numeroProcesso} |  |
| Número do processo referência (o número do drap estará nessa variável) | #{processoTrfHome.instance.processoReferencia} |  |
| Objeto do processo | #{processoTrfHome.instance.objeto} |  |
| Órgão Julgador Processo | #{processoTrfHome.instance.orgaoJulgador} |  |
| Papel usuário logado | #{usuarioLogadoLocalizacaoAtual.papel} |  |
| Partes dentro da certidão de julgamento | #{processoJudicialManager.recuperarParteFormatada(sessaoProcessoDocumentoHome.sessaoPautaProcessoTrf.processoTrf, false,true,false,'A','P','T')} |  |
| Partes do processo para uso em modelos de oficial de justiça | #{processoJudicialManager.recuperarParteFormatada(processoExpedienteCentralMandadoHome<br>.instance.processoExpediente.processoTrf, false,true,false,'A','P','T')} |  |
| Partes formatadas | #{processoJudicialAction.recuperarParteFormatada(true, true, 'A', 'P', 'T')} | [Detalhamento]({{< relref "recuperarparteformatada" >}}) |
| Partes polo ativo | #{processoTrfHome.processoPartePoloAtivoSemAdvogadoStr} |  |
| Partes polo passivo | #{processoTrfHome.processoPartePoloPassivoSemAdvogadoStr} |  |
| Parte - Uma das partes do polo ativo com cpf (Se usar 0 retorna a primeira parte do polo ativo) | #{processoTrfHome.instance.getProcessoPartePoloAtivoSemAdvogadoList().get(0)} |  Se for utilizado o número 1 e não existir a segunda parte no polo ativo, o sistema dá erro de tradução  |
| Parte - Uma das partes do polo passivo com cpf (Se usar 0 retorna a primeira parte do polo passivo) | #{processoTrfHome.instance.getProcessoPartePoloPassivoSemAdvogadoList().get(0)} | Se for utilizado o número 1 e não existir a segunda parte no polo passivo, o sistema dá erro de tradução |
| Parte - Uma das partes do polo ativo sem cpf (Se usar 0 retorna a primeira parte do polo ativo) | #{processoTrfHome.instance.getProcessoPartePoloAtivoSemAdvogadoList().get(0).getTipoParte()} - #{processoTrfHome.instance.getProcessoPartePoloAtivoSemAdvogadoList().get(0).getPessoa()} | Se for utilizado o número 1 e não existir a segunda parte no polo ativo, o sistema dá erro de tradução |
| Parte - Uma das partes do polo passivo sem cpf (Se usar 0 retorna a primeira parte do polo passivo) | #{processoTrfHome.instance.getProcessoPartePoloPassivoSemAdvogadoList().get(0).getTipoParte()} - #{processoTrfHome.instance.getProcessoPartePoloAtivoSemAdvogadoList().get(0).getPessoa()} | Se for utilizado o número 1 e não existir a segunda parte no polo passivo, o sistema dá erro de tradução |
| Período (sessões contínuas) ou data (sessão presencial) da sessão - para uso no documento de intimação de Pauta | #{periodoSessao} |  |
| Presidente da sessão | #{sessaoComposicaoOrdemManager.obterPresidenteSessao(sessaoPautaProcessoTrfManager<br>.getSessaoPautaProcessoTrfJulgado(tramitacaoProcessualService.recuperaProcesso()).sessao, true)} |  |
| Processos associados | #{processoTrfHome.instance.getProcessoTrfConexaoListStr()} |  |
| Procurador da sessão | #{pessoaProcuradorManager.getTituloProcurador(sessaoPautaProcessoTrfManager<br>.getSessaoPsautaProcessoTrfJulgado(tramitacaoProcessualService.recuperaProcesso()).sessao)} |  |
| Recupera a última composição do processo na sessão. False = não traz o presidente. True = traz o presidente | #{sessaoComposicaoOrdemManager.obterComposicaoSessao(sessaoHome.instance, false)} |  |
| Recupera conteúdo do documento ementa vinculada à última sessão onde o processo foi "Julgado" e a sessão teve movimento registrado ou o processo teve o julgamento individual finalizado | #{sessaoProcessoDocumentoManager.getEmenta()} |  |
| Recupera conteúdo do documento relatório à última sessão onde o processo foi "Julgado" e a sessão teve movimento registrado ou o processo teve o julgamento individual finalizado | #{sessaoProcessoDocumentoManager.getRelatorio(null)} |  |
| Recupera conteúdo do documento voto vinculado à última sessão onde o processo foi "Julgado" e a sessão teve movimento registrado ou o processo teve o julgamento individual finalizado. O sistema procura o voto do vencedor. Caso não encontre, procura o voto do relator | #{sessaoProcessoDocumentoManager.getVoto(null)} |  |
| Recupera data da última sessão de julgamento onde o processo foi "Julgado" | #{sessaoProcessoDocumentoManager.getDataUltimaSessaoJulgamento(null)} |  |
| Relator (processos de sgundo grau/TSE) | #{processoTrfHome.nomeRelator} |  |
| Revisor | #{pessoaMagistradoManager.getMagistradoTitular(orgaoJulgadorColegiadoOrgaoJulgadorManager<br>.recuperarOrgaoJulgadorRevisorPadrao(tramitacaoProcessualService.recuperaProcesso()).orgaoJulgadorRevisor.orgaoJulgador).getNome().toUpperCase()} |  |
| Sala de Audiência | #{processoTrfHome.salaAudiencia} |  |
| Tipo de Audiência | #{processoTrfHome.tipoAudiencia} |  |
| Tipo Nome Réu Processo | #{processoTrfHome.instance.tipoNomeReuProcesso} |  |
| UF Órgão Julgador | #{processoTrfHome.instance.orgaoJulgador.localizacao.endereco.cep.municipio.estado.codEstado} |  |
| Usuário Logado | #{usuarioLogado.nome} |  |
| Magistrado responsável pelo órgão julgador (primeiro grau) | #{orgaoJulgadorManager.recuperaResponsavel(processoTrfHome.orgaoJulgador, null)} |  |
| Solicitante | #{habilitacaoAutosManager.getSolicitanteUltimaHabilitacao(processoTrfHome.instance)} | Disponível somente para a [funcionalidade de certidão automática de habilitação nos autos]({{< relref "automacao/certidao/habilitacao_autos" >}}). |
| Partes | #{habilitacaoAutosManager.getPartesUltimaHabilitacao(processoTrfHome.instance)} | Disponível somente para a [funcionalidade de certidão automática de habilitação nos autos]({{< relref "automacao/certidao/habilitacao_autos" >}}). |
| Inclusão do(a) advogado(a) | #{habilitacaoAutosManager.getUltimaInclusao(processoTrfHome.instance)} | Disponível somente para a [funcionalidade de certidão automática de habilitação nos autos]({{< relref "automacao/certidao/habilitacao_autos" >}}). |
| Exclusão do(a) advogado(a) | #{habilitacaoAutosManager.getUltimaSubstituicao(processoTrfHome.instance)} | Disponível somente para a [funcionalidade de certidão automática de habilitação nos autos]({{< relref "automacao/certidao/habilitacao_autos" >}}). |
| Tipo do documento | #{certidaoPublicacaoMuralService.getTipoAto()} | Disponível somente para a [funcionalidade de certidão automática de publicação no Mural]({{< relref "automacao/certidao/certidao_mural" >}}). |
| Id do documento | #{certidaoPublicacaoMuralService.getIdAto()} | Disponível somente para a [funcionalidade de certidão automática de publicação no Mural]({{< relref "automacao/certidao/certidao_mural" >}}). |
| URL para o documento | #{certidaoPublicacaoMuralService.getUrlVisualizarDocumento()} | Disponível somente para a [funcionalidade de certidão automática de publicação no Mural]({{< relref "automacao/certidao/certidao_mural" >}}). |
| Data da publicação | #{certidaoPublicacaoMuralService.getDataPublicacao()} | Disponível somente para a [funcionalidade de certidão automática de publicação no Mural]({{< relref "automacao/certidao/certidao_mural" >}}). |
| Tipo do documento | #{certidaoDisponibilizacaoDJEService.getTipoAto()} | Disponível somente para a [funcionalidade de certidão automática de disponibilização no DJe]({{< relref "automacao/certidao/certidao_dje" >}}). |
| Id do documento | #{certidaoDisponibilizacaoDJEService.getIdAto()} | Disponível somente para a [funcionalidade de certidão automática de disponibilização no DJe]({{< relref "automacao/certidao/certidao_dje" >}}). |
| URL para o documento | #{certidaoDisponibilizacaoDJEService.getUrlVisualizarDocumento()} | Disponível somente para a [funcionalidade de certidão automática de disponibilização no DJe]({{< relref "automacao/certidao/certidao_dje" >}}). |
| Data da publicação | #{certidaoDisponibilizacaoDJEService.getDataDisponibilizacao()} | Disponível somente para a [funcionalidade de certidão automática de disponibilização no DJe]({{< relref "automacao/certidao/certidao_dje" >}}). |

{{</table>}}

