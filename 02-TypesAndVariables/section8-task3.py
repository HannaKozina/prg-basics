cel = float(input("Enter temperature in celsius: "))

far = (cel * 1.8) + 32
kel = cel + 273.15
far = round(far, 2)

print(f'Your temperature in Fahrenheit is : {far} and your temperature in Kelvin is {kel}')