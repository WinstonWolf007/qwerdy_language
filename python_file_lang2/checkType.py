class CheckTypeVariable:

    def __init__(self, valueVar):
        self.value_variable = valueVar

    def is_int(self):
        return isinstance(self.value_variable[0], int)

    def is_float(self):
        return isinstance(self.value_variable[0], float)

    def is_string(self):
        return True if self.value_variable[0][0] == '"' and self.value_variable[-1][-1] else False

    def is_bool(self):
        return True if self.value_variable[0] == "True" or self.value_variable[0] == "False" else False
