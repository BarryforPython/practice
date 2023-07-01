# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "Finally!"
# 猜錯的話 要告訴他 "higher"/"lower"
# 延伸1:告訴他這是你猜的第幾次

import random
r = random.randint(1, 100)
cont = 0
while True:
    cont += 1 # 這是個快寫法 完全等於 cont = cont +1
    a = input('Guess a number between 1~100:')
    a = int(a)
    if a == r:
        print('Finally!')
        print('this is your', cont, 'guess')
        break
    elif a < r:
        print('higher')
    elif a > r:
        print('lower')
    print('this is your', cont, 'guess')