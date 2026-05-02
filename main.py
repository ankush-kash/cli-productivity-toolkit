import argparse
from toolkit.todo import add_task,list_tasks,mark_done,delete_task
from toolkit.expense import add_expense,category_total,list_expenses
from toolkit.organizer import organize_folder
from toolkit.pdf_merge import merge_pdfs
from toolkit.renamer import bulk_rename


parser = argparse.ArgumentParser()

parser.add_argument("module")
parser.add_argument("action")
parser.add_argument("value",nargs='?')
parser.add_argument("extra",nargs='*')

args = parser.parse_args()

if args.module == 'todo':
    if args.action == 'add':
        add_task(args.value)
        
    elif args.action == 'list':
        list_tasks()

    elif args.action == 'done':
        mark_done(int(args.value))

    elif args.action == 'delete':
        delete_task(int(args.value))

elif args.module == 'expense':
    if args.action == 'add':
        add_expense(float(args.value),args.extra[0])
    
    elif args.action == 'list':
        list_expenses()

    elif args.action == 'total':
        category_total()

elif args.module == 'organize':
    organize_folder(args.action)

elif args.module == 'pdf':
    if args.action == 'merge':
        merge_pdfs(args.value,args.extra)

elif args.module == "rename":

    bulk_rename(args.action,args.value)



