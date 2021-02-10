# Print customers and mobile numbers in sorted order of customer name

data = ['Jason,383939333', 'Kevin,383882222', 'Bob,281881111', 'Jason,19392932323',
        'Bob,2911921222', 'Jason,293921212',
        'Mike,3838811212', 'Richards,398181212', 'Kevin,9898883833']

customers = {}

for entry in data:
    name, mobile = entry.split(",")
    if name in customers:
        customers[name].add(mobile)  # add to existing customer
    else:
        customers[name] = {mobile}  # add new customer with a set for mobile numbers

for name, mobiles in sorted(customers.items()):
    sortedmobiles = ','.join(sorted(mobiles))
    print(f"{name:15} {sortedmobiles}")
