import random

def pirate_plunder(treasure_chest, bank_account):
    while bank_account > 0:
        wager = int(input("Place your wager: "))
        
        if wager > bank_account:
            print("You don't have enough money to place that wager!")
            continue
        
        grabbed_item = random.choice(treasure_chest)
        bank_account -= wager
        
        if grabbed_item == "Gold":
            bank_account += wager * 2
            print("Congratulations! You found Gold!")
        else:
            print("Sorry, you didn't find any valuable treasure.")
        
        print("Bank Account Balance:", bank_account)
        
        if bank_account <= 0:
            print("You're out of funds! Game Over!")
            break

# Populate the treasure chest
treasure_items = ["Gold", "Silver", "Diamonds", "Coins", "Jewelry"]
initial_bank_account = 1000

# Start the game
pirate_plunder(treasure_items, initial_bank_account)
