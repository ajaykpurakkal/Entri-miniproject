
details=[("ajay","1234",500),("aghil","2345",1000),("sherin","3456",2000),("Abhijith","4567","1500"),("athul","5678",2500)]

class Banking:
    def __init__(self,username,password,balance=0):
        self.username=username
        self.password=password
        self.__balance=balance
    def deposit(self,amount):
        self.amount=amount
        if self.amount>=0:
            self.__balance+=self.amount
            print("Current Balance: ",self.__balance)
        else:
            print("Invalid amount.Enter a valid amount")
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>=0:
            if self.amount<=self.__balance:
                self.__balance -= self.amount
                print("Current Balance: ",self.__balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid amount.Enter a valid amount")


accounts=[]
for account in details:
    username,password,balance=account
    accounts.append(Banking(username,password,float(balance)))

def main():
    print("Welcome to Ajay's Bank")

    while True:
        print("select one option")
        print("1:LogIn")
        print("2:Exit")
        try:
            choice=int(input("Enter your choice: "))

            if choice==1:
                username=input('Username: ')
                password=input("Password: ")
                for account in accounts:
                    if account.username==username and account.password==password:
                        transaction(account)
                        break
                else:
                    print("Incorrect credentials")
            elif choice==2:
                print("Thank you for Banking")
                break

            else:
                print("Invalid option. Choose either 1 or 2.")
        except ValueError:
            print("Enter a numer as option")

def transaction(account):
    print("LogIn successful")
    while True:
        print("Select one option")
        print("1:Deposit")
        print("2:Withdraw")
        print("3:logOut")
        try:

            choice=int(input("Enter your choice: "))
            if choice==1:
                amount=float(input("Enter the amount: "))
                account.deposit(amount)
            elif choice==2:
                amount=float(input("Enter the amount: "))
                account.withdraw(amount)
            elif choice==3:
                print("logged Out")
                break
            else:
                print("Invalid option. select 1,2 or 3")
        except ValueError:
            print("Invalid option.Enter a number as option")
if __name__ == "__main__":
    main()
