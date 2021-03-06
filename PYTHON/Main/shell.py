#####################################
# IMPORT
#####################################
from main import Code
import PYTHON.System.data as data
from PYTHON.System.color import Color


if __name__ == '__main__':

    #####################################
    # DEFAULT VALUE
    #####################################
    line = 0
    run = True
    print(Color(txt='''** Qwerdy Language **''').green())

    #####################################
    # COMMAND LINE
    #####################################
    while run:

        # create/update value
        line += 1

        try:
            txt = input(Color(txt=f'[{line}] ').black())
            code = txt.split()
        except KeyboardInterrupt:
            txt, code = None, None
            print('\nexit code 0')
            exit()

        # check if there are the comment or if is empty
        if txt.replace(" ", "") == "" or code[0] == '//' or txt[0:2] == "//":
            pass

        # detected if the code is in file
        elif code[0] == "FILE" and code[2] == "RUN":
            run = False

            # open file for pick code
            file = open(str(code[1]), 'r')
            stock = file.readlines()

            # remove comment
            n = 0
            for i in stock:
                if i[0] == '/':
                    del stock[n]
                n += 1

            # split all code in list
            lineCodeFile = "".join(stock).replace('\n', '')
            txt = lineCodeFile.split(';')
            txt = [ele for ele in txt if ele.strip()]

            # execute the code if is in the file
            data.CODE = txt
            data.LINE = line
            data.FILE = True
            Code()

        else:
            # execute the code if is not in the file
            data.CODE = code
            data.LINE = line
            data.FILE = False
            Code()