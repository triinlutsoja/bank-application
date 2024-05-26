def get_transaction_amount(sum):
  while True:
    try:
      sum = abs(float(input("Please enter the transaction amount: ")))
      return sum
      break
    except ValueError:
      print("Invalid input. Please enter a decimal number without words or currency symbols!")

print("Welcome to the Bank of Estonia!\nWhat would you like to do today? Please enter the number of the desired action.")
print("1. Deposit money")
print("2. Withdraw money")
print("3. Check balance")
print("4. Exit")

balance = 0
deposits_today = 0
withdrawals_today = 0
action = None
transaction_amount = 0


while True:
  while True:
    try:
      action = int(input("Please enter the number of the desired action: "))
      if action not in [1, 2, 3, 4]:
        print("Please enter an integer number between 1 and 4!")
        continue
      break
    except ValueError:
      print("Please enter an integer number between 1 and 4!")
  if action == 1:  # Deposit
    print("You chose to deposit money to your account.")
    transaction_amount = get_transaction_amount(transaction_amount)
    balance += transaction_amount
    deposits_today += transaction_amount
    print(f"Deposit successful! {transaction_amount:.2f} € has been deposited to your account.")
  elif action == 2:  # Withdrawal
    print("You chose to withdraw money from your account.")
    transaction_amount = get_transaction_amount(transaction_amount)
    if transaction_amount <= balance:
      balance -= transaction_amount
      withdrawals_today += transaction_amount
      print(f"Withdrawal successful! {transaction_amount:.2f} € has been withdrawed from your account.")
    else:
      print(f"Withdrawal declined. You don't have enough money in your accoutn to withdraw {transaction_amount:.2f} €.")
  elif action == 3:  # Check balance
    print(f"You chose to check your balance. Your current balance is {balance:.2f} €.")
  elif action == 4:  # Exit
    print(f"You chose to exit. You've deposited {deposits_today:.2f} € and withdrawed {withdrawals_today:.2f} € today. Have a nice day!")
    break
