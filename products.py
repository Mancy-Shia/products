products =[]
while True:
    name = input('Please enter the name of the product:')
    if name == 'q':
        break
    price = input('Please enter the price:')
    products.append([name,price])
print(products)

# for p in products:
#     print(p)
with open('product.csv','w', encoding ='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0]+','+p[1]+'\n')