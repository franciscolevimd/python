from stacks import StackDeque


def verify_symbols(value):
    stack = StackDeque()
    peers = {')': '(', '}': '{', ']': '['}
    for v in value:
        if v in '({[':
            stack.push(v)
        elif v in ')}]':
            if stack.is_empty() or stack.pop() != peers[v]:
                return False
    return stack.is_empty()


print(verify_symbols("({[]})"))   # Returns True
print(verify_symbols("({[)"))     # Returns False
print(verify_symbols("{[()]}"))   # Returns True
print(verify_symbols("(((()))"))  # Returns False
