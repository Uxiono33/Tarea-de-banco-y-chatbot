from bank import Bank_acount
true_pin = 1234
pin= int(input("Enter your pin to access the acount please:"))
amount=0
acount1=Bank_acount(amount)
while pin == true_pin:
    
    
    comand=int(input("Please enter 1 if you want to deposit money, enter 2 if you want to withdraw money, enter 3 to see the balance of your account, please type anything else to exit:"))
    
    if comand==1:
        deposit =int(input("You have chosen to deposit money, please enter the amount you want to deposit"))
        acount1.deposit(deposit)
        
        
    if comand==2:
        withdraw=int(input('You have chosen to withdraw money, please enter the amount you want to withdraw form the account'))
        acount1.withdraw(withdraw)
        
        
    if comand==3:
        print("You have chosen to see the balance of the account,the current amount on your acount is",),acount1.get_balance()
    if comand!=1 and comand !=2 and comand!=3:
        break


else: print("Incorrect pin")