# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話印出'終於猜對了'
# 猜錯的話要提示比答案大或小

import random
r = random.randint(1, 100)
while True:
	num = input('請猜1到100之間一個數字: ')
	num = int(num)
	if num == r:
		print('恭喜你猜中了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print ('比答案小')