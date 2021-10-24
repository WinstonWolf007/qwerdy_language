#####################################
# IMPORT
#####################################

import string
from ERROR import ERROR
from checkType import CheckTypeVariable

#####################################
# TOKEN
#####################################

LETTERS = string.ascii_letters + "_"
TT_VAR = {}


##########################################
# MAIN CODE
##########################################

class Code:
    def __init__(self, code: str, lineCode):
        self.code = code.split()
        self.lineCode = lineCode
        self.CODE_LANG()

    def CODE_LANG(self):

        ERROR_CODE = False

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
            case ['DO', name1, operator, name2, '?']:

                try:
                    name1 = TT_VAR.get(name1[1:])[1]
                    print(TT_VAR.get(name1[1:])[1])
                except: pass

                try:
                    name2 = TT_VAR.get(name2[1:])[1]
                    print(TT_VAR.get(name2[1:])[1])
                except: pass

                if operator in ['==', '>', '>=', "<", "<="]:
                    if operator == "==":
                        result = True if name1 == name2 else False
                        print(result)
                    elif operator == ">":
                        result = True if name1 > name2 else False
                        print(result)
                    elif operator == ">=":
                        result = True if name1 >= name2 else False
                        print(result)
                    elif operator == "<":
                        result = True if name1 < name2 else False
                        print(result)
                    elif operator == '<=':
                        result = True if name1 <= name2 else False
                        print(result)
                    else:
                        result = False
                        print(result)
                else:
                    print(ERROR('SyntaxError', f"'{operator}' is not exist"))
                    ERROR_CODE = True

            ########################################################################
            #                             VARIABLE                                 #
            ########################################################################

            # give new value in variable exist
            case [name2, '=', *values2]:

                # check error
                if name2[0] != "$":
                    print(ERROR('ValueError', f"'{name2}' not found !", "create the variable"))
                    ERROR_CODE = True

                if TT_VAR.get(name2[1:]) is None:
                    print(ERROR('SyntaxError', f"Variable '{name2}' is not exist", self.lineCode))
                    ERROR_CODE = True

                if not ERROR_CODE and TT_VAR.get(name2[1:])[0] == 'int' and len(values2) > 1:
                    v = "".join(values2)
                    result = eval(v)
                    TT_VAR[name2[1:]] = ['int', int(result)]
                    print(TT_VAR[name2[1:]])
                    print(TT_VAR)

                elif not ERROR_CODE and TT_VAR.get(name2[1:]):
                    TT_VAR[name2[1:]] = [TT_VAR.get(name2[1:])[0], " ".join(values2)]

            # create variable
            case [type_, name, "=", *values]:
                ERROR().checkErrorCreateVar(name, type_, values, LETTERS, CheckTypeVariable)
                if not ERROR_CODE:

                    if type_[:-1] == 'int':
                        try:
                            if len(values) == 1:
                                TT_VAR[name[1:]] = [type_[:-1], values[0]]
                            else:
                                n = 0
                                for i in values:
                                    if TT_VAR.get(i[1:]) is not None:
                                        if TT_VAR.get(i[1:])[0] in ['int', 'float']:
                                            values[n] = TT_VAR.get(i[1:])[1]
                                        else:
                                            print(ERROR('ValueError', f"'{i}' is not int or float", self.lineCode))
                                    n += 1
                                TT_VAR[name[1:]] = [type_[:-1], eval(" ".join(values))]
                        except:
                            print(ERROR("ValueError", f"'{values}' cannot be an int type", self.lineCode))

                    elif type_[:-1] == 'float':
                        try:
                            TT_VAR[name[1:]] = [type_[:-1], float(values[0])]
                        except:
                            pass

                    elif type_[:-1] == 'string':
                        if values[0][0] == '"' and values[-1][-1] == '"':
                            TT_VAR[name[1:]] = [type_[:-1], " ".join(values)]

                    elif type_[:-1] == 'bool':
                        try:
                            if len(values) == 1:
                                if values[0] == 'true':
                                    TT_VAR[name[1:]] = [type_[:-1], 'true']
                                elif values[0] == 'false':
                                    TT_VAR[name[1:]] = [type_[:-1], 'false']
                                else:
                                    print(ERROR("ValueError", f"'{values}' cannot be an bool type", self.lineCode))
                            elif values[0] == "DO" and values[-1] == "?":
                                print("small condition detected")
                        except:
                            print(ERROR("ValueError", f"'{values}' cannot be an bool type", self.lineCode))

            # print value variable
            case [name] if name[0] == '$' and len(self.code) == 1:
                try:
                    print('\033[34m' + str(TT_VAR.get(name[1:])[1]) + '\033[0m')
                except:
                    print(ERROR("NameError", f"Variable '{name}' is not exist", self.lineCode))

            # print type variable
            case ['type:', name]:
                try:
                    print('\033[34m' + f"<typeof '{str(TT_VAR.get(name[1:])[0])}'>" + '\033[0m')
                except:
                    print(ERROR("SyntaxError or ValueError", f"Variable '{name}' is not exist or the syntax is incorrect", "$[name]"))

            case ['list:', names, '>', *lists] if lists[0][0] == '[' and lists[-1][-1] == ']' and names[0] == '$':
                list1 = "".join(lists).replace(" ", "").replace("[", "").replace("]", "").split(",")
                TT_VAR[names[1:]] = ['list', list1]

            ########################################################################
            #                             OPERATOR                                 #
            ########################################################################
            case [*ops] if len(ops) >= 3:
                if not ERROR_CODE:
                    number = ops[0::2]
                    operator = ops[1::2]
                    resultSTR = ''
                    num = 0
                    oper = 0
                    bools = True
                    j = 0

                    for i in number:
                        if TT_VAR.get(str(i[1:])) is None:
                            j += 1
                        else:
                            if TT_VAR.get(str(i[1:]))[0] in ['float', 'int']:
                                if TT_VAR.get(str(i[1:]))[0] == 'int':
                                    number[j] = int(TT_VAR.get(str(i[1:]))[1])
                                    j += 1
                                else:
                                    number[j] = float(TT_VAR.get(str(i[1:]))[1])
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
                                result = eval(resultSTR)
                                print('\033[34m' + str(result) + '\033[0m')
                            except ZeroDivisionError:
                                print(ERROR("ZeroDivisionError", 'the number cannot be divided by 0', self.lineCode))
                            except:
                                print(ERROR("ValueError", 'problem in syntax do your operator', self.lineCode, 'Exp: 1 + 2 - 3 * 4 / 5'))
                    except:
                        print(ERROR("ValueError", f"type '{str(TT_VAR.get(number[0][1:])[0])}' in {str(number[0])} is not 'int' or 'float'", self.lineCode))
            case _:
                print(ERROR("CommandError", f"{self.code} is not found !", self.lineCode, "'help' command for vew all command"))
