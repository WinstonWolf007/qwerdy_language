from PYTHON.System.error import Error
import PYTHON.System.data as data
from PYTHON.System.checkType import CheckTypeVariable


def var(ops: list):
    name = ops[0]
    equal = ops[1]
    value = ops[2:]

    # check if there are the one equal
    if equal != '=':
        Error(SyntaxError, 6)

    # check name variable syntax
    elif name[0] != '$':
        Error(SyntaxError, 0)

    for el in name[1:]:
        if el not in data.LETTERS:
            Error(SyntaxError, 3, CODE_variable_name_letter=el)

    if CheckTypeVariable(value).is_type2()[0]:
        data.TT_VAR[name[1:]] = value
    elif CheckTypeVariable(value).is_type2() == (False, 'float'):
        Error(SyntaxError, 7)
    elif CheckTypeVariable(value).is_type2() == (False, 'float2'):
        Error(SyntaxError, 9)
    elif CheckTypeVariable(value).is_type2() == (False, 'string'):
        Error(SyntaxError, 4, CODE_variable_value=" ".join(value))
    else:
        Error(SyntaxError, 8)