import tkinter as tk
from enum import Enum
import re
import pandas
import pandastable as pt
from nltk.tree import *


class TokenType(Enum):  # listing all tokens type
    And = 1
    Array = 2
    Begin = 3
    Case = 4
    Constant = 5
    Divide = 6
    Do = 7
    Downto = 8
    Else = 9
    End = 10
    File = 11
    For = 12
    Function = 13
    Goto = 14
    If = 15
    In = 16
    Label = 17
    Mod = 18
    Nil = 19
    Not = 20
    Of = 21
    Or = 22
    Packed = 23
    Procedure = 24
    Program = 25
    Record = 26
    Repeat = 27
    Set = 28
    Then = 29
    To = 30
    Type = 31
    Until = 32
    Var = 33
    While = 34
    With = 35
    Dot = 36
    Semicolon = 37
    LessThanOp = 38
    GreaterThanOp = 39
    LessThanEqOp = 40
    GreaterThanEqOp = 41
    EqualOp = 42
    AssignmentOp = 43
    PlusOp = 44
    MinusOp = 45
    MultiplyOp = 46
    DivideOp = 47
    OpenMultiCommentOp = 48
    CloseMultiCommentOp = 49
    CloseCommentOp = 50
    OpenCommentOp = 51
    rightparenthesis = 52
    leftparenthesis = 53
    quote = 54
    WriteLine = 55
    ReadLine = 56
    Integer = 57
    Real = 58
    Character = 59
    String = 60
    Boolean = 61
    Identifier = 62
    Number = 63
    Error = 64


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


# Reserved word Dictionary
ReservedWords = {
    "AND": TokenType.And,
    "ARRAY": TokenType.Array,
    "BEGIN": TokenType.Begin,
    "CASE": TokenType.Case,
    "CONST": TokenType.Constant,
    "DIV": TokenType.Divide,
    "DO": TokenType.Do,
    "DOWNTO": TokenType.Downto,
    "ElSE": TokenType.Else,
    "END": TokenType.End,
    "FILE": TokenType.File,
    "FOR": TokenType.For,
    "FUNCTION": TokenType.Function,
    "GOTO": TokenType.Goto,
    "IF": TokenType.If,
    "IN": TokenType.In,
    "LABEL": TokenType.Label,
    "MOD": TokenType.Mod,
    "NIL": TokenType.Nil,
    "NOT": TokenType.Not,
    "OF": TokenType.Of,
    "OR": TokenType.Or,
    "PACKED": TokenType.Packed,
    "PROCEDURE": TokenType.Procedure,
    "PROGRAM": TokenType.Program,
    "RECORD": TokenType.Record,
    "SET": TokenType.Set,
    "THEN": TokenType.Then,
    "TO": TokenType.To,
    "TYPE": TokenType.Type,
    "UNTIL": TokenType.Until,
    "VAR": TokenType.Var,
    "WHILE": TokenType.While,
    "WITH": TokenType.With
}

ArithmeticOperators = {
    ".": TokenType.Dot,
    ";": TokenType.Semicolon,
    "=": TokenType.EqualOp,
    ":=": TokenType.AssignmentOp,
    "+": TokenType.PlusOp,
    "-": TokenType.MinusOp,
    "*": TokenType.MultiplyOp,
    "/": TokenType.DivideOp
}

RelationalOperators = {
    "<=": TokenType.LessThanEqOp,
    ">=": TokenType.GreaterThanEqOp,
    "=": TokenType.EqualOp,
    "<": TokenType.LessThanOp,
    ">": TokenType.GreaterThanOp
}

Comments = {
    "{*": TokenType.OpenMultiCommentOp,
    "}*": TokenType.CloseMultiCommentOp,
    "{": TokenType.OpenCommentOp,
    "}": TokenType.CloseCommentOp,
    ")": TokenType.rightparenthesis,
    "(": TokenType.leftparenthesis,
    "'": TokenType.quote
}

Constants = {
    "writeln": TokenType.WriteLine,
    "readln": TokenType.ReadLine,
    "INTEGER": TokenType.Integer,
    "REAL": TokenType.Real,
    "CHAR": TokenType.Character,
    "STRING": TokenType.String,
    "BOOLEAN": TokenType.Boolean

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
            new_token=token(le,TokenType.Constant)
            Tokens.append(new_token)
        elif (re.match("^([a-zA-Z][a-zA-Z0-9]*)$",le)):
            new_token=token(le,TokenType.Identifier)
            Tokens.append(new_token)
        else :
            new_token=token(le,TokenType.Error)
            errors.append("Lexical error  "+ le)


def Parse():
    j = 0
    Children = []
    # Header_dict=Header(j)
    # Children.append(Header_dict["node"])
    dic_output = Match(TokenType.Dot, j)
    Children.append(dic_output["node"])
    Node = Tree('Program', Children)

    return Node


def Header(j):
    Children = []
    dic_output = Match(TokenType.Program, j)
    Children.append(dic_output["node"])
    dic_output = Match(TokenType.Identifier, dic_output["index"])
    Children.append(dic_output["node"])
    dic_output = Match(TokenType.Semicolon, dic_output["index"])
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
