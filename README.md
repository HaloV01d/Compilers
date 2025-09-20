# 🧠 Compilers — LPSIMP Language Implementation

This project implements the **scanner** and **parser** for **LPSIMP**, a Spanish programming language designed specifically for this compiler. It uses [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/), an open-source toolkit for building compilers and interpreters in Python.

---

## ⚡ Quick Start — Virtual Environment Setup (Windows)

This project uses a local virtual environment named `.venv` located in the root directory.  
All commands below are intended for the **VS Code terminal** on **Windows**.

### 1️⃣ Create the virtual environment

```bat
py -m venv .venv
```

This creates:

- `.venv\Scripts\python.exe`  
- `.venv\Scripts\pip.exe`

### 2️⃣ Upgrade pip inside the virtual environment

```bat
.\.venv\Scripts\python -m pip install --upgrade pip
```

### 3️⃣ Install dependencies

```bat
.\.venv\Scripts\python -m pip install -r requirements.txt
```

### 4️⃣ Run the compiler

```bat
.\.venv\Scripts\python run.py
```

### 5️⃣ (Optional) Activate the virtual environment for shorter commands

#### CMD

```bat
.\.venv\Scripts\activate.bat
python run.py
```

#### PowerShell

If scripts are blocked, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate:

```powershell
.\.venv\Scripts\Activate.ps1
python run.py
```

---

## 📁 Project Structure

```
├── .venv/                 # Virtual environment
├── lexer.py               # Scanner implementation
├── parser.py              # Parser implementation
├── run.py                 # Entry point for the compiler
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🧩 About LPSIMP

LPSIMP is a custom-designed programming language with Spanish syntax, created to explore compiler construction using Python. The language features:

- Lexical analysis via regular expressions
- Syntax parsing using context-free grammar
- Modular design for extensibility

---

## 💡 Technologies Used

- **Python 3.x**
- **PLY (Python Lex-Yacc)**
- **VS Code** (recommended IDE)

---

## 📌 Notes

- This project is intended for educational and experimental purposes.
- Make sure your Python installation is accessible via the `py` launcher on Windows.
- For best results, use the virtual environment to isolate dependencies.

---

## 🙌 Contributing

Feel free to fork the repo and submit pull requests with improvements, bug fixes, or new language features. Contributions are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.
