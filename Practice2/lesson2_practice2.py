# -*- coding: utf8 -*-

# msg=u'中文測試'
# print("msg=", msg)
# print("len(msg)=", len(msg))
# msg2='中文測試'
# print("msg2=", msg2)
# print("len(msg2)=", len(msg2))

# #中文轉換
# msg='晚上七點水源星巴克見'
# for achr in msg:
#     print(ord(achr), end= " ")


# #中文解碼    
# # code="26202 19978 19971 40670 27700 28304 26143 24052 20811 35211"
# code="21830 31649 31243 24335 35373 35336"
# tmpcode=code.split(" ")
# msg=" "
# for acode in tmpcode:
#     msg = msg + chr(int(acode))
# print(msg)


# #變成大寫
# s = "athletes could not join the parade"
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.replace("athletes", "guests"))

#count計數
# s2 = "media and mania"
# print(s2.count("ia"))


#in operation
#uletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
#'A' in uletter #True
#'z' in uletter #False
#'AD' in uletter #False 因為中間有跳
#'MN' in uletter #True

# #找位置
# s3 = "02-33661184"
# s3.find('-')

# #是不是數字
# s4="1234"
# s4.isnumeric()
# s4="1234.5"
# s4.isnumeric()


# print('www.example.com'.strip('cmowz.'))
# print("%s同學您好, 您借的書已逾期%d天，請盡速歸還。" % ("王大雄", 55))

print(ord("!"))
str_a="abc"
str_b="def"

# str_c = str_a + str_b
# print(str_c)
# print("str_a"*3)
# str_c=str_a[:]
# print(str_c)
str_b[0]="z"
print(str_b)
