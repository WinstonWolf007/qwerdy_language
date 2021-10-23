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

        ########################################################################
        #                             VARIABLE                                 #
        ########################################################################

        match self.code:

            # help command
            case ["help"]:
                print('\033[34m' + "Read 'syntax.txt', file for vew all information" + '\033[0m')

            # give new value in variable exist
            case [name2, '=', *values2]:
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

            case [type_, name, "=", *values]:

                if type_[:-1] != "string":
                    value = values[0]

                if name[0] == "$":
                    for letters in name[1:]:
                        if letters not in LETTERS:
                            print(ERROR("SyntaxError", f"Expected '{letters}' is not in [{LETTERS}]", self.lineCode))
                            ERROR_CODE = True
                else:
                    for letters in name:
                        if letters not in LETTERS:
                            print(ERROR("SyntaxError", f"Expected '{letters}' is not in [{LETTERS}]", self.lineCode))
                            ERROR_CODE = True

                if type_[-1] == ':':
                    if type_[:-1] not in ['int', 'float', 'string', 'bool']:
                        print(ERROR("TypeError", f"'{type_}' is not exist in (int, float, string, bool)", self.lineCode))
                        ERROR_CODE = True
                else:
                    if type_ not in ['int', 'float', 'string', 'bool']:
                        print(ERROR("TypeError", f"'{type_}' is not exist in (int, float, string, bool)", self.lineCode))
                        ERROR_CODE = True

                if type_[-1] != ":":
                    print(ERROR("SyntaxError", f"is missing ':' to the end '{type_}'", "[type]:"))
                    ERROR_CODE = True

                if name[0] != "$":
                    print(ERROR("SyntaxError", "It missing '$' the start of the variable", '$[name]'))
                    ERROR_CODE = True

                if type_[:-1] == "string":
                    if values[0][0] != '"' or values[-1][-1] != '"':
                        print(ERROR("SyntaxError", f"It missing '\"\"' in type 'string'", self.lineCode))
                        ERROR_CODE = True

                if type_[:-1] in ['int', 'float', 'string', 'bool'] and type_[-1] == ':' and name[0] == "$" and ERROR_CODE == False:

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
                            print(ERROR("ValueError", f"'{value}' cannot be an int type", self.lineCode))

                    elif type_[:-1] == 'float':
                        try:
                            TT_VAR[name[1:]] = [type_[:-1], float(value)]
                        except:
                            print("probleme")

                    elif type_[:-1] == 'string':
                        if values[0][0] == '"' and values[-1][-1] == '"':
                            TT_VAR[name[1:]] = [type_[:-1], " ".join(values)]

                    elif type_[:-1] == 'bool':
                        try:
                            if value == 'true':
                                TT_VAR[name[1:]] = [type_[:-1], 'true']
                            elif value == 'false':
                                TT_VAR[name[1:]] = [type_[:-1], 'false']
                            else:
                                print(ERROR("ValueError", f"'{value}' cannot be an bool type", self.lineCode))
                        except:
                            print(ERROR("ValueError", f"'{value}' cannot be an bool type", self.lineCode))

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
                    print(
                        ERROR("SyntaxError or ValueError", f"Variable '{name}' is not exist or the syntax is incorrect",
                              "$[name]"))

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
