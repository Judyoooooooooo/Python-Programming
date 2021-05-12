gradeStr=input() #12345
grades = gradeStr.split()
print(grades) # ['1', '2', '3', '4', '5']
for i in range(len(grades)):
    grades[i] = int(grades[i]) * 2
    print(grades)


# months is a list used as a lookup table
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
n = int(input("Enter a month number (1-12): ")) 
print("The month is", months[n - 1] + ".")

#井字遊戲
game = [[1, 0, 1], [1, 1, 0], [0, 0, 1]] # 2-dim list
for i in range(3):
    if game[i][0] == game[i][1] and game[i][1] == game[i][2]:
        print("winner:", game[i][0]) 
        break
# then check for columns and diagonals