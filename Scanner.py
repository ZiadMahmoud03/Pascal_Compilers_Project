import tkinter as tk
import re
import pandas
from Constants import *
from tokenizer import token, Tokens

my_text = []


def find_token(my_text):

    result = ""
    tokens = re.findall('\w+|[\.\;\:\=\+\-\*\/\<\>\(\)\{\}\']', my_text)
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
            token_type = Token_type.Identifier
            result += f"{t}: {token_type}\n"
        elif re.match("[-+]?\d+(\.\d+)?([eE][-+]?\d+)?", t):
            token_type = Token_type.Number
            result += f"{t}: {token_type}\n"
        elif t == ">" and t + 1 == "=":
            token_type = Token_type.GreaterThanEqOp
            result += f"{t}: {token_type}\n"
        else:
            token_type = Token_type.Error

    print(result)

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


def Scan():
    x1 = entry1.get()
    find_token(x1)
    df = pandas.DataFrame.from_records([lexeme.to_dict() for lexeme in Tokens])
    print(df)
    label3 = tk.Label(root, text="Lexem " + x1 + " is:", font=("helvetica", 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text="Token_type" + x1, font=("helvetica", 10, "bold"))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(
    text="Scan", command=Scan, bg="brown", fg="white", font=("helvetica", 9, "bold")
)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
