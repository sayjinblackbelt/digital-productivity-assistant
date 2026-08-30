"""Digital Productivity Assistant - MVP CLI"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_json(relative_path):
    with open(BASE_DIR / relative_path, "r", encoding="utf-8") as file:
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
    value = input("\n" + prompt + "\n> ").strip()
    return value or default

def build_formula(operation, formula):
    if operation == "lookup":
        value = ask("Qual célula contém o valor procurado? Ex.: D2", "D2")
        search_range = ask("Qual intervalo contém os valores de busca? Ex.: A:A", "A:A")
        return_range = ask("Qual intervalo contém o resultado? Ex.: B:B", "B:B")
        if formula == "PROCX":
            return f'=PROCX({value};{search_range};{return_range};"Não encontrado")'
        table = ask("Qual intervalo completo da tabela? Ex.: A:B", "A:B")
        column = ask("Qual número da coluna deve ser retornada? Ex.: 2", "2")
        return f"=PROCV({value};{table};{column};FALSO)"
    if operation == "sum":
        cr = ask("Intervalo do critério. Ex.: A:A", "A:A")
        criterion = ask("Critério. Ex.: Vendas", "Vendas")
        sr = ask("Intervalo a ser somado. Ex.: B:B", "B:B")
        return f'=SOMASE({cr};"{criterion}";{sr})'
    if operation == "count":
        rng = ask("Intervalo que será contado. Ex.: A:A", "A:A")
        criterion = ask("Critério. Ex.: Presente", "Presente")
        return f'=CONT.SE({rng};"{criterion}")'
    if operation == "condition":
        condition = ask("Qual condição deve ser testada? Ex.: A2>=7", "A2>=7")
        true_value = ask("Resultado verdadeiro", "Aprovado")
        false_value = ask("Resultado falso", "Reprovado")
        return f'=SE({condition};"{true_value}";"{false_value}")'

def run_formula_flow():
    rules = load_json("decision_engine/decision_rules.json")
    responses = load_json("responses/spreadsheet_responses.json")
    category = "Criar uma fórmula"
    options = list(rules["categories"][category]["options"].keys())
    operation_name = choose_option(rules["categories"][category]["question"], options)
    operation = rules["categories"][category]["options"][operation_name]["next"]
    print("\nVamos entender sua necessidade.")
    for question in rules["flows"][operation]["questions"]:
        ask(question)
    available = responses.get(operation, {})
    formula_names = list(available.keys())
    formula = choose_option("Qual solução você deseja gerar?", formula_names)
    result = build_formula(operation, formula)
    print("\n" + "=" * 50)
    print("FÓRMULA PERSONALIZADA")
    print("=" * 50)
    print(result)
    print("\nExplicação:")
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
    else:
        print("\nEsta categoria está prevista para as próximas versões.")

if __name__ == "__main__":
    main()
