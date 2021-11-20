code = input('>').split()


class Func:
    def __init__(self, *args):
        self.args = args
        self.all_func = {
            'out': self.out,
            'type': self.type
        }
        self.all_func_syntax = [
            "OUT:",
            "TYPE:"
        ]

    def exe(self, idx, funcName):
        if code[0] == self.all_func_syntax[idx]:
            self.all_func.get(funcName)(self.args)

    def out(self, *args):
        print(" ".join(args[0][0]))

    def type(self, *args):
        print('typeof <' + "".join(args[0][0]) + '>')


func = Func(code[1:])

func.exe(0, 'out')
func.exe(1, 'type')