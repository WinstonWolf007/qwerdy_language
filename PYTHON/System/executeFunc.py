#####################################
# IMPORT
#####################################
import data
data_ = data.Data()
data.CODE = input('>').split()


class Execute:
    def __init__(self, *args):
        self.args = args
        self.all_func = {
            'out': self.out
        }
        self.all_func_syntax = [
            'OUT:'
        ]

    def exe(self, idx, funcName):
        if data.Data().code[0] == self.all_func_syntax[idx]:
            self.all_func.get(funcName)(self.args)

    def out(self, *args):
        print(args[0][0])


exe = Execute(data.CODE[1:])

exe.exe(0, 'out')