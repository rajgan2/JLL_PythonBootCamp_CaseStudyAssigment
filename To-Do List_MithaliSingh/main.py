"""main.py"""
import uuid
from typing import List
from pathlib import Path
from datetime import datetime

import typer
from rich import print as rprint
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt


from task import Task

app = typer.Typer()

FILE_NAME = "db.txt"

TASKS = []


def load_data_store() -> List[Task]:
    """Load data store which is text file
    if file exists load tasks else create file
    """
    data = []
    if Path(FILE_NAME).exists():
        with open(FILE_NAME, "r", encoding="utf-8") as fil:
            for line in fil.readlines():
                task = line.split("\t")
                data.append(
                    Task(
                        idx=task[0].strip(),
                        title=task[1].strip(),
                        description=task[2].strip(),
                        is_done=bool(int(task[3].strip())),
                        due_date=datetime.fromisoformat(task[4].strip()),
                    )
                )
    return data


def save(tasks: List[Task]) -> None:
    """Save all the tasks in data store"""
    lines = []
    for task in tasks:
        status = 1 if task.is_done else 0
        if len(lines) == 0:
            lines.append(
                f"{task.idx}\t{task.title}\t{task.description}\t{status}\t{task.due_date.isoformat()}"
            )
        else:
            lines.append(
                f"\n{task.idx}\t{task.title}\t{task.description}\t{status}\t{task.due_date.isoformat()}"
            )

    with open(FILE_NAME, "w", encoding="utf-8") as fil:
        fil.writelines(lines)


@app.command()
def add():
    """Add task"""
    title = Prompt.ask("Task title")
    description = Prompt.ask("Task description")
    due_date = datetime.strptime(Prompt.ask("Task due date (DD/MM/YYYY)"), "%d/%m/%Y")

    task = Task(
        idx=str(uuid.uuid4()), title=title, description=description, due_date=due_date
    )
    TASKS.append(task)
    save(TASKS)

    rprint("[bold green] Task created!")


@app.command()
def update(task_id: str):
    """Update task"""
    title = Prompt.ask("New title").strip()
    description = Prompt.ask("New description").strip()
    if not title and not description:
        rprint(
            "[bold red]Task not update![/bold red] Can't set title/description empty!"
        )
        return
    for task in TASKS:
        if task_id == task.idx:
            task.title = title
            if description:
                task.description = description
            save(TASKS)
            rprint(f"[bold green]Done![/bold green] {task.title} updated! :boom:")
            return
    rprint(f"[bold red]Task not found![/bold red] {task_id}!")


@app.command()
def show():
    """Show all the tasks"""
    console = Console()
    table = Table("ID", "Title", "Description", "Due Date", "Status")
    for task in TASKS[:]:
        status = "Not Completed"
        if task.is_done:
            status = "Completed"
        table.add_row(
            task.idx, task.title, task.description, str(task.due_date), status
        )
    console.print(table)


@app.command()
def mark(task_id: str, done: bool = True):
    """Mark task as complete/incomplete"""
    for task in TASKS:
        if task_id == task.idx:
            task.is_done = 1 if done else 0
            save(TASKS)
            rprint(f"[bold green]Done![/bold green] {task.title}! :boom:")
            return
    rprint(f"[bold red]Task not found![/bold red] {task_id}!")


@app.command()
def delete(task_id: str):
    """Delete task"""
    tasks = filter(lambda task: task.idx != task_id, TASKS[:])
    save(tasks)
    rprint(f"[bold green]Done![/bold green] Task {task_id} delete! :boom:")


if __name__ == "__main__":
    TASKS = load_data_store()
    app()
