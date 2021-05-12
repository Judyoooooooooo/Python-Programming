#彼此間的距離
numLoc = 5 
dst=[[0,9,6,7,4], [9,0,5,9,6], [6,5,0,3,1], [7,9,3,0,4], [4,6,1,4,0]] 
#0到1,2,3... )1到0,1,2,,, 若雙向不一樣大小，就依此

origin=0
# tour: a list that will contain the solution 
# tourLen: the total distance of the solution 
# unvisited: a list that contains those unvisited locations at any time 
tour = [origin]
tourLen = 0
unvisited = [] #記錄目前還沒去過的點
for i in range(numLoc):
    unvisited.append(i) 
unvisited.remove(origin)

# The algorithm
cur = origin #目前在的點 一開始從原點出發
for i in range(numLoc - 1): #假設有5個點，因為從原點開始，所以接下來只要選4個點
    next = -1 #下一個要走的點
    minDst = 999
    for j in unvisited:
        if dst[cur][j] < minDst: 
            next=j
            minDst = dst[cur][j]

    # move "next" from unvisited to tour
    unvisited.remove(next) 
    tour.append(next) 
    tourLen += minDst
    print(tour, tourLen)
    # print out the solution
    # run the next iteration from the next location
    cur = next

# complete the tour
tour.append(origin) 
tourLen += dst[cur][origin]
print(tour, tourLen) # print out the solution