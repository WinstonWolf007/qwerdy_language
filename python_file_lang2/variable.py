from ERROR import ERROR

class Variable:
    def __init__(self, TT_VAR, line):
        self.TT_VAR = TT_VAR
        self.lineCode = line

    def displayValueVariable(self, name):
        try:
            print('\033[34m' + str(self.TT_VAR.get(name[1:])[1]) + '\033[0m')
        except:
            print(ERROR("NameError", f"Variable '{name}' is not exist", self.lineCode))

    def displayTypeVariable(self, name):
        ERROR_CODE = False
        if name[0] != "$":
            print(ERROR("SyntaxError", f"It missing '$' the start of the variable", self.lineCode, "type: $[name]"))
            ERROR_CODE = True

        if not ERROR_CODE:
            try:
                print('\033[34m' + f"<typeof '{str(self.TT_VAR.get(name[1:])[0])}'>" + '\033[0m')
            except:
                print(ERROR("SyntaxError or ValueError", f"Variable '{name}' is not exist or the syntax is incorrect", "$[name]"))
