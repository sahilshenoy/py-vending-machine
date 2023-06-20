from tabulate import tabulate

# [Name, ItemCode, Price, Stock]
stock = [["Lays Green", 1, 20, 12], [
    "Lays Blue", 2, 20, 8], ["Lays Red", 3, 20, 15]]
amount = 2000

print("Welcome to the Vending Machine")


def show():
    global item_choice
    filtered_stock = [['Item Name', 'Item Code', 'Item Price']]
    for i in stock:
        if i[3] > 0:
            filtered_stock.append(i[:-1])
    if filtered_stock:
        print(tabulate(filtered_stock, headers='firstrow', tablefmt='fancy_grid'))

    item_choice = int(input("Type the Item Code of the Product: "))
    for i in stock:
        if item_choice in [i[1] for i in stock if i[3] > 0]:
            print(f"Item {item_choice} is in Stock.")
            return True
        else:
            print(f"Item {item_choice} is not in Stock.")
            return False


def money():
    global amount
    if show() == True:
        notes = int(input("Amount in Notes: "))
        coins = int(input("Amount in Coins: "))
        money = notes + coins
        for i in stock:
            if i[1] == item_choice:
                if money == i[2]:
                    print(f"Rs{money} Received!, and {i[0]} is Disbursed.")
                    amount += money
                elif money > i[2]:
                    change = money - i[2]
                    print(
                        f"Rs{money} Received!, and {i[0]} and {change} is disbursed.")
                    amount = amount + money - change
                else:
                    fund_less = i[2] - money
                    print(
                        f"Funds are not sufficient, you are less by {fund_less}.")


def main():
    choice = "Y"
    while choice.upper() != "N":
        money()
        choice = input("Do you want to continue? (Y/N): ")
        if choice == "report":
            print(amount)
            print(stock)
            choice = input("Do you want to continue? (Y/N): ")


main()
