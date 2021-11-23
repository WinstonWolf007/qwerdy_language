#####################################
# IMPORT
#####################################
import PYTHON.System.error as error
import PYTHON.System.data as data
from PYTHON.System.checkType import CheckTypeVariable


# class 'Variable' is used display type, value the variables
class Variable:
    def __init__(self):
        self.TT_VAR = data.TT_VAR
        self.lineCode = data.LINE
        self.error = error

    def displayValueVariable(self, name):
        try:
            print('\033[34m' + str(self.TT_VAR.get(name[1:])[1]) + '\033[0m')
        except:
            self.error.Error(NameError, 0)

    def displayTypeVariable(self, name):
        if name[0] != "$":
            self.error.Error(SyntaxError, 0)
        else:
            try:
                print('\033[34m' + f"<typeof '{str(self.TT_VAR.get(name[1:])[0])}'>" + '\033[0m')
            except:
                self.error.Error("FaltalError", 0)

    def var(self, ops: list):
        name = ops[0]
        equal = ops[1]
        value = ops[2:]

        # check if there are the one equal
        if equal != '=':
            self.error.Error(SyntaxError, 6)

        # check name variable syntax
        elif name[0] != '$':
            self.error.Error(SyntaxError, 0)

        for el in name[1:]:
            if el not in data.LETTERS:
                self.error.Error(SyntaxError, 3, CODE_variable_name_letter=el)

        if CheckTypeVariable(value).is_type2()[0]:
            data.TT_VAR[name[1:]] = [CheckTypeVariable(value).is_type()[1], value]
        elif CheckTypeVariable(value).is_type2() == (False, 'float'):
            self.error.Error(SyntaxError, 7)
        elif CheckTypeVariable(value).is_type2() == (False, 'float2'):
            self.error.Error(SyntaxError, 9)
        elif CheckTypeVariable(value).is_type2() == (False, 'string'):
            self.error.Error(SyntaxError, 4, CODE_variable_value=" ".join(value))
        else:
            self.error.Error(SyntaxError, 8)