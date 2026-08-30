"""Digital Productivity Assistant - MVP CLI"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_json(path):
    with open(BASE_DIR / path, "r", encoding="utf-8") as file:
        return json.load(file)

def choose_option(prompt, options):
    print("\n" + prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("\nEscolha uma opção: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Opção inválida. Tente novamente.")

def ask(prompt, default=""):
    return input("\n" + prompt + "\n> ").strip() or default

def run_spreadsheet_organization():
    problem = choose_option("Qual problema você deseja resolver?", ["Dados duplicados", "Organizar colunas e cabeçalhos", "Padronizar datas", "Padronizar números", "Separar dados misturados", "Melhorar a estrutura geral"])
    tool = ask("Qual ferramenta você está utilizando?", "Excel")
    print("\nORIENTAÇÃO PRÁTICA")
    print("=" * 50)
    print(f"Ferramenta: {tool}")
    guidance = {
        "Dados duplicados": "Faça uma cópia dos dados, identifique a coluna única e use a remoção de duplicatas. Exemplo: =CONT.SE(A:A;A2)>1",
        "Organizar colunas e cabeçalhos": "Use uma única linha de cabeçalho, nomes claros e uma informação por coluna. Evite células mescladas na base.",
        "Padronizar datas": "Verifique se as datas são valores de data e escolha um formato único, como dd/mm/aaaa.",
        "Padronizar números": "Verifique números armazenados como texto e padronize moeda, porcentagem e casas decimais.",
        "Separar dados misturados": "Identifique o separador e use Texto para Colunas ou funções de divisão.",
        "Melhorar a estrutura geral": "Checklist: cabeçalho único, uma informação por coluna, sem linhas vazias, formatos consistentes e duplicados revisados."
    }
    print(guidance[problem])
    print("\nFaça uma cópia antes de alterações estruturais.")

def run_data_interpretation():
    raw = ask("Informe valores separados por ponto e vírgula. Ex.: 10;15;20")
    values = []
    for item in raw.split(";"):
        try:
            values.append(float(item.strip().replace(",", ".")))
        except ValueError:
            pass
    if not values:
        print("Nenhum valor numérico válido foi informado.")
        return
    choice = choose_option("O que você deseja descobrir?", ["Maior valor", "Menor valor", "Média", "Comparar primeiro e último valor", "Resumo geral"])
    maximum, minimum = max(values), min(values)
    average = sum(values) / len(values)
    print("\nRESULTADO DA ANÁLISE")
    print("=" * 50)
    if choice == "Maior valor":
        print(f"Maior valor: {maximum:g}")
    elif choice == "Menor valor":
        print(f"Menor valor: {minimum:g}")
    elif choice == "Média":
        print(f"Média: {average:.2f}")
    elif choice == "Comparar primeiro e último valor":
        first, last = values[0], values[-1]
        change = last - first
        print(f"Valor inicial: {first:g}")
        print(f"Valor final: {last:g}")
        print(f"Variação absoluta: {change:+g}")
        if first != 0:
            print(f"Variação percentual: {change / first * 100:+.2f}%")
        print("Interpretação: aumento." if change > 0 else "Interpretação: redução." if change < 0 else "Interpretação: sem variação.")
    else:
        print(f"Quantidade: {len(values)}")
        print(f"Menor: {minimum:g}")
        print(f"Maior: {maximum:g}")
        print(f"Média: {average:.2f}")
        print("Interpretação: indicadores básicos; o significado depende do contexto.")

def run_formula_correction():
    tool = ask("Qual ferramenta você está utilizando? Ex.: Excel")
    formula = ask("Qual fórmula está apresentando problema?")
    error = ask("Qual erro aparece? Ex.: #N/D, #VALOR!, #REF!")
    expected = ask("Qual resultado você esperava obter?")
    suggestions = {"#N/D": "O valor procurado pode não existir ou os dados podem ter formatos diferentes.", "#VALOR!": "Verifique argumentos e tipos de dados.", "#REF!": "A fórmula pode apontar para uma referência removida.", "#DIV/0!": "A fórmula está tentando dividir por zero ou por uma célula vazia."}
    print("\nDIAGNÓSTICO INICIAL")
    print("=" * 50)
    print(f"Ferramenta: {tool}")
    print(f"Erro: {error}")
    print(f"Resultado esperado: {expected}")
    print(suggestions.get(error.upper().replace(" ", ""), "Verifique fórmula, intervalos e dados."))
    print("Fórmula informada:", formula)

def run_formula_flow():
    rules = load_json("decision_engine/decision_rules.json")
    responses = load_json("responses/spreadsheet_responses.json")
    category = "Criar uma fórmula"
    options = list(rules["categories"][category]["options"].keys())
    operation_name = choose_option(rules["categories"][category]["question"], options)
    operation = rules["categories"][category]["options"][operation_name]["next"]
    for question in rules["flows"][operation]["questions"]:
        ask(question)
    available = responses.get(operation, {})
    formula = choose_option("Qual solução você deseja gerar?", list(available.keys()))
    if operation == "lookup":
        value = ask("Célula do valor procurado. Ex.: D2", "D2")
        if formula == "PROCV":
            table_range = ask("Intervalo completo da tabela. Ex.: A:B", "A:B")
            column_index = ask("Número da coluna de retorno. Ex.: 2", "2")
            result = f"=PROCV({value};{table_range};{column_index};FALSO)"
        else:
            search_range = ask("Intervalo de busca. Ex.: A:A", "A:A")
            return_range = ask("Intervalo de retorno. Ex.: B:B", "B:B")
            result = f'=PROCX({value};{search_range};{return_range};"Não encontrado")'
    elif operation == "sum":
        if formula == "SOMA":
            result = f'=SOMA({ask("Intervalo a ser somado. Ex.: B2:B100", "B2:B100")})'
        elif formula == "SOMASES":
            sum_range = ask("Intervalo da soma. Ex.: C:C", "C:C")
            criteria_range1 = ask("Primeiro intervalo de critério. Ex.: A:A", "A:A")
            criteria1 = ask("Primeiro critério. Ex.: Vendas", "Vendas")
            criteria_range2 = ask("Segundo intervalo de critério. Ex.: B:B", "B:B")
            criteria2 = ask("Segundo critério. Ex.: Janeiro", "Janeiro")
            result = f'=SOMASES({sum_range};{criteria_range1};"{criteria1}";{criteria_range2};"{criteria2}")'
        else:
            result = f'=SOMASE({ask("Intervalo do critério", "A:A")};"{ask("Critério", "Vendas")}";{ask("Intervalo da soma", "B:B")})'
    elif operation == "count":
        result = f'=CONT.SE({ask("Intervalo", "A:A")};"{ask("Critério", "Presente")}")'
    else:
        result = f'=SE({ask("Condição", "A2>=7")};"{ask("Resultado verdadeiro", "Aprovado")}";"{ask("Resultado falso", "Reprovado")}")'
    print("\nFÓRMULA PERSONALIZADA")
    print("=" * 50)
    print(result)
    print(available[formula]["explanation"])

def main():
    print("=" * 50)
    print("DIGITAL PRODUCTIVITY ASSISTANT")
    print("MVP — Assistente de Produtividade Digital")
    print("=" * 50)
    options = ["Criar uma fórmula", "Corrigir uma fórmula", "Organizar uma planilha", "Criar ou organizar uma tabela", "Interpretar dados", "Formatar um documento", "Corrigir ou melhorar um texto", "Criar uma resposta ou conteúdo"]
    choice = choose_option("Olá! O que você deseja resolver?", options)
    if choice == "Criar uma fórmula":
        run_formula_flow()
    elif choice == "Corrigir uma fórmula":
        run_formula_correction()
    elif choice == "Organizar uma planilha":
        run_spreadsheet_organization()
    elif choice == "Interpretar dados":
        run_data_interpretation()
    else:
        print("\nEsta categoria está prevista para as próximas versões.")

if __name__ == "__main__":
    main()
