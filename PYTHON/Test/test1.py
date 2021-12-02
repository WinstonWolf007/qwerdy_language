from PYTHON.System.changeVariableInOperator import ChangeVariableForValue
import PYTHON.System.data as data
from PYTHON.System.checkType import CheckTypeVariable


data.TT_VAR['a'] = ['int', '3']
data.TT_VAR['b'] = ['int', '4']


def var(ops: list):
    name = ops[0]
    equal = ops[1]
    value = ops[2:]

    try:
        value = list(map(str, ChangeVariableForValue(value).changeData()))
        return [eval(" ".join(value))]
    except:
        if len(value) == 1 and CheckTypeVariable(value).is_type2():
            return '\033[92m'+'ok is just value'+'\033[0m'
        else:
            return '\033[91m'+'SyntaxError: invalid operator'+'\033[0m'


print(var(['$c', '=', '$a', '+', '$b']))
