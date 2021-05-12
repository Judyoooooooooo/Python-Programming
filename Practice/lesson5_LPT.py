#LPT implementation
# read and prepare n, m, and p
n = int(input("Number of jobs: "))
m = int(input("Number of machines: ")) 
pStr = input("Processing times: ")

p = pStr.split(' ')  #依照空白鍵分開工作的時間
for i in range(n):
    p[i] = int(p[i]) #轉成int形式再存回p[i]

# machine completion times答案
loads=[0]*m  #花多少時間
assignment = [0] * n #第一個job要分給machine幾

# in iteration j, assign job j to the least loaded machine
for j in range(n): #要挑出list中最小load的數字find the least loaded machine
    leastLoadedMachine = 0
    leastLoad = loads[0]  #假設最小地load是第0台
    for i in range(1, m):
        if loads[i] < leastLoad: #依序去跑load[i]再與目前的leastload比較
            leastLoadedMachine = i  #若比較小 他就要當目前的指標
            leastLoad = loads[i]
    # schedule a job
    loads[leastLoadedMachine] += p[j]  #把最小load的機器時數加到他原本的時數(累積)
    assignment[j] = leastLoadedMachine + 1  #machine 0,1,2,3,...(程式讀到的) --> 跑出來的結果

    #to check the process
    print(str(p[j])+":"+ str(loads))

# the result
print("Job assignment: " + str(assignment)) 
print("Machine loads: " + str(loads))