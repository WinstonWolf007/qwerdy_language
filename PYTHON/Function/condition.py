#####################################
# IMPORT
#####################################
from PYTHON.System.error import Error
from PYTHON.System.checkType import CheckTypeVariable
from PYTHON.System.changeVariableInOperator import ChangeVariableForValue


# class 'Condition' is used for to do the condition in 'qwerdy' language
class Condition:

    # function 'Type' is used for change variable python type (exp: operator)
    def Type(self, value):
        if CheckTypeVariable(value).is_int():
            return int(value)
        elif CheckTypeVariable(value).is_float():
            return float(value)
        else:
            return value

    # do conditon is small condition -> VAR: $is_minor = DO: $age > 17....
    def do(self, ops):

        # variable attribution
        name1_, name2_, operator_ = ops
        values = ChangeVariableForValue([name1_, operator_, name2_]).changeData()
        values[0] = self.Type(values[0])
        values[2] = self.Type(values[2])

        # get True or False according to operator
        ops = {
            '==': True if name1_ == name2_ else False,
            '>': True if name1_ > name2_ else False,
            '>=': True if name1_ >= name2_ else False,
            '<': True if name1_ < name2_ else False,
            "<=": True if name1_ <= name2_ else False,
            '!=': True if name1_ != name2_ else False
        }

        # print result
        print(str(ops.get(operator_)).lower() if ops.get(operator_) is not None else Error(SyntaxError, 5))

    # IF, ELSIF, ELSE conditon is big condition -> IF: 1 == 1, ELSIF: 2 != 2, ELSE: [...]
    def if_elif_else(self, ops):

        """

        to change for the futur

        """

        """idx = 0
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
        """