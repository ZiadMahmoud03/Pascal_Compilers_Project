import tkinter   as tk
import pandas
from   Constants import *
from   tokenizer import *

#adding this comment to try something
my_text = []
tokens = token.find_token(my_text)


def identify_token():
    result = []
    inside_comment = False

    for t in tokens:
        if inside_comment:
            if t == "}" or t == "*}":
                inside_comment = False
                result += f"{t}: {Comments[t]}\n"
        else:
            if t in ReservedWords:
                result += f"{t}: {ReservedWords[t.upper()]}\n"
            elif t in ArithmeticOperators:
                result += f"{t}: {ArithmeticOperators[t]}\n"
            elif t in Comments and t != "}" and t != "*}" and t != "{" and t != "{*":
                result += f"{t}: {Comments[t]}\n"
            elif t in RelationalOperators:
                result += f"{t}: {RelationalOperators[t]}\n"
            elif t in Constants:
                result += f"{t}: {Constants[t.upper()]}\n"
            elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", t):
                result += f"{t}: Identifier\n"
            elif re.match("[-+]?\d+(\.\d+)?([eE][-+]?\d+)?", t):
                result += f"{t}: Number\n"
            elif t == "{" or t == "{*":
                inside_comment = True
                result += f"{t}: {Comments[t]}\n"
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
    identify_token(x1)
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
