import tkinter as tk
from enum import Enum
import re
import pandas
import pandastable as pt
from nltk.tree import *
from Constants import *
from Scanner2 import *

errors = []


def Program():
    Children = []

    Children.append(Header())
    Children.append(DeclarationSec())
    Children.append(Execution())
    # Block_dict=Block(Header_dict["index"])
    # Children.append(Block_dict["Node"])
    # dic_output = Match(Token_type.Program, j)
    # Children.append(dic_output["node"])
    Node = Tree('Program', Children)

    return Node


def Header():
    j = 0
    output = dict()
    Children = []
    ProgramID_Dict = Program_ID(j)
    Uses_Dict = Uses(j)
    Children.append(ProgramID_Dict["node"])
    Children.append(Uses_Dict["node"])
    # dic_output = Match(Token_type.Program, j)
    # Children.append(dic_output["node"])
    Node = Tree('Header', Children)
    output["node"] = Node

    return Node


def DeclarationSec():
    j = 5
    output = dict()
    Children = []
    Declaration_Dict = Declaration(j)
    ProcedureDeclarationSec_Dict = ProcedureDeclarationSec(j + 1)
    Children.append(Declaration_Dict["node"])
    Children.append(ProcedureDeclarationSec_Dict["node"])
    # dic_output = Match(Token_type.Program, j)
    # Children.append(dic_output["node"])
    Node = Tree('DeclarationSec', Children)
    output["node"] = Node

    return Node


def Execution():
    j = 2
    output = dict()
    children = []
    # complete
    out1 = Match(Token_type.If, j)
    children.append(out1["node"])
    # out2 = Match(Token_type.Const, out1["index"])
    # out3 = Match(Token_type.Type, out2["index"])

    Node = Tree("Execution", children)
    output["node"] = Node
    output["index"] = out1["index"]

    return output


def Program_ID(j):
    output = dict()
    children = []
    # complete
    out1 = Match(Token_type.Program, j)
    children.append(out1["node"])

    out2 = Match(Token_type.Identifier, out1["index"])
    children.append(out2["node"])

    out3 = Match(Token_type.Semicolon, out2["index"])
    children.append(out3["node"])

    Node = Tree("Program_ID", children)
    output["node"] = Node
    output["index"] = out3["index"]

    return output


def Uses(j):
    output = dict()
    children = []
    # complete
    out1 = Match(Token_type.Uses, j)
    children.append(out1["node"])

    out2 = Match(Token_type.Identifier, out1["index"])
    children.append(out2["node"])

    out3 = Match(Token_type.Semicolon, out2["index"])
    children.append(out3["node"])

    Node = Tree("Uses", children)
    output["node"] = Node
    output["index"] = out3["index"]

    return output


def Declaration(j):
    output = dict()
    children = []
    # complete
    out1 = Match(Token_type.Function, j)
    children.append(out1["node"])

    out2 = Match(Token_type.Identifier, out1["index"])
    children.append(out2["node"])

    out3 = Match(Token_type.Semicolon, out2["index"])
    children.append(out3["node"])

    Node = Tree("Declaration", children)
    output["node"] = Node
    output["index"] = out3["index"]

    return output


def ProcedureDeclarationSec(j):
    output = dict()
    children = []
    # complete
    out1 = Match(Token_type.Procedure, j)
    children.append(out1["node"])

    out2 = Match(Token_type.Identifier, out1["index"])
    children.append(out2["node"])

    out3 = Match(Token_type.Semicolon, out2["index"])
    children.append(out3["node"])

    Node = Tree("ProcedureDecSec", children)
    output["node"] = Node
    output["index"] = out3["index"]

    return output


def Statements(j):
    output = dict()
    children = []

    current = Tokens[j].to_dict()

    if (current['token type'] == Token_type.Read):
        readOutput = Match(Token_type.Read, j)
        children.append(readOutput['node '])

        identifierOutput = Match(Token_type.Identifier, readOutput['index'])
        children.append(identifierOutput['node'])
    else:
        writeOutput = Match(Token_type.Write, j)
        children.append(writeOutput['node'])
        identifierOutput = Match(Token_type.Identifier, writeOutput['index'])
        children.append(identifierOutput['node'])
    Node = Tree('Statements', children)
    output["node"] = Node
    output["Index"] = identifierOutput["Index"]
    return output


def lookahead(Arr, pos):
    for i in Arr:
        if Match(i, pos, False)["node"] != ["error"]:
            return True
    return False


def Match(a, j, report=True):
    output = dict()
    if j < len(Tokens):
        temp = Tokens[j].to_dict()
        if temp["token_type"] == a:
            output["node"] = [temp["Lex"]]
            output["index"] = j + 1
            return output
        else:
            output["mode"] = ["error"]
            output["node"] = ["error"]
            output["index"] = j
            if report:
                errors.append("Syntax error : " + temp["Lex"] + F" Expected {a}")
            return output
    else:
        output["node"] = ["error"]
        output["index"] = j
        if report:
            errors.append("Syntax error : " + F" Expected {a}")
        return output


def is_error(arr):
    return 'mode' in arr[-1].keys() and arr[-1]['mode'] == ['error']


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
    Node = Program()

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

#
#