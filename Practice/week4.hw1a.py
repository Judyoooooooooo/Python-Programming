c=int(input("單位成本： ")) #進貨成本
r=int(input("單位零售價： ")) #單位零售價
N=int(input("需求可能數： ")) #預估需求可能數
q=int(input("訂貨量： ")) #訂貨量
list = []
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))

exp = 0
sum = 0.0
prob = 0.0
maxP = 0

for i in range(0,q+1) :
    exp = r * i - c * q
    if i != q :
        sum += list[i] * exp
        prob += list[i]
    else:
        sum += (1-prob) * exp
        break

print(int(sum))
