# Fluxo Conversacional

## Fluxo principal

```text
Mensagem inicial
      ↓
Identificar intenção
      ↓
Contexto suficiente?
   ↙             ↘
 NÃO             SIM
  ↓               ↓
Pergunta        Gerar solução
específica           ↓
  ↓             Explicar resultado
Atualizar            ↓
contexto       Sugerir próximo passo
  ↓
Reavaliar
```

## Prioridade

1. Entender o problema.
2. Identificar a ferramenta.
3. Descobrir o resultado esperado.
4. Solicitar apenas os dados necessários.
5. Entregar uma solução prática.
6. Explicar a solução quando isso agregar valor.

## Exemplo

Usuário:

> Quero buscar um telefone pelo nome.

Pergunta complementar:

> Você está usando Excel, Google Sheets ou LibreOffice Calc?

Depois:

> Em qual coluna estão os nomes e em qual coluna estão os telefones?

Após obter o contexto, o assistente seleciona a fórmula adequada.
