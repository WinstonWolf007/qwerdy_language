#####################################
# IMPORT
#####################################
import string

from ERROR import ERROR
from checkType import CheckTypeVariable
from data import Data

from variable import Variable
from condition import Condition

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
            print(ERROR("SyntaxError", "it missing ';' the end code", self.lineCode))
            exit()
        else:
            self.code = " ".join(self.code).replace(";", '').split(" ")

        match self.code:

            # write file
            case ['qwerdy', '-o', file]:
                print(file)

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

            ########################################################################
            #                             VARIABLE                                 #
            ########################################################################

            # give new value in variable exist
            case [name2, '=', *values2]:

                # check error
                if name2[0] != "$":
                    print(ERROR('ValueError', f"'{name2}' not found !", "create the variable", self.lineCode))
                    ERROR_CODE = True

                if self.data.GET_var().get(name2[1:]) is None:
                    print(ERROR('SyntaxError', f"Variable '{name2}' is not exist", self.lineCode))
                    ERROR_CODE = True

                if not ERROR_CODE and self.data.GET_var().get(name2[1:])[0] == 'int' and len(values2) > 1:
                    v = "".join(values2)
                    result = eval(v)
                    self.data.POST_var(name2[1:], ['int', int(result)])
                    print(self.data.GET_var(name2[1:]))
                    print(self.data.GET_var())

                elif not ERROR_CODE and self.data.GET_var().get(name2[1:]):
                    self.data.POST_var(name2[1:], [self.data.GET_var().get(name2[1:])[0], " ".join(values2)])

            # create variable
            case [type_, name, "=", *values]:
                ERROR('', '', 0).checkErrorCreateVar(name, type_, values, LETTERS, CheckTypeVariable)
                if not ERROR_CODE:

                    if type_[:-1] == 'int':
                        try:
                            if len(values) == 1:
                                self.data.POST_var(name[1:], [type_[:-1], values[0]])
                            else:
                                n = 0
                                for i in values:
                                    if self.data.GET_var().get(i[1:]) is not None:
                                        if self.data.GET_var().get(i[1:])[0] in ['int', 'float']:
                                            values[n] = self.data.GET_var().get(i[1:])[1]
                                        else:
                                            print(ERROR('ValueError', f"'{i}' is not int or float", self.lineCode))
                                    n += 1
                                self.data.POST_var(name[1:], [type_[:-1], eval(" ".join(values))])

                        except:
                            print(ERROR("ValueError", f"'{values}' cannot be an int type", self.lineCode))

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
                                    print(ERROR("ValueError", f"'{values}' cannot be an bool type", self.lineCode))

                            elif values[0] == "DO:" and values[2] in ['==', '>', '>=', '<', "<="]:
                                if self.CONDITION_CLASS.smallCondition_do(values[1], values[2], values[3]):
                                    self.data.POST_var(name[1:], [type_[:-1], 'true'])
                                else:
                                    self.data.POST_var(name[1:], [type_[:-1], 'false'])
                        except:
                            print(ERROR("ValueError", f"'{values}' cannot be an bool type", self.lineCode))

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
                if CheckTypeVariable(ops).is_string():
                    print(" ".join(ops))
                elif len(ops) == 1:
                    self.VARIABLE_CLASS.displayValueVariable(ops[0])
                else:
                    number = ops[0::2]
                    operator = ops[1::2]
                    resultSTR = ''
                    num = 0
                    oper = 0
                    bools = True
                    j = 0

                    for i in number:
                        if self.data.GET_var().get(str(i[1:])) is None:
                            j += 1
                        else:
                            if self.data.GET_var().get(str(i[1:]))[0] in ['float', 'int']:
                                if self.data.GET_var().get(str(i[1:]))[0] == 'int':
                                    number[j] = int(self.data.GET_var().get(str(i[1:]))[1])
                                    j += 1
                                else:
                                    number[j] = float(self.data.GET_var().get(str(i[1:]))[1])
                                    j += 1
                            else:
                                print(ERROR("CrachCodeError", f"Fatal error", self.lineCode))
                                ERROR_CODE = True

                    try:
                        if not ERROR_CODE:
                            for x in range(len(number) + len(operator)):
                                if bools:
                                    resultSTR += str(number[num])
                                    bools = False
                                    num += 1
                                else:
                                    resultSTR += str(operator[oper])
                                    bools = True
                                    oper += 1

                            try:
                                """
                                    bug is it
                                """
                                result = eval(resultSTR)
                                print('\033[34m' + str(result) + '\033[0m')
                            except ZeroDivisionError:
                                print(ERROR("ZeroDivisionError", 'the number cannot be divided by 0', self.lineCode))
                            except:
                                print(ERROR("ValueError", 'problem in syntax do your operator', self.lineCode, 'Exp: 1 + 2 - 3 * 4 / 5'))
                    except:
                        print(ERROR("ValueError", f"type '{str(self.data.GET_var().get(number[0][1:])[0])}' in {str(number[0])} is not 'int' or 'float'", self.lineCode))
            case _:
                print(ERROR("CommandError", f"{self.code} is not found !", self.lineCode, "'help' command for vew all command"))
