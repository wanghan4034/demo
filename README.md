# my_project

A minimal demo Python project showing a basic project layout with:

- a package (`demo/`)
- a small utility module (`utils.py`)
- a main entry script (`main.py`)
- a sample data file (`data/example.csv`)

## 1. Create and activate a virtual environment (recommended)

```bash
# Example using venv
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
```

## 2. Install dependencies
```bash

pip install -r requirements.txt

```

## 3. Project structure
```text

demo/
├── README.md
├── requirements.txt
├── demo/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
└── data/
    └── example.csv

```

## 4. How to run
```bash

# Option 1: run the main script directly
python -m my_project.main

# Option 2: specify a custom CSV path
python -m my_project.main --csv-path data/example.csv

```