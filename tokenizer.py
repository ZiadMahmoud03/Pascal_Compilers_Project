import re
# Categorise each lexeme into tokens
# If invalid token found, report an error.
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


def find_token(text):
     tokens = re.findall('\w+|[\.\;\:\=\+\-\*\/\<\>\(\)\{\}\']', text)

