items = [
    {'id' : 1, 'name' : 'book', 'price' : 5},
    {'id' : 2, 'name' : 'pencil', 'price' : 3.5},
    {'id' : 3, 'name' : 'eraser', 'price' : 2}
]

item_ids = [item['id'] for item in items]
item_prices = [item['price'] for item in items]
print(min(item_ids))
print(sum(item_prices))
