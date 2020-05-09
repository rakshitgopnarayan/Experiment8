from random import *

record={"A":[11111111111,1111111111,'1111'],
        "B":[22222222222,2222222222,'2222'],
        "C":[33333333333,3333333333,'3333'],
	      "D":[44444444444,4444444444,'4444'],
        "E":[55555555555,5555555555,'5555']}

class Atm:
    def _init_(self,name,acc_no,mobileno,pin):
        self.acc_no=acc_no
        self.pin=pin
        self.balance= randint(0,10000)
        self.name=name
        self.mobileno=mobileno

    
    def pin_authentication(self):
        userpin = input("Enter PIN: ")
        count=1
        flag=0
        while(userpin != self.pin):
            print("PIN INCORRECT")
            userpin = input("Enter PIN: ")
            count=count+1
            if(count == 3 and userpin != self.pin ):
                print("ACCOUNT BLOCKED")
                flag=1
                break

        if flag == 0:
            print("User Authenticated")
        return flag
    
    def account_info(self):
        print(f"Name: {self.name}\nAccount Number: {self.acc_no}\nMobile no.: {self.mobileno}\nBalance(in Rs): {self.balance}\nPIN:{self.pin}")
    def pin_change(self):
        print("Old Pin details")
        new_pin=self.pin
        confirm_new_pin=0
        temp=self.pin_authentication()
        if (temp==0):
            while(new_pin != confirm_new_pin):
                while True:
                    try:
                        new_pin=int(input("Enter new 4-digit pin: "))
                    except:
                        print("Invalid input")
                        continue
                    else:
                        break
                while True:
                    try:
                        confirm_new_pin=int(input("Re-enter new 4-digit pin: "))
                    except:
                        print("Invalid input")
                        continue
                    else:
                        break
                
                   
                if(new_pin == confirm_new_pin):
                    record[self.name][2]= str(new_pin)
                    print("PIN successfully changed!")
                    break
                else:
                    print("PIN did not match!")
        
        return temp,new_pin
        

    def balance_inquiry(self):
        print(f"Your Account balance in Rs is {self.balance}")
    
    def withdrawal(self):
        while True:
            try:
                w_amount=int(input("Enter the amount to be withdrawn in Rs: "))
            except:
                print("Invalid input")
                continue
            else:
                break
        if (w_amount >  self.balance):
            print("Funds unavailable! ")
        elif(w_amount<500):
            print("Minimum withdrawal limit is Rs 500\nWithdrawal Denied!")
        elif (self.balance- w_amount <500):
            print("Minium balance should be Rs.500\nWithdrawal Denied!")
        else:
            self.balance=self.balance-w_amount
            print("Withdrawal Successful\nNew Balance-")
            self.balance_inquiry()
        

    def deposit(self):
        while True:
            try:
                d_amount=int(input("Enter amount to be deposited in Rs: "))
            except:
                print("Invalid input")
                continue
            else:
                break
        if(d_amount<100):
            print("Minimum amount for deposition is Rs.500\nDeposition Denied!")
        else:
            self.balance=self.balance+d_amount
            print("Deposition Successful!\nNew Balance-")
            self.balance_inquiry()

        

def start(Atm):
    option=0
    while True:
            try:
                name=input("Enter your name: ").capitalize()
            except:
                print("User Not Found!")
                continue
            else:
                break
    
    obj=Atm(name,record[name][0],record[name][1],record[name][2])
    user=obj.pin_authentication()
    if user==0:
        op_dict={1:"Account Information",2:"Pin Change",3:"Balance Inquiry",4:"Withdrawal",5:"Deposit",6:"Exit"}
        while(option != 6):
            for i in op_dict:
                print("{:<3}-{:<15}".format(i,op_dict[i]))
   
            option=int(input())

            if(option==1):
                obj.account_info()
            elif(option==2):
                check,new=obj.pin_change()
                if(check==1):
                    break 
                database[name][2]=new
                obj=Atm(name,record[name][0],record[name][1],record[name][2])
            elif(option==3):
                obj.balance_inquiry()
            elif(option==4):
                obj.withdrawal()
            elif(option==5):
                obj.deposit()
            elif(option==6):
                break


start(Atm)
