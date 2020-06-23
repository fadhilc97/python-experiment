items = [
    {'id' : 1, 'name' : 'book'},
    {'id' : 2, 'name' : 'pencil'},
    {'id' : 3, 'name' : 'eraser'}
]

item_ids = [item['id'] for item in items]
print(min(item_ids))
