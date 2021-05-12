# a1="career"
# print(len(a1))
# for ch in a1:
#     print("Get a character:", ch)

# #Example Converting Date Format
# def ymd2dmy(dstr):
# #Convert date format from ymd to dmy E.g. 20150312 to 12032015
#     y1 = dstr[0:4]
#     m1 = dstr[4:6]
#     d1 = dstr[6:8]
#     return d1 + m1 + y1
# d1 = "20150512"
# d2 = ymd2dmy(d1)
# print()
# print("Converted date is", d2)


# #Example Validating Taiwan ID String
# idstr = "A123456789"
# code1 = ord(idstr[0])
# if (code1 < 65 or code1 > 90):
#     print("not valid") 
# else:
#     print("valid")

# idstr = "b123456789"
# code1 = ord(idstr[0])
# if (code1 < 65 or code1 > 90):
#     print("not valid") 
# else:
#     print("valid") 

#validation of Taiwan ID String
# idstr="A123456789"
idstr="E240211835"
code1 = ord(idstr[0])
cmap = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
num1 = cmap[code1 - 65]
newid = str(num1) + idstr[1:]
print("newid=", newid)
weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
checksum = 0
for i in range(0, 11):
    checksum += weight[i] * int(newid[i])
    remainder = checksum % 10
print("checksum=", checksum)
print("remainder=", remainder)


# #Verify Taiwan ID Number Return True if valid; False otherwise
# #check length
# def verify_twid(idstr):
#     if len(idstr) != 10:
#         return False
#     #check first letter
#     code1 = ord(idstr[0])
#     if (code1 < 65 or code1 > 90):
#         return False
#         #check the remaining letters
#     for i in range(1,10):
#         code2 = ord(idstr[i])
#     if (code2 < 48 or code2 > 57):
#         return False
#      #... Continue from previous slide ... #check the second character
#     code2 = ord(idstr[1])
#     if (code2 < 49 or code2 > 50):
#         return False 
#         #convert first English character to two-digit number.
#     cmap = [10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33]
#     num1 = cmap[code1 - 65]
#     newid = str(num1) + idstr[1:]
#     weight = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
#     checksum = 0
#     for i in range(0, 11):
#         checksum += weight[i] * int(newid[i])
#         if checksum % 10 == 0:
#             return True
#         else:
#             return False
