import re


# Categorise each lexeme into tokens
# If invalid token found, report an error.
# class token to hold string and token type


# class token to hold string and token type
class token:
    def _init_(self, lex, token_type):
        self.lex = lex
        self.token_type = token_type

    def to_dict(self):
        return {
            'Lex': self.lex,
            'token_type': self.token_type
        }

    @staticmethod
    def find_token(self, text):
        result = ""
        tokens = re.findall('\w+|<=|>=|==|<>|\{\*|\*\}|\{\*\}\}|[\.\;\,\:\=\+\-\*\/\<\>\(\)\{\}\'\[\]]', text)
        return tokens


Tokens = []  # to add tokens to list