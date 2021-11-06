from error import Error
from checkType import CheckTypeVariable
from function import Function
from ChangeVariableInOperator import ChangeVariableForValue
from data import *


def Type(value):
    if CheckTypeVariable(value).is_int(): return int(value)
    elif CheckTypeVariable(value).is_float(): return float(value)
    else: return value

class Condition:
    def __init__(self):
        self.function = Function()

    def smallCondition_do(self, name1_, operator_, name2_):

        values = ChangeVariableForValue([name1_, operator_, name2_]).changeData()
        values[0] = Type(values[0])
        values[2] = Type(values[2])

        # get True or False according to operator
        ops = {
            '==': True if name1_ == name2_ else False,
            '>': True if name1_ > name2_ else False,
            '>=': True if name1_ >= name2_ else False,
            '<': True if name1_ < name2_ else False,
            "<=": True if name1_ <= name2_ else False,
            '!=': True if name1_ != name2_ else False
        }
        return ops.get(operator_) if ops.get(operator_) is not None else Error(SyntaxError, 5)

    def bigCondition_if_elseIf_else(self, condition):

        idx = 0
        condition_dict = {}

        c = " ".join(condition)
        c1 = c.replace(" ELSIF: ", "|").replace(" ELSE: ", "|").split("|")
        print(c1)
        exit()
        for i in c1:
            c3 = i.split(" THEN ")
            print(c3)
            syntax_dict = {
                idx: {
                    'do': c3[0].split(),
                    'func': c3[1].split()
                }
            }
            condition_dict.update(syntax_dict)
            idx += 1

        ChangeVariableForValue(condition_dict[0]['do']).changeData()

        for i in condition_dict:
            if self.smallCondition_do(condition_dict[i]['do'][0], condition_dict[i]['do'][1], condition_dict[i]['do'][2]):
                if condition_dict[i]['func'][0] == 'OUT:':
                    self.function.out(condition_dict[i]['func'][1:])

                elif condition_dict[i]['func'][0] in self.function.all_func_create:
                    print('created function detected')