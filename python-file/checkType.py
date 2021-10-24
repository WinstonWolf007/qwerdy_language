class CheckTypeVariable:

    def __init__(self, valueVar):
        self.value_variable = valueVar

    def is_int(self):
        try:
            return isinstance(int(self.value_variable[0]), int)
        except:
            return False

    def is_float(self):
        try:
            for i in self.value_variable[0]:
                if i == ".":
                    return True
            return False
        except:
            return False

    def is_string(self):
        return True if self.value_variable[0][0] == '"' and self.value_variable[-1][-1] else False

    def is_bool(self):
        return True if self.value_variable[0] == "true" or self.value_variable[0] == "false" else False
