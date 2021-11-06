#####################################
# IMPORT
#####################################
from condition import Condition
from data import Data
import error
from function import Function
from variable import Variable

##########################################
# MAIN CODE
##########################################

class Code:
    def __init__(self):
        # function
        self.data = Data()
        self.function = Function()
        self.error = error

        # attribute variable stock in data for variable in basic2.py
        self.code = self.data.code.split() if isinstance(self.data.code, str) else self.data.code
        self.lineCode = self.data.line
        self.file = self.data.file
        self.LETTERS = self.data.LETTERS
        self.IS_FILE = self.data.IS_FILE

        # function in other file
        self.VARIABLE_CLASS = Variable()
        self.CONDITION_CLASS = Condition()

        self.CODE_FILE() if self.file else self.CODE_LANG()

    def CODE_FILE(self):
        code_stock = self.code
        for i in code_stock:
            self.code = i.split()
            self.CODE_LANG()
            self.lineCode += 1

    def CODE_LANG(self):

        if not self.file and self.code[-1][-1] != ";" and self.code[0] != 'FUNC:':
            self.error.Error(SyntaxError, 1)
        else:
            self.code = " ".join(self.code).replace(";", '').split(" ")

        match self.code:

            # help command
            case ["HELP"]:
                print('\033[34m' + "Read 'syntax.txt', file for vew all information" + '\033[0m')

            ########################################################################
            #                            CONDITION                                 #
            ########################################################################

            # small condition
            case ['DO:', name1, operator, name2, '?']:
                if self.CONDITION_CLASS.smallCondition_do(name1, operator, name2):
                    print('\033[34m' + "true" + '\033[0m')
                else:
                    print('\033[34m' + "false" + '\033[0m')

            case ["IF:", *opr]:
                self.CONDITION_CLASS.bigCondition_if_elseIf_else(opr)

            ########################################################################
            #                             VARIABLE                                 #
            ########################################################################

            # give new value in variable exist
            case [name2, '=', *values2]:

                if self.data.GET_var().get(name2[1:]) is None:
                    self.error.Error(NameError, 0, CODE_variable_name=name2)

                if self.data.GET_var().get(name2[1:])[0] == 'int' and len(values2) > 1:
                     n = 0
                     for i in values2:
                        if self.data.GET_var().get(i[1:]) is not None:
                            if self.data.GET_var().get(i[1:])[0] in ['int', 'float']:
                                values2[n] = str(self.data.GET_var().get(i[1:])[1])
                            else:
                                self.error.Error(ValueError, 1)
                        n += 1

                     self.data.POST_var(name2[1:], ['int', eval(" ".join(values2))])

                elif self.data.GET_var().get(name2[1:]):
                    self.data.POST_var(name2[1:], [self.data.GET_var().get(name2[1:])[0], " ".join(values2)])

            # create variable
            case [type_, name, "=", *values]:
                self.error.CheckIfError().createVariable(name, type_, values)
                if type_[:-1] == 'int':
                    try:
                        if len(values) == 1:
                            self.data.POST_var(name[1:], [type_[:-1], values[0]])
                        if self.error.CheckTypeVariable(values).is_string():
                            self.error.Error(ValueError, 1, CODE_variable_value=" ".join(values), CODE_variable_type=type_)
                        else:
                            n = 0
                            for i in values:
                                if self.data.GET_var().get(i[1:]) is not None:
                                    if self.data.GET_var().get(i[1:])[0] in ['int', 'float']:
                                        values[n] = str(self.data.GET_var().get(i[1:])[1])
                                    else:
                                        self.error.Error(ValueError, 1)
                                n += 1
                            self.data.POST_var(name[1:], [type_[:-1], eval(" ".join(values))])

                    except:
                        print(values)
                        self.error.Error(ValueError, 1, CODE_variable_type=type_, CODE_variable_value=" ".join(values))

                elif type_[:-1] == 'float':
                    try:
                        self.data.POST_var(name[1:], [type_[:-1], float(values[0])])
                    except:
                        pass

                elif type_[:-1] == 'string':
                    if values[0][0] == '"' and values[-1][-1] == '"':
                        self.data.POST_var(name[1:], [type_[:-1], " ".join(values)])

                elif type_[:-1] == 'bool':
                    try:
                        if len(values) == 1:
                            if values[0] in ['true', 'false']:
                                self.data.POST_var(name[1:], [type_[:-1], values])
                            else:
                                self.error.Error(ValueError, 1, CODE_variable_value=" ".join(values), CODE_variable_type=type_)

                        elif values[0] == "DO:":
                            if self.CONDITION_CLASS.smallCondition_do(values[1], values[2], values[3]):
                                self.data.POST_var(name[1:], [type_[:-1], 'true'])
                            else:
                                self.data.POST_var(name[1:], [type_[:-1], 'false'])
                    except:
                        self.error.Error(ValueError, 1, CODE_variable_value=" ".join(values), CODE_variable_type=type_)

            # print type variable
            case ['TYPE:', name]:
                self.VARIABLE_CLASS.displayTypeVariable(name)

            ########################################################################
            #                             OPERATOR                                 #
            ########################################################################
            case ['OUT:', *ops]:
                self.function.out(ops)

            ########################################################################
            #                             FUNCTION                                 #
            ########################################################################

            case ['FUNC:', name, *parameter]:
                parameters = " ".join(parameter).replace('[', '').replace(']', '').split(',')
                self.function.created_function(name, parameters)

            case _:
                self.error.Error(NameError, 2)
