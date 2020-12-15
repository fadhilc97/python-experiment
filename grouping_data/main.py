ids = list(range(23))
record_per_group = 5
groups = []

for idx, val in enumerate([0, 5, 10, 15, 20]):
    if idx == 0:
    	groups.append(ids[0:record_per_group])
    elif idx == len([0, 5, 10, 15, 20]) - 1:
    	groups.append(ids[val:len(ids)])
    else:
    	groups.append(ids[val:val+record_per_group])
        
print(ids)
print(groups)