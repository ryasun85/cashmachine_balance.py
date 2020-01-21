#input_pin = 1234

#if input_pin = True

balance = 5000
pin = 1234

def takes_input(pin,amount):
    
    if pin == 1234 and amount <= balance:
        print("you can get your money")
        print(balance - amount)

    elif pin !=1234:
        print("pin incorrect")
    elif amount > balance:
        print("you dont have enough funds")
    else:
        print("wait for your money")

takes_input(pin, 99)

   




# def amount_after_with(balance, amount):

#     amount_after_with(5000, 88)

#     return balance - amount

#     print("After withdrawal your balance is {}.".formt(amount_after_with()))

# amount_after_with()
