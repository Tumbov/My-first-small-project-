import uuid
import json
from datetime import datetime

FILE_NAME = "tasks.json"

# --- Load tasks from file ---
def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# --- Save tasks to file ---
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# --- Task operations ---
def add_task(description):
    tasks = load_tasks()
    task = {
        "id": str(uuid.uuid4()),  # unique identifier
        "description": description,
        "status": "todo",  # default status
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def update_task(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print("✏️ Task updated!")
            return
    print("❌ Task not found!")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print("🗑 Task deleted!")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for task in tasks:
        if filter_status is None or task["status"] == filter_status:
            print(f"[{task['status']}] {task['description']} (ID: {task['id']})")

# --- Main program loop ---
def main():
    while True:
        print("\n=== Task Manager ===")
        print("1. Add task")
        print("2. Update task status")
        print("3. Delete task")
        print("4. List all tasks")
        print("5. List tasks by status")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == "2":
            task_id = input("Enter task ID: ")
            new_status = input("Enter new status (todo/in-progress/done): ")
            update_task(task_id, new_status)
        elif choice == "3":
            task_id = input("Enter task ID: ")
            delete_task(task_id)
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            status = input("Enter status (todo/in-progress/done): ")
            list_tasks(status)
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
