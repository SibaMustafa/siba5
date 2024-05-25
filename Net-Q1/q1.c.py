L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

items_b = [x for x in L if x.startswith('B')]

if items_b:
    print("Items starting with 'B':")
    for x in items_b:
        print(x)
else:
    print("No items found starting with 'B'") 