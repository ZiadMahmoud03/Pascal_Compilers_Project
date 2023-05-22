import tkinter as tk
import re
import pandas
from Constants import *
from tokenizer import *


my_text =[]
find_token(my_text)
result = []

for t in find_token.tokens:
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
    else:
        token_type = Token_type.Error

    print(result)
    



def scan():
    x1 = "Program  { X }  \
         = 5 THEN Y = 2 ;"
    uppercase_text = x1.upper()
    find_token(uppercase_text)
    df = pandas.DataFrame.from_records([t.to_dict() for t in Tokens])
    print(df)


scan()
