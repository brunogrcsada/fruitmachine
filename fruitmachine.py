import random 

machine_symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
player_balance = 1

money_won = 0
money_lost = 0

print("Welcome to the Fruit Machine Simulator. Every spin costs 20p!")

def currency_format(value):
    if value >= 0:
        return '£{:,.2f}'.format(value)
    else:
        return '-£{:,.2f}'.format(abs(value))

def generate_rolls():
    current_symbols = []

    for _ in range(3):
        current_symbols.append(random.choice(machine_symbols))

    return current_symbols

spin_number = 0

while player_balance > 0:
    if (input("\nWould you like to spin the fruits? (Enter Y to continue and N to collect earnings): ").lower() == "y"):
        spin_number += 1

        current_balance = player_balance

        obtained_values = generate_rolls()

        print("Your values are: " + str(obtained_values))

        if (obtained_values.count("Bell") == 3):
            player_balance += 5

        elif (obtained_values.count("Skull") == 2):
            player_balance -= 1

        elif (obtained_values.count("Skull") == 3):
            player_balance -= player_balance

        elif (obtained_values[1:] == obtained_values[:-1]):
            player_balance += 1

        for item in obtained_values:
            if(obtained_values.count(item) == 2):
                player_balance += 0.5
                break

        player_balance = round(player_balance, 2)
        change = round(player_balance - (+current_balance), 2)

        player_balance = player_balance - 0.2

    else:
        break

    if (change > 0):    
        print("\nYou have won " + str(currency_format(change)))
        money_won += change
    elif(change < 0):
        print("\nYou have lost " + str(currency_format(-change)))
        money_lost -= change
    else:
        print("\nYou haven't lost or won any amount!")
    
    print("Your current balance is: " + str(currency_format(player_balance)))

    if (player_balance <= 0):
        print("You have reached your demise. Game Over...")
        break

        

print("\nThank you for playing Fruit Machine!")

print("Your total number of spins was " + str(spin_number))
print("You won £" + str(money_won) + " throughout the game")
print("You lost £" + str(money_lost) + " throughout the game\n")