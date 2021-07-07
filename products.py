
#product #用二維度做出清單中的清單，同時裝入品名跟價格
products = [] 
with open('products.csv',"r",encoding= 'utf-8') as f:   #先讀取舊有的檔案，之後再繼續寫入新的資料
    for line in f:
        if '商品,價格' in line:  #如果這個字串菜檔案裡
            continue   #這樣就會跳過這行，然後繼續讀下一行資料，不會跳出迴圈，但是break會
        name, price = line.strip().split(',')   #先把換行符號去掉   再把裡面的資料一個一個抓出來，用逗點區隔(切割)
        #name = s[0]    用name, price存進去這兩行就可以省略了
        #price = s[1]
        products.append([name, price])
print(products)   #輸出出來會便清單,因為我們使用split功能 

'''
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    p = []   #p =[name,price]，以下兩行可省略
    p.append(name)  
    p.append(price)
    products.append(p)
print(products)  #[['shoes', '100'], ['bags', '200'], ['clothes', '99']]
'''
#這個寫法更簡潔
#products = []   #因為我們已有了舊檔案，所以不用再寫這行了
#讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    products.append([name, price])
print(products)  #[['shoes', '100'], ['bags', '200'], ['clothes', '99']]
#print(products[0][0])


#印出所有購買紀錄
for p in products:  #這裡的p是小清單
    print(p[0],'的價格是', p[1])

#寫入檔案
with open('products.csv', 'w',encoding= 'utf-8') as f:
    f.write(('商品,價格\n'))   #產生的CSV檔時，標題便亂碼，這是因為牽扯到編碼的問題，所以我們指定utf-8
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') # 用加法把字串合併，這個write才真正寫入
        #,用來資料分隔   '\n'用來資料換行
        #寫入，跟讀取都各自有不同的編碼方法
        
'''
字串可以合併
'abc' + 123 = 'abc123'    
'''
