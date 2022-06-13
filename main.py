from javalang import tokenizer
import math


OPERANDS = {
    'Literal',
    'Integer',
    'DecimalInteger',
    'OctalInteger',
    'BinaryInteger',
    'HexInteger',
    'FloatingPoint',
    'DecimalFloatingPoint',
    'HexFloatingPoint',
    'Boolean',
    'Character',
    'String',
    'Null',
    'Annotation',
    'Identifier',
}


def tokenize(code):
    return list(tokenizer.tokenize(code))


def calculate_operands_and_operators(tokens):
    operands = {}
    operators = {}
    n1 = 0
    N1 = 0
    n2 = 0
    N2 = 0
    for token in tokens:
        name, value = token.__class__.__name__, token.value
        # print(name, value)
        if name in OPERANDS:
            # TODO: remove if condition
            if name == 'String':
                value = value[1:-1]
            operands[value] = operands.get(value, 0) + 1
            N2 += 1
        else:
            operators[value] = operators.get(value, 0) + 1
            N1 += 1

    n2 = len(operands)
    n1 = len(operators)
    return n1, N1, n2, N2, operands, operators


def calculate_halstead(n1, N1, n2, N2):
    N = N1 + N2
    n = n1 + n2
    estimated_length = n1 * math.log2(n1) + n2 * math.log2(n2)
    PR = estimated_length / N
    V = estimated_length * math.log2(n)
    D = (n1 / 2) * (N2 / n2)
    E = D * V
    T = E / 18
    B = V / 3000
    return {
        'Program length': N,
        'Program vocabulary': n,
        'Estimated length': round(estimated_length, 3),
        'Purity ratio': round(PR, 3),
        'Volume': round(V, 3),
        'Difficulty': round(D, 3),
        'Program effort': round(E, 3),
        'Time required to program': round(T, 3),
        'Number of delivered bugs': round(B, 3),
    }


def calculate_cyclomatic(operators):
    complexity = 1
    loops_conditions = {'for', 'while', 'if', 'case'}
    for cyc_operator in loops_conditions:
        if(cyc_operator in operators):
            complexity += operators[cyc_operator]
    return complexity


def format_dict(dict):
    space = max([len(key) for key in dict.keys()])
    for key, value in dict.items():
        print(' {0:{space}} |  {1}'.format(key, value, space=space))
    print('\n--------------------\n')


file_url = input('Enter java file path: ')

try:
    with open(file_url, 'r') as file:
        source = file.read()
        tokens = tokenize(source)
        n1, N1, n2, N2, operands, operators = calculate_operands_and_operators(
            tokens)

        print("\nOperators: \n")
        format_dict(operators)
        print("\nOperands: \n")
        format_dict(operands)
        print("Operators n1: ", n1)
        print("Operators N1: ", N1)
        print("Operands n2: ", n2)
        print("Operands N2: ", N2)
        print('\n--------------------')
        halstead = calculate_halstead(n1, N1, n2, N2)
        cyclomatic = calculate_cyclomatic(operators)
        print("\nHalstead complexity: \n")
        format_dict(halstead)
        print("Cyclomatic complexity: ", cyclomatic, '\n\n--------------------')
except FileNotFoundError:
    print('File not found')
    exit()
