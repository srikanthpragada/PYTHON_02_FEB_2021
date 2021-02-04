# Calculate net amount with 20% discount and 5% tax

# Input
price = int(input("Enter price : "))
qty = int(input("Enter qty  : "))

# Process
amount = price * qty
discount = amount * .20
discounted_amount = amount - discount
tax = discounted_amount * 0.05
net_amount = discounted_amount + tax

# Output
print(f"Amount       {amount:10.2f}")
print(f"- Discount   {discount:10.2f}")
print(f"             ----------")
print(f"             {discounted_amount:10.2f}")
print(f"+ Tax        {tax:10.2f}")
print(f"             ----------")
print(f"             {net_amount:10.2f}")
