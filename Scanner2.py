import tkinter as tk
from enum import Enum
import re
import pandas
from Constants import *
from Util import *

class token:
    def _init_(self, lex, token_type):
        self.lex = lex
        self.token_type = token_type

    def to_dict(self):
        return {
            'Lex': self.lex,
            'token_type': self.token_type
        }


Tokens = []  # to add tokens to list


def find_token(text):
    # Split text into list of lexemes
    lexemes = re.findall('\w+|<=|>=|==|<>|\{\|\\}|\{\\}\}|[\.\;\,\:\=\+\-\\/\<\>\(\)\{\}\'\[\]]', text)
    # Process each lexeme and create a token
    inside_comment = False
    for lex in lexemes:
        if inside_comment:
            if lex == '}' or lex == '*}':
                inside_comment = False
                Tokens.append(token(lex, Comments[lex]))
            else:
                Tokens.append(token(lex, Token_type.Comment))
        else:
            if lex in Comments:
                if lex != '{' and lex != '{*':
                    Tokens.append(token(lex, Comments[lex]))
                elif lex == '{' or lex == '{*':
                    inside_comment = True
                    Tokens.append(token(lex, Comments[lex]))
            elif lex.upper() in ReservedWords:
                Tokens.append(token(lex, ReservedWords[lex]))
            elif lex.upper() in Constants:
                Tokens.append(token(lex, Constants[lex]))
                # Check if the lexeme is an operator
            elif lex in ArithmeticOperators:
                Tokens.append(token(lex, ArithmeticOperators[lex]))
            elif lex in RelationalOperators:
                Tokens.append(token(lex, RelationalOperators[lex]))
                # Check if the lexeme is an identifier
            elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", lex):
                Tokens.append(token(lex, Token_type.Identifier))
                # Check if the lexeme is a constant
            elif re.match("[-+]?\d+(\.\d+)?([eE][-+]?\d+)?", lex):
                Tokens.append(token(lex, Token_type.Number))
                # If none of the above, mark the lexeme as an error token
            else:
                Tokens.append(token(lex, Token_type.Error))
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


def scan():
    x1 = '[1,2,3,4,5]'
    uppercase_text = x1.upper()
    find_token(uppercase_text)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
    print(df)
    label3 = tk.Label(root, text='Lexem ' + x1 + ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text="Token_type" + x1, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Scan', command=Scan, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
