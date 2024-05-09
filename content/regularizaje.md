## Secretaria Judiciária

|  Localização  | Papel |
|:--------------|:----------|
|Secretaria Judiciária SJD | Secretário Judiciário
|Secretaria Judiciária SJD | Colaborador
|Secretaria Judiciária SJD | Servidor 
|Unidade de Processamento Judiciário | Coordenador
|Unidade de Processamento Judiciário | Chefe de Seção
|Unidade de Processamento Judiciário | Servidor
|Unidade de Processamento Judiciário | Colaborador
|Unidade de Autuação e Distribuição | Coordenador 
|Unidade de Autuação e Distribuição | Chefe de Seção 
|Unidade de Autuação e Distribuição | Servidor 
|Unidade de Autuação e Distribuição | Colaborador 


## Unidade de processamento

|  Localização  | Papel |
|:--------------|:----------|
|Secretaria Judiciária SJD | Secretário Judiciário
|Secretaria Judiciária SJD | Colaborador
|Secretaria Judiciária SJD | Servidor 
|Unidade de Processamento Judiciário | Coordenador
|Unidade de Processamento Judiciário | Chefe de Seção
|Unidade de Processamento Judiciário | Servidor
|Unidade de Processamento Judiciário | Colaborador

## Unidade de autuação e distribuição

|  Localização  | Papel |
|:--------------|:----------|
|Secretaria Judiciária SJD | Secretário Judiciário 
|Secretaria Judiciária SJD | Servidor 
|Unidade de Autuação e Distribuição | Coordenador 
|Unidade de Autuação e Distribuição | Chefe de Seção 
|Secretaria Judiciária SJD | Colaborador 
|Unidade de Autuação e Distribuição | Servidor 
|Unidade de Autuação e Distribuição | Colaborador 

## Fluxo - Classes Originárias

Este fluxo define o fluxo básico de tarefas pelas quais passa um processo. É a porta de entrada no PJe para a maioria dos processos.

Ao entrar nesse fluxo, caso não tenha havido no processo movimento de decisão terminativa (que é o caso de processos que acabaram de ser protocolados) o sistema encaminha o processo para a primeira tarefa, [Verificar e Certificar Dados do Processo](regularizaje.md#verificar-e-certificar-dados-do-processo). Caso o processo já tenha tido movimento de decisão terminativa lançado, o sistema encaminha o processo para o Verificar Pendências.

No caso de processos do programa Regulariza JE, o processo iniciará na tarefa [Verificar processo Regulariza JE](regularizaje.md#verificar-processo-regulariza-je)

### Verificar e Certificar dados do processo

Responsabilidade: [Unidade de autuação e distribuição](regularizaje.md#unidade-de-autuacao-e-distribuicao)

Um processo de uma classe não corregedoria entra no PJe por meio do [Fluxo Originárias](regularizaje.md#fluxo-classes-originarias) na tarefa Verificar e Certificar dados do processo. 

O processo da classe Petição Cível do programa Regulariza JE deve ser encaminhado para a tarefa [Verificar processo Regulariza JE](regularizaje.md#verificar-processo-regulariza-je)

### Verificar processo Regulariza JE

Responsabilidade: [Secretaria Judiciária](regularizaje.md#secretaria-judiciaria)
