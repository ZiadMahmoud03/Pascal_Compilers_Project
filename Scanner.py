import tkinter as tk
from enum import Enum
import re
import pandas


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
            token_type = TokenType.Identifier
            result += f"{t}: {token_type}\n"
        elif re.match("[-+]?\d+(\.\d+)?([eE][-+]?\d+)?", t):
            token_type = TokenType.Number
            result += f"{t}: {token_type}\n"

    print(result)
    return result


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
    label4 = tk.Label(root, text="Lexem is " + find_token(uppercase_text), font=("helvetica", 10, "bold"))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(
    text="Scan", command=scan, bg="brown", fg="white", font=("helvetica", 9, "bold")
)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
