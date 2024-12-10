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

## Como alterar níveis de sigilo dos processos já distribuídos

Havendo a necessidade de se alterar o nível de segredo do processo, é necessário acessar os autos digitais. No menu ao lado direito, selecionar a opção **segredo/sigilo,** em seguida **opções** e **alterar o nível de acesso.** A opção também é acessível no ícone em formato de olho, disponibilizado na barra dos autos digitais.
 
A alteração do nível de acesso será possível independentemente do valor do nível de acesso configurado na competência classe x assunto, e os níveis disponíveis para edição são limitados ao nível do usuário. Caso o processo tenha um nível maior que o do usuário (usuário pode visualizar os níveis porque foi incluído como visualizador), o usuário não poderá alterar o nível do processo.

Caso o processo gere nível 5 de segredo de justiça, ele entrará na tarefa **Atribuir visualização de processo** e só ficará visível para o papel de magistrado. A tarefa servirá para que o magistrado saiba que um processo de segredo 5 foi peticionado e, conforme a necessidade, possa incluir visualizadores.

{{% notice note %}}
A simples alteração do nível de sigilo do processo não fará com que o visualizador perca tal permissão. Para que isso ocorra será necessária a retirada da visualização.
{{% /notice %}}

Regras importantes:
+ O usuário somente consegue alterar o nível de segredo do processo se os níveis de segredo de justiça do processo e o nível de acesso do usuário forem compatíveis, ou seja, nível do usuário maior ou igual ao nível do processo; 
+	Nas zonas eleitorais, embora sejam apenas 3 níveis, aparecerão, na alteração do nível do processo, os 5 níveis. Os usuários devem utilizar apenas os níveis 1, 3 e 5;


