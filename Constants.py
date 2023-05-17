from enum import Enum


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
