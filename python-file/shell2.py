from basic2 import *

lineCode = 0
run = True

print('\033[92m---> The Qwerdy Language is create by WinstonWolf007 <---'+"\n\t* [VERSION] => [5.0]\033[90m")
print('\n')

while run:
    lineCode += 1

    txt = input(f"\033[90m[{lineCode}] \033[0m")
    fileTxtStr = txt.split()

    if fileTxtStr[0] == "FILE" and fileTxtStr[2] == "RUN":

        run = False

        # open file for pick code
        file = open(str(fileTxtStr[1]), 'r')
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
        Code(txt, lineCode, True)

    # remove space and comment in console and execute Code
    elif txt.replace(" ", "") == "":
        pass
    elif txt.split()[0] == '//' or txt[0] == "/" and txt[1] == '/':
        pass
    else:
        Code(txt, lineCode)