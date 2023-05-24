from Dfa import *
import tkinter as tk
from enum import Enum
import re
import pandas
import time
from Constants import *
from Util import *

class token:
    def __init__(self, lex, token_type):
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
root.title("Scanner Phase")
root.geometry("600x500")

# Styling
root.configure(bg="#1E1E1E")
canvas1 = tk.Canvas(root, width=600, height=500, relief='raised', bg="#1E1E1E")
canvas1.pack()

label1 = tk.Label(root, text='Scanner Phase', font=('Arial', 20, 'bold'), fg='#FFFFFF', bg="#1E1E1E")
canvas1.create_window(300, 50, window=label1)

label2 = tk.Label(root, text='Source code:', font=('Arial', 14), fg='#FFFFFF', bg="#1E1E1E")
canvas1.create_window(300, 120, window=label2)

entry1 = tk.Entry(root, font=('Arial', 12), width=40)
canvas1.create_window(300, 160, window=entry1)

token_box = tk.Text(root, font=('Arial', 12), width=40, height=15, bg='#FFFFFF')
token_box.tag_configure("bold", font=('Arial', 12, 'bold'))
canvas1.create_window(300, 350, window=token_box)

def scan():
    x1 = entry1.get()  # Get the value entered by the user
    uppercase_text = x1.upper()
    draw_dfa_from_input(uppercase_text)
    find_token(uppercase_text)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
    print(df)
    
    # Clear token box
    token_box.delete('1.0', tk.END)

    # Output all tokens with animation
    delay = 0.5  # Delay between displaying tokens
    for i, token in enumerate(Tokens):
        token_box.insert(tk.END, f"Token {i + 1}: ", "bold")
        token_box.insert(tk.END, f"{token.lex} ({token.token_type})\n")
        token_box.see(tk.END)  # Scroll to the end
        root.update()  # Update the window
        time.sleep(delay)

button1 = tk.Button(text='Scan', command=scan, bg='#FF6600', fg='#FFFFFF', font=('Arial', 12, 'bold'))
canvas1.create_window(300, 190, window=button1)


root.mainloop()
