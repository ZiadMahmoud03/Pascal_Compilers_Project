import sys
import tkinter as tk
import re
import pandas
from Constants import *

'''
def _is_next(self, expected):
        if self._is_at_end():
            return False

        if self._source[self._current] != expected:
            return False

        self._current += 1
        return True

def _is_at_end(self):
        return self._current >= len(self._source)

def _advance(self):
    self._current += 1
    return self._source[self._current - 1]
'''


def _is_at_end(self):
    return self._current >= len(self._source)


Tokens = []  # to add tokens to list

in_comment = False

''''
def find_token(text):
    lexemes = re.findall(r'[a-zA-Z0-9_]+|\S', text)
    i = 0
    while i < len(lexemes):
        if lexemes[i] in ReservedWords:
            t=token()
            Tokens.lex=str(lexemes[i])
            t.token_type=ReservedWords[lexemes[i]]
        elif lexemes[i] in ArithmeticOperators:
            t=token()
            Tokens.lex=str(lexemes[i])
            t.token_type=ArithmeticOperators[lexemes[i]]
        elif lexemes[i] in RelationalOperators:
            t=token()
            Tokens.lex=str(lexemes[i])
            t.token_type=RelationalOperators[lexemes[i]]
        elif lexemes[i] in Comments:
            t=token()
            Tokens.lex=str(lexemes[i])
            t.token_type=Comments[lexemes[i]]
        elif lexemes[i] in Constants:
            t=token()
            Tokens.lex=str(lexemes[i])
            t.token_type=Constants[lexemes[i]]
        elif re.match("[a-zA-Z][a-zA-Z0-9]*", t):
            t=token()       
            Tokens.lex=str(lexemes[i])
            t.token_type=Token_type.ValIdentifier
        elif re.match("[A-Z][a-zA-Z0-9]*", t):
            t=token()
            Tokens.lex=str(lexemes[i])
            t.token_type=Token_type.VarIdentifier
        elif re.match("[0-9]+(\.[0-9]*)?", t):
            t=token()
            Tokens.lex=str(lexemes[i])
            t.token_type=Token_type.Number    
        else:
            t.token_type = Token_type.Error

    return Tokens
    '''


def find_token(text):
    tokens = re.findall(r'\w+|[\=\+\-\*\/\<\>\(\)\{\}\'\"\n\:\[\]\,\!\." "]', text)
    print(tokens)
    i = 0
    """while i<len(tokens):
        if(tokens[i]=="="and tokens[i+1]=="="):
            Tokens.append(token(i, Token_type.EQUALCOMP))
            i+=1
        i+=1
        """
    while i < len(tokens):
        if tokens[i] == "{":
            t = token()
            t.lex = str(tokens[i])
            t.token_type = Token_type.OpenCommentOp
            Tokens.append(t)
            j = i + 1
            comments = ""
            while j < len(tokens):
                if tokens[j] != "\n":
                    comments += tokens[j]
                    j += 1
                else:
                    break
            i = j
            s = token()
            s.lex = comments
            s.token_type = Token_type.CloseCommentOp
            Tokens.append(s)
            print(Tokens[1].to_dict())
        elif tokens[i] == "{" and i + 1 < len(tokens):
            if tokens[i + 1] == "*":
                t = token()
                t.lex = str(tokens[i] + tokens[i + 1])
                t.token_type = Token_type.OpenMultiCommentOp
                Tokens.append(t)
                j = i + 1
                comments = ""
                while j < len(tokens):
                    if tokens[j] == "*}":
                        t = token()
                        t.lex = str(tokens[i] + tokens[i + 1])
                        t.token_type = Token_type.CloseMultiCommentOp
                        Tokens.append(t)
                        break
                    else:
                        comments += tokens[j]
                        j += 1

                i = j
                s = token()
                s.lex = comments
                s.token_type = Token_type.OpenMultiCommentOp
                Tokens.append(s)

        elif tokens[i] in ReservedWords:
            t = token()
            t.lex = str(tokens[i])
            t.token_type = ReservedWords[tokens[i]]
            Tokens.append(t)
        elif (re.match("[a-zA-Z][a-zA-Z0-9]*", tokens[i])):
            t = token()
            t.lex = str(tokens[i])
            t.token_type = Token_type.ValIdentifier
            Tokens.append(t)
        elif tokens[i] in Operators:
            if tokens[i] == "=" and i + 1 < len(tokens):
                if tokens[i + 1] == "=":
                    t = token()
                    t.lex = "=="
                    t.token_type = Operators["=="]
                    Tokens.append(t)
                    i = i + 1
                else:
                    t = token()
                    t.lex = "="
                    t.token_type = Operators["="]
                    Tokens.append(t)

            elif tokens[i] == "<" and i + 1 < len(tokens):
                if tokens[i + 1] == "=":
                    t = token()
                    t.lex = "<="
                    t.token_type = Operators["<="]
                    Tokens.append(t)
                    i = i + 1
                else:
                    t = token()
                    t.lex = "<"
                    t.token_type = Operators["<"]
                    Tokens.append(t)
            elif tokens[i] == ">" and i + 1 < len(tokens):
                if tokens[i + 1] == "=":
                    t = token()
                    t.lex = ">="
                    t.token_type = Operators[">="]
                    Tokens.append(t)
                    i = i + 1
                else:
                    t = token()
                    t.lex = ">"
                    t.token_type = Operators[">"]
                    Tokens.append(t)
            elif tokens[i] == ":" and i + 1 < len(tokens):
                if tokens[i + 1] == ":":
                    t = token()
                    t.lex = "::"
                    t.token_type = Operators["::"]
                    Tokens.append(t)
                    i = i + 1
                else:
                    t = token()
                    t.lex = ":"
                    t.token_type = Operators[":"]
                    Tokens.append(t)
            else:
                t = token()
                t.lex = str(tokens[i])
                t.token_type = Operators[tokens[i]]
                Tokens.append(t)
        elif re.match("([0-9]+)+(.[0-9]*)?", tokens[i]):
            t = token()
            t.lex = str(tokens[i])
            t.token_type = Token_type.Constant
            Tokens.append(t)
        else:
            t = token()
            t.lex = str(tokens[i])
            t.token_type = Token_type.Error
            Tokens.append(t)
            break
        i += 1

    return (Tokens)


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