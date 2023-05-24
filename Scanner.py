import tkinter as tk
from enum import Enum
import re
import pandas
from Constants import *
from Tokenizer import *


def find_token(text):
    # Split text into list of lexemes
    lexemes = re.findall('\w+|<=|>=|==|<>|\{\*|\*\}|\{\*\}\}|[\.\;\,\:\=\+\-\*\/\<\>\(\)\{\}\'\[\]]', text)
    # Process each lexeme and create a token
    inside_comment = False
    for lex in lexemes:
        if inside_comment:
            if lex == '}' or lex == '*}':
                inside_comment = False
                t1 = Tokens(lex, Comments[lex])
                Tokens_List.append(t1)
            else:
                t1 = Tokens(lex, 'Token_type.Comment')
                Tokens_List.append(Tokens(lex, 'Token_type.Comment'))
        else:
            if lex in Comments:
                if lex != '{' and lex != '{*':
                    Tokens_List.append(Tokens(lex, Comments[lex]))
                elif lex == '{' or lex == '{*':
                    inside_comment = True
                    Tokens_List.append(Tokens(lex, Comments[lex]))
            elif lex.upper() in ReservedWords:
                Tokens_List.append(Tokens(lex, ReservedWords[lex]))
            elif lex.upper() in Constants:
                Tokens_List.append(Tokens(lex, Constants[lex]))
                # Check if the lexeme is an operator
            elif lex in ArithmeticOperators:
                Tokens_List.append(Tokens(lex, ArithmeticOperators[lex]))
            elif lex in RelationalOperators:
                Tokens_List.append(Tokens(lex, RelationalOperators[lex]))
                # Check if the lexeme is an identifier
            elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", lex):
                Tokens_List.append(Tokens(lex, Token_type.Identifier))
                # Check if the lexeme is a constant
            elif re.match("[-+]?\d+(\.\d+)?([eE][-+]?\d+)?", lex):
                Tokens_List.append(Tokens(lex, Token_type.Number))
                # If none of the above, mark the lexeme as an error token
            else:
                Tokens_List.append(Tokens(lex, Token_type.Error))
            pass


# GUI
root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Scanner Phase')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Source code:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def Scan():
    x1 = entry1.get()
    find_token(x1)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens_List])
    print(df)
    label3 = tk.Label(root, text='Lexem ' + x1 + ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text="Token_type" + x1, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Scan', command=Scan, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()