# CLI Productivity Toolkit

A Python-based command line productivity toolkit featuring:

- Todo Manager
- Expense Tracker
- File Organizer
- PDF Merger
- Bulk Renamer

---

## Features

### Todo Manager
- Add tasks
- List tasks
- Mark tasks complete
- Delete tasks

### Expense Tracker
- Add expenses
- View expenses
- Category-wise totals

### File Organizer
- Automatically organize files by extension

### PDF Merger
- Merge multiple PDFs into one file

### Bulk Renamer
- Rename multiple files with prefixes

---

## Tech Stack

- Python
- argparse
- pathlib
- shutil
- PyPDF2
- JSON

---

## Installation

```bash
git clone <your-repo-url>
cd cli-productivity-toolkit
pip install -r requirements.txt
```

---

## Usage

### Todo

```bash
python main.py todo add "Study Python"
python main.py todo list
```

### Expense

```bash
python main.py expense add 250 food
python main.py expense total
```

### Organizer

```bash
python main.py organize test_folder
```

### PDF Merger

```bash
python main.py pdf merge output.pdf a.pdf b.pdf
```

### Renamer

```bash
python main.py rename test_folder trip
```

---

## What I Learned

- CLI application development
- File handling
- JSON storage
- Filesystem automation
- Working with external libraries
- Error handling