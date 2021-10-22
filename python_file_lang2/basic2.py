#####################################
# IMPORT
#####################################

import string

#####################################
# TOKEN
#####################################

LETTERS = string.ascii_letters + "_"
NUMBERS = '0123456789'

TT_VAR = {}

####################################
# ERROR
####################################

class ERROR:
    def __init__(self, error_type, error_detail, error_suggestion=None):
        self.type = error_type
        self.detail = error_detail
        self.info = error_suggestion

    def __str__(self):
        if self.info is None:
            return "\033[91m" + f"[{self.type}]: {self.detail}" + "\033[0m"
        else:
            return "\033[91m" + f"[{self.type}]: {self.detail} == {self.info}" + "\033[0m"

####################################
# CODE
####################################

class Code:
    def __init__(self, code: str):
        self.code = code.split()
        self.var()

    ######################################

    def var(self):
        match self.code:
            #########################################
            # VARIABLE
            #########################################

            # create variable
            case [type_, name, "=", value] if name[0] == "$":

                for letters in name[1:]:
                    if letters not in LETTERS:
                        print('error letter is not in', LETTERS, f": Expected '{letters}'")

                if type_[-1] != ":":
                    print("SyntaxError", "is missing ':'", "[type]: $[name] = [value]")

                if type_[:-1] in ['int', 'float', 'string', 'bool']:

                    if type_[:-1] == 'int':
                        try: TT_VAR[name[1:]] = [type_[:-1], int(value)]
                        except: print(ERROR("ValueError", f"'{value}' cannot be an int type"))

                    elif type_[:-1] == 'float':
                        try: TT_VAR[name[1:]] = [type_[:-1], float(value)]
                        except: print(ERROR("ValueError", f"'{value}' cannot be an float type"))

                    elif type_[:-1] == 'string':
                        try:
                            if value[0] == '"' and value[-1] == '"':
                                TT_VAR[name[1:]] = [type_[:-1], str(value)]
                            else:
                                print(ERROR("ValueError", f"'{value}' cannot be an string type, he missing the \"\""))

                        except: print(ERROR("ValueError", f"'{value}' cannot be an string type, he missing the '\"\"'"))

                    elif type_[:-1] == 'bool':
                        try:
                            if value == 'true':
                                TT_VAR[name[1:]] = [type_[:-1], 'true']
                            elif value == 'false':
                                TT_VAR[name[1:]] = [type_[:-1], 'false']
                            else:
                                print(ERROR("ValueError", f"'{value}' cannot be an bool type"))
                        except: print(ERROR("ValueError", f"'{value}' cannot be an bool type"))

            # print value variable
            case [name] if name[0] == '$' and len(self.code) == 1:
                try:
                    print('\033[34m' + str(TT_VAR.get(name[1:])[1]) + '\033[0m')
                except:
                    print(ERROR("NameError", f"Variable '{name}' is not exist !"))

            # print type variable
            case ['type:', name] if name[0] == "$":
                print('\033[34m' + f"<typeof '{str(TT_VAR.get(name[1:])[0])}'>" + '\033[0m')

            #########################################
            # OPERATOR
            #########################################

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
                    for x in range(len(number)+len(operator)):
                        if bools:
                            resultSTR += str(number[num])
                            bools = False
                            num += 1
                        else:
                            resultSTR += str(operator[oper])
                            bools = True
                            oper += 1

                    print('\033[34m' + str(eval(resultSTR)) + '\033[0m')

                except:
                    print(ERROR("ValueError", f"type '{str(TT_VAR.get(number[0][1:])[0])}' in {str(number[0])} is not 'int' or 'float'"))
