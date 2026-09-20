# caesar-cipher-encoder
A lightweight cryptography utility implementing ASCII-based character shifting and modulo arithmetic in Python.

## Features
- **Case-Insensitive Shift:** Automatically handles and preserves uppercase and lowercase letters.
- **Punctuation & Space Safe:** Leaves spaces, numbers, and special characters completely untouched while shifting the alphabet.
- **Modulo Wrap-Around:** Seamlessly wraps shifts past 'z' (e.g., shifting 'z' by 1 becomes 'a').

## How to Run It

1. Make sure you have Python installed on your computer.
2. Download or clone this repository.
3. Open your terminal or command prompt in the project folder and run:
   ```bash
   python main.py
