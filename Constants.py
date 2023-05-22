from enum import Enum


class Token_type(Enum):  # listing all tokens type
    And = 1
    Array = 2
    Begin = 3
    Case = 4
    Const = 5
    Div = 6
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
    Semicolon = 36
    EqualOp = 37
    LessThanOp = 38
    GreaterThanOp = 39
    NotEqualOp = 40
    GreaterThanEqOp = 41
    SmallerThanEqOp = 42
    PlusOp = 43
    MinusOp = 44
    MultiplyOp = 45
    DivideOp = 46
    Identifier = 47
    Constant = 48
    Comma = 49
    String = 50
    OpenParenthesis = 51
    CloseParenthesis = 52
    AssignmentOp = 53
    Dot = 54
    Colon = 55
    OpenMultiCommentOp = 56
    CloseMultiCommentOp = 57
    CloseCommentOp = 58
    OpenCommentOp = 59
    Error = 60
    Uses = 61
    Boolean = 62
    Real = 63
    Integer = 64
    Character = 65
    Read = 66
    ReadLn = 67
    Write = 68
    WriteLn = 69
    LessThanEqOp = 70
    RightParenthesis = 71
    LeftParenthesis = 72
    Quote = 73
    Number = 74


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
    "WITH": Token_type.With,
    "REPEAT": Token_type.Repeat,
    "USES": Token_type.Uses
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
    ")": Token_type.RightParenthesis,
    "(": Token_type.LeftParenthesis,
    "'": Token_type.Quote
}

Constants = {
    "WRITELN": Token_type.WriteLn,
    "READLN": Token_type.ReadLn,
    "INTEGER": Token_type.Integer,
    "REAL": Token_type.Real,
    "CHAR": Token_type.Character,
    "STRING": Token_type.String,
    "BOOLEAN": Token_type.Boolean,
    "READ": Token_type.Read,
    "WRITE": Token_type.Write,

}