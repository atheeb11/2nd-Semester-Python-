price = float(input("Enter the item price: "))
if price >= 100000:
    discount = price * 0.10
    print("You received a 10% discount!")
else:
    discount = 0
    print("No discount applied.")

total_payment = price - discount

print(f"Total payment: {total_payment}")