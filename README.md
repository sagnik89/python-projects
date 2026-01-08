# Task Tracker CLI (Python)

A simple **Command-Line Task Manager** built with Python that allows you to create, update, delete, list, and manage tasks using a local JSON file as storage. Tasks can be marked as **todo**, **in-progress**, or **done**, and are displayed in a clean tabular format using `PrettyTable`.

---

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as:
    - Todo
    - In Progress
    - Done
- List all tasks or filter by status
- Persistent storage using `db.json`
- User-friendly table output in the terminal

---

## Requirements

- Python **3.10+** (required for `match-case`)
- `prettytable` library

Install dependencies:

```bash
pip install prettytable
```

---

## Project Structure

```
.
├── task-tracker.py   # Main CLI application
├── db.json           #JSONdatabase (auto-created)
└── README.md

```

---

## ⚙️ Usage

Run the program from the command line:

```bash
python task-tracker.py <command> [arguments]

```

---

## Commands

### Add a Task

```bash
python task-tracker.py add "Buy groceries"

```

### Update a Task

```bash
python task-tracker.py update <id> "Updated task description"

```

### Delete a Task

```bash
python task-tracker.py delete <id>

```

### Mark Task Status

- Mark as **in-progress**

```bash
python task-tracker.py mark-in-progress <id>

```

- Mark as **done**

```bash
python task-tracker.py mark-done <id>

```

- Mark as **todo**

```bash
python task-tracker.py mark-todo <id>

```

---

### List Tasks

- List **all tasks**

```bash
python task-tracker.py list

```

- Filter by status

```bash
python task-tracker.py list todo
python task-tracker.py list in-progress
python task-tracker.py listdone

```

---

### Help

```bash
python task-tracker.py help

```

---

## Data Storage

Tasks are stored locally in a `db.json` file with the following structure:

```json
{
"1":{
"id":1,
"description":"Sample Task",
"status":"todo",
"createdAt":"2026-01-01 12:00:00",
"updatedAt":"2026-01-01 12:00:00"
}
}

```

---

Project Description: https://roadmap.sh/projects/task-tracker