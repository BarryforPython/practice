# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "Finally!"
# 猜錯的話 要告訴他 "higher"/"lower"
# 延伸1:告訴他這是你猜的第幾次
# 延伸2:給使用者決定猜數字的範圍
import random
start = input('pls decide your lower limit of numberguess game:')
end = input('pls decide your upper limit of numberguess game:')
start = int(start)
end = int(end)
r = random.randint(start, end)
cont = 0
print('Guess a number between:', start, '~', end)
while True:
    cont += 1 # 這是個快寫法 完全等於 cont = cont +1
    a = input('Guess a number:')
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