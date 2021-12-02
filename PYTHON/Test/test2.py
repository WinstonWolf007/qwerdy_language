import string

a = input('\033[96m>\033[0m').lower()

list_word = [i for i in a if i in string.ascii_lowercase]
list_find = ['' for x in range(len(a))]
run = True
health = 5

while run:
    choise = input('\033[90mLetter: \033[0m').lower()
    if choise in string.ascii_lowercase and choise in list_word:
        for j, letter in enumerate(list_word):
            if letter == choise:
                list_find[j] = letter
        for k, lettres in enumerate(list_find):
            if lettres == "":
                break
            elif k+1 == len(list_find):
                print(f"Game Win [{''.join(list_word)}]")
                exit()
        print("\033[92m"+str(list_find)+"\033[0m")
    else:
        if health <= 1:
            print(f"Game Over [{''.join(list_word)}]")
            exit()
        else:
            health -= 1
            print("\033[91mletter != '" + choise + "'\033[0m")