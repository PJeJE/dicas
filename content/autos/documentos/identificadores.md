---
title: "Identificadores de Documentos (IDs)"
date: 2022-11-23T17:56:56-03:00
weight: 5
linkTitle: "IDs"
---

A Justiça Eleitoral implantou o PJe da seguinte forma: no primeiro grau (PJE Zona) há uma instância para cada UF; assim como no segundo grau (TREs), onde há uma instância para cada Tribunal Regional Eleitoral; e, no terceiro grau (TSE) há uma instância própria.

Cada instalação (instância) tem suas próprias configurações e banco de dados. Os identificadores de todos os registros do banco de dados são denominados comumente pela equipe de TI como IDs. 

Algumas telas do PJe apresentam os Ids para facilitar o suporte, principalmente quando o usuário está com algum problema em um registro específico (por exemplo: se o problema é em um documento específico, é mais fácil identificar qual o documento pelo ID dele).

Tais registros são criados aleatoriamente pelo banco de dados, não são um dado negocial. Criou-se o hábito de utilizar esse identificador para referenciar alguma decisão terminativa ou outro documento ao longo das comunicações do processo. Não há qualquer problema nessa praxe, mas é preciso saber que, ao remeter o processo, serão criados novos registros de documentos na instância de destino, com Ids específicos gerados pelo banco de dados (ou seja, esses documentos serão renumerados).

Para a finalidade de identificação de documentos, existe um campo negocial, denominado **Número** do documento. Esse dado é enviado e permanece inalterado na remessa. Outro ponto positivo é que campo é pesquisável na consulta processual. Tal campo está disponível na juntada de anexos, apesar de não estar disponível no editor de documentos presente na construção de decisões, despachos:

![Numero Opcional](/imagens/numero_opcional.jpg)

O campo **Número** também está disponível na juntada de documentos pelos autos digitais e, quando informado, ele é exibido nos autos digitais e na lista de documentos do processo.

![Numero Opcional](/imagens/numero_opcional_2.png)
