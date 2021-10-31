from checkType import CheckTypeVariable
from variable import Variable
import data
from error import Error

class Function:

    def __init__(self):
        self.data = data.Data()
        self.VARIABLE_CLASS = Variable(self.data.GET_var(), data.LINE)
        self.all_func_create = []

    def out(self, ops):
        if CheckTypeVariable(ops).is_string():
            print('\033[34m' + " ".join(ops) + '\033[0m')
        else:
            number = ops[0::2]
            operator = ops[1::2]
            resultSTR = ''
            num = 0
            oper = 0
            bools = True
            j = 0

            for i in number:
                if self.data.GET_var().get(str(i[1:])) is None:
                    j += 1
                else:
                    if self.data.GET_var().get(str(i[1:]))[0] in ['float', 'int']:
                        if self.data.GET_var().get(str(i[1:]))[0] == 'int':
                            number[j] = int(self.data.GET_var().get(str(i[1:]))[1])
                            j += 1
                        else:
                            number[j] = float(self.data.GET_var().get(str(i[1:]))[1])
                            j += 1
                    else:
                        Error('FatalError', 0, data.LINE, data.CODE, data.FILE)

            try:
                for x in range(len(number) + len(operator)):
                    if bools:
                        resultSTR += str(number[num])
                        bools = False
                        num += 1
                    else:
                        resultSTR += str(operator[oper])
                        bools = True
                        oper += 1

                try:
                    result = eval(resultSTR)
                    print('\033[34m' + str(result) + '\033[0m')

                except ZeroDivisionError:
                    e = True
                    Error(ZeroDivisionError, 0, CODE_variable_value=number)

                except:
                    Error(SyntaxError, 5)
            except:
                Error(ValueError, 1, CODE_variable_value=number)

    def created_function(self, name, parameter: list):
        run = True
        all_code = []

        while run:
            code = input("\033[90m" + "." + str(len(str(self.data.line)) * '.') + "." + '    ' + "\033[0m")
            all_code.append(code)

            if code == 'END;':
                run = False

        print(all_code)