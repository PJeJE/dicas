---
title: "Erros de acesso"
date: 2023-07-16T12:21:54-03:00
weight: 7
menuTitle: "Erros de acesso"
---
## Ao logar com token físico (certificado digital) o PJe apenas "pisca" e volta para a tela inicial

Ao tentar logar, após clicar em entrar com certificado digital e digitar a senha, a tela do PJe é atualizada mas não acontece nada, conforme vídeo abaixo. 

{< video "/videos/pje_piscando_ao_fazer_login.mp4" "my-play6" >}}

IMPORTANTE: na situação narrada o sistema não apresenta nenhum aviso de erro, apenas atualiza a página sem a realização do login.

Inicie verificando no PJe Office se o endereço do PJe que você está tentando acessar está autorizado (clique com o botão direito do mouse sobre o ícone do PJe Office e vá em Segurança/Sites Autorizados), especialmente se estiver com a versões anteriores à PRO.

Caso não seja problema de permissão, a solução é solicitar uma senha na tela inicial do PJe aguardar a chegada do e-mail contendo o link para definição desta. Uma vez gerada a senha e feito o login com ela, basta acessar novamente com certificado digital e o problema estará resolvido.

Aparentemente o erro decorre de falta de sincronia na [Plataforma do Poder Judiciário do CNJ](https://www.cnj.jus.br/tecnologia-da-informacao-e-comunicacao/plataforma-digital-do-poder-judiciario-brasileiro-pdpj-br/) (PDPJ) e a geração de uma senha faz os ajustes necessários, pois o CNJ utiliza uma [tecnologia de login único](https://docs.pdpj.jus.br/servicos-estruturantes/autenticacao-sso/) (SSO), que combina as telas de login de vários aplicativos diferentes em uma única tela.

{{% notice warning %}}
Sugerimos que a senha cadastrada seja a mesma eventualmente utilizada em outros sitemas do CNJ vinculados à PDPJ, para evitar conflitos, pois o login é único, por meio do RHSSO, para todos os sistemas vinculados à Plataforma.
{{% /notice %}}