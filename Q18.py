class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def Account_balance(self):
        return self.__balance

    def deposit(self,money):
        if money > 0 :
            self.__balance += money
            print(f"{money} is added succesfully to ur bank account!")
        else:
            print(f"you can deposite only.")

    def withdraw(self,money):
        if money>self.__balance:
            print(f"insufficient balance.")
        else:
            self.__balance-=money
            print(f"{money} is withdrawed from ur balance.")

account = BankAccount(1000)

print(account.Account_balance())

account.withdraw(233)

print(account.Account_balance())

account.deposit(3453)

print(account.Account_balance())