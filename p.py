import os # operating system

#讀取檔案
def read_file(filename):
    products =[]
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 繼續
            name, price = line.strip().split(',')
            products.append([name, price])   
    return  products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品的價格: ')
        price = int(price)  
        products.append([name, price]) # 小清單裡存 name 和 price，把小清單(p)存進大清單(products)
    print(products)
    return products

# 印出所有商品購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n') # csv檔用'，'區隔

# 程式的進入點
def main():
    filename = 'products.csv'
    products =[]
    if os.path.isfile(filename): # 檢查檔案在不在
        print('yeah~找到檔案了!')
        products = read_file(filename)
    else:
         print('找不到原檔案QQ')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()