from Constants import *
import re
import pandas
from tokenizer import *
import tkinter   as tk

# class token to hold string and token type
Tokens = []  # to add tokens to list


def find_token(text):
    result = []
    tokens = re.findall('\w+|<=|>=|==|<>|\{\*|\*\}|\{\*\}\}|[\.\;\,\:\=\+\-\*\/\<\>\(\)\{\}\'\[\]]', text)
    inside_comment = False
    for t in tokens:
        if inside_comment:
            if t == "}" or t == "*}":
                inside_comment = False
                result.append(f"{t}: {Comments[t]}\n")
        else:
            if t in ReservedWords:
                result.append(f"{t}: {ReservedWords[t.upper()]}\n")
            elif t in ArithmeticOperators:
                result.append(f"{t}: {ArithmeticOperators[t]}\n")
            elif t in Comments and t != "}" and t != "*}" and t != "{" and t != "{*":
                result.append(f"{t}: {Comments[t]}\n")
            elif t in RelationalOperators:
                result.append(f"{t}: {RelationalOperators[t]}\n")
            elif t in Constants:
                result.append(f"{t}: {Constants[t.upper()]}\n")
            elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", t):
                result.append(f"{t}: Identifier\n")
            elif re.match("[-+]?\d+(\.\d+)?([eE][-+]?\d+)?", t):
                result.append(f"{t}: Number\n")
            elif t == "{" or t == "{*":
                inside_comment = True
                result.append(f"{t}: {Comments[t]}\n")

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

#
# x1 =  '[1,2,3,4,5]'
#     uppercase_text = x1.upper()
#     find_token(uppercase_text)
#     df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
#     print(df)

def Scan():
    x1 = entry1.get()
    uppercase_text = x1.upper()
    find_token(uppercase_text)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
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