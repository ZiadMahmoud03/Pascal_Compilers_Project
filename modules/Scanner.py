import tkinter as tk
from enum import Enum
import re
import pandas


class Token_type(Enum):  # listing all tokens type
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
    "AND": Token_type.And,
    "ARRAY": Token_type.Array,
    "BEGIN": Token_type.Begin,
    "CASE": Token_type.Case,
    "CONST": Token_type.Constant,
    "DIV": Token_type.Divide,
    "DO": Token_type.Do,
    "DOWNTO": Token_type.Downto,
    "ElSE": Token_type.Else,
    "END": Token_type.End,
    "FILE": Token_type.File,
    "FOR": Token_type.For,
    "FUNCTION": Token_type.Function,
    "GOTO": Token_type.Goto,
    "IF": Token_type.If,
    "IN": Token_type.In,
    "LABEL": Token_type.Label,
    "MOD": Token_type.Mod,
    "NIL": Token_type.Nil,
    "NOT": Token_type.Not,
    "OF": Token_type.Of,
    "OR": Token_type.Or,
    "PACKED": Token_type.Packed,
    "PROCEDURE": Token_type.Procedure,
    "PROGRAM": Token_type.Program,
    "RECORD": Token_type.Record,
    "SET": Token_type.Set,
    "THEN": Token_type.Then,
    "TO": Token_type.To,
    "TYPE": Token_type.Type,
    "UNTIL": Token_type.Until,
    "VAR": Token_type.Var,
    "WHILE": Token_type.While,
    "WITH": Token_type.With
}

ArithmeticOperators = {
    ".": Token_type.Dot,
    ";": Token_type.Semicolon,
    "=": Token_type.EqualOp,
    ":=": Token_type.AssignmentOp,
    "+": Token_type.PlusOp,
    "-": Token_type.MinusOp,
    "*": Token_type.MultiplyOp,
    "/": Token_type.DivideOp
}

RelationalOperators = {
    "<=": Token_type.LessThanEqOp,
    ">=": Token_type.GreaterThanEqOp,
    "=": Token_type.EqualOp,
    "<": Token_type.LessThanOp,
    ">": Token_type.GreaterThanOp
}

Comments = {
    "{*": Token_type.OpenMultiCommentOp,
    "}*": Token_type.CloseMultiCommentOp,
    "{": Token_type.OpenCommentOp,
    "}": Token_type.CloseCommentOp,
    ")": Token_type.rightparenthesis,
    "(": Token_type.leftparenthesis,
    "'": Token_type.quote
}

Constants = {
    "writeln": Token_type.WriteLine,
    "readln": Token_type.ReadLine,
    "INTEGER": Token_type.Integer,
    "REAL": Token_type.Real,
    "CHAR": Token_type.Character,
    "STRING": Token_type.String,
    "BOOLEAN": Token_type.Boolean

}

Tokens = []  # to add tokens to list


def find_token(text):
    result = ""
    tokens = re.findall('\w+|[\.\;\:\=\+\-\*\/\<\>\(\)\{\}\']', text)

    for t in tokens:
        if t in ReservedWords:
            token_type = ReservedWords[t.upper()]
            result += f"{t}: {token_type}\n"
        elif t in ArithmeticOperators:
            token_type = ArithmeticOperators[t]
            result += f"{t}: {token_type}\n"
        elif t in RelationalOperators:
            token_type = RelationalOperators[t]
            result += f"{t}: {token_type}\n"
        elif t in Comments:
            token_type = Comments[t]
            result += f"{t}: {token_type}\n"
        elif t in Constants:
            token_type = Constants[t.upper()]
            result += f"{t}: {token_type}\n"
        elif re.match("^[a-zA-Z][a-zA-Z0-9]*$", t):
            token_type = Token_type.Identifier
            result += f"{t}: {token_type}\n"
        elif re.match("[-+]?\d+(\.\d+)?([eE][-+]?\d+)?", t):
            token_type = Token_type.Number
            result += f"{t}: {token_type}\n"

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


def scan():
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
    text="Scan", command=scan, bg="brown", fg="white", font=("helvetica", 9, "bold")
)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
