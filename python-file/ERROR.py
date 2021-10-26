class ERROR_STOCK:

    def __init__(self, error_type, index, lineCodeError):
        print('call is')

        self.ERROR_STOCK = {
            'SyntaxError': [
                "It missing '$' the start of the variable",
                "It missing ';' the end code",
                "It missing ':' the end type"
            ],
            'ValueError': [],
            'ZeroDivisionError': [],
            'NameError': []
        }

        print(ERROR(error_type, self.ERROR_STOCK.get(error_type)[index], lineCodeError))

class ERROR:

    def __init__(self, error_type, error_detail, errorLine, error_suggestion=None):

        self.type = error_type
        self.detail = error_detail
        self.info = error_suggestion
        self.lineCodeERROR = errorLine

    def __str__(self):
        print("\033[91m" + f"[{self.type}]: (line: {str(self.lineCodeERROR)}): {self.detail}" + "\033[0m")
        exit()

    def checkErrorCreateVar(self, name, type_, values, LETTERS, CheckTypeVariable):

        # check error
        if name[0] != "$":
            ERROR_STOCK('SyntaxError', 0, self.lineCodeERROR)

        if name[0] == "$":
            for letters in name[1:]:
                if letters not in LETTERS:
                    print(ERROR("SyntaxError", f"Expected '{letters}' is not in [{LETTERS}]", self.lineCodeERROR))
                    ERROR_CODE = True

        if type_[-1] != ":":
            print(ERROR("SyntaxError", f"is missing ':' to the end '{type_}'", self.lineCodeERROR,  "[type]:"))
            ERROR_CODE = True

        if type_[-1] == ':':
            if type_[:-1] not in ['int', 'float', 'string', 'bool']:
                print(ERROR("TypeError", f"'{type_}' is not exist in (int, float, string, bool)", self.lineCodeERROR))
                ERROR_CODE = True

        if type_[:-1] in ['int', 'float', 'string', 'bool']:

            if type_[:-1] == 'int' and len(values) == 1 and not CheckTypeVariable(values).is_int():
                print(ERROR("ValueError", f"'{values}' cannot be this value with the type '{type_}'", self.lineCodeERROR))
                ERROR_CODE = True

            elif type_[:-1] == 'float' and not CheckTypeVariable(values).is_float():
                print(ERROR("ValueError", f"'{values}' cannot be this value with the type '{type_}'", self.lineCodeERROR))
                ERROR_CODE = True

            elif type_[:-1] == 'string' and not CheckTypeVariable(values).is_string():
                print(ERROR("SyntaxError", f"It missing '\"\"' in type 'string'", self.lineCodeERROR))
                ERROR_CODE = True

            elif type_[:-1] == 'bool':
                if len(values) == 1 and values[0] not in ['true', 'false']:
                    print(ERROR("ValueError", f"'{values}' cannot be this value with the type '{type_}'", self.lineCodeERROR))
                    ERROR_CODE = True
        else:
            print(ERROR('ValueTypeVariable', f"the type '{type_}' is not exist. the variables type is (int, float, string, bool)", self.lineCodeERROR))
            ERROR_CODE = True