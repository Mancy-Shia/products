#讀取
products =[]
with open('product.csv','r', encoding ='utf-8') as f:
    for line in f:
        name, price = line.strip().split(',')
        products.append([name,price])
print(products)
#
products =[]
while True:
    name = input('Please enter the name of the product:')
    if name == 'q':
        break
    price = input('Please enter the price:')
    products.append([name,price])
print(products)
#印出商品名稱價格
for p in products:
    print(p)
#寫入檔案
with open('product.csv','w', encoding ='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0]+','+p[1]+'\n')