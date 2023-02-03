import os
#讀取檔案
def read_file(filename):
    products =[]
    
    with open(filename,'r', encoding ='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name,price])
    return products
#輸入
def user_input(products):
    while True:
        name = input('Please enter the name of the product:')
        if name == 'q':
            break
        price = input('Please enter the price:')
        products.append([name,price])
    print(products)
    return products
#印出商品名稱價格
def print_products(products):
    for p in products:
        print(p)
#寫入檔案
def write_file(filename, products):
    with open(filename,'w', encoding ='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0]+','+p[1]+'\n')

def main():
    filename = 'product.csv'            
    if os.path.isfile(filename):
        products = read_file(filename)
    else:
            print('file not found')    
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()

