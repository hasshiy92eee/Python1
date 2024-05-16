year = 2021
month = 4
day = 10
message = '今日は{}年{}月{}日です'.format(year,month,day)
print(message)

message = '今日は{1}月{2}日です。西暦{0}年です。'.format(year,month,day)
print(message)

print(f'今日は{year}年{month}月{day}日です。')
