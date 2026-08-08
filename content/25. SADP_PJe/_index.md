+++
title = "Migração SADP"
date = 2026-08-08T15:07:27-03:00
weight = 25
chapter = true
pre = "<b>1. </b>"
+++

### Seção 25


# Guia prático para migração de processos físicos e híbridos para o PJe.



## 1. Introdução

Este manual tem como objetivo orientar os servidores da Justiça Eleitoral no procedimento de migração de processos do Sistema de Acompanhamento de Documentos e Processos (SADP) para o Processo Judicial Eletrônico (PJE). A funcionalidade foi desenvolvida para garantir que o acervo legado seja integrado ao sistema eletrônico de forma segura, automatizada e com preservação da integridade dos dados históricos.

## 2. Acesso 

Para utilizar a ferramenta de migração, o usuário deve observar os seguintes critérios de acesso:

### Processo > Outras Ações > Migrar processo do SADP.

<img width="1037" height="452" alt="image" src="https://github.com/user-attachments/assets/701d4c1e-32fd-4dab-9ac0-9f7b5419d2c7" />


## 3. Regras de Localização e Arquivamento

Antes de iniciar a migração, verifique se o processo atende aos requisitos de situação e localidade, conforme o grau de jurisdição:

### 3.1. Primeiro Grau (Zonas Eleitorais)
O usuário só poderá migrar processos que estejam **ARQUIVADOS LOCALMENTE** na Zona Eleitoral em que está logado no momento. Não é possível migrar processos de outras zonas ou que ainda estejam em tramitação ativa no SADP.

### 3.2. Segundo e Terceiro Graus (Tribunais)
Nos Tribunais Regionais e no Tribunal Superior, a migração é permitida para processos que se encontram na fase **ARQUIVO CENTRAL** no sistema SADP.




## 4. Procedimento de Migração (Passo a Passo)

Siga as etapas abaixo para realizar a migração de um processo de forma correta:

### Passo 1: Identificação do Processo
No campo indicado, informe o **Número de Protocolo** do processo no SADP. O sistema realizará uma busca automática na base de dados do SADP.

<img width="1280" height="581" alt="image" src="https://github.com/user-attachments/assets/caced4f3-52b8-477a-9c66-69275c98847b" />


### Passo 2: Conferência de Dados Básicos
Se o protocolo for válido e atender às regras de arquivamento, o sistema exibirá os dados básicos recuperados do SADP. Confira atentamente se os dados básicos correspondem ao processo físico/legado que se deseja migrar.

<img width="1363" height="705" alt="image" src="https://github.com/user-attachments/assets/e610c00a-313b-4402-84e0-6587049dd487" />


### Passo 3: Definição da Classe Judicial
O sistema tentará converter a classe do SADP para uma classe correspondente no PJE. No entanto, observe:
1. Se a classe original não possuir correspondência direta ou estiver inativa no PJE, o campo "Classe Judicial PJE" ficará em branco.
2. Neste caso, você **DEVERÁ** selecionar manualmente uma classe válida na lista suspensa.
3. Mesmo que o sistema sugira uma classe, o usuário tem a prerrogativa de alterá-la para melhor adequação jurídica.

<img width="1376" height="731" alt="image" src="https://github.com/user-attachments/assets/44debd6c-0a22-418e-9a14-faf74dcf79ca" />

### Passo 4: Seleção do Órgão Julgador
Selecione para qual órgão julgador o processo será direcionado no PJE. No caso do 1º Grau, o sistema exibirá apenas o órgão correspondente à zona eleitoral do usuário logado.

### Passo 5: Validação de Partes e Advogados
Este é o ponto mais crítico da migração. O PJE exige a identificação por CPF ou CNPJ:
* **Migração Automática:** Apenas partes e advogados que possuam CPF ou CNPJ cadastrados no SADP serão migrados automaticamente.
* **Dados Ausentes:** Se o processo não possuir nenhuma parte com CPF, o sistema listará as 5 primeiras partes do polo ativo. Você deverá preencher obrigatoriamente o CPF de, pelo menos, uma delas para prosseguir.
* **Advogados:** Profissionais sem CPF no SADP não serão importados e deverão ser cadastrados manualmente no PJE após a migração, se necessário.

<img width="1383" height="790" alt="image" src="https://github.com/user-attachments/assets/c14b2924-5a35-4530-b930-3a2da46b7a63" />


### Passo 6: Finalização e Confirmação
Após validar todos os campos, clique em **"Confirmar Migração"**. O sistema processará a transferência e exibirá uma mensagem de sucesso. Ao final, será gerado um Documento de Confirmação de Migração, que deve ser conferido e, se necessário, juntado aos autos ou arquivado conforme diretrizes locais.

<img width="1363" height="572" alt="image" src="https://github.com/user-attachments/assets/d35c024d-114d-40c9-a5e4-02849bb71ea2" />



## 5. Orientações Finais e Suporte

> *"A qualidade da migração é diretamente proporcional à qualidade dos dados no sistema de origem. Recomenda-se o saneamento prévio de dados no SADP sempre que possível."*

* **Integridade:** Caso perceba divergências graves nos dados após a migração, não realize atos processuais e reporte o erro imediatamente.
* **Dúvidas:** Em caso de inconsistências técnicas ou erros de sistema durante o processo, abra um chamado enviando e-mail para `8800@tse.jus.br`.

<img width="1310" height="917" alt="image" src="https://github.com/user-attachments/assets/43c59268-d4bb-40de-993a-9c56a5d45460" />
