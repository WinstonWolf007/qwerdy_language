from ERROR import ERROR
from checkType import CheckTypeVariable

class Condition:
    def __init__(self, TT_VAR, line, LETTERS):
        self.TT_VAR = TT_VAR
        self.lineCode = line
        self.LETTERS = LETTERS

    def smallCondition_do(self, name1_, operator_, name2_):

        try:
            if name2_ in ['true', 'false'] or name1_ in ['true', 'false']:
                pass

            elif name1_[0] == "$":
                name1_ = self.TT_VAR.get(name1_[1:])[1]
                type1_ = self.TT_VAR.get(name1_[1:])[0]

                if CheckTypeVariable(name1_).is_int() and type1_[:-1] == 'int':
                    name1_ = int(name1_)
                elif CheckTypeVariable(name1_).is_float() and type1_[:-1] == 'float':
                    name1_ = float(name1_)
                elif CheckTypeVariable(name1_).is_string() and type1_[:-1] == 'string':
                    name1_ = name1_
                elif CheckTypeVariable(name1_).is_bool() and type1_[:-1] == 'bool':
                    name1_ = name1_

            else:
                if CheckTypeVariable(name1_).is_string():
                    pass
                if CheckTypeVariable(name1_).is_string():
                    pass

                else:
                    if name1_[0] == '"':
                        pass
                    elif name2_[0] == '"':
                        pass
                    elif name1_[0] != "$":
                        print(ERROR("SyntaxError", f"it missing '$' the start variable '{name1_}'"))
                    elif name2_[0] != "$":
                        print(ERROR("SyntaxError", f"it missing '$' the start variable '{name2_}'"))

        except: pass

        try:
            if name2_[0] == "$":
                name2_ = self.TT_VAR.get(name2_[1:])[1]
                type2_ = self.TT_VAR.get(name2_[1:])[0]

                if CheckTypeVariable(name2_).is_int() and type2_[:-1] == 'int':
                    name2_ = int(name2_)
                elif CheckTypeVariable(name2_).is_float() and type2_[:-1] == 'float':
                    name2_ = float(name2_)
                elif CheckTypeVariable(name2_).is_string() and type2_[:-1] == 'string':
                    name2_ = name2_
                elif CheckTypeVariable(name2_).is_bool() and type2_[:-1] == 'bool':
                    name2_ = name2_
            else:
                for l in self.LETTERS:
                    if l == name2_[1]:
                        print(ERROR("SyntaxError", "it missing '$' the start variable"))
                        break

        except: pass

        if operator_ in ['==', '>', '>=', "<", "<="]:
            if operator_ == "==":
                return True if name1_ == name2_ else False

            elif operator_ == ">":
                return True if name1_ > name2_ else False

            elif operator_ == ">=":
                return True if name1_ >= name2_ else False

            elif operator_ == "<":
                return True if name1_ < name2_ else False

            elif operator_ == '<=':
                return True if name1_ <= name2_ else False

            else:
                return False

        else:
            print(ERROR('SyntaxError', f"'{operator_}' is not exist", self.lineCode))
            ERROR_CODE = True