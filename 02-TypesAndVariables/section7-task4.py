tree_length = int(input("Enter tree diameter in cm: "))
tree_circumference = 3.14 * tree_length
cut_ok = tree_circumference >= 50


print(f'The tree can be cut down: {cut_ok}')