# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話印出'終於猜對了'
# 猜錯的話要提示比答案大或小
# 2nd version添加count'你現在猜了幾次' (count = 0不能寫在while True否則永遠都是猜了0次)
# 3rd version改成讓使用者自訂數字範圍

import random
start = input('請輸入隨機整數範圍起始值: ')
end = input('請輸入隨機整數範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	num = input('請猜數字: ')
	num = int(num)
	count += 1 # 就是count = count + 1
	if num == r:
		print('恭喜你猜中了! 你現在猜了第', count, '次')
		break
	elif num > r:
		print('比答案大，你現在猜了第', count, '次')
	elif num < r:
		print ('比答案小，你現在猜了第', count, '次')
