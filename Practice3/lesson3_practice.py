# #List transformed to tuple
# alist = [11, 22, 33]
# atuple = tuple(alist)
# print(atuple)

# newtuple = tuple('Hello World!')
# print(newtuple)

# def cksum_twid(idstr): #Compute Checksum for Taiwn ID"""
#     code1 = ord(idstr[0]) #convert first English character to two-digit number.
#     cmap = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
#     num1 = cmap[code1 - 65]
#     newid = str(num1) + idstr[1:]
#     weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
#     checksum = 0
#     for i in range(0, 11):
#         checksum += weight[i] * int(newid[i])
#         print("checksum=%d" % checksum)


# #lambda
# f2 = lambda x: x**2
# print()
# print (f2(8))
# list1=[3,5,1.2, 4, 9]
# out2=map(lambda x: x**2, list1)
# print(list(out2))

# #dictionary-key/value
# eng2cn = dict()
# print(eng2cn)
# eng2cn['one'] = '一'
# eng2cn['two'] = '二'
# eng2cn['three'] = '三'
# eng2cn['four'] = '四'
# # print(eng2cn)
# # print(eng2cn['one'])
# # print(eng2cn['five'])
# # print(eng2cn.get('five'))
# # if 'five' in eng2cn:
# #     print(eng2cn['five'])
# print(eng2cn.keys())
# print(eng2cn.values())
# print(eng2cn.items())

# #某個字母出現的頻率
# def histogram(seq):
#     d = dict()
#     for element in seq:
#         if element not in d:
#             d[element] = 1
#         else:
#             d[element] += 1
#             return d
# h = histogram('brontosaurus')
# print(h)


# def print_hist(hist):
#     for key in hist:
#         print(key, hist[key])
# h = histogram('brontosaurus')
# print(h)

# def print_hist3(hist):
#     keys = hist.keys()
#     for key in sorted(keys):
#         print (key, hist[key])
# h = histogram('brontosaurus')
# print_hist3(h)

# def invert_dict(d):
#     inv = dict()
#     for key in d:
#         val = d[key]
#         if val not in inv:
#             inv[val] = [key]
#         else:
#             inv[val].append(key)
#     return inv

# hist = histogram('parrot')
# print (hist)
# inverted = invert_dict(hist)
# print (inverted)

# import datetime
# d1=datetime.datetime(2005,5,3)
# print(d1)
# d2=datetime.datetime(2017, 2, 5, 8, 5, 20)
# print(d2)
# print(d2.date())
# print(d2.time())
# print(d2.weekday())
# print(datetime.date.today())

# d3=datetime.datetime(1998, 2, 5, 8, 5, 20)
# d4=datetime.datetime(1999, 2, 1, 22, 4, 15)
# diff = d4 - d3
# print(diff)

# diff2 = datetime.timedelta(days=3,seconds=4)
# d5 = datetime.datetime(2000,1,1,0,0,0)
# d6 = d5 + diff2
# print(d6)

# d7 = datetime.datetime(2002,5,2,13,15,45)
# print(str(d7))
# print(d7.strftime('%Y-%m-%d'))
# print(d7.strftime('%B %d, %Y'))
# print(d7.strftime('%Y-%m-%d %H:%M:%S'))
# print(d7.strftime('%Y-%m-%d %I:%M:%S %p, %A'))

# #讀檔
# test='/Users/ouyijun/Desktop/python_lecture/商管程式設計二/test.txt'
# f=open(test, 'r', encoding = 'utf-8')
# data=f.read()
# print(data)
# f.close()


import os
os.getcwd()