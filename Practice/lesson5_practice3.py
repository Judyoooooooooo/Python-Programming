lst=[3,1,4,1,5,9] 
lst.append(2)
print(lst) # [3, 1, 4, 1, 5, 9, 2]

lst.sort()
print(lst) # [1, 1, 2, 3, 4, 5, 9]

lst.reverse()
print(lst) # [9, 5, 4, 3, 2, 1, 1]
print(lst.index(4)) # 2

lst.insert(4, "Hi") 
print(lst) # [9, 5, 4, 3, 'Hi', 2, 1, 1]
print(lst.count(1)) #2

lst.remove(1)
print(lst) # [9, 5, 4, 3, 'Hi', 2, 1]
print(lst.pop(3)) #3
print(lst) #[9,5,4, 'Hi', 2, 1]

#another example
aList = [1, 2, 3]
anotherList = aList
anotherList[0] = 5 
print(aList) # [5, 2, 3]

anotherList=[]
for i in aList:
    anotherList.append(i)
    print(aList)
    print(anotherList)