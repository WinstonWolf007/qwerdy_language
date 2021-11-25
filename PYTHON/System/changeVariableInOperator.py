#####################################
# IMPORT
#####################################
import PYTHON.System.data as data


# class 'ChangeVariableForValue' is used for change the variable value -> ($a = 3)
class ChangeVariableForValue:

    def __init__(self, values: list):
        self.data = data.Data()
        self.values = values

    def changeData(self):
        for j, val in enumerate(self.values):
            if val[0] == '$':
                typeVar, dataVar = self.data.GET_var(val[1:])
                if typeVar in ['int', 'float']:
                    self.values[j] = dataVar[0]
                else:
                    self.values[j] = dataVar

        return self.values
