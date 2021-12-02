# class 'CheckTypeVariable' is used know the variable type
class CheckTypeVariable:

    def __init__(self, valueVar):
        self.value_variable = valueVar

    # check if the type is 'int' -> (1, 4, 54, -23, -2, 9)
    def is_int(self):
        return str(self.value_variable[0]).isdigit(), None

    # check if the type is 'float' -> (2.40, 4.7, -1.5, -0.5, 9.10)
    def is_float(self):
        if '.' in str(self.value_variable[0]):
            if str(self.value_variable[0]).count('.') != 1:
                return False, 'error'
            else:
                val = str(self.value_variable[0]).split('.')
                if CheckTypeVariable(val[0]).is_int()[0] and CheckTypeVariable(val[1]).is_int()[0]:
                    return True, None

                return False, 'error-number'
        else:
            return False, None

    # check if the type is 'string' -> ("hello", "1", "3.4", "A", "true")
    def is_string(self):
        if str(self.value_variable[0])[0] == '"' or str(self.value_variable[-1])[-1] == '"':
            if self.value_variable[0][0] == '"' and self.value_variable[-1][-1] == '"':
                return True, None
            return False, 'error'
        return False, None

    # check if the type is 'bool' -> (true, false)
    def is_bool(self):
        return self.value_variable[0] in ['true', 'false'], None

    # check all type and return True if is to exist else False
    def is_type(self):
        value = self.value_variable
        if CheckTypeVariable(value).is_int()[0]:
            return True, 'int'
        elif CheckTypeVariable(value).is_float()[0]:
            return True, 'float'
        elif CheckTypeVariable(value).is_string()[0]:
            return True, 'string'
        elif CheckTypeVariable(value).is_bool()[0]:
            return True, 'bool'
        return False, None

    def is_type2(self):
        if CheckTypeVariable(self.value_variable).is_type()[0]:
            return True, None
        else:
            if CheckTypeVariable(self.value_variable).is_float() == (False, 'error'):
                return False, 'float'
            elif CheckTypeVariable(self.value_variable).is_float() == (False, 'error-number'):
                return False, 'float2'
            elif CheckTypeVariable(self.value_variable).is_string() == (False, 'error'):
                return False, 'string'

            return False, None

