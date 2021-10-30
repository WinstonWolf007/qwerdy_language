import string

TT_VAR = {}

CODE = ''
LINE = 0
FILE = ''
LETTERS = string.ascii_letters + "_"
IS_FILE = False

class Data:

    def __init__(self):
        self.LETTERS = LETTERS
        self.IS_FILE = IS_FILE
        self.code = CODE
        self.line = LINE
        self.file = FILE

    def GET_var(self, value=None):
        if value is not None:
            return TT_VAR[value]
        return TT_VAR

    def POST_var(self, key, value):
        TT_VAR[key] = value