# Amount  : 15.84
# VAT 23% :  3.64
amount = float(input("Enter amount of money: "))
vat = (amount * 23)/ 100
amount = round(amount, 2)
vat = round(vat, 2)

print(f"Amount : {amount}")
print(f"VAT 23 % : {vat}")