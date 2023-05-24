# class token to hold string and token type
class Tokens:

    token_num = 0
    def _init_(self, lex, token_type):
        self.lex = lex
        self.token_type = token_type
        self.token_num += 1

    def to_dict(self):
        return {
            'Lex': self.lex,
            'token_type': self.token_type
        }


Tokens_List = []  # to add tokens to list