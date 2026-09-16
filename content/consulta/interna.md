---
title: "Consulta interna"
date: 2022-11-29T16:19:55-03:00
linkTitle: "Interna"
weight: 5
---

A **Consulta de Processos** disponiveis para usuários logados pode ser acessada pelo menu **Processo - Pesquisar - Processo** (você também pode utilizar o acesso rápido para digitar a expressão de busca):

![Tela de consulta interna](/imagens/consulta_1.jpg)

Também é possível acessar a consulta pelo ícone da **lupa** disponível no **Painel do Usuário:**

![Tela de consulta interna](/imagens/consulta_2.jpg)

A tela da consulta exibe uma variedade de campos de pesquisa, livres e tabelados, que podem ser utilizados de maneira isolada ou em conjunto, para filtrar o processo ou grupo de processos de acordo com os critérios desejados.

{{% notice warning %}}
Os resultados da consulta são apresentados ordenados por data de autuação, sendo que dia, hora, minutos e segundos são considerados para a esta ordenação.
{{% /notice %}}

A consulta Processual do PJe Eleitoral é diferente da versão nacional do sistema (utilizado em outros tribunais), seu correto funcionamento exige que o SSO do CNJ esteja ativo e que os navegadores sejam configurados para permitir cookies de terceiros.

Se a tela for apresentada em branco, é provável que o navegador esteja bloqueando o uso de cookies de terceiros. Para corrigir o problema, será necessário fazer a configuração:

    No computador, abra o Chrome.
    No canto superior direito, selecione "os três pontinhos verticais" e depois "Configurações".
    Clique em "Privacidade e segurança" e depois "Cookies de terceiros".
    Selecione a opção:
        Permitir cookies de terceiros.

[Chrome:] (https://support.google.com/accounts/answer/61416?hl=pt-BR&co=GENIE.Platform%3DDesktop )

A seguir, um **vídeo** que mostra o problema ocorrendo e a solução no chrome:

{{< video src="/videos/chrome.mp4">}}        

    No computador, abra o Firefox.
    No canto superior direito, selecione "as três barrinhas horizontais" e depois "Configurações".
    Clique em "Privacidade e segurança"
    Na seção "Proteção aprimorada contra rastreamento", selecione o modo "Personalizado" 
    Desmarque a opção "Cookies"

[Firefox:] (https://support.mozilla.org/pt-BR/kb/desative-cookies-terceiros-impedir-rastreamento )

A seguir, um **vídeo** que mostra o problema ocorrendo e a solução no firefox:

{{< video src="/videos/firefox.mp4">}}


Essa liberação também é necessária para o painel de tarefas ser carregado corretamente.


## Consulta de processos para servidor de outra instância:

No PJe 1G há um perfil de servidor chamado **Consulta de processos para servidor,** exclusivamente para consulta, não sendo possível consultar processos sigilosos. 

O cadastro dos usuários vinculados a esse perfil deve ser feito pela funcionalidade **Configuração - Pessoa - Servidor,** selecionando apenas a Localização Física (Estado) e o opção Papel (Consulta de processos para servidor):

![Tela de consulta interna](/imagens/consulta_4.jpg)

Nos TREs, os administradores locais podem criar um perfil semelhante em **Configuração - Controle de Acesso - Papéis.**

Basta Criar um novo papel com o nome Consulta de processos para servidor de outra instância, utilizando o identificador consulta. Na aba **Herdeiros** desse papel, deve ser vinculado o papel Colaborador e, na aba **Recursos**, deve ser associado o recurso Página Processo/Consulta/Consulta de Processo.

O cadastro dos usuários vinculados ao perfil é feito em **Configuração - Pessoa - Servidor,** da forma descrita acima, sendo que no PJe2G o preenchimento do campo **Órgão julgador colegiado** é facultativa:

![Tela de consulta interna](/imagens/consulta_5.jpg)

## Procuradorias

Outra forma de usuários de uma instância terem acesso ou praticarem atos em processos que estão em outra instância é mediante a criação de procuradorias.

No TSE a consulta processual para usuários dos TREs se dá por procuradores cadastrados. 
