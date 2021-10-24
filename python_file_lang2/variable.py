from ERROR import ERROR

class Variable:

    def displayValueVariable(self, name, TT_VAR):
        try:
            print('\033[34m' + str(TT_VAR.get(name[1:])[1]) + '\033[0m')
        except:
            print(ERROR("NameError", f"Variable '{name}' is not exist", self.lineCode))