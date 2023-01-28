# """
# пушкин = 1799
# путин = 1952
# сталин = 1878
# николай2 = 1868
# есенин = 1895
# """
again = 'да'
while again == 'да':
    right: int = 0
    wrong: int = 0

    pushkin = input('В каком году родился Пушкин?')
    if pushkin == '1799':
        print('Верно')
        right += 1
    else:
        print('Неверно')
        wrong += 1

    putin = input('В каком году родился Путин?')
    if putin == '1952':
        print('Верно')
        right += 1
    else:
        print('Неверно')
        wrong += 1

    stalin = input('В каком году родился Сталин?')
    if stalin == '1878':
        print('Верно')
        right += 1
    else:
        print('Неверно')
        wrong += 1

    nikolai = input('В каком году родился Николай 2?')
    if nikolai == '1868':
        print('Верно')
        right += 1
    else:
        print('Неверно')
        wrong += 1

    esenin = input('В каком году родился Есенин?')
    if esenin == '1895':
        print('Верно')
        right += 1
    else:
        print('Неверно')
        wrong += 1

    print('Верно', right)
    print('Неверно', wrong)
    print('Верно', right * 100/5, 'percent')
    print('Неверно', wrong * 100/5, 'percent')
    again = input('Начнем с начала?')