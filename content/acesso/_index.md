+++
title = "Acesso ao Sistema"
date = 2022-11-21T14:56:44-03:00
weight = 1
chapter = true
pre = "<b>1. </b>"
+++

### Seção 1

# Acesso ao Sistema

{{% children  %}}

Os sistemas da PDPJ - Plataforma Digital do Poder Judiciário (o que inclui o PJe) utilizam MFA para realizar a autenticação de seus usuários. MFA significa Autenticação Multifator (Multi-Factor Authentication), o que consiste em um método de segurança digital que exige duas ou mais formas de verificação para confirmar sua identidade. Dessa forma, além do usuário e senha do usuário ou do uso do certificado digital, o sistema validará alguma outra informação para garantir que o usuário é realmente aquele que está se identificando.  

A partir de 18 de maio de 2026, a autenticação de dois fatores (MFA) para acessar sistemas judiciais (PJe inclusive) e demais serviços integrados à PDPJ e disponíveis no portal Jus.br será por meio de aplicativo autenticador. Em substituição ao código enviado por email para servidores, o usuário verificará o código pelo aplicativo instalado em seu celular e o fornecerá ao fazer login. 

Sob uma perspectiva operacional, o fluxo de autenticação com certificado digital ou mediante uso de usuário/senha passará a funcionar da seguinte forma:
1. o usuário se autentica no PJe por meio de certificado digital ou login/senha;
2. no primeiro acesso, será exibido um QR Code para configuração de um aplicativo autenticador (Google Authenticator, FreeOTP ou similar);
3. o usuário deverá informar, no PJe, o código temporário de 6 dígitos gerado pelo aplicativo para concluir o acesso; e
4. nos acessos seguintes, o usuário seguirá os passos 1 e 3.

Essa medida reduz significativamente o risco de acessos indevidos. Com isso, reforça-se a confiabilidade dos sistemas utilizados no dia a dia. Além disso, eliminamos os recorrentes problemas que temos na Justiça Eleitoral de envio do código temporário para emails aos quais o usuário não tem mais acesso.

A plataforma de autenticação dos sistemas da PDPJ fica centralizada no CNJ. Caso haja necessidade de alteração no aplicativo autenticador, seja por atualização ou perda do celular, a Central de Atendimento aos Usuários do CNJ deve ser acionada. A cental está disponível pelo link https://suporteti.cnj.jus.br .
