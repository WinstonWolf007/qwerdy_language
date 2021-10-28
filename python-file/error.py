class Error:

    def __init__(self, error_type='<?>Error', index=0, line='?', code_line='<code>', file='False', CODE_variable_name_letter=None, CODE_variable_type=None, CODE_variable_name=None, CODE_variable_value=None):

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

        if self.error_type == 'SyntaxError' and self.index == 1:
            pass
        else:
            self.code_line += ";"

        print("\033[91m" + f"Traceback (most recent call last):\n  File '{self.file}', line {self.line}\n\n\t{self.code_line}\n\n[{self.error_type}]: {self.error_detail}" + "\033[0m")
        exit(2)

    def create(self, error_types, idx):
        print("\033[91m" + f"Traceback (most recent call last):\n  File 'None', line ?\n\n\t\n\n[{error_types}]: {self.error_list.get(error_types)[idx]}" + "\033[0m")
        exit(2)

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
            Error('TypeError', 0, Error_line, Error_code_line, Error_file, CODE_variable_type=type_)

        else:

            if type_[:-1] == 'int' and len(values) == 1 and not CheckTypeVariable(values).is_int():
                Error('ValueError', 0, Error_line, Error_code_line, Error_file, CODE_variable_type=type_, CODE_variable_value="".join(values))

            elif type_[:-1] == 'float' and not CheckTypeVariable(values).is_float():
                Error('ValueError', 0, Error_line, Error_code_line, Error_file, CODE_variable_type=type_, CODE_variable_value=" ".join(values))

            elif type_[:-1] == 'string' and not CheckTypeVariable(values).is_string():
                Error('SyntaxError', 4, Error_line, Error_code_line, Error_file, CODE_variable_value=" ".join(values))

            elif type_[:-1] == 'bool':
                if len(values) == 1 and values[0] not in ['true', 'false']:
                    Error('ValueError', 0, Error_line, Error_code_line, Error_file, CODE_variable_value=values[0])