import data
from checkType import CheckTypeVariable

class Error:

    def __init__(self, error_type, index, CODE_variable_name_letter=None, CODE_variable_type=None, CODE_variable_name=None, CODE_variable_value=None):

        self.CODE_variable_name_letter = CODE_variable_name_letter
        self.CODE_variable_type = CODE_variable_type
        self.CODE_variable_name = CODE_variable_name
        self.CODE_variable_value = CODE_variable_value

        self.error_type = error_type
        self.index = index
        self.line = data.LINE
        self.file = data.FILE
        self.code_line = " ".join(data.CODE)

        self.error_list = {
            'SyntaxError': [
                f"It missing '$' the start of the variable name '{self.CODE_variable_name}'",
                "It missing ';' the end code",
                f"It missing ':' the end variable type '{self.CODE_variable_type}'",
                f"Expected '{self.CODE_variable_name_letter}' in variable name is not in [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_]",
                f"It missing '\"\"' for 'string' type of the variable value '{self.CODE_variable_value}'",
                "problem in your operator"
            ],
            'ValueError': [
                f"'{self.CODE_variable_value}' cannot be this value with the type '{self.CODE_variable_type}'",
                f"'{self.CODE_variable_value}' is not int or float",
            ],
            'TypeError': [
                f"'{self.CODE_variable_type}' is not exist in (int, float, string, bool)"
            ],
            'ZeroDivisionError': [
                f"the number '{self.CODE_variable_value}' cannot be divided by 0"
            ],
            'NameError': [
                f"Variable '{self.CODE_variable_name}' is not exist !"
            ],
            'FatalError': [
                'error not found, fatal error',
                'command not found !'
            ]
        }

        self.error_detail = self.error_list.get(self.error_type)[self.index]

        if not self.error_type == 'SyntaxError' and not self.index == 1:
            self.code_line += ";"

        print("\033[91m" + f"Traceback (most recent call last):\n  File '{self.file}', line {self.line}\n\n\t{self.code_line}\n\n[{self.error_type}]: {self.error_detail}" + "\033[0m")
        exit(2)

class CheckIfError:

    def createVariable(self, name, type_, values):

        if type_[-1] != ":":
            Error('SyntaxError', 2, CODE_variable_type=type_)

        if name[0] != "$":
            Error('SyntaxError', 0, CODE_variable_name=name)

        for letters in name[1:]:
            if letters not in data.LETTERS:
                Error('SyntaxError', 3, CODE_variable_name_letter=letters)

        if type_[:-1] not in ['int', 'float', 'string', 'bool']:
            Error('TypeError', 0, CODE_variable_type=type_)

        else:

            if type_[:-1] == 'int' and len(values) == 1 and not CheckTypeVariable(values).is_int():
                Error('ValueError', 0, CODE_variable_type=type_, CODE_variable_value="".join(values))

            elif type_[:-1] == 'float' and not CheckTypeVariable(values).is_float():
                Error('ValueError', 0, CODE_variable_type=type_, CODE_variable_value=" ".join(values))

            elif type_[:-1] == 'string' and not CheckTypeVariable(values).is_string():
                Error('SyntaxError', 4, CODE_variable_value=" ".join(values))

            elif type_[:-1] == 'bool':
                if len(values) == 1 and values[0] not in ['true', 'false']:
                    Error('ValueError', 0, CODE_variable_value=values[0])