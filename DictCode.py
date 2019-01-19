products = [
    {'name':'apple','color':'white','price':45000},
    {'name':'redmi','color':'black','price':15000},
    {'name':'samsung','color':'white','price':55000},
    {'name':'apple','color':'silver','price':75000,'cod':False}
]

'''
products = {
    "name" : ['apple','redmi','samsung','apple'],
    "color" : ['white','black','white','silver'],
    "price" : [45000,15000,55000,75000]
    }
'''
p_name = 'apple'
for i in range(len(products)):
    if products[i]['name'] == p_name:
        print(products[i])
