from Scanner    import *
from Constants  import *
from tokenizer  import *
from enum import Enum
import graphviz

def create_relational_operator_dfa(user_input):
    transitions = {}
    accepting_states = set()
    initial_state = 0

    current_state = initial_state
    for char in user_input:
        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state

    # Check if the final state corresponds to a relational operator in the RelationalOperators dictionary
    if user_input in RelationalOperators:
        accepting_states.add(current_state)
        token_type = RelationalOperators[user_input]  # Derive token type from RelationalOperators dictionary
        transitions[current_state] = {'': token_type}

    return transitions, accepting_states, initial_state





def create_arithmetic_operator_dfa(user_input):
    transitions = {}
    accepting_states = set()
    initial_state = 0

    current_state = initial_state
    for char in user_input:
        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state

    # Check if the final state corresponds to an arithmetic operator in the ArithmeticOperators dictionary
    if user_input in ArithmeticOperators:
        accepting_states.add(current_state)
        token_type = ArithmeticOperators[user_input]  # Derive token type from ArithmeticOperators dictionary
        transitions[current_state] = {'': token_type}

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
                char = 'ε'
            dot.edge(str(state), str(next_state), label=char, constraint='false')

    # Add transitions for asterisks
    if Token_type.OpenMultiCommentOp in accepting_states:
        dot.node("asterisk1", shape='circle', label='*', width='0.1')
        dot.edge(str(initial_state), "asterisk1", label='*', constraint='false')

    if Token_type.CloseMultiCommentOp in accepting_states:
        dot.node("asterisk2", shape='circle', label='*', width='0.1')
        for state in accepting_states:
            dot.edge(str(state), "asterisk2", label='*', constraint='false')

    dot.attr('node', shape='none')
    dot.node('start', '')
    dot.edge('start', str(initial_state), label='start', constraint='false')

    dot.format = format
    dot.render('dfa', cleanup=True)


def create_constant_dfa(user_input):
    transitions = {}
    accepting_states = set()
    initial_state = 0

    current_state = initial_state
    for char in user_input:
        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state

    # Check if the final state corresponds to a constant in the Constants dictionary
    if user_input.upper() in Constants:
        accepting_states.add(current_state)
        token_type = Constants[user_input.upper()]  # Derive token type from Constants dictionary
        transitions[current_state] = {'': token_type}

    return transitions, accepting_states, initial_state



def create_reserved_word_dfa(user_input):
    transitions = {}
    accepting_states = set()
    initial_state = 0

    current_state = initial_state
    for index, char in enumerate(user_input):
        if current_state not in transitions:
            transitions[current_state] = {}

        next_state = current_state + 1
        transitions[current_state][char] = next_state
        current_state = next_state

    # Add the final state as an accepting state with the derived token type
    accepting_states.add(current_state)
    token_type = ReservedWords[user_input.upper()]  # Derive token type from ReservedWords dictionary
    transitions[current_state] = {'': token_type}

    return transitions, accepting_states, initial_state
def create_comment_dfa(user_input):
    transitions = {}
    accepting_states = {2,5,9,11}
    initial_state = 0

    current_state = initial_state
    for char in user_input:
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
        else:
            next_state = 0

        transitions[current_state][char] = next_state
        current_state = next_state

    transitions[current_state] = {}

    return transitions, accepting_states, initial_state


def draw_comment_dfa(user_input):
    transitions, accepting_states, initial_state = create_comment_dfa(user_input)
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR')

    for state, state_transitions in transitions.items():
        if state in accepting_states:
            dot.node(str(state), shape='doublecircle')
        else:
            dot.node(str(state))

        for char, next_state in state_transitions.items():
            dot.edge(str(state), str(next_state), label=char)

    dot.attr('node', shape='none')
    dot.node('start', '')
    dot.edge('start', str(initial_state), label='start')

    dot.format = 'png'
    dot.render('comment_dfa', cleanup=True)



def draw_dfa_from_input(user_input):
    transitions, accepting_states, initial_state = create_comment_dfa(user_input)
    draw_dfa(transitions, accepting_states, initial_state, format='png')
