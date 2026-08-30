# Decision Engine

## Objetivo

O Decision Engine é responsável por transformar uma necessidade identificada em perguntas específicas e, posteriormente, em uma recomendação ou solução.

## Fluxo inicial

```text
INTENÇÃO
   ↓
Criar fórmula
   ↓
Qual operação?
   │
   ├── Procurar
   │      ↓
   │   PROCX / PROCV / ÍNDICE + CORRESP
   │
   ├── Somar
   │      ↓
   │   SOMA / SOMASE / SOMASES
   │
   ├── Contar
   │      ↓
   │   CONT.VALORES / CONT.SE / CONT.SES
   │
   └── Condição
          ↓
       SE / SES / E / OU
```

## Princípio

A recomendação de uma fórmula não deve depender apenas do nome da função.

O mecanismo deve considerar:

- ferramenta utilizada;
- estrutura dos dados;
- objetivo do usuário;
- quantidade de critérios;
- necessidade de compatibilidade.

## Próxima evolução

- implementar regras para correção de fórmulas;
- adicionar análise de mensagens de erro;
- criar fluxos para documentos;
- integrar respostas da base de conhecimento;
- adicionar interpretação de linguagem natural.
