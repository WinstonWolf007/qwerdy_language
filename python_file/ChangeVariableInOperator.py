from data import Data


class ChangeVariableForValue:

    def __init__(self, values: list):
        self.data = Data()
        self.values = values

    def changeData(self):
        j = 0
        for i in self.values:
            if i[0] == '$':
                dataVar = self.data.GET_var(i)
                self.values[j] = dataVar
                j += 1

        return self.values
