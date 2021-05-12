# import math
# print(math.sqrt(2))


# def give_total(n):
#   unitp = 1.2
#   total = unitp * n
#   return total
# unitp=0
# total=0
# print(give_total(1))
# print(unitp)


# def give_total(n):
#   print("Weekend=%d" % weekend)
#   unitp = 1.2
#   total = unitp * n
#   return total
# weekend = True
# m=give_total(5)


#你在這個函數內部做了這個改變的 並不會影響到函數外面的這個世界的這個變數的值
# def give_total(n):
#   unitp = 1.2
#   weekend = False
#   print("New Weekend=%d" % weekend)
#   total = unitp * n
#   return total
# weekend = True
# print("Outside, before calling: Weekend=%d" % weekend)
# m1=give_total(5)
# print("Outside: Weekend=%d" % weekend)


# def give_total(n):
#   global weekend
#   print("Weekend= %d " % weekend)
#   unitp = 1.2
#   weekend = False
#   print("New Weekend= %d " % weekend)
#   total = unitp * n
#   return total
# weekend = True
# m=give_total(5)


# def min_max(x1, x2, x3, x4):
#   r1 = min(x1, x2, x3, x4)
#   r2 = max(x1, x2, x3, x4)
#   return r1, r2
# a1=input("Provide input value a1: ")
# a2=input("Provide input value a2: ")
# a3=input("Provide input value a3: ")
# a4=input("Provide input value a4: ")
# out1,out2 = min_max (float(a1), float(a2), float(a3), float(a4))
# print("Minimal =", out1)
# print("Maximal =", out2)


# def myabs(x):
#   if x< 0:
#     return -x
#   if x>= 0:
#     return x
# print(myabs(-3.5))
# print(myabs(0))


# def swap1(x1, x2):
#   tmp=x1
#   x1=x2
#   x2=tmp
#   print("Inside swap1: x1=", x1, "x2=", x2)
# x1, x2 = 100, 5
# print("Outside: x1=", x1, "x2=", x2)
# swap1(x1, x2)
# print("Outside: x1=", x1, "x2=", x2)

# #遞迴
# def factorial(n):
#   if n == 0:
#     return 1 
#   else:
#     recurse = factorial(n-1)
#     result = n * recurse
#     return result


# def factorial(n):
#   if not isinstance(n, int):
#     print('Factorial is only defined for integers.')
#     return None
#   elif n<0:
#     print('Factorial is not defined for negative values.')
#     return None
#   elif n==0:
#     return 1 
#   else:
#     return n * factorial(n-1)
# factorial("Qoo")


def factorial(n):
  space = ' ' * (4*n)
  print(space, 'factorial', n)
  if not isinstance(n, int):
    print('Factorial is only defined for integers.')
    return None
  elif n<0:
    print('Factorial is not defined for negative values.')
    return None
  elif n==0:
    print(space, 'returning 1')
    return 1
  else:
    result = n * factorial(n-1)
    print(space, 'returning', result)
    return result

factorial(4)


# def print_msg(item, ndays=30):
#   print("Please return %s in %d days" % (item, ndays))
# print_msg("items") 
# print_msg("items", 50)

# def n_ducks(num):
#   print("%s little ducks went out one day" % num)
# def only_n(num):
#   print("But only %s little ducks came back" % num)
# def over_mother():
#   print("Over the hills and far away") 
#   print("Mother duck said quack quack quack")
# n_ducks("Five") 
# over_mother() 
# only_n("Four") 
# print() 
# n_ducks("Four") 
# over_mother() 
# only_n("Three") 
# print() 
# n_ducks("Three") 
# over_mother() 
# only_n("Two")

# def sing_unit(num1, num2):
#   n_ducks(num1)
#   over_mother()
#   only_n(num2)
# sing_unit("Five", "Four") 
# print()
# sing_unit("Four", "Three") 
# print()
# sing_unit("Three", "Two")