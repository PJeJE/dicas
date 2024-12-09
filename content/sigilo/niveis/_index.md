+++
title = "Níveis de sigilo"
date = 2023-01-15T10:49:43-03:00
weight = 2
chapter = true
+++

## Níveis e papeis

{{< tabs groupId="niveis_sigilo" >}}
{{% tab name="ZONAS" %}}
Para as Zonas Eleitorais, em razão do menor número de papeis disponíveis para os usuários, foram fixados três níveis de acesso com os respectivos visualizadores.

NÍVEL DE ACESSO UM:
+ juiz eleitoral;
+ servidor e servidor processamento; 
+ polo ativo e seus representantes;
+ membros do Ministério Público, como fiscal da lei.

NÍVEL DE ACESSO TRÊS:
+ juiz eleitoral;
+ servidor;
+ polo ativo e seus representantes.

NÍVEL DE ACESSO CINCO:
+ juiz eleitoral;
+ polo ativo e seus representantes.

{{% /tab %}}
{{% tab name="TREs" %}}
Aguardar regulamentação.
{{% /tab %}}
{{% tab name="TSE" %}}
Aguardar regulamentação.
{{% /tab %}}
{{< /tabs >}}

## Como atribuir níveis de sigilo aos processos

A atribuição dos níveis de sigilo depende de configuração realizada pelo administrador do sistema, previamente à entrada do processo no PJe.

Tal configuração é feita no item de menu **Cadastro de nível de acesso por competência (Configuração – Competência – sigilo)**, por meio da competência x classe x assunto (o nível de segredo das classes e assuntos processuais foram decididos em reunião do grupo de trabalho).

A definição do nível de segredo leva em conta a combinação de classe com o assunto processual. Nesse contexto, é possível existir uma classe processual sem nível específico de sigilo com assunto processual que possua segredo, caso em que o processo terá segredo em razão do assunto processual e não da classe. O inverso também é viável.

O nível da classe ou assunto será, no mínimo, 1. 

Em caso de haver uma combinação em que a classe é nível 1, mas o assunto é nível 3, prevalecerá o nível 3.

Assim, quando uma classe é considerada pública (prestação de contas, por exemplo), o advogado pode pedir sigilo, marcando Sim na opção **Segredo de Justiça,** na Aba Características. 

{{% notice warning %}}
Ainda que a combinação classe X assunto tenha configurada o nível 5 como padrão, o processo protocolado naquela combinação só será sigiloso se o usuário protocolador assim o solicitar (é necessário atribuir sigilo ao processo, após a atribuição do sigilo é que o sistema o classifica em níveis, conforme a configuração).
{{% /notice %}}

Regras importantes:
+ O usuário que peticiona não escolhe o nível de segredo do processo, isso é configurado pelo administrador do sistema;
+ Para que ao processo seja atribuído o nível de segredo que se deseja, é necessário escolher adequadamente a classe e o assunto processual.



