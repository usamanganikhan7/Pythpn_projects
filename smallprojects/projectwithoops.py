class Atm:

  def __init__(self):

    self.__pin = ""
    self.__balance = 0

    self.__menu()

  def get_pin(self):
    return self.__pin  

  
  def set__pin(self, new_pin):

    self.__pin = new_pin

    print("pin changed")

    

  def __menu(self):
    
    user_input = input("""  

    1. enter 1 to creat your pin
    2. enter 2 to creat deposit your money
    3. enter 3 to creat withdraw your money
    4. enter 4 to creat check balance
    5. enter 5 to exit

""")  


    if user_input == "1":

      self.create_pin()

    elif user_input == "2":
      self.deposit()

    elif user_input == "3":
      self.withdraw()

    elif user_input == "4":
      self.check_balance()

    else:
      print("bye")
    self.__menu()

  def create_pin(self):

    self.__pin = int(input("enter your pin "))

    print("pin set successfully ")


  def deposit(self):

    print("enter your pin")

    temp = int(input("enter your pin"))

    if temp == self.__pin:

      amount = int(input("enter your amount to deposit in your account"))
      self.__balance = amount + self.__balance
      print("deposit success")

    else:
      print("invalid pin")  
    
    self.__menu()

  def withdraw(self):

    pin = int(input("enter your pin "))
    if pin == self.__pin:

      witthd_amount = int(input("enter your amount "))

      self.__balance = self.__balance - witthd_amount

      print("withdraw successfull")

    else:
      print("invalid pin")    

    self.__menu()

  def check_balance(self):

    pin = int(input("enter your pin "))
    if pin == self.__pin:

      your_bal = self.__balance

      print(your_bal)

    else:
      print("invalid pin")    

  



sbi = Atm()

print(sbi.get_pin)