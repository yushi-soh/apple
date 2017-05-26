
#A+BのAの部分を入力してもらう
input_numberA = input('数値を入力してください: ')
while not input_numberA.isdigit():
    input_numberA = input('数値を入力してください: ')
numberA = int(input_numberA)

input_while = ' '
answer = numberA

while input_while != 'end':
    print(answer)
    print("1, +\n2, -\n3, ×\n4, ÷ ")

    #演算記号の選択をしてもらう
    input_symbol = input('使いたい演算記号と対応する数字を入力してください:')
    while not input_symbol.isdigit():
        input_symbol = input('使いたい演算記号と対応する数字を入力してください:')
    symbol = int(input_symbol)
    while symbol < 1 or symbol > 4 :
        input_symbol = input('使いたい演算記号と対応する数字を入力してください:')
        while not input_symbol.isdigit():
            input_symbol = input('使いたい演算記号と対応する数字を入力してください:')
        symbol = int(input_symbol)

    #A+BのBの部分を入力してもらう
    input_numberB = input('数値を入力してください:')
    while not input_numberB.isdigit():
        input_numberB = input('数値を入力してください:')
    numberB = int(input_numberB)

    #計算する
    if symbol == 1:
        answer += numberB
        print(answer)
    elif symbol == 2:
        answer -= numberB
        print(answer)
    elif symbol == 3:
        answer *= numberB
        print(answer)
    elif symbol == 4:
        while numberB == 0:
            print("Error")
            input_numberB = input('正しい数値を入力してください:')
            while not input_numberB.isdigit():
                input_numberB = input('数値を入力してください:')
            numberB = int(input_numberB)
        answer /= numberB
        print(answer)
    else:
        print('正しい数値を入力してください')

    print('計算を終了する場合は end と入力してください')
    print('計算を続ける場合はエンターキーを押してください')
    input_while = input(':')

print('計算結果は'+ str(answer) + 'です')
