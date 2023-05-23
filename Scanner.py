import tkinter as tk
from enum import Enum
import re
import pandas
from pandastable import Table
from Constants import Token_type, ReservedWords, ArithmeticOperators, RelationalOperators, Constants, Comments



# class token to hold string and token type
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
    lexemes = re.findall('\w+|<=|>=|==|<>|\{\*|\*\}|\{\*\}\}|[\.\;\,\:\=\+\-\*\/\<\>\(\)\{\}\'\[\]]', text)
    # Process each lexeme and create a token
    inside_comment = False
    for lex in lexemes:
        if inside_comment:
            if lex == "}" or lex == "*}":
                inside_comment = False
                Tokens.append(token(lex, Token_type.Comments))
        else:
            if lex.upper() in ReservedWords:
                Tokens.append(token(lex, ReservedWords[lex]))
            elif lex.upper() in Constants:
                Tokens.append(token(lex, Constants[lex]))
                # Check if the lexeme is an operator
            elif lex in ArithmeticOperators:
                Tokens.append(token(lex, ArithmeticOperators[lex]))
            elif lex in RelationalOperators:
                Tokens.append(token(lex, RelationalOperators[lex]))
                # Check if the lexeme is an identifier
            elif lex in Comments and (lex != "}" and lex != "*}" and lex != "{" and lex != "{*"):
                Tokens.append(token(lex, Comments[lex]))
            elif lex in Comments and lex == "{" or lex == "{*":
                inside_comment = True
                Tokens.append(token(lex, Comments[lex]))
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
canvas1 = tk.Canvas(root, width=800, height=600)


def Scan():
    x1 = entry1.get('1.0', 'end-1c')
    tokens = find_token(x1)
    arr = [t.to_dict() for t in tokens]
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)
    df = pandas.DataFrame.from_records([t.to_dict() for t in tokens])
    table = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
    table.show()
    canvas1.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox('all'))


canvas1.pack(side='left', fill='both', expand=True)
scrollbar = tk.Scrollbar(root, command=canvas1.yview)
scrollbar.pack(side='right', fill='y')
canvas1.config(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas1)
canvas1.create_window((0, 0), window=frame, anchor='nw')

label1 = tk.Label(frame, text='Scanner Phase')
label1.config(font=('helvetica', 14))

label2 = tk.Label(frame, text='Source code:')
label2.config(font=('helvetica', 10))
entry1 = tk.Text(frame, width=100, height=25)

label1.pack()
label2.pack()
entry1.pack()
button1 = tk.Button(frame,
                    text='Scan',
                    command=Scan,
                    bg='brown',
                    fg='white',
                    font=('helvetica', 9, 'bold'))
button1.pack()

frame.update_idletasks()
canvas1.config(scrollregion=canvas1.bbox('all'))
root.mainloop()