price = float(input("Enter price: "))
discount = int(input("Enter discount %: "))
reduction = ( price * discount) / 100
price_with_discount = price - reduction

price = round(price, 2)
reduction = round(reduction, 2)
price_with_discount = round(price_with_discount, 2)

print(f"Entered price: {price}")
print(f"Entered discount:{discount}")
print(f'Price with discount: {price_with_discount}')
print(f'Reduction: {reduction}')