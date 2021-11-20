# class 'CheckTypeVariable' is used know the variable type
class CheckTypeVariable:

    def __init__(self, valueVar):
        self.value_variable = valueVar

    # check if the type is 'int' -> (1, 4, 54, -23, -2, 9)
    def is_int(self):
        try:
            return isinstance(int(self.value_variable[0]), int)
        except:
            return False

    # check if the type is 'float' -> (2.40, 4.7, -1.5, -0.5, 9.10)
    def is_float(self):
        try:
            for i in self.value_variable[0]:
                if i == ".":
                    return True
            return False
        except:
            return False

    # check if the type is 'string' -> ("hello", "1", "3.4", "A", "true")
    def is_string(self):
        return True if self.value_variable[0][0] == '"' and self.value_variable[-1][-1] == '"' else False

    # check if the type is 'bool' -> (true, false)
    def is_bool(self):
        return True if self.value_variable[0] == "true" or self.value_variable[0] == "false" else False