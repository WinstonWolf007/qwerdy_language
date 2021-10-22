from python_file_lang1 import basic

while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
