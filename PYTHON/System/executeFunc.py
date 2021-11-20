import data


class Execute:
    def __init__(self):
        self.all_func = {}
        self.all_func_syntax = []
        self.code = data.Data().code

    # create function syntax for command line
    def exe(self, idx_syntax, func, *args):
        if self.code[0] == self.all_func_syntax[idx_syntax]:
            self.all_func.get(func)()