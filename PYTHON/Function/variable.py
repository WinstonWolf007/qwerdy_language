#####################################
# IMPORT
#####################################
import PYTHON.System.error as error
from PYTHON.System.data import *


# class 'Variable' is used display type, value the variables
class Variable:
    def __init__(self):
        self.TT_VAR = TT_VAR
        self.lineCode = LINE
        self.error = error

    def displayValueVariable(self, name):
        try:
            print('\033[34m' + str(self.TT_VAR.get(name[1:])[1]) + '\033[0m')
        except:
            self.error.Error(NameError, 0)

    def displayTypeVariable(self, name):
        if name[0] != "$":
            self.error.Error(SyntaxError, 0)
        else:
            try:
                print('\033[34m' + f"<typeof '{str(self.TT_VAR.get(name[1:])[0])}'>" + '\033[0m')
            except:
                self.error.Error("FaltalError", 0)