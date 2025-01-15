import random

#global constant
MAX_LINE = 3 #maximum betting line
MAX_BET = 50
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 6, "B": 8, "C": 10, "D": 30}
symbol_win_value = {"A": 50, "B": 10, "C": 6, "D": 2}

#check the bet result
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)

    return winnings, winning_line

#slot result generator
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        remaining_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(remaining_symbols)
            remaining_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#print slot machine spin result
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

#prompt user to specify deposit amount
def deposit():
    while True:
        amount = input("Please enter the amount to deposit: $")
        try:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid amount.")
    return amount

#prompt user to specify how many lines they like to bet on
def get_number_of_lines():
    while True:
        lines = input(f"How many lines do you like to bet on (1-{MAX_LINE})?")
        try:
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Please enter a valid number of lines")
        except ValueError:
            print(f"The lines must be between 1-{MAX_LINE}.")
    return lines

#prompt user to specify how much to bet
def get_bet():
    while True:
        bet = input(f"How much would you like to bet on each line ({MIN_BET}-{MAX_BET})? ")
        try:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Please enter a valid amount to bet")
        except ValueError:
            print(f"The amount must be between ${MIN_BET} and ${MAX_BET}.")
    return bet

#execute game
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You do not have sufficient balance to bet that amount. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} line(s). Total bet is equal to ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(slots, lines, bet, symbol_win_value)
    print(f"Your winning is ${winnings}.")
    print(f"You won on lines:", *winning_line)

    return winnings - total_bet

#main slot machine program
def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        result = input("Press 'enter key' to play, or type 'quit' to quit: ")
        if result == "quit":
            break
        balance += spin(balance)

    print(f"Thank you for playing the slot. Your final balance is ${balance}. See you soon!")

main()

