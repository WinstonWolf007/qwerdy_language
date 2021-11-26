class Color:

    def __init__(self, *, txt):
        self.txt = txt
        self.color = {
            'red': '\033[91m' + str(self.txt) + '\033[0m',
            'blue': '\033[94m' + str(self.txt) + '\033[0m',
            'green': '\033[92m' + str(self.txt) + '\033[0m',
            'yellow': '\033[93m' + str(self.txt) + '\033[0m',
            'grey': '\033[98m' + str(self.txt) + '\033[0m',
            'white': '\033[97m' + str(self.txt) + '\033[0m',
            'black': '\033[90m' + str(self.txt) + '\033[0m',
            'purple': '\033[95m' + str(self.txt) + '\033[0m'
        }

    def red(self):
        return self.color.get(self.red.__name__)

    def blue(self):
        return self.color.get(self.blue.__name__)

    def green(self):
        return self.color.get(self.green.__name__)

    def yellow(self):
        return self.color.get(self.yellow.__name__)

    def grey(self):
        return self.color.get(self.grey.__name__)

    def white(self):
        return self.color.get(self.white.__name__)

    def black(self):
        return self.color.get(self.black.__name__)

    def purple(self):
        return self.color.get(self.purple.__name__)