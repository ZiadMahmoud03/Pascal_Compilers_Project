from Scanner    import *
from Constants  import *
from tokenizer  import *
from enum import Enum
import graphviz


def create_relational_operator_dfa(user_input):
    mylist = r'\w+|<=|>=|==|<>|{|}|{|}|[|]|.;,:=+-\/<>()' '[a-zA-Z0-9]'
    transitions = {}
    accepting_states = set()
    error_state = 'error'
    initial_state = 0
    current_state = initial_state

    transitions[initial_state] = {mylist[1:]: error_state}

    for char in user_input:
        transitions[current_state] = {mylist: error_state}
        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state
        transitions[current_state] = {mylist: error_state}

    # Check if the final state corresponds to a relational operator in the RelationalOperators dictionary
    if user_input in RelationalOperators:
        accepting_states.add(current_state)
        token_type = RelationalOperators[user_input]  # Derive token type from ArithmeticOperators dictionary
        transitions[current_state] = {'': token_type}

    return transitions, accepting_states, initial_state


def create_arithmetic_operator_dfa(user_input):
    mylist = r'\w+|<=|>=|==|<>|{|}|{|}|[|]|.;,:=+-\/<>()' '[a-zA-Z0-9]'
    transitions = {}
    accepting_states = set()
    error_state = 'error'
    initial_state = 0
    current_state = initial_state

    transitions[initial_state] = {mylist[1:]: error_state}

    for char in user_input:
        transitions[current_state] = {mylist: error_state}
        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state
        transitions[current_state] = {mylist: error_state}

    # Check if the final state corresponds to an arithmetic operator in the ArithmeticOperators dictionary
    if user_input in ArithmeticOperators:
        accepting_states.add(current_state)
        token_type = ArithmeticOperators[user_input]  # Derive token type from ArithmeticOperators dictionary
        transitions[current_state] = {'': token_type}

    return transitions, accepting_states, initial_state


def create_constant_dfa(user_input):
    mylist = r'\w+|<=|>=|==|<>|{|}|{|}|[|]|.;,:=+-\/<>()' '[a-zA-Z0-9]'
    transitions = {}
    accepting_states = set()
    error_state = 'error'
    initial_state = 0
    current_state = initial_state

    transitions[initial_state] = {mylist[1:]: error_state}

    for char in user_input:
        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state
        transitions[current_state] = {mylist: error_state}

    # Check if the final state corresponds to a constant in the Constants dictionary
    if user_input.upper() in Constants:
        accepting_states.add(current_state)
        token_type = Constants[user_input.upper()]  # Derive token type from Constants dictionary
        transitions[current_state] = {'': token_type}

    return transitions, accepting_states, initial_state


def create_reserved_word_dfa(user_input):
    mylist = r'\w+|<=|>=|==|<>|{|}|{|}|[|]|.;,:=+-\/<>()' '[a-zA-Z0-9]'
    transitions = {}
    accepting_states = set()
    error_state = 'error'
    initial_state = 0
    current_state = initial_state

    transitions[initial_state] = {mylist[1:]: error_state}  # Add initial error transition

    for index, char in enumerate(user_input):
        transitions[current_state] = {mylist: error_state}

        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state
        transitions[current_state] = {mylist: error_state}

    # Add the final state as an accepting state with the derived token type
    if user_input.upper() in ReservedWords:
        accepting_states.add(current_state)
        token_type = ReservedWords[user_input.upper()]
        transitions[current_state] = {'': token_type}

    return transitions, accepting_states, initial_state


def create_combined_dfa(user_input):
    mylist = r'\w+|<=|>=|==|<>|{|}|{|}|[|]|.;,:=+-\/<>()' '[a-zA-Z0-9]'
    transitions = {}
    accepting_states = set()
    error_state = 'error'
    initial_state = 0

    current_state = initial_state

    transitions[initial_state] = {mylist[1:]: error_state}
    for index, char in enumerate(user_input):
        transitions[current_state] = {mylist: error_state}
        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state
        transitions[current_state] = {mylist: error_state}

    # Add the final state as an accepting state with a token type representing the combined DFA
    accepting_states.add(current_state)
    token_type = Token_type.Combined  # Replace with the desired token type for the combined DFA
    transitions[current_state] = {'': token_type}

    return transitions, accepting_states, initial_state


def create_comment_dfa(user_input):
    mylist = r'\w+|<=|>=|==|<>|{|}|{|}|[|]|.;,:=+-\/<>()' '[a-zA-Z0-9]'
    transitions = {}
    accepting_states = {2, 5, 9, 11, 12}
    initial_state = 0
    error_state = 'error'
    current_state = initial_state

    transitions[initial_state] = {mylist[1:]: error_state}

    for char in user_input:
        transitions[current_state] = {mylist: error_state}
        if current_state not in transitions:
            transitions[current_state] = {}

        if current_state == 0:
            if char == "{":
                next_state = 1
            elif char == "(":
                next_state = 4
            elif char == "*":
                next_state = 7
            elif char == "'":
                next_state = 10
            elif char == "[":
                next_state = 13
            else:
                next_state = 0
        elif current_state == 1:
            if char == "}":
                next_state = 2
            elif char == "*":
                next_state = 7
            else:
                next_state = 1
        elif current_state == 4:
            if char == ")":
                next_state = 5
            else:
                next_state = 4
        elif current_state == 7:
            if char == "*":
                next_state = 8
            else:
                next_state = 7
        elif current_state == 8:
            if char == "}":
                next_state = 9
            else:
                next_state = 7
        elif current_state == 10:
            if char == "'":
                next_state = 11
            else:
                next_state = 10
        elif current_state == 13:
            if char == "]":
                next_state = 12
        else:
            next_state = 0

        transitions[current_state][char] = next_state
        current_state = next_state
        transitions[current_state] = {mylist: error_state}

    transitions[current_state] = {}

    return transitions, accepting_states, initial_state


def draw_dfa(transitions, accepting_states, initial_state, format='png'):
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR')

    for state, state_transitions in transitions.items():
        if state in accepting_states:
            dot.node(str(state), shape='doublecircle')
        else:
            dot.node(str(state))

        for char, next_state in state_transitions.items():
            if char == '':
                char = ''
            dot.edge(str(state), str(next_state), label=char)

    dot.attr('node', shape='none')
    dot.node('start', '')
    dot.edge('start', str(initial_state), label='start')

    dot.format = 'png'
    dot.render('dfa', cleanup=True)


def create_combined_dfa(user_input):
    transitions = {}
    initial_state = None
    accepting_states = set()
    inside_comment = False

    for token in get_tokens(user_input):
        t_transitions, t_accepting_states, t_initial_state = create_dfa(token)

        if t_initial_state is not None:
            if not initial_state:
                initial_state = t_initial_state
            accepting_states = accepting_states.union(t_accepting_states)

            for state, t_transitions in t_transitions.items():
                if state not in transitions:
                    transitions[state] = {}

                for input, next_state in t_transitions.items():
                    if input in transitions and transitions[input] != next_state:
                        # Conflicting transition, handle here
                        if not inside_comment:
                            raise Exception('Conflicting transition!')
                    else:
                        transitions[state][input] = next_state

            # Add epsilon transitions
            for t_state, t_next_state in t_transitions.items():
                if t_next_state in t_accepting_states:
                    transitions[t_state][''] = t_next_state

                    # Check if token opened a multiline comment
            if token == '{*' and not inside_comment:
                inside_comment = True
            # Check if token closed a multiline comment
            elif token == '*}' and inside_comment:
                inside_comment = False

    return transitions, accepting_states, initial_state


def get_tokens(user_input):
    tokens = []
    inside_comment = False
    # Use a regex to get all tokens
    for token in re.findall(r'\d+|\w+|[<>=!]+|:=|[{}();\*\"\'|]', user_input):
        if not inside_comment:
            if token in ['{*', '{']:
                inside_comment = True
            else:
                tokens.append(token)
        else:
            if token == '*}':
                inside_comment = False
            else:
                pass  # Ignore token inside comment
    return tokens


def create_dfa(token):
    # Check full token to determine correct DFA
    if token in ReservedWords:
        return create_reserved_word_dfa(token)
    elif token in ArithmeticOperators or token == ':=':
        return create_arithmetic_operator_dfa(token)
    elif token in RelationalOperators:
        return create_relational_operator_dfa(token)
    elif token in Constants:
        return create_constant_dfa(token)
    elif token in Comments:
        return create_comment_dfa(token)
    return {}, set(), None
    # Add logic for strings, identifiers and numbers here


def draw_dfa_from_input(user_input):
    transitions, accepting_states, initial_state = create_comment_dfa(user_input)
    draw_dfa(transitions, accepting_states, initial_state, format='png')

