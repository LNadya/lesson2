"""
Подсказки для викторины:
Чайковский, год рождения - 1840
Моцарт, год рождения - 1756
Паганини, год рождения - 1782
Бах, год рождения - 1685
Бетховен, год рождения - 1770
"""
offer = input('Хотите поучаствовать в викторине? ')
while offer == 'да':
    quetion_1 = int(input('В каком году родился Чайковский? '))
    quetion_2 = int(input('В каком году родился Моцарт? '))
    quetion_3 = int(input('В каком году родился Паганини? '))
    quetion_4 = int(input('В каком году родился Бах? '))
    quetion_5 = int(input('В каком году родился Бетховен? '))

    if quetion_1 == 1840:
        quetion_1 = 1
    else:
        quetion_1 = 0
    if quetion_2 == 1756:
        quetion_2 = 1
    else:
        quetion_2 = 0
    if quetion_3 == 1782:
        quetion_3 = 1
    else:
        quetion_3 = 0
    if quetion_4 == 1685:
        quetion_4 = 1
    else:
        quetion_4 = 0
    if quetion_5 == 1770:
        quetion_5 = 1
    else:
        quetion_5 = 0

    true_answers = str(quetion_1 + quetion_2 + quetion_3 + quetion_4 + quetion_5)
    false_answers = str(5 - quetion_1 - quetion_2 - quetion_3 - quetion_4 - quetion_5)
    print('количество правильных ответов: ' + true_answers)
    print('количество ошибок: ' + false_answers)
    print('процент правильных ответов: ' + str(int(int(true_answers) * 100 / 5)))
    print('процент неправильных ответов: ' + str(int(int(false_answers) * 100 / 5)))

    offer = input('Хотите поучаствовать в викторине? ')