from curses.ascii import isdigit


num1 = input('digite um número: ')
num2 = input('digite um número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('não pode converter estes digitos não realiza contas')