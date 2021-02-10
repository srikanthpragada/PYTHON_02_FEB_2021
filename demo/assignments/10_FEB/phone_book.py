
data = ['Jason,383939333','Kevin,383882222','Bob,281881111',
        'Mike,3838811212','Richards,398181212','Kevin,9898883833']

customers = {}

for entry in data:
    name,mobile = entry.split(",")
    customers[name] = mobile

for name,mobile in sorted(customers.items()):
    print(f"{name:15} {mobile}")
