import tkinter as tk
from Constants import *
import re
import pandas
import pandastable as pt
from nltk.tree import *


# class token to hold string and token type
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


errors = []


def find_token(text):
    lexems=text.split()
    for le in  lexems:
        if(le in ReservedWords ):
            new_token=token(le,ReservedWords[le])
            Tokens.append(new_token)
        elif(le in RelationalOperators):
            new_token=token(le,RelationalOperators[le])
            Tokens.append(new_token)
        elif (re.match("^\d+(\.[0-9]*)?$",le)):
            new_token=token(le,Token_type.Constant)
            Tokens.append(new_token)
        elif (re.match("^([a-zA-Z][a-zA-Z0-9]*)$",le)):
            new_token=token(le,Token_type.Identifier)
            Tokens.append(new_token)
        else :
            new_token=token(le,Token_type.Error)
            errors.append("Lexical error  "+ le)


def Parse():
    j = 0
    Children = []
    # Header_dict=Header(j)
    # Children.append(Header_dict["node"])
    dic_output = Match(Token_type.Dot, j)
    Children.append(dic_output["node"])
    Node = Tree('Program', Children)

    return Node


def Header(j):
    Children = []
    dic_output = Match(Token_type.Program, j)
    Children.append(dic_output["node"])
    dic_output = Match(Token_type.Identifier, dic_output["index"])
    Children.append(dic_output["node"])
    dic_output = Match(Token_type.Semicolon, dic_output["index"])
    Children.append(dic_output["node"])
    Node = Tree('Header', Children)
    return Node
    pass


def Match(a, j):
    output = dict()
    if (j < len(Tokens)):
        Temp = Tokens[x].to_dict()
        if (Temp['token_type'] == a):
            j += 1
            output["node"] = [Temp['Lex']]
            output["index"] = j
            return output
        else:
            output["node"] = ["error"]
            output["index"] = j + 1
            errors.append("Syntax error : " + Temp['Lex'] + " Expected dot")
            return output
    else:
        output["node"] = ["error"]
        output["index"] = j + 1
        return output


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
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
    # print(df)

    # to display token stream as table
    dTDa1 = tk.Toplevel()
    dTDa1.title('Token Stream')
    dTDaPT = pt.Table(dTDa1, dataframe=df, showtoolbar=True, showstatusbar=True)
    dTDaPT.show()
    # start Parsing
    Node = Parse()

    # to display errorlist
    df1 = pandas.DataFrame(errors)
    dTDa2 = tk.Toplevel()
    dTDa2.title('Error List')
    dTDaPT2 = pt.Table(dTDa2, dataframe=df1, showtoolbar=True, showstatusbar=True)
    dTDaPT2.show()
    Node.draw()
    # clear your list

    # label3 = tk.Label(root, text='Lexem ' + x1 + ' is:', font=('helvetica', 10))
    # canvas1.create_window(200, 210, window=label3)

    # label4 = tk.Label(root, text="Token_type"+x1, font=('helvetica', 10, 'bold'))
    # canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Scan', command=Scan, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
root.mainloop()
