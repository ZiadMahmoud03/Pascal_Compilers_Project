from Scanner2 import *
from nltk.tree import *
import pandastable as pt
import pandas
import unittest
from nltk.draw import TreeWidget
from nltk.draw.util import CanvasFrame
import nltk

class RecursiveDescent:
    def __init__(self,tokens):
        self.tokens = tokens
        self.errors = []
    def parse(self):
        pointer=0
        Children=[]
        program_output = self.program(pointer)
        Children.append(program_output["node"])

        node=Tree('Program',Children)


        return self.remove_empty_nodes(node)


    def program(self, pointer):
        output = dict()
        children = []

        heading_output = self.heading(pointer)
        children.append(heading_output['node'])

        declaration_output = self.declaration(heading_output['index'])
        children.append(declaration_output['node'])

        execution_output = self.execution(declaration_output['index'])
        children.append(execution_output['node'])

        Node = Tree('Program', children)
        output["node"] = Node
        output["index"] = execution_output["index"]

        return output

    def heading(self, pointer):
        output = dict()
        children = []

        programID_output = self.programID(pointer)
        children.append(programID_output['node'])

        uses_output = self.uses(programID_output['index'])
        children.append(uses_output['node'])

        Node = Tree('Heading', children)
        output["node"] = Node
        output["index"] = uses_output["index"]

        return output

    def declaration(self, pointer):
        output = dict()
        children = []

        consdec_output = self.constDec(pointer)
        children.append(consdec_output['node'])

        typedec_output = self.typedec(consdec_output['index'])
        children.append(typedec_output['node'])

        vardec_output = self.vardec(typedec_output['index'])
        children.append(vardec_output['node'])

        functiondec_output = self.functiondec(vardec_output['index'])
        children.append(functiondec_output['node'])

        proceduredec_output = self.proceduredec(functiondec_output['index'])
        children.append(proceduredec_output['node'])

        Node = Tree('DeclarationSec', children)
        output["node"] = Node
        output["index"] = proceduredec_output["index"]

        return output

    def execution(self, pointer):
        output = dict()
        children = []

        block_output = self.codeblock(pointer)
        children.append(block_output['node'])

        Node = Tree('Execution', children)
        output["node"] = Node
        output["index"] = block_output["index"]

        return output


    def programID(self,pointer):
        output = dict()
        children = []

        program_output = self.match(Token_type.Program, pointer)
        children.append(program_output['node'])

        identifier_output = self.match(Token_type.Identifier, program_output['index'])
        children.append(identifier_output['node'])

        semicolon_output = self.match(Token_type.Semicolon, identifier_output['index'])
        children.append(semicolon_output['node'])

        Node = Tree('ProgramID', children)
        output["node"] = Node
        output["index"] = semicolon_output["index"]

        return output

    def uses(self, pointer):
        output = dict()
        children = []
        if pointer >= len(self.Tokens):
            # Handle end of token list
            output["node"] = ["error"]
            output["index"] = pointer + 1
            return output

        current = self.tokens[pointer].as_dict()

        if current['type'] == Token_type.Uses:
            uses_output = self.match(Token_type.Uses, pointer)
            children.append(uses_output['node'])

            packagelist_output = self.packagelist(uses_output['index'])
            children.append(packagelist_output['node'])

            semicolon_output = self.match(Token_type.Semicolon, packagelist_output['index'])
            children.append(semicolon_output['node'])
        else:
            semicolon_output = None

        Node = Tree('Uses', children)
        output["node"] = Node
        output["index"] = semicolon_output["index"] if semicolon_output else pointer

        return output

    def constDec(self, pointer):
        output = dict()
        children = []

        if pointer >= len(self.tokens):
            # Handle end of token list
            output["node"] = ["error"]
            output["index"] = pointer + 1
            return output

        current = self.tokens[pointer].as_dict()

        if current['type'] == Token_type.Const:
            const_output = self.match(Token_type.Const , pointer)
            children.append(const_output['node'])

            constdecprime_output = self.constdecprime(const_output['index'])
            children.append(constdecprime_output['node'])
        else:
            constdecprime_output = None

        Node = Tree('ConstDec', children)
        output["node"] = Node
        output["index"] = constdecprime_output["index"] if constdecprime_output else pointer

        return output
    def constdecprime(self, pointer):
        output = dict()
        children = []

        identifier_output = self.match(Token_type.Identifier , pointer)
        children.append(identifier_output['node'])

        equal_output = self.match(Token_type.EqualOp , identifier_output['index'])
        children.append(equal_output['node'])

        data_type_values_output = self.data_type_values(equal_output['index'])
        children.append(data_type_values_output['index'])

        semicolon_output = self.match(Token_type.Semicolon , data_type_values_output['index'])
        children.append(semicolon_output['node'])

        constdec2_output = self.constdec2(semicolon_output['index'])
        children.append(constdec2_output['node'])

        Node = Tree('ConstDec', children)
        output["node"] = Node
        output["index"] = constdec2_output["index"]

        return output

    def constdec2(self, pointer):
        output = dict()
        children = []

        if pointer >= len(self.tokens):
            # Handle end of token list
            output["node"] = ["error"]
            output["index"] = pointer + 1
            return output

        current = self.tokens[pointer].as_dict()

        if current['type'] == Token_type.Identifier:
            constdecprime_output = self.constdecprime(pointer)
            children.append(constdecprime_output['node'])
        else:
            constdecprime_output = None

        Node = Tree('Constant Definitions Prime', children)
        output["node"] = Node
        output["index"] = constdecprime_output["index"] if constdecprime_output else pointer

        return output

    def typedec(self, pointer):
        output = dict()
        children = []

        if pointer >= len(self.tokens):
            # Handle end of token list
            output["node"] = ["error"]
            output["index"] = pointer + 1
            return output

        current = self.tokens[pointer].as_dict()

        if current['type'] == Token_type.Type:
            type_output = self.match(Token_type.Type , pointer)
            children.append(type_output['node'])

            typedecprime_out = self.typedecprime(type_output['index'])
            children.append(typedecprime_out['node'])

        else:
            typedecprime_out = None

        Node = Tree('TypeDec', children)
        output["node"] = Node
        output["index"] = typedecprime_out["index"] if typedecprime_out else pointer

        return output

    def typedecprime(self, pointer):
        output = dict()
        children = []

        identifier_output = self.match(Token_type.Identifier , pointer)
        children.append(identifier_output['node'])

        equal_output = self.match(Token_type.EqualOp , identifier_output['index'])
        children.append(equal_output['node'])

        data_type_output = self.data_type(equal_output['index'])
        children.append(data_type_output['node'])

        semicolon_output = self.match(Token_type.Semicolon, data_type_output['index'])
        children.append(semicolon_output['node'])


        Node = Tree('TypeDec', children)
        output["node"] = Node
        output["index"] = semicolon_output["index"]

        return output

    def typedec2(self, pointer):
        output = dict()
        children = []

        if pointer >= len(self.tokens):
            # Handle end of token list
            output["node"] = ["error"]
            output["index"] = pointer + 1
            return output

        current = self.tokens[pointer].as_dict()

        if current['type'] == Token_type.Identifier:
            typedecprime_out = self.typedecprime(pointer)
            children.append(typedecprime_out['node'])
        else:
            typedecprime_out = None

        Node = Tree('TypeDec2', children)
        output["node"] = Node
        output["index"] = typedecprime_out["index"] if typedecprime_out else pointer

        return output

    def vardec(self, pointer):
        output = dict()
        children = []

        if pointer >= len(self.tokens):
            # Handle end of token list
            output["node"] = ["error"]
            output["index"] = pointer + 1
            return output

        current = self.tokens[pointer].as_dict()

        if current['type'] == Token_type.Var:
            vardec_output = self.match(Token_type.Var, pointer)
            children.append(vardec_output['node'])

            vardecprime_output = self.vardecprime(vardec_output['index'])
            children.append(vardecprime_output['node'])

        else:
            vardecprime_output = None

        Node = Tree('VarDec', children)
        output["node"] = Node
        output["index"] = vardecprime_output["index"] if vardecprime_output else pointer

        return output

    def vardecprime(self, pointer):
        output = dict()
        children = []

        varidlist_output = self.identifiers_list(pointer)
        children.append(varidlist_output['node'])

        vardecprime_output = self.vardecprime_prime(varidlist_output['index'])
        children.append(vardecprime_output['node'])

        colon_output = self.match(Token_type.Colon , varidlist_output['index'])
        children.append(colon_output['node'])

        data_type_output = self.data_type(colon_output['index'])
        children.append(data_type_output['node'])

        semicolon_output = self.match(Token_type.Semicolon , data_type_output['index'])
        children.append(semicolon_output['node'])

        vardecprime_output = self.vardecprime_prime(semicolon_output['index'])
        children.append(vardecprime_output['node'])

        Node = Tree('VarDec', children)
        output["node"] = Node
        output["index"] = vardecprime_output["index"]

        return output

    def vardec2(self, pointer):
        output = dict()
        children = []

        if pointer >= len(self.tokens):
            # Handle end of token list
            output["node"] = ["error"]
            output["index"] = pointer + 1
            return output

        current = self.tokens[pointer].as_dict()

        if current['type'] == Token_type.Identifier:
            variable_definition_prime_output = self.vardecprime(pointer)
            children.append(variable_definition_prime_output['node'])

        else:
            vardecprime_output = None

        Node = Tree('Variables Definition Prime', children)
        output["node"] = Node
        output["index"] = vardecprime_output["index"] if vardecprime_output else pointer

        return output

    def remove_empty_nodes(self, node):
        # if isinstance(node, str):
        #     return node

        # Recursively process child nodes
        children = [self.remove_empty_nodes(child) for child in node]

        # Remove empty child nodes
        children = [child for child in children if child]

        # If all child nodes were removed, return None
        if not children:
            return None

        # Update the children of the current node
        node.clear()
        node.extend(children)

        return node

    def match(self, expected_token_type, pointer):
        output = dict()
        if pointer < len(self.tokens):
            actual_token_type = self.tokens[pointer].as_dict()
            if actual_token_type['type'] == expected_token_type:
                pointer += 1
                output["node"] = [actual_token_type['lexeme']]
                output["index"] = pointer
                return output
            else:
                return self.fail_match(expected_token_type.name, actual_token_type, pointer)
        else:
            output["node"] = ["error"]
            output["index"] = pointer + 1
            return output


#
# def draw_nltk_tree(tree):
#     cf = CanvasFrame()
#     tc = TreeWidget(cf.canvas(), tree)
#     cf.add_widget(tc, 10, 10)
#     cf.print_to_file('tree.ps')
#     cf.destroy()
#     nltk.draw.tree.draw_trees(tree)
#
#
# def display_error_list(error_list):
#     df1 = pandas.DataFrame(error_list)
#     dTDa2 = tk.Toplevel()
#     dTDa2.title('Error List')
#     dTDaPT2 = pt.Table(dTDa2, dataframe=df1, showtoolbar=True, showstatusbar=True)
#     dTDaPT2.show()
# class ParserTest(unittest.TestCase):
#     def test_one_statement(self):
#         source_code = "PROGRAM TEST; USES x; VAR X : INTEGER;"
#         tokens = find_token(source_code)
#         parser = RecursiveDescent(tokens)
#         try:
#             result = parser.parse()
#             display_error_list(parser.errors)
#             draw_nltk_tree(result)
#             result.pretty_print()
#         except Exception as e:
#             print(f"Exception occurred during parsing: {e}")
#
#
# ParserTest.test_one_statement()











# def lookahead(Arr, pos):
#     for i in Arr:
#         if Match(i, pos, False)["node"] != ["error"]:
#             return True
#     return False

# def Match(a, j, report=True):
#     output = dict()
#     if j < len(Tokens):
#         temp = Tokens[j].to_dict()
#         if temp["token_type"] == a:
#             output["node"] = [temp["Lex"]]
#             output["index"] = j + 1
#             return output
#         else:
#             output["mode"] = ["error"]
#             output["node"] = ["error"]
#             output["index"] = j
#             if report:
#                 errors.append("Syntax error : " + temp["Lex"] + F" Expected {a}")
#             return output
#     else:
#         output["node"] = ["error"]
#         output["index"] = j
#         if report:
#             errors.append("Syntax error : " + F" Expected {a}")
#         return output

# def is_error(arr):
#     return 'mode' in arr[-1].keys() and arr[-1]['mode'] == ['error']


#GUI
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
    Node = RecursiveDescent.parse()

    # to display errorlist
    df1 = pandas.DataFrame(RecursiveDescent.errors)
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

