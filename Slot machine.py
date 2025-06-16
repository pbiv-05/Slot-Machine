import random  #bcoz we want the symols generation to be random



MAX_LINES = 3
MAX_BET=103
MIN_BET=1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
 }

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
 }

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = [] # a list to store the index o lines we won on
    for line in range(lines): #loop will iterate through line from 0 to lines-1 to check the current line we are on
        symbol = columns[0][line] #symbol is the value of first symbol found in 0 index ie 1st column at the current line
        for column in columns: #iterate through each column in the columns list ,to check if symbol in current line matches symbols in all other lines
            symbol_to_check = column[line]  #symbol_to_check is assigned the symbol found in the current column at the current line. This checks if the symbol in the current column matches the symbol from the first column.
            if symbol != symbol_to_check:  # if symbol to check is not equal to the symbol from the first column we got it breaks
                break
        else:
                winnings += values[symbol] * bet #if symbol matches it calculates winnings by multiplying the value to bet
                winning_lines.append(line + 1) # we will add the lines in our winning lines list and line+1 because var line is index so ww have to increment
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []  #creates a list to store all our symbols
    for symbol, symbol_count in symbols.items(): # iterating through dictionary to get symbol and symbol count
        for _ in range(symbol_count): #using anonymous operator to run the loop till the no of symbol count
            all_symbols.append(symbol)  #append the symbol in the list all symbols

    columns = [] #create a list to store the no of columns by storing small lists for each columns
    for _ in range(cols): #for every column generate values equal to our row number
        column = []  # for every row store the values for 1 column
        current_symbols = all_symbols[:] # make a copy bcoz the next time we select elemeents from the allsymbols it will have some eleme=nts already removed
        for _ in range(rows): #nested for bcoz for every cols we will generate values equal to the row number
            value = random.choice(current_symbols) #we will now choose the random values from current symbols for each row
            current_symbols.remove(value)  #after choosing the elements we will remove them so it does not choose values higher than than the count we defined
            column.append(value) #adds the value in column list


        columns.append(column)   #adds the column list in our columns list to  get the total columns in 1 list

    return columns

def print_slot_machine(columns): #defines a fxn to print  our slot machine
    for row in range(len(columns[0])): #rows we have is the elements in each column and index 0 bcoz atleast we will have 1 column
        for i, column in enumerate(columns): #it gives index to each individual colmn in our columns
            if i != len(columns) - 1: #bcoz we need pipe operator after every digit except the last which is why we pass lencolumns bcoz that is the max index we have
               print(column[row], end=" | ")   #we will print the row to corrosponding column index where if i<lencolumna it will print pipe
            else:
                print(column[row], end="")  # if i is equal to lencolumns it will not print pipe

        print()

def deposit():  #defines a fxn deposit
    while True:  #repeatedly executes until the execution is true
        amount = input("what would you like to deposit? $") #create a prompt to take input from user
        if amount.isdigit():  #method on string to check if entered value is a valid number(whole)
           amount = int(amount) #by default this comes an string so we convert it into numeric value we wanna have for our balance
           if amount > 0:
            break
           else:
            print("amount must be greater than 0.")
        else:
            print("please enter a number:")

    return amount

def get_number_of_lines():
    while True:  # repeatedly executes until the execution is true
        lines = input("how many lines would you like to bet on (1-" +str(MAX_LINES) + ")?")  #to concatenate and converting to string bcozcant add string to nummber
        if lines.isdigit():  # method on string to check if entered value is a valid number(whole)
            lines = int(lines) # by default this comes an string so we convert it into numeric value we wanna have for our lines
            if 1<= lines <= MAX_LINES:  #check if entered lines are within the bound
                break
            else:
                print("lines should be between 1 and 3")
        else:
            print("please enter a number between 1 and 3:")

    return lines

def get_bet():
    while True:  # repeatedly executes until the execution is true
        bet = input("how much would you like to bet on each lines?")  #to concatenate and converting to string bcozcant add string to nummber
        if bet.isdigit():  # method on string to check if entered value is a valid number(whole)
            bet = int(bet) # by default this comes an string so we convert it into numeric value we wanna have for our lines
            if MIN_BET <= bet <= MAX_BET:  #check if entered lines are within the bound
                break
            else:
                print(f"bet amount should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a valid bet amount:")

    return bet

def spin(balance):  # defines a fxn so we can can run this again and again
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you dont have sufficient balance to bet ${total_bet}.Your current balance is ${balance} ")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines.Your total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on lines :", *winning_lines)
    return winnings-total_bet  #returns the amount we have left after winning against what we have bet
def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance} ")
        play = input("press enter to play and q to quit.")
        if play == "q":
            break
        balance += spin(balance)

    print(f"you left with ${balance}")
main()