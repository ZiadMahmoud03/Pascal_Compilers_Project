from enum import Enum


class TokenType(Enum):  # listing all tokens type
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
    GreaterThanOrEqualOp = 41
    SmallerThanOrEqualOp = 42
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
    Char = 65
    Read = 66
    ReadLn = 67
    Write = 68
    WriteLn = 69


# Reserved word Dictionary
ReservedWords = {
    "if": TokenType.If,
    "downto": TokenType.Downto,
    "function": TokenType.Function,
    "mod": TokenType.Mod,
    "packed": TokenType.Packed,
    "set": TokenType.Set,
    "var": TokenType.Var,
    "case": TokenType.Case,
    "goto": TokenType.Goto,
    "nil": TokenType.Nil,
    "procedure": TokenType.Procedure,
    "then": TokenType.Then,
    "while": TokenType.While,
    "const": TokenType.Const,
    "not": TokenType.Not,
    "program": TokenType.Program,
    "to": TokenType.To,
    "with": TokenType.With,
    "end": TokenType.End,
    "begin": TokenType.Begin,
    "do": TokenType.Do,
    "else": TokenType.Else,
    "and": TokenType.And,
    "div": TokenType.Div,
    "file": TokenType.File,
    "of": TokenType.Of,
    "in": TokenType.In,
    "record": TokenType.Record,
    "type": TokenType.Type,
    "array": TokenType.Array,
    "label": TokenType.Label,
    "or": TokenType.Or,
    "repeat": TokenType.Repeat,
    "until": TokenType.Until,
    "for": TokenType.For,
    "uses": TokenType.Uses,
    "boolean":TokenType.Boolean,
    "string":TokenType.String,
    "real" : TokenType.Real,
    "integer":TokenType.Integer,
    "read" : TokenType.Read,
    "readln" :TokenType.ReadLn,
    "write" :TokenType.Write,
    "writeln":TokenType.WriteLn

}

Operators = {
    # Arithmetic
    "+": TokenType.PlusOp,
    "-": TokenType.MinusOp,
    "*": TokenType.MultiplyOp,
    "/": TokenType.DivideOp,
    "=": TokenType.EqualOp,
    "<": TokenType.LessThanOp,
    ">": TokenType.GreaterThanOp,
    ">=": TokenType.GreaterThanOrEqualOp,
    "<=": TokenType.SmallerThanOrEqualOp,
    "(": TokenType.OpenParenthesis,
    ")": TokenType.CloseParenthesis,
    ":=": TokenType.AssignmentOp,
    ";": TokenType.Semicolon,
    ",": TokenType.Comma,
    ":": TokenType.Colon,
}

Comments = {
    "{*": TokenType.OpenMultiCommentOp,
    "}*": TokenType.CloseMultiCommentOp,
    "{": TokenType.OpenCommentOp,
    "}": TokenType.CloseCommentOp,
}