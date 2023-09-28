class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def display_info(self):
        print(f" First name: {self.first_name}")
        print(f" Last name: {self.last_name}")
        print(f" Email: {self.email}")
        return self
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_acc_info()
        return self

    


class BankAccount:
    all_bank_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_bank_accounts.append(self)

    @classmethod
    def print_all(cls):
        for accounts in cls.all_bank_accounts:
            accounts.display_acc_info()


    def deposit(self, amount):
        self.balance += amount
        print(f"You have successfully deposited ${amount}")
        return self
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount}")
            return self
        else: 
            print("Insufficient funds to withdraw. Charging $5 overdraft fee")
            self.balance-= 5
            return self
        
    def display_acc_info(self):
        print(f"Your current balance is: ${self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
            return self
        else:
            return self
            
user1 = User("Leader", "Tyler", "TheLeader6969@yahoo.com")
user1.display_info().display_user_balance().make_deposit(500).make_withdraw(200).display_user_balance()


print("-"*20)
user2 = User("Michael", "Santagata", "Micktheman2624@hotmail.com")
user2.display_info().display_user_balance().make_deposit(100).make_withdraw(200).display_user_balance()
print("-"*20)


user3 = User("Gorlock", "TheDestroyer", "GorlockTheDestroyer@outlook.com")
user3.display_info().display_user_balance().make_deposit(5000).make_withdraw(600).display_user_balance()
print("-"*20)