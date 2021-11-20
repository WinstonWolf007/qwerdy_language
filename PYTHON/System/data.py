#####################################
# IMPORT
#####################################
import string

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
    def __init__(self):
        self.LETTERS = LETTERS
        self.IS_FILE = IS_FILE
        self.code = CODE
        self.line = LINE
        self.file = FILE

    # return value this variable
    def GET_var(self, value=None):
        return TT_VAR[value] if value is not None else TT_VAR

    # update dict 'TT_VAR' for change, create variable
    def POST_var(self, key, value):
        TT_VAR[key] = value
