class BankAccount:
  def __init__(self, account_number, pin, balance=0.0):
      self.account_number = account_number
      self.pin = pin
      self.balance = balance

  def check_balance(self):
      return self.balance

  def deposit(self, amount):
      if amount > 0:
          self.balance += amount
          print("Deposit successful. New balance:", self.balance)
      else:
          print("Invalid deposit amount.")

  def withdraw(self, amount):
      if amount > 0:
          if self.balance >= amount:
              self.balance -= amount
              print("Withdrawal successful. New balance:", self.balance)
          else:
              print("Insufficient funds.")
      else:
          print("Invalid withdrawal amount.")


class BankSystem:
  def __init__(self):
      self.accounts = {}

  def create_account(self, account_number, pin):
      if account_number in self.accounts:
          print("Account number already exists. Please choose a different account number.")
      else:
          account = BankAccount(account_number, pin)
          self.accounts[account_number] = account
          print("Account created successfully.")

  def authenticate(self, account_number, pin):
      if account_number in self.accounts:
          account = self.accounts[account_number]
          if account.pin == pin:
              print("Authentication successful.")
              return account
          else:
              print("Invalid PIN.")
      print("Invalid account number.")
      return None


# Example usage
bank = BankSystem()

# Create accounts
bank.create_account(12345, 1111)
bank.create_account(67890, 2222)

# Authenticate and perform transactions
account = bank.authenticate(12345, 1111)
if account:
  print("Balance:", account.check_balance())

  account.deposit(900)
  account.withdraw(700)

account = bank.authenticate(67890, 1234)  # Invalid PIN
if account:
  print("Balance:", account.check_balance())

account = bank.authenticate(99999, 2222)  # Invalid account number
if account:
  print("Balance:", account.check_balance()) 