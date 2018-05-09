class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)


def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if token == "" or token == " ":
            continue
        if token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == "-":
            difference = stack.pop() - stack.pop()
            stack.push(difference)
        elif token == "/":
            quotient = stack.pop() / stack.pop()
            stack.push(quotient)
        else:
            stack.push(int(token))
    return stack.pop()

eval_postfix("2 3 + 4 *")