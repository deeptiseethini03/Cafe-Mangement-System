menu = {
    "Coffee ☕": 50,
    "Bubble Tea 🧋": 30,
    "Sandwich 🥪": 70,
    "Burger 🍔": 100,
    "Pizza 🍕": 120,
    "Noodles 🍜": 80,
    "Fries 🍟": 99
}
total_bill = 0
print("WELCOME TO CAFE 🍵\n")
print("Menu:")
for item, price in menu.items():
    print(f"{item} : Rs {price}")
while True:
    user_input = input("\nEnter item you want to order: ").strip().lower()
    found = False
    for key in menu:
        # remove emoji part
        item_name = key.split()[0].lower()
        if user_input == item_name:
            total_bill += menu[key]
            print(f"{key} added. Current bill: Rs {total_bill}")
            found = True
            break
    if not found:
        print("Item not available")
    another = input("Do you want to order anything else? (yes/no): ").strip().lower()
    if another != "yes":
        break
print("\nTotal amount to pay: Rs", total_bill)
print("Thank you! Visit us again 😊😇")