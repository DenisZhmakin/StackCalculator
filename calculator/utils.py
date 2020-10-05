from stack import Stack


def infix_to_postfix(tokens_list: list):
    if type(tokens_list) != list and \
            tokens_list == []:
        raise ValueError

    priority = {'**': 4, '*': 3, '/': 3, '+': 2, '-': 2}
    op_stack = Stack()
    postfix_list = []

    for token in tokens_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                    (priority[op_stack.peek()] >= priority[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


def parse_string(text: str):
    tokens_list = []
    current_number = ''

    for index, char in enumerate(text.replace(' ', '')):
        if char.isdigit():
            if index + 1 < len(text) and text[index + 1].isdigit():
                current_number += char
            else:
                current_number += char
                tokens_list.append(current_number)
                current_number = ''
        elif char == '-':
            if index + 1 < len(text) and text[index + 1].isdigit():
                current_number += '-'
                continue

            tokens_list.append('-')
        else:
            tokens_list.append(char)

    return tokens_list
