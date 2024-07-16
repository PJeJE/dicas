---
title: "Erros de acesso"
date: 2023-07-16T12:21:54-03:00
weight: 7
menuTitle: "Erros de acesso"
---
## Ao logar com token físico (certificado digital) o PJe apenas "pisca" e volta para a tela inicial

Ao tentar logar, após clicar em entrar com certificado digital e digitar a senha, a tela do PJe é atualizada mas não acontece nada, conforme vídeo abaixo. 

IMPORTANTE: na situação narrada o sistema não apresenta nenhum aviso de erro, apenas atualiza a página sem a realização do login.

A solução é solicitar uma senha na tela inicial do PJe aguardar a chegada do e-mail contendo o link para definição desta. Uma vez gerada a senha e feito o login com ela, basta acessar novamente com certificado digital e o problema estará resolvido.

Aparentemente o erro decorre de falta de sincronia na PDPJ (Plataforma do Poder Judiciário do CNJ) e a geração de uma senha faz os ajustes necessários. O CNJ utiliza uma tecnologia de login único (SSO), que combina as telas de login de vários aplicativos diferentes em uma única tela.

{{% notice warning %}}
Sugerimos que a senha cadastrada seja a mesma eventualmente utilizada em outros sitemas do CNJ vinculados à PDPJ, para evitar conflitos, pois o login é único, por meio do RHSSO, para todos os sistemas vinculados à Plataforma.
{{% /notice %}}
