<h1 align="center">ToDo</h1>
<p align="center">Your ToDo App</p>

We have built a CLI tool for Task Management

> NOTE: to run this script you need python version 3.11.x

## Usage

1. Create a python virtual environment

```bash
python -m venv venv

# for macOS
source venv/bin/activate

# for windows
cd venv\Scripts
activate.bat
```

2. View all available command

```bash
python main.py --help
```

3. Available Commands
   1. `python main.py add`
   2. `python main.py show`
   3. `python main.py mark <task-id>`
   4. `python main.py update <task-id>`
   5. `python main.py delete <task-id>`
