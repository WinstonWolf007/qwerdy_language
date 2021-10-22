#####################################
# IMPORT
#####################################

import string
from ERROR import ERROR

#####################################
# TOKEN
#####################################

LETTERS = string.ascii_letters + "_"
TT_VAR = {}


##########################################
# MAIN CODE
##########################################

class Code:
    def __init__(self, code: str):
        self.code = code.split()
        self.CODE_LANG()

    def CODE_LANG(self):

        ########################################################################
        #                             VARIABLE                                 #
        ########################################################################

        match self.code:
            case [type_, name, "=", value]:

                if name[0] == "$":
                    for letters in name[1:]:
                        if letters not in LETTERS:
                            print(ERROR("SyntaxError", f"Expected '{letters}' is not in [{LETTERS}]"))
                else:
                    for letters in name:
                        if letters not in LETTERS:
                            print(ERROR("SyntaxError", f"Expected '{letters}' is not in [{LETTERS}]"))

                if type_[-1] == ':':
                    if type_[:-1] not in ['int', 'float', 'string', 'bool']:
                        print(ERROR("TypeError", f"'{type_}' is not exist in (int, float, string, bool)"))
                else:
                    if type_ not in ['int', 'float', 'string', 'bool']:
                        print(ERROR("TypeError", f"'{type_}' is not exist in (int, float, string, bool)"))

                if type_[-1] != ":":
                    print(ERROR("SyntaxError", f"is missing ':' to the end '{type_}'", "[type]:"))

                if name[0] != "$":
                    print(ERROR("SyntaxError", "It missing '$' the start of the variable", '$[name]'))

                if type_[:-1] in ['int', 'float', 'string', 'bool'] and type_[-1] == ':' and name[0] == "$":

                    if type_[:-1] == 'int':
                        try:
                            TT_VAR[name[1:]] = [type_[:-1], int(value)]
                        except:
                            print(ERROR("ValueError", f"'{value}' cannot be an int type"))

                    elif type_[:-1] == 'float':
                        try:
                            TT_VAR[name[1:]] = [type_[:-1], float(value)]
                        except:
                            print("probleme")

                    elif type_[:-1] == 'string':
                        try:
                            if value[0] == '"' and value[-1] == '"':
                                TT_VAR[name[1:]] = [type_[:-1], str(value)]
                            else:
                                print(ERROR("ValueError", f"'{value}' cannot be an string type, he missing the \"\""))

                        except:
                            print(ERROR("ValueError", f"'{value}' cannot be an string type, he missing the '\"\"'"))

                    elif type_[:-1] == 'bool':
                        try:
                            if value == 'true':
                                TT_VAR[name[1:]] = [type_[:-1], 'true']
                            elif value == 'false':
                                TT_VAR[name[1:]] = [type_[:-1], 'false']
                            else:
                                print(ERROR("ValueError", f"'{value}' cannot be an bool type"))
                        except:
                            print(ERROR("ValueError", f"'{value}' cannot be an bool type"))

            # print value variable
            case [name] if name[0] == '$' and len(self.code) == 1:
                try:
                    print('\033[34m' + str(TT_VAR.get(name[1:])[1]) + '\033[0m')
                except:
                    print(ERROR("NameError", f"Variable '{name}' is not exist !"))

            # print type variable
            case ['type:', name]:
                try:
                    print('\033[34m' + f"<typeof '{str(TT_VAR.get(name[1:])[0])}'>" + '\033[0m')
                except:
                    print(
                        ERROR("SyntaxError or ValueError", f"Variable '{name}' is not exist or the syntax is incorrect",
                              "$[name]"))

            ########################################################################
            #                             OPERATOR                                 #
            ########################################################################
            case [*ops]:
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

                try:
                    for x in range(len(number) + len(operator)):
                        if bools:
                            resultSTR += str(number[num])
                            bools = False
                            num += 1
                        else:
                            resultSTR += str(operator[oper])
                            bools = True
                            oper += 1

                    result = eval(resultSTR)
                    print('\033[34m' + str(result) + '\033[0m')

                except:
                    print(ERROR("ValueError",
                                f"type '{str(TT_VAR.get(number[0][1:])[0])}' in {str(number[0])} is not 'int' or 'float'"))
