data = [1, 3, 5, 7, 9]
msg = "Numbers:{} {} {} {}".format(data[0], data[1], data[2], data[3])
with open('practice02.csv', 'w') as f:
    for d in  msg:
        f.write(msg)   #

'''
data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼

x = 0
with open('practice.csv', 'w') as f:
    for d in data:
        print(str(data[x]))
        f.write(str(data[x]))   #13579
        x += 1
 '''       
        
'''  
x = 0
d = []
while True:
    for d in data: 
        a =input((data[x]))
        a =str(a)
        #d.append([a])
        x += 1       
print(d[0])

with open('practice02.csv', 'w') as f:
    for d in data:
        f.write(d[0])
                  
   d= d.append(data[x])
        x +=1
        print(d)
'''   
      
                