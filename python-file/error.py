class Error:

    def __init__(self, error_type, index, line, code_line, file, CODE_variable_name_letter=None, CODE_variable_type=None, CODE_variable_name=None, CODE_variable_value=None):

        self.CODE_variable_name_letter = CODE_variable_name_letter
        self.CODE_variable_type = CODE_variable_type
        self.CODE_variable_name = CODE_variable_name
        self.CODE_variable_value = CODE_variable_value

        self.error_type = error_type
        self.index = index
        self.line = line
        self.file = file
        self.code_line = " ".join(code_line)

        self.error_list = {
            'SyntaxError': [
                f"It missing '$' the start of the variable name '{self.CODE_variable_name}'",
                "It missing ';' the end code",
                f"It missing ':' the end variable type '{self.CODE_variable_type}'",
                f"Expected '{self.CODE_variable_name_letter}' in variable name is not in [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_]"
            ],
            'ValueError': [],
            'TypeError': [
                f"'{self.CODE_variable_type}' is not exist in (int, float, string, bool)"
            ],
            'ZeroDivisionError': [],
            'NameError': []
        }

        self.error_detail = self.error_list.get(self.error_type)[self.index]

        print("\033[91m" + f"Traceback (most recent call last):\n  File '{self.file}', line {self.line}\n\n\t{self.code_line}\n\n[{self.error_type}]: {self.error_detail}" + "\033[0m")
        exit(0)

class CheckIfError:

    def createVariable(self, name, type_, values, LETTERS, CheckTypeVariable, Error_line, Error_file, Error_code_line):

        if type_[-1] != ":":
            Error('SyntaxError', 2, Error_line, Error_code_line, Error_file, CODE_variable_type=type_)

        if name[0] != "$":
            Error('SyntaxError', 0, Error_line, Error_code_line, Error_file, CODE_variable_name=name)

        for letters in name[1:]:
            if letters not in LETTERS:
                Error('SyntaxError', 3, Error_line, Error_code_line, Error_file, CODE_variable_name_letter=letters)

        if type_[:-1] not in ['int', 'float', 'string', 'bool']:
                print(ERROR("TypeError", 0, self.lineCodeERROR))
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