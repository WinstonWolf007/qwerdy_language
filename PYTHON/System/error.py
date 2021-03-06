#####################################
# IMPORT
#####################################
import PYTHON.System.data as data


# class 'Error' is used create and display the error in the console
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

        # the place who stock all error
        self.error_list = {

            # SyntaxError -> VAR: age = 2; != VAR: $age = 2;
            SyntaxError: [
                f"It missing '$' the start of the variable name '{self.CODE_variable_name}'",
                "It missing ';' the end code",
                f"It missing ':' the end variable type '{self.CODE_variable_type}'",
                f"Expected '{self.CODE_variable_name_letter}' in variable name is not in [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_]",
                f"It missing '\"\"' for 'string' type of the variable value '{self.CODE_variable_value}'",
                "problem in your operator",
                "It missing '=' in the syntax of the variable",
                "Expected '.' in float variable",
                "Problem in your value variable",
                "there must be 1 number on each side of the point"
            ],

            # ValueError -> 1 + '2' != 1 + 2
            ValueError: [
                f"'{self.CODE_variable_value}' cannot be this value with the type '{self.CODE_variable_type}'",
                f"'{self.CODE_variable_value}' is not int or float",
            ],

            # TypeError -> VAR: $a = a; != VAR: $a = 'a';
            TypeError: [
                f"'{self.CODE_variable_type}' is not exist in (int, float, string, bool)"
            ],

            # ZeroDivisionError -> 2 / 0
            ZeroDivisionError: [
                f"the number '{self.CODE_variable_value}' cannot be divided by 0"
            ],

            # NameError -> OUT: $a; != VAR: $a = 3; +  OUT: $a;
            NameError: [
                f"Variable '{self.CODE_variable_name}' is not exist !",
                f"Function '{self.CODE_variable_name}' is not exist !"
            ],

            # FatalError -> the rest
            'FatalError': [
                'error not found, fatal error',
                'command not found !'
            ]
        }

        # get value error
        self.error_detail = self.error_list.get(self.error_type)[self.index]

        # to util for not python error code
        if not self.error_type == 'SyntaxError' and not self.index == 1:
            self.code_line += ";"

        # display error and exit code
        print("\033[91m" + f"Traceback (most recent call last):\n  File '{self.file}', line {self.line}\n\n\t{self.code_line}\n\n[{str(self.error_type)[8:-2]}]: {self.error_detail}" + "\033[0m")
        exit()