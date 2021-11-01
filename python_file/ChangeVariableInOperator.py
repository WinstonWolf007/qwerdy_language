from data import Data


class ChangeVariableForValue:

    def __init__(self, values: list):
        self.data = Data()
        self.values = values

    def changeData(self):
        j = 0
        for i in self.values:
            if i[0] == '$':
                typeVar, dataVar = self.data.GET_var(i[1:])
                self.values[j] = str(dataVar)
                j += 1

        print(self.values)
        return self.values
