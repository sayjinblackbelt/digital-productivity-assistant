# Fórmulas de Busca

## Objetivo

Orientar o assistente na escolha de fórmulas para localizar um valor e retornar uma informação relacionada.

## Perguntas de contexto

Antes de gerar uma fórmula, identificar:

1. Qual ferramenta está sendo utilizada?
2. Qual valor será procurado?
3. Onde está o valor procurado?
4. Qual informação deve ser retornada?
5. A busca precisa ser exata?
6. A estrutura permite uma busca moderna como PROCX/XLOOKUP?

## PROCX

Exemplo:

```excel
=PROCX(D2;A:A;B:B;"Não encontrado")
```

Uso: procura o valor de D2 na coluna A e retorna o correspondente da coluna B.

## PROCV

Exemplo:

```excel
=PROCV(D2;A:B;2;FALSO)
```

Uso: procura D2 na primeira coluna do intervalo A:B e retorna a segunda coluna.

## Regra de decisão

```text
Ferramenta suporta PROCX?
       │
   SIM ↓ NÃO
    PROCX
          ↓
       PROCV
          ↓
Necessita buscar à esquerda?
          │
      SIM → considerar ÍNDICE + CORRESP
```

## Tratamento de erros

Perguntar se ocorre:

- #N/D;
- #VALOR!;
- #REF!;
- resultado incorreto.

Solicitar a fórmula atual e um exemplo simplificado antes de propor uma correção.
