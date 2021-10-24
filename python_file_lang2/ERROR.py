class ERROR:
    def __init__(self, error_type="", error_detail="", errorLine="", error_suggestion=None):
        self.type = error_type
        self.detail = error_detail
        self.info = error_suggestion
        self.errorLine = errorLine
        self.lineCode = self.errorLine

    def __str__(self):
        if self.info is None:
            return "\033[91m" + f"[{self.type}]: (line: {str(self.errorLine)}) > {self.detail}" + "\033[0m"
        else:
            return "\033[91m" + f"[{self.type}]: {self.detail} (line: {str(self.errorLine)}) == {self.info}" + "\033[0m"

    def checkErrorCreateVar(self, name, type_, values, LETTERS, CheckTypeVariable):

        # check error
        if name[0] != "$":
            print(ERROR("SyntaxError", "It missing '$' the start of the variable", '$[name]'))
            ERROR_CODE = True

        if name[0] == "$":
            for letters in name[1:]:
                if letters not in LETTERS:
                    print(ERROR("SyntaxError", f"Expected '{letters}' is not in [{LETTERS}]", self.lineCode))
                    ERROR_CODE = True

        if type_[-1] != ":":
            print(ERROR("SyntaxError", f"is missing ':' to the end '{type_}'", "[type]:"))
            ERROR_CODE = True

        if type_[-1] == ':':
            if type_[:-1] not in ['int', 'float', 'string', 'bool']:
                print(ERROR("TypeError", f"'{type_}' is not exist in (int, float, string, bool)", self.lineCode))
                ERROR_CODE = True

        if type_[:-1] in ['int', 'float', 'string', 'bool']:

            if type_[:-1] == 'int' and len(values) == 1 and not CheckTypeVariable(values).is_int():
                print(ERROR("ValueError", f"'{values}' cannot be this value with the type '{type_}'", self.lineCode))
                ERROR_CODE = True

            elif type_[:-1] == 'float' and not CheckTypeVariable(values).is_float():
                print(ERROR("ValueError", f"'{values}' cannot be this value with the type '{type_}'", self.lineCode))
                ERROR_CODE = True

            elif type_[:-1] == 'string' and not CheckTypeVariable(values).is_string():
                print(ERROR("SyntaxError", f"It missing '\"\"' in type 'string'", self.lineCode))
                ERROR_CODE = True

            elif type_[:-1] == 'bool':
                if len(values) == 1 and values[0] not in ['true', 'false']:
                    print(ERROR("ValueError", f"'{values}' cannot be this value with the type '{type_}'", self.lineCode))
                    ERROR_CODE = True
        else:
            print(ERROR('ValueTypeVariable', f"the type '{type_[:-1]}' is not exist. the variables type is (int, float, string, bool)", self.lineCode))
            ERROR_CODE = True

