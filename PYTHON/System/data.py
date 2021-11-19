import string

TT_VAR = {}
TT_FUNC = {}

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
        self.all_func = []
        self.all_func_syntax = []

    def GET_var(self, value=None):
        return TT_VAR[value] if value is not None else TT_VAR

    def POST_var(self, key, value):
        TT_VAR[key] = value