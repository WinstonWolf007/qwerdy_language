#####################################
# IMPORT
#####################################
from PYTHON.Main.basic2 import *
import PYTHON.System.data as data

#####################################
# DEFAULT VALUE
#####################################
line = 0
run = True
print('\033[92m---> The Qwerdy Language is create by WinstonWolf007 <---'+"\n\t* [VERSION] => [6.1]\033[90m\n")

#####################################
# COMMAND LINE
#####################################
while run:

    # create/update value
    line += 1
    txt = input(f"\033[90m[{line}] \033[0m")
    code = txt.split()

    # check if there are the comment or if is empty
    if txt.replace(" ", "") == "" or code[0] == '//' or txt[0] == "/" and txt[1] == '/':
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