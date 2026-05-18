---
title: "Autenticação multifator (MFA)"
date: 2026-05-18T10:00:00-03:00
weight: 3
---

Os sistemas da PDPJ - Plataforma Digital do Poder Judiciário (o que inclui o PJe) utilizam MFA (Autenticação Multifator) para autenticar seus usuários. Trata-se de um método de segurança que exige duas ou mais formas de verificação de identidade: além do usuário e senha ou do certificado digital, o sistema valida uma informação adicional para confirmar quem está acessando.

Desde 18 de maio de 2026, essa verificação adicional nos sistemas integrados à PDPJ (inclusive o PJe) e nos demais serviços disponíveis no portal Jus.br é feita por meio de aplicativo autenticador instalado no celular, como Google Authenticator, Microsoft Authenticator ou FreeOTP. Anteriormente o código de verificação era enviado por e-mail; agora ele é gerado pelo próprio aplicativo. Essa medida reduz significativamente o risco de acessos indevidos. Com isso, reforça-se a confiabilidade dos sistemas utilizados no dia a dia. Além disso, eliminamos os recorrentes problemas que temos na Justiça Eleitoral de envio do código temporário para emails aos quais o usuário não tem mais acesso.

## Primeiro acesso

1. Acesse o portal do [PJe da Justiça Eleitoral](https://pje.tse.jus.br/pje/login.seam) ou a plataforma PDPJ;
2. Autentique-se com usuário e senha ou com certificado digital;
3. Após o login, o sistema exibe um **QR Code** na tela;
4. No celular, instale um aplicativo autenticador (Google Authenticator, Microsoft Authenticator, FreeOTP ou similar);
5. Abra o aplicativo autenticador e leia o QR Code exibido na tela;
6. O aplicativo gera um código temporário de 6 dígitos;
7. Digite esse código no campo solicitado pelo sistema para concluir o acesso.

{{% notice note %}}
[Clicando aqui](https://acrobat.adobe.com/id/urn:aaid:sc:EU:061c2aa7-9038-4976-904b-d02ce7bbcf7f) você encontra um tutorial detalhado de configuração do aplicativo autenticador.
{{% /notice %}}

## Acessos seguintes

Nos próximos acessos ao PJe ou à PDPJ, o procedimento é simplificado:

1. Acesse o sistema normalmente;
2. Faça login com usuário e senha ou certificado digital;
3. Abra o aplicativo autenticador no celular;
4. Informe o código temporário de 6 dígitos gerado pelo aplicativo;
5. O acesso é liberado.

A imagem a seguir resume o passo a passo de configuração e uso do aplicativo autenticador:

![Passo a passo para configurar o aplicativo autenticador](/imagens/configurarmfa.png?width=600)

## Troca ou perda do celular

Caso o usuário troque ou perca o celular vinculado ao aplicativo autenticador, a recuperação do acesso é feita da seguinte forma:

1. Acesse normalmente o Portal Jus.br ou o PJe;
2. Na etapa de validação do código temporário, clique na opção **recuperação de dispositivo**;
3. O sistema envia um link de validação para o [e-mail corporativo cadastrado](https://corporativo.cnj.jus.br/);
4. Acesse o e-mail e confirme a solicitação;
5. O sistema exibe um novo QR Code;
6. Leia o QR Code com o novo celular;
7. O dispositivo anterior é desvinculado automaticamente.

## Suporte do CNJ

A plataforma de autenticação dos sistemas da PDPJ é centralizada no Conselho Nacional de Justiça.

Se os passos acima não resolverem o problema — ou se for necessário alterar o aplicativo autenticador ou atualizar o cadastro —, o usuário deve acionar a Central de Atendimento aos Usuários do CNJ, disponível em https://suporteti.cnj.jus.br.
