# Python Inheritance Checker 🔗

A simple Python script to detect circular dependencies in class inheritance definitions. It determines if a given class structure is "possible" or "impossible" by analyzing its inheritance graph.

In object-oriented programming, a class cannot inherit from itself, either directly or indirectly (e.g., Class A inherits from B, and Class B inherits from A). This creates an impossible circular dependency. This script parses simplified class definitions and reports if such a loop exists.

---

## 🚀 How to Use

1.  **Save the Code:** Save the script as a Python file (e.g., `checker.py`).

2.  **Run the Script:** Execute the file from your terminal.
    ```bash
    python checker.py
    ```

3.  **Provide Input:** Paste your class definitions directly into the terminal. The script reads lines until it receives an end-of-file (EOF) signal.

4.  **End Input:**
    -   On **Linux** or **macOS**, press `Ctrl + D`.
    -   On **Windows**, press `Ctrl + Z`, then `Enter`.

The script will then process the input and print `possible` or `impossible`.

---

## 📋 Input Format & Examples

The script only processes lines containing the word `class`. You can use a simplified syntax.

