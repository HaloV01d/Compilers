# 🧠 Compilers — LPSIMP Language Implementation

A compiler implementation for **LPSIMP** (Lenguaje de Programación Simple), a Spanish-based programming language built with [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/). This project features a complete **lexer** (scanner) and **parser** for educational exploration of compiler design.

---

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [LPSIMP Language Specification](#-lpsimp-language-specification)
- [Usage Examples](#-usage-examples)
- [Testing](#-testing)
- [Technologies](#-technologies-used)
- [License](#-license)

---

## ✨ Features

- **Lexical Analysis**: Token recognition using regular expressions
- **Syntax Parsing**: Context-free grammar validation
- **Error Reporting**: Colored console output for lexical and syntax errors
- **Spanish Keywords**: Natural language syntax for Spanish speakers
- **Test Suite**: Multiple test cases for validation

---

## ⚡ Quick Start

### Prerequisites

- Python 3.x
- Windows (commands adapted for Windows terminal)

### Virtual Environment Setup

This project uses a local virtual environment named `.venv` in the root directory.

#### 1️⃣ Create the virtual environment

```bat
py -m venv .venv
```

#### 2️⃣ Upgrade pip

```bat
.\.venv\Scripts\python -m pip install --upgrade pip
```

#### 3️⃣ Install dependencies

```bat
.\.venv\Scripts\python -m pip install -r requirements.txt
```

#### 4️⃣ Run the lexer

```bat
.\.venv\Scripts\python lexer.py
```

#### 5️⃣ Run the parser

```bat
.\.venv\Scripts\python parser.py
```

### Alternative: Activate Virtual Environment

**CMD:**
```bat
.\.venv\Scripts\activate.bat
python lexer.py
```

**PowerShell** (run once if scripts are blocked):
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate:
```powershell
.\.venv\Scripts\Activate.ps1
python lexer.py
```

---

## 📁 Project Structure

```
├── .venv/                      # Virtual environment (isolated dependencies)
├── __pycache__/                # Python bytecode cache
├── Test/                       # Test cases directory
│   ├── Caso_Correcto1.txt     # Valid test case 1
│   ├── Caso_Correcto2.txt     # Valid test case 2
│   ├── Caso_Correcto3.txt     # Valid test case 3
│   ├── Caso_Incorrecto1.txt   # Invalid test case 1 (lexical errors)
│   ├── Caso_Incorrecto2.txt   # Invalid test case 2 (lexical errors)
│   ├── Caso_Incorrecto3.txt   # Invalid test case 3 (lexical errors)
│   ├── Prueba1.txt            # Test file 1
│   ├── Prueba2.txt            # Test file 2
│   └── Prueba3.txt            # Test file 3
├── .gitignore                  # Git ignore rules
├── lexer.py                    # Lexical analyzer (scanner)
├── parser.py                   # Syntax analyzer (parser)
├── parsetab.py                 # PLY-generated parse table (auto-generated)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🧩 LPSIMP Language Specification

### Reserved Keywords

| Keyword | Description |
|---------|-------------|
| `inicio` | Program start |
| `final` | Program end |
| `Si` | Conditional (if) |
| `sino` | Alternative branch (else) |
| `finsi` | End conditional |
| `Lee` | Read input |
| `Escribe` | Write output |

### Operators

- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `<`, `>`, `<=`, `>=`, `==`, `<>`
- **Assignment**: `=`

### Identifiers

- Must start with a lowercase letter
- Followed by one or more lowercase letters or digits
- Examples: `numero1`, `suma`, `contador`

### Syntax Rules

- Statements can optionally end with `;`
- Expressions support parentheses for grouping
- Conditional blocks require `Si` and `finsi`

---

## 💡 Usage Examples

### Valid Program Example

```text
inicio
primer = 3
segundo = 5
Si (primer < segundo)
Escribe(primer);
sino
Escribe(segundo);
finsi
final
```

### Testing the Lexer

Edit the file path in [`lexer.py`](lexer.py):

```python
ruta = 'Test\\Caso_Correcto1.txt'
```

Run:
```bat
python lexer.py
```

### Testing the Parser

Edit the file path in [`parser.py`](parser.py):

```python
ruta = 'Test\\Caso_Correcto1.txt'
```

Run:
```bat
python parser.py
```

---

## 🧪 Testing

The project includes comprehensive test cases in the [`Test/`](Test/) directory:

### Valid Test Cases
- [`Caso_Correcto1.txt`](Test/Caso_Correcto1.txt) - Conditional statement
- [`Caso_Correcto2.txt`](Test/Caso_Correcto2.txt) - Arithmetic operations
- [`Caso_Correcto3.txt`](Test/Caso_Correcto3.txt) - Input/output operations

### Invalid Test Cases (Error Detection)
- [`Caso_Incorrecto1.txt`](Test/Caso_Incorrecto1.txt) - Invalid identifiers starting with numbers
- [`Caso_Incorrecto2.txt`](Test/Caso_Incorrecto2.txt) - Illegal characters and case sensitivity errors
- [`Caso_Incorrecto3.txt`](Test/Caso_Incorrecto3.txt) - Special characters and string literals (not supported)

Run tests by changing the `ruta` variable in [`lexer.py`](lexer.py) or [`parser.py`](parser.py).

---

## 💡 Technologies Used

- **Python 3.x** - Core programming language
- **PLY (Python Lex-Yacc)** - Lexer and parser generator
- **VS Code** - Recommended IDE

---

## 📌 Development Notes

- Lexical errors are displayed in red with line numbers
- The parser generates [`parsetab.py`](parsetab.py) automatically (included in [`.gitignore`](.gitignore))
- Virtual environment dependencies are isolated in `.venv/`
- All test files use UTF-8 encoding

---

## 🔮 Future Enhancements

- [ ] Semantic analyzer implementation
- [ ] Intermediate code generation
- [ ] Symbol table management
- [ ] Runtime interpreter
- [ ] IDE integration for real-time error checking

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👤 Author

Built as an educational project for compiler construction coursework.

---

**Made with ❤️ using Python and PLY**
