import tkinter as tk
import re
import pandas
from Constants import *

Tokens = []  # to add tokens to list


def find_token(text):
    result = ""
    tokens = re.findall('\w+|[\.\;\:\=\+\-\*\/\<\>\(\)\{\}\']', text)

    for t in tokens:
        if t in ReservedWords:
            token_type = ReservedWords[t.upper()]
            result += f"{t}: {token_type}\n"
        elif t in ArithmeticOperators:
            token_type = ArithmeticOperators[t]
            result += f"{t}: {token_type}\n"
        elif t in RelationalOperators:
            token_type = RelationalOperators[t]
            result += f"{t}: {token_type}\n"
        elif t in Comments:
            token_type = Comments[t]
            result += f"{t}: {token_type}\n"
        elif t in Constants:
            token_type = Constants[t.upper()]
            result += f"{t}: {token_type}\n"
        elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", t):
            token_type = TokenType.Identifier
            result += f"{t}: {token_type}\n"
        elif re.match("[-+]?\d+(\.\d+)?([eE][-+]?\d+)?", t):
            token_type = TokenType.Number
            result += f"{t}: {token_type}\n"
        else:
            token_type = TokenType.Error

    print(result)
    return result


root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief="raised")
canvas1.pack()

label1 = tk.Label(root, text="Scanner Phase")
label1.config(font=("helvetica", 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text="Source code:")
label2.config(font=("helvetica", 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def scan():
    x1 = entry1.get()
    uppercase_text = x1.upper()
    find_token(uppercase_text)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
    print(df)
    label4 = tk.Label(root, text="Lexem is " + find_token(uppercase_text), font=("helvetica", 10, "bold"))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(
    text="Scan", command=scan, bg="brown", fg="white", font=("helvetica", 9, "bold")
)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
