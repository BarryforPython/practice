# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "Finally!"
# 猜錯的話 要告訴他 "higher"/"lower"

import random
r = random.randint(1,100)
while True:
    a = input('Guess a number between 1~100:')
    a = int(a)
    if a == r:
        print('Finally!')
        break
    elif a < r:
        print('higher')
    elif a > r:
        print('lower')