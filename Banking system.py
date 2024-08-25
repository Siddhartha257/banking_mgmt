import csv

# Parent class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        
    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Updated balance is:", self.balance)
        
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient amount | Balance Available:", self.balance)
        else:
            self.balance -= self.amount
            print("Updated balance is:", self.balance)
            
    def view_balance(self):
        self.show_details()
        print("Balance amount:", self.balance)
        
    def update_name(self, name):
        self.name = name
        
    def update_age(self, age):
        self.age = age
        
    def update_gender(self, gender):
        self.gender = gender
        
    def transfer(self, recipient, amount):
        self.amount = amount
        if self.amount < self.balance:
            self.balance -= self.amount
            recipient.balance += self.amount
            print(f"Transferred {amount} to {recipient.name}. Your new balance: {self.balance}")
        else:
            print("Insufficient balance")

# store account details to a CSV file
def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account Name", "Name", "Age", "Gender", "Balance"])
        for key, account in data.items():
            writer.writerow([key, account.name, account.age, account.gender, account.balance])

# Load account details from a CSV file
def load_from_csv(filename):
    data = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row['Account Name']
                account = Bank(row['Name'], int(row['Age']), row['Gender'])
                account.balance = float(row['Balance'])
                data[key] = account
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")
    return data

det = load_from_csv('accounts.csv') 

while True:
    print("\nSelect the service you need....")
    print("1. Create an account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View balance")
    print("6. View personal details")
    print("7. Update account details")
    print("8. Exit and save")

    ans = int(input("Enter your choice: "))

    if ans == 1:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")
        key = f"{name}_{age}"
        det[key] = Bank(name, age, gender)
        print("Account created successfully. Your account name is:", key)

    elif ans == 2:
        acc = input("Enter your account name: ")
        if acc in det:
            amount = int(input("Enter the amount to deposit: "))
            det[acc].deposit(amount)
        else:
            print("Account does not exist. Check the account name again.")

    elif ans == 3:
        acc = input("Enter your account name: ")
        if acc in det:
            amount = int(input("Enter the amount to withdraw: "))
            det[acc].withdraw(amount)
        else:
            print("Account does not exist. Check the account name again.")

    elif ans == 4:
        acc = input("Enter your account name: ")
        if acc in det:
            recp = input("Enter the recipient's account name: ")
            if recp in det:
                amount = int(input("Enter the amount to transfer: "))
                det[acc].transfer(det[recp], amount)
            else:
                print("Invalid recipient account name.")
        else:
            print("Invalid account name.")

    elif ans == 5:
        acc = input("Enter your account name: ")
        if acc in det:
            det[acc].view_balance()
        else:
            print("Invalid account name.")

    elif ans == 6:
        acc = input("Enter your account name: ")
        if acc in det:
            det[acc].show_details()
        else:
            print("Invalid account name.")

    elif ans == 7:
        acc = input("Enter your account name: ")

        if acc in det:
            name = input("Enter the name to update, or enter 'NO' to skip: ")
            if name.lower() != 'no': 
                det[acc].update_name(name)

            age = input("Enter the age to update, or enter 'NO' to skip: ")
            if age.lower() != 'no':
                det[acc].update_age(int(age))

            new_acc = f"{det[acc].name}_{det[acc].age}"
            if new_acc != acc:
                det[new_acc] = det.pop(acc)  
                print("Account updated. Your new account name is:", new_acc)

            det[new_acc].show_details()
        else:
            print("Invalid account name.")

    elif ans == 8:
        break
    else:
        print("Please select a valid service number.")

    save_to_csv('accounts.csv', det) 
