"""
Python Study Planner — Individual school project
A simple command-line task planner that can add, list, complete, and summarize tasks.
Tasks are saved locally in tasks.json.
Run: python study_planner.py
"""
import json
from pathlib import Path
from datetime import date

TASK_FILE = Path(__file__).with_name("tasks.json")

def load_tasks():
    if not TASK_FILE.exists():
        return []
    try:
        return json.loads(TASK_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

def save_tasks(tasks):
    TASK_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")

def show_tasks(tasks):
    if not tasks:
        print("\\nNo tasks yet. Add your first task from the menu.\\n")
        return
    print("\\n--- Your Study Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "DONE" if task["done"] else "TODO"
        print(f"{i}. [{status}] {task['title']} | Subject: {task['subject']} | Due: {task['due']}")
    print()

def main():
    tasks = load_tasks()
    while True:
        print("\\n=== PYTHON STUDY PLANNER ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Progress summary")
        print("5. Exit")
        choice = input("Choose 1-5: ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            subject = input("Subject: ").strip()
            due = input("Due date (YYYY-MM-DD, or leave blank): ").strip() or "Not set"
            if not title or not subject:
                print("Task title and subject cannot be empty.")
                continue
            tasks.append({"title": title, "subject": subject, "due": due, "done": False})
            save_tasks(tasks)
            print("Task added and saved.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    number = int(input("Task number to mark complete: "))
                    if 1 <= number <= len(tasks):
                        tasks[number - 1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked complete.")
                    else:
                        print("Please enter a number shown in the list.")
                except ValueError:
                    print("Please enter a whole number.")
        elif choice == "4":
            total = len(tasks)
            done = sum(1 for t in tasks if t["done"])
            percent = round((done / total) * 100) if total else 0
            print(f"Tasks: {total} | Completed: {done} | Remaining: {total-done} | Progress: {percent}%")
        elif choice == "5":
            print("Your tasks are saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
