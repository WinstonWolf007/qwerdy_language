from basic2 import *

print('\033[92m---> The Qwerdy Language is create by WinstonWolf007 <---'+"\n\t* [VERSION] => [5.0]\033[90m")
print('\n')
while True:
    txt = input("\033[90mQwerdy-shell>\033[0m")
    if txt.replace(" ", "") == "":
        pass
    elif txt.split()[0] == '//' or txt[0] == "/" and txt[1] == '/':
        pass
    else:
        Code(txt)