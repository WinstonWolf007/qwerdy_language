#####################################
# IMPORT
#####################################
import PYTHON.System.data as data
from PYTHON.Function.function import Function
from PYTHON.Function.condition import Condition


class Execute:
    def __init__(self, *args):
        self.args = args
        self.all_func = {
            'out': Function().out,
            'help': Function().help,
            'var': Function().var,
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