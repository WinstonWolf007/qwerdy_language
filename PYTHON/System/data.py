#####################################
# IMPORT
#####################################
import string
import PYTHON.Function.function as function

#####################################
# Main stock var -> (variable, function, number line)
#####################################
TT_VAR = {}
TT_FUNC = {}
CODE = ''
LINE = 0
FILE = ''
LETTERS = string.ascii_letters + "_"
IS_FILE = False

# class 'Data' is used that stock all value, type, key in the code
class Data:
    def __init__(self, *param):
        self.LETTERS = LETTERS
        self.IS_FILE = IS_FILE
        self.code = CODE
        self.line = LINE
        self.file = FILE
        self.all_func = {
            'out': function.Function().out(param)
        }
        self.all_func_syntax = []

    # return value this variable
    def GET_var(self, value=None):
        return TT_VAR[value] if value is not None else TT_VAR

    # update dict 'TT_VAR' for change, create variable
    def POST_var(self, key, value):
        TT_VAR[key] = value

    # create function syntax for command line
    def createFunc(self, idx_syntax, func, *args):
        if self.code[0] == self.all_func_syntax[idx_syntax]:
            self.all_func.get(func)()