import os 
import sys
from datetime import datetime 
import json
from prettytable import PrettyTable


def add_task(task):
    # print("Task should be added here")    
    
    
    try:
        with open("db.json", "r+") as f:
            prev_data = json.load(f)

            num = len(prev_data.keys())
            
            data = {
                "id": num+1,
                "description": task,
                "status": 'todo',
                "createdAt": str(datetime.now()),
                "updatedAt": str(datetime.now())
            }
            
            new_data = {
                num+1 : data
            }
            
            
            
            prev_data.update(new_data)
            
            f.seek(0)
            f.truncate(0)
            
            json.dump(prev_data, f, indent=4)
            
        
    except FileNotFoundError:
        with open("db.json", "w") as f:
            data = {
            "id": id,
            "description": task,
            "status": 'todo',
            "createdAt": str(datetime.now()),
            "updatedAt": str(datetime.now())
        }
            json.dump({1 : data}, f, indent=10)
        
    print(data)

def update_task(task, current_id):
    
    with open("db.json", "r+") as f:
        prev_data = json.load(f)
        
        for value in prev_data.values():
            
            if value.get("id") == int(current_id):
                value.update({"description":task})
                f.seek(0)
                f.truncate(0)
                json.dump(prev_data, f, indent=4)
                
                print(value)
                return                
        
        print("id not found!")
        
def delete_task(current_id):
    with open("db.json", "r+") as f:
        prev_data = json.load(f)
        
        for key,value in prev_data.items():
            
            if value.get("id") == int(current_id):
                print(value)
                prev_data.pop(key)
                f.seek(0)
                f.truncate(0)
                json.dump(prev_data, f, indent=4)
                return
                
            
        print("id not found.")

def mark(current_id, status):
    with open("db.json", "r+") as f:
        prev_data = json.load(f)
        
        for key,value in prev_data.items():
            
            if value.get("id") == int(current_id):
                
                match status:
                    case "ip":
                        value.update({"status":"in-progress"})
                    case "td":
                        value.update({"status":"todo"})
                    case "d":
                        value.update({"status":"done"})
                        
                print(value)
                
                f.seek(0)
                f.truncate(0)
                json.dump(prev_data, f, indent=4)
                return
                
            
        print("id not found.")

def list_tasks(order=None):
    table = PrettyTable()
    
    table.field_names = ["Id", "Task", "Status"]
    
    with open("db.json", "r+") as f:
        
        prev_data = json.load(f)
        
        if order == None:
            for value in prev_data.values():
                table.add_row([value.get("id"), value.get("description"), value.get("status")])
        else:
            for value in prev_data.values():
                if value.get("status") == order:
                    table.add_row([value.get("id"), value.get("description"), value.get("status")])
    
    print(table)

    
    

def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("Please select a task.")
        return
    
    match args[0]:
        case "add":
            add_task(args[1])
        case "update":
            update_task(args[2], args[1])
        case "delete":
            delete_task(args[1])
        case "mark-in-progress":
            mark(args[1], "ip")
        case "mark-done":
            mark(args[1], "d")
        case "mark-todo":
            mark(args[1], "td")
        case "list":
            if len(args) > 1:
                list_tasks(args[1])
            else:
                list_tasks()
        case _:
            print("Invalid Command")
    
    
if __name__ == "__main__":
    main()

