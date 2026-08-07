---
title: "Configuração do computador e pré-requisitos"
date: 2022-11-21T15:21:54-03:00
weight: 1
---

+ Ainda que o acesso para usuários previamente cadastrados seja possível com uso de login e senha, usuários externos precisam de um certificado digital válido para poder juntar documentos;
+ Usuários internos podem acessar com certificado digital físico, com o Token PJe ou com o Certificado P12 (as duas últimas opções são soluções específicas da Justiça Eleitoral);
+ Para utilizar o PJe é necessário ter acesso à internet;
+ Deve-se usar preferencialmente o navegador Mozilla Firefox. O Navegador do Google Chrome costuma ser compatível com o PJe e pode ser utilizado de forma alternativa;
+ Para utilização do certificado digital é preciso ter o [PJe Office](https://pjeoffice.trf3.jus.br/) instalado na máquina. Sendo que os usuários externos devem estar sempre na versão mais atualizada e os usuários internos precisam estar em versão compatível com as modalidades de assinatura específicas da justiça eleitoral (tópicos seguintes);
+ Para o uso do certificado digital físico, é preciso ter o driver do certificado instalado no computador;
+ Para o uso do mobile (apenas usuários internos) é preciso ter o aplicativo instalado no celular;
+ Na página inicial do PJe, ao clicar em **Pré-Requisitos**, é possível verificar se está tudo em ordem para o acesso ao sistema:
![Tela requisitos](/imagens/requisitos.jpg)

## Erro "PJE Office não instalado" no momento da assinatura

Em algumas versões mais recentes de navegadores está ocorrendo um erro onde o PJe não reconhece o PJe Office corretamente instalado e configurado. Nestes casos, após login com o certificado digital (utilizando o PJe Office) ser realizado com sucesso, dá erro no momento da assinatura.

Para corrigir a falha de acesso ao sistema, realize os procedimentos abaixo, conforme o navegador utilizado:

* Google Chrome

Abra o navegador e digite na barra de endereços: chrome://flags/

No campo de pesquisa localizado na parte superior da página, digite Network.

Localize a opção Local Network Access Checks e altere a configuração para Disabled.

Após realizar a modificação, reinicie o navegador e tente acessar novamente o sistema.

* Microsoft Edge

Abra o Edge e digite na barra de endereços: edge://flags/

No campo de pesquisa, digite Network.

Localize a opção Block insecure private network requests e altere para Disabled.

Reinicie o navegador e realize novo teste de acesso.

* Mozilla Firefox

Abra o Firefox e digite na barra de endereços: about:config

Aceite os riscos para prosseguir.

No campo de pesquisa, digite network.security.ports.bypass.

Adicione a porta necessária ou desative a opção correspondente.

Reinicie o navegador e teste novamente o acesso.

* Opera

Abra o navegador e digite na barra de endereços: opera://flags/

No campo de pesquisa, digite Network.

Localize a opção Local Network Access Checks e altere para Disabled.

Reinicie o navegador e realize novo teste.
