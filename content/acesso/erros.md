---
title: "Erros de acesso"
date: 2023-07-16T12:21:54-03:00
weight: 7
menuTitle: "Erros de acesso"
---
## 1. Ao logar com token físico (certificado digital) o PJe apenas "pisca" e volta para a tela inicial

Ao tentar logar, após clicar em entrar com certificado digital e digitar a senha, a tela do PJe é atualizada mas não acontece nada, conforme vídeo abaixo. 

{{< video src="/videos/pje_piscando_login.mp4">}}

IMPORTANTE: na situação narrada o sistema não apresenta nenhum aviso de erro, apenas atualiza a página sem a realização do login.

Inicie verificando no PJe Office se o endereço do PJe que você está tentando acessar está autorizado (clique com o botão direito do mouse sobre o ícone do PJe Office e vá em Segurança/Sites Autorizados), especialmente se estiver com a versões anteriores à PRO.

Caso não seja problema de permissão, a solução é solicitar uma senha na tela inicial do PJe aguardar a chegada do e-mail contendo o link para definição desta. Uma vez gerada a senha e feito o login com ela, basta acessar novamente com certificado digital e o problema estará resolvido.

Aparentemente o erro decorre de falta de sincronia na [Plataforma do Poder Judiciário do CNJ](https://www.cnj.jus.br/tecnologia-da-informacao-e-comunicacao/plataforma-digital-do-poder-judiciario-brasileiro-pdpj-br/) (PDPJ) e a geração de uma senha faz os ajustes necessários, pois o CNJ utiliza uma [tecnologia de login único](https://docs.pdpj.jus.br/servicos-estruturantes/autenticacao-sso/) (SSO), que combina as telas de login de vários aplicativos diferentes em uma única tela.

{{% notice warning %}}
Sugerimos que a senha cadastrada seja a mesma eventualmente utilizada em outros sitemas do CNJ vinculados à PDPJ, para evitar conflitos, pois o login é único, por meio do RHSSO, para todos os sistemas vinculados à Plataforma.
{{% /notice %}}

## 1. Erro de usuário não encontrado no momento de gerar a senha de acesso

Ao abrir o link para cadastramento de senha, deve aparecer uma tela como a da imagem abaixo, indicando o **nome** e o **CPF** corretos do usuário:

IMG_SENHA_1

Quando o usuário solicita a nova senha mais de uma vez, se o e-mail demora muito para chegar, ou se o usuário ultrapassa o limite de validade do link, a tela apresentada será diferente:

IMG_SENHA_2

Isso acontece porque os links enviados por e-mail tem um prazo de validade, eles precisam ser utilizados antes da expiração. Além disso, sempre que um novo link é gerado (seja por solicitação do usuário ou por um administrador do sistema), o antigo perde a validade. Caso o usuário já tenha feito uma nova solicitação de recuperação de senha e utilize um link enviado anteriormente, haverá erro.

Caso tenha dificuldades ao executar o procedimento, todos os e-mails com links para geração de senha devem ser apagados antes de fazer nova tentativa. Ao efetivar o cadastro da nova senha, o sistema apresenta a seguinte tela:

IMG_SENHA_3
