#####################################
# IMPORT
#####################################
import PYTHON.System.data as data
from PYTHON.Function import function, condition, variable

Function = function.Function
Condition = condition.Condition
Variable = variable.Variable


class Execute:
    def __init__(self, *args):
        self.args = args
        self.all_func = {
            'out': Function().out,
            'help': Function().help,
            'var': Variable().var,
            'do': Condition().do
        }
        self.all_func_syntax = [
            'OUT:',
            'HELP:',
            'VAR:',
            'DO:'
        ]

    def exe(self, idx, funcName):
        if data.CODE == "":
            return
        if data.CODE[0] == self.all_func_syntax[idx]:
            self.all_func.get(funcName)(self.args[0])