from basic2 import *
import data

line = 0
run = True

print('\033[92m---> The Qwerdy Language is create by WinstonWolf007 <---'+"\n\t* [VERSION] => [6.1]\033[90m")
print('\n')

while run:

    line += 1
    txt = input(f"\033[90m[{line}] \033[0m")
    code = txt.split()
    print(code)
    if txt.replace(" ", "") == "" or txt.split()[0] == '//' or txt[0] == "/" and txt[1] == '/':
        pass

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

        # execute Code
        data.CODE = txt
        data.LINE = line
        data.FILE = True

        Code()

    else:
        # execute Code
        data.CODE = code
        data.LINE = line
        data.FILE = False

        Code()