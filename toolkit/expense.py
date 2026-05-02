import json
from pathlib import Path

expense_file = Path('data/expenses.json')

def load_expenses():

    if not expense_file.exists():
        return []
    
    with open(expense_file,'r') as f:
        return json.load(f)
    

def save_expenses(expenses):

    with open(expense_file,'w') as f:
        json.dump(expenses,f,indent=4)



def add_expense(amount,category):
    expenses = load_expenses()

    expenses.append({
        'amount' : amount,
        'category' : category
    })

    save_expenses(expenses)

    print('Expense Added!')

def list_expenses():

    expenses = load_expenses()

    if not expenses:
        print("No expense found.")

    for index,exp in enumerate(expenses,start=1):

        print(f"{index}. ₹{exp['amount']} "
            f"- {exp['category']}")
        
def category_total():

    expenses = load_expenses()

    total_d = {}

    for exp in expenses:

        category = exp['category']
        amount = exp['amount']

        if category in total_d:

            total_d[category] += amount

        else:

            total_d[category] = amount

    for key, value in total_d.items():

        print(f'category - {key} | total - {value}')