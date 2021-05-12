gradeStr=input() #12345 
grades = gradeStr.split()
grades.append([9, 7, 5])
print(grades)
print(grades[3][0],grades[3][1]) #list中的list值
print(grades[3], grades[2] * 2)
print(len(grades)) #長度

