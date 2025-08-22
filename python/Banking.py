# Bank account with custom functions in classes

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance  
  
  def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

  def display_balance(self):
        return self.balance


acct = BankAccount("Jane", "Doe", 1234, "Checking", 4321, 100)

print(acct.deposit(96))
print(acct.withdraw(25))
print(acct.display_balance())
