---
title: "Desmembramento de Processos"
date: 2026-07-22T16:31:43-03:00
weight: 1
---
# Desmembramento de Processos

O desmembramento permite criar um novo processo a partir de um existente, replicando partes, assuntos e documentos selecionados. O fluxo é estruturado em três etapas automáticas:

1. **Seleção:** Definição das partes e documentos que comporão o novo processo.
2. **Validação:** Verificação das regras de negócio e integridade do processo.
3. **Gravação:** Execução da transferência ou duplicação dos dados.

> **Nota sobre o Fiscal da Lei:** 
> Se a classe judicial exigir a presença de Fiscal da Lei, o sistema o 
> vinculará automaticamente ao novo processo, dispensando qualquer 
> necessidade de intervenção ou escolha manual pelo usuário.

## Gestão de Partes e Advogados

*   **Automação:** Ao selecionar uma parte principal, seus advogados e representantes são incluídos automaticamente. O sistema emitirá um alerta sobre este comportamento. 
*   **Consistência nos Vínculos:** O sistema verifica se o advogado atua para partes que permanecem no processo original. Em caso positivo, é criada uma cópia do vínculo para o processo novo em vez de removê-lo da origem.
*   **Transferência vs. Cópia:** Se o advogado não atuar para mais ninguém no original, ele é transferido; caso contrário, é copiado.
*   **Fiscal da Lei:** Esta figura é omitida da tela de seleção para evitar erros, sendo incluída automaticamente apenas se a classe judicial exigir.

| Regra de Seleção | Comportamento |
| :--- | :--- |
| **100% do Polo Ativo** | Permite (Cópia). As partes permanecem em ambos os processos. |
| **100% de todos os polos** | O polo passivo é deslocado ao novo processo. Retifique a autuação do original, se necessário. |
| **Seleção Parcial** | Permite (Transferência). Apenas o selecionado migra para o novo processo. |
| **Ausência de Polo Ativo** | Bloqueado. Deve haver ao menos uma parte no polo ativo. |

### Confirmação e Segurança
Na etapa final, o sistema exibe o detalhamento das partes separadas por polo e seus respectivos representantes, com paginação para facilitar a revisão e mensagens orientativas. 

*   **Processos Sigilosos:** A configuração de visibilidade no novo processo deve ser ajustada manualmente após a conclusão do desmembramento.

## Gestão de Documentos

*   **Replicação, não exclusão:** Os documentos escolhidos são copiados para o novo processo e permanecem inalterados no original.
*   **Integridade:** Cada documento mantém seu arquivo (binário), assinaturas e metadados. Alterações ou exclusões posteriores, seja na origem ou no destino, não afetam a outra parte.

### Limites de Interface
*   **Seleção até 20.000 documentos:** Comportamento padrão de movimentação entre listas.
*   **Seleção acima de 20.000 documentos:** Por limitação de exibição, itens podem aparecer visualmente em ambos os lados, mas a seleção permanece íntegra.
*   **Aba "Detalhe":** Caso exceda 20.000 itens, a lista pode estar oculta por padrão. Utilize o botão "Visualizar documentos" para carregar a relação.
*   **Paginação:** O sistema exibe lotes de 50 documentos por página.

## Processamento e Validações
O sistema ajusta a performance conforme o volume de carga:

*   **Até 1.000 documentos:** A cópia ocorre via método padrão, item a item.
*   **Acima de 1.000 documentos:** O sistema utiliza rotina otimizada diretamente no banco de dados para evitar sobrecarga.
*   **Petição Inicial:** É obrigatória a sua inclusão, conforme exigido pela classe processual.
*   **Assinaturas:** Até 1.000 documentos, a verificação é individual. Acima disso, é feita uma varredura resumida para identificar documentos sem assinatura.
*   **Botão "Adicionar todos":** Busca no banco a totalidade de documentos juntados e ativos, independentemente do carregamento da interface.

