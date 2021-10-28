#####################################
# IMPORT
#####################################
import string

from error import *
from checkType import CheckTypeVariable
from data import Data

from variable import Variable
from condition import Condition
from function import Function

#####################################
# TOKEN
#####################################

LETTERS = string.ascii_letters + "_"
IS_FILE = False

##########################################
# MAIN CODE
##########################################

class Code:
    def __init__(self, code, lineCode, file=False):
        self.code = code.split() if isinstance(code, str) else code
        self.lineCode = lineCode
        self.file = file

        # data
        self.data = Data()

        # function in other file
        self.VARIABLE_CLASS = Variable(self.data.GET_var(), self.lineCode)
        self.CONDITION_CLASS = Condition(self.data.GET_var(), self.lineCode, LETTERS)

        if self.file:
            self.CODE_FILE()
        else:
            self.CODE_LANG()

    def CODE_FILE(self):
        code_stock = self.code

        for i in code_stock:
            self.code = i.split()
            self.CODE_LANG()
            self.lineCode += 1

    def CODE_LANG(self):

        ERROR_CODE = False

        if not self.file and self.code[-1][-1] != ";":
            Error('SyntaxError', 1, self.lineCode, self.code, self.file)
        else:
            self.code = " ".join(self.code).replace(";", '').split(" ")

        match self.code:

            # help command
            case ["help"]:
                print('\033[34m' + "Read 'syntax.txt', file for vew all information" + '\033[0m')

            ########################################################################
            #                            CONDITION                                 #
            ########################################################################

            # small condition
            case ['DO:', name1, operator, name2, '?']:
                if self.CONDITION_CLASS.smallCondition_do(name1, operator, name2):
                    print('\033[34m' + "true" + '\033[0m')

                elif not self.CONDITION_CLASS.smallCondition_do(name1, operator, name2):
                    print('\033[34m' + "false" + '\033[0m')

            case ["IF:", *opr]:
                self.CONDITION_CLASS.bigCondition_if_elseIf_else(opr)

            ########################################################################
            #                             VARIABLE                                 #
            ########################################################################

            # give new value in variable exist
            case [name2, '=', *values2]:

                if self.data.GET_var().get(name2[1:]) is None:
                    Error('NameError', 0, self.lineCode, self.code, self.file, CODE_variable_name=name2)
                    ERROR_CODE = True

                if self.data.GET_var().get(name2[1:])[0] == 'int' and len(values2) > 1:
                    v = "".join(values2)
                    result = eval(v)
                    self.data.POST_var(name2[1:], ['int', int(result)])
                    print(self.data.GET_var(name2[1:]))
                    print(self.data.GET_var())

                elif self.data.GET_var().get(name2[1:]):
                    self.data.POST_var(name2[1:], [self.data.GET_var().get(name2[1:])[0], " ".join(values2)])

            # create variable
            case [type_, name, "=", *values]:
                CheckIfError().createVariable(name, type_, values, LETTERS, CheckTypeVariable, self.lineCode, self.file, self.code)
                if not ERROR_CODE:

                    if type_[:-1] == 'int':
                        try:
                            if len(values) == 1:
                                self.data.POST_var(name[1:], [type_[:-1], values[0]])
                            if CheckTypeVariable(values).is_string():
                                Error('ValueError', 1, self.lineCode, self.code, self.file, CODE_variable_value=" ".join(values), CODE_variable_type=type_)
                            else:
                                n = 0
                                for i in values:
                                    if self.data.GET_var().get(i[1:]) is not None:
                                        if self.data.GET_var().get(i[1:])[0] in ['int', 'float']:
                                            values[n] = self.data.GET_var().get(i[1:])[1]
                                        else:
                                            Error('ValueError', 1, self.lineCode, self.code, self.file)
                                    n += 1
                                self.data.POST_var(name[1:], [type_[:-1], eval(" ".join(values))])

                        except:
                            Error('ValueError', 1, self.lineCode, self.code, self.file, CODE_variable_type=type_, CODE_variable_value=" ".join(values))

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
                                if values[0] == 'true':
                                    self.data.POST_var(name[1:], [type_[:-1], 'true'])
                                elif values[0] == 'false':
                                    self.data.POST_var(name[1:], [type_[:-1], 'false'])
                                else:
                                    Error('ValueError', 1, self.lineCode, self.code, self.file, CODE_variable_value=" ".join(values), CODE_variable_type=type_)

                            elif values[0] == "DO:" and values[2] in ['==', '>', '>=', '<', "<="]:
                                if self.CONDITION_CLASS.smallCondition_do(values[1], values[2], values[3]):
                                    self.data.POST_var(name[1:], [type_[:-1], 'true'])
                                else:
                                    self.data.POST_var(name[1:], [type_[:-1], 'false'])
                        except:
                            Error('ValueError', 1, self.lineCode, self.code, self.file, CODE_variable_value=" ".join(values), CODE_variable_type=type_)

            # print value variable
            # case ['OUT:', name] if len(self.code) == 2:
            #     if name[0] == '$':
            #         self.VARIABLE_CLASS.displayValueVariable(name)
            #     else:
            #         print(ERROR("SyntaxError", f"it missing '$' the start variable '{name}'", self.lineCode))

            # print type variable
            case ['type:', name]:
                self.VARIABLE_CLASS.displayTypeVariable(name)

            # this section is not ready
            # case ['list:', names, '>', *lists] if lists[0][0] == '[' and lists[-1][-1] == ']' and names[0] == '$':
            #     list1 = "".join(lists).replace(" ", "").replace("[", "").replace("]", "").split(",")
            #     TT_VAR[names[1:]] = ['list', list1]

            ########################################################################
            #                             OPERATOR                                 #
            ########################################################################
            case ['OUT:', *ops]:
                Function(self.lineCode, self.code, self.file).out(ops)
            case _:
                Error('FatalError', 1, self.lineCode, self.code, self.file)
