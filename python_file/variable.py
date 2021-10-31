import error
from data import Data

class Variable:
    def __init__(self, TT_VAR, line):
        self.TT_VAR = TT_VAR
        self.lineCode = line
        self.error = error

    def displayValueVariable(self, name):
        try:
            print('\033[34m' + str(self.TT_VAR.get(name[1:])[1]) + '\033[0m')
        except:
            self.error.Error("NameError", 0)

    def displayTypeVariable(self, name):
        ERROR_CODE = False
        if name[0] != "$":
            self.error.Error("SyntaxError", 0)
            ERROR_CODE = True

        if not ERROR_CODE:
            try:
                print('\033[34m' + f"<typeof '{str(self.TT_VAR.get(name[1:])[0])}'>" + '\033[0m')
            except:
                self.error.Error("FaltalError", 0)