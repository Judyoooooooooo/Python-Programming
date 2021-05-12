 #QR policy最小化存貨、訂貨、缺貨成本
 #找到最佳的再訂購點 R
 # past sales
salesStr = "14,23,26,17,17,12,24,19,10,18,22,31,19,16,22,28,20,27,20,32" 
sales = salesStr.split(',')
for i in range(len(sales)):
    sales[i] = int(sales[i])

# given information
stgCost = 2 #shortage cost
invCost = 1000 * 0.073 / 365   #買一個東西需要$1000，若買了之後就會損失把$1000元存在銀行的利息 
Q=30 #訂貨量 
I=20 #期初存貨

# finding the best R
bestR = 0
costOfBestR = 100000000 #找到比較小的就會更新
for R in range(Q):
    totalStgCost = 0
    totalInvCost = 0
# finding the total cost of this R
    for s in sales:
        I-=s #存貨變少
        if I<0: 
            totalStgCost += -I * stgCost  #缺貨成本
            I+=Q #訂貨
        elif I<R: 
            I+=Q
            totalInvCost += I * invCost
    totalCost=totalStgCost + totalInvCost
# update bestR when necessary
    if totalCost < costOfBestR: 
        bestR = R
        costOfBestR = totalCost
    print(R, totalStgCost, totalInvCost, totalCost)
print(bestR)