class Bank_acount:
   
   def __init__(self,acount_number):
      self.acount_number = acount_number
      
   def deposit(self,Deposit):
      self.Deposit=Deposit
      self.acount_number += Deposit
   def withdraw(self,withdraw_amount):
      self.withdraw_amount=withdraw_amount
      if withdraw_amount> self.acount_number:
        print("Insuficient amount for the transaction")
      else:self.acount_number-=withdraw_amount
   def get_balance(self):
      print(self.acount_number)






    
      
      
