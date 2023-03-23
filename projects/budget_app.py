class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.balance = 0

    def check_funds(self, amount):
        # Check if the amount is valid given current balance
        # Note: amount will be negative if withdrawing
        if self.balance + amount < 0:
            return False
        else:
            return True

    def deposit(self, amount, description=''):
        # Make sure deposit amount is positive
        deposit_amount = abs(amount)
        # If the transaction is valid, update ledger
        if self.check_funds(deposit_amount):
            self.balance += deposit_amount
            self.ledger.append({
                'amount': deposit_amount,
                'description': description
            })
            return True
        # Return False if not a valid transaction
        else:
            return False

    def withdraw(self, amount, description=''):
        # Make sure withdraw amount is negative
        withdraw_amount = -1.0*abs(amount)
        # If the transaction is valid, update ledger
        if self.check_funds(withdraw_amount):
            self.balance += withdraw_amount
            self.ledger.append({
                'amount': withdraw_amount,
                'description': description
            })
            return True
        # Return False if not a valid transaction
        else:
            return False
        
    def transfer(self, amount, destination_category):
        # Make sure amount is always positve
        transfer_amount = abs(amount)

        # Check if source category has enough funds before transferring
        if self.check_funds(transfer_amount):
            # -------- Source category object --------
            # Create string for the description
            source_description = 'Transfer to ' + destination_category.get_category()
            # Create a withdrawal for the transfer
            self.withdraw(transfer_amount, source_description)

            # ------ Destination category object -----
            # Create string for the description
            destination_description = 'Transfer from ' + self.get_category()
            # Create a deposit for the transfer
            destination_category.deposit(transfer_amount, destination_description)

            # Transfer successful
            return True
        else:
            # Transfer unsuccessul
            return False

    def get_category(self):
        # Getter for object category name
        return self.category

    def get_balance(self):
        # Getter for object balance
        return self.balance
    
    def get_ledger(self):
        return self.ledger
    
    def __str__(self):
        # String method for printing the object
        # Find the number of asterisks needed on either side of category
        asterisk_count = (30 - len(self.category)) // 2
        display = '*'*asterisk_count + self.category + '*'*asterisk_count

        # If the length of the category name is odd, add an additional asterisk 
        # at the beginning of the display string
        if len(self.category) % 2 == 1:
            display = '*' + display

        # Loop through ledger and add each transaction to the display
        for transaction in self.ledger:
            # Add a new line
            display += '\n'
            # Get the description for the current transaction and
            # concatenate to 23 characters if too large
            display_description = transaction['description']
            if len(display_description) > 23:
                display_description = display_description[:23]

            # Add the description to the display
            display += display_description

            # Format the amount to a currency string
            display_amount = '{:.2f}'.format(transaction['amount'])
            
            # Add white space between the description and the amount
            display += ' '*(30 - len(display_description) - len(display_amount))

            # Add the amount to the display
            display += display_amount

        # Add new line after all transactions are added
        display += '\n'

        # Add the total balance to the display
        display += 'Total: '
        display += '{:.2f}'.format(self.balance)

        return display
        
def create_spend_chart(categories):
    pass

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print()
print(clothing)
print()
print(auto)

# print(create_spend_chart([food, clothing, auto]))

# Spend Chart

# Create categories list from objects
categories = [food, clothing, auto]

# Create empty category list variable and total withdrawls
categories_list = list()
total_withdrawals = 0

# Loop through each category and find the total amount withdrawn (exlcuding transfers)
for cat in categories:
    # Find withdrawal amount
    cat_withdrawls = 0

    # Loop through each transaction in the category object ledger
    for transaction in cat.get_ledger():
        # Check if transaction was negative, and add to total withdrawals
        # and individual category withdrawals (excluding transfers)
        if transaction['amount'] < 0 and transaction['description'][:12] != 'Transfer to ':
            total_withdrawals += abs(transaction['amount'])
            cat_withdrawls += abs(transaction['amount'])

    # Append the category name and withdrawal amount
    categories_list.append([cat.get_category(),cat_withdrawls])

# Convert the withdrawal amounts to percentages of total amount withdrawn
categories_percent = list()

for cat in categories_list:
    # Round to nearest 10
    cat_percentage = int(round(((cat[1] / total_withdrawals) * 10), 0)*10)
    categories_percent.append([cat[0],cat_percentage])


# categories_percent = [['Food',60], ['Clothing',20], ['Auto',10]]

# List comprehension for creating a list of descending percentages
percentages = [str(100 - i) for i in range(0,101,10)]

# Add percentages and bars to chart
for percentage in percentages:
    print(' '*(3 - len(percentage)), end='')
    print(percentage + '|', end='')
    for cat in categories_percent:
        if cat[1] >= int(percentage):
            print(' o ', end='')
        else:
            print('   ', end='')
    print()

# Add x axis to chart
print(' '*4 + '-'*(3*len(categories_percent) + 1))

# Add x axis labels
labels = categories_percent.copy()

# Find max length category
max_len = max([len(i[0]) for i in categories_percent])
# Add white space to shorter categories
for label in labels:
    label[0] = label[0] + ' '*(max_len - len(label[0]))

# Loop through each label and add to chart
for i in range(max_len):
    print('    ', end='')
    for label in labels:
        print(f' {label[0][i]} ', end='')
    print(' ')


