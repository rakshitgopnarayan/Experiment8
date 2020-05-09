class atm:
    def __init__(self,name):
        self.name=name
    def acc_info(self):
        print('Account Info: ')
        print('Name: ', name, end='\n')
        print('Account No.: ', info[name][0], end='\n')
        print('Mobile No.: ', info[name][1], end='\n')
    def pin_change(self):
        i=3
        while(i>0):
            p=int(input('Enter Original PIN: '))
            if p==info[name][2]:
                x=input('Enter New PIN: ')
                info[name][2]=x
                break
            else:
                i=i-1
                print('Incorrect PIN, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Maximum Tries Reached , Account Blocked!!!')
    def acc_balance(self):
        print('Account Balance: ',info[name][3])
    def withdraw(self):
        print('Account Balance: ',info[name][3])
        amt=float(input('Enter Amount To Withdraw: '))
        if amt<=info[name][3]:
            info[name][3]=info[name][3]-amt
            print('New Account Balance: ', info[name][3])
        else:
            print('Insufficient Balance in Account!')
    def deposit(self):
        amt=float(input('Enter Amount To Deposit: '))
        info[name][3]=info[name][3]+amt
        print('New Account Balance: ', info[name][3])
    
info={"user1":[11111111111,1111111111,1111,10000], 
      "user2":[22222222222,2222222222,2222,12000], 
      "user3":[33333333333,3333333333,3333,15000], 
      "user4":[44444444444,4444444444,4444,9000], 
      "user5":[55555555555,5555555555,5555,20000]}
k=info.keys()
while (1):
    name=str(input('Enter Name: '))
    if name in k:
        i=3
        while(i>0):
            pin=int(input('Enter PIN: '))
            if pin==info[name][2]:
                a=atm(name)
                while(1):
                    print('Enter 1 For Account Info')
                    print('Enter 2 For PIN Change')
                    print('Enter 3 For Balance Inquiry')
                    print('Enter 4 For Withdrawal')
                    print('Enter 5 For Deposit')
                    s=int(input('Select Operation: '))
                    if s==1:
                        a.acc_info()
                    elif s==2:
                        a.pin_change()
                    elif s==3:
                        a.acc_balance()
                    elif s==4:
                        a.withdraw()
                    elif s==5:
                        a.deposit()
                    else:
                        print('Invalid Option Selected! Choose Again')
                        continue
                    e=input('Enter E to exit, press any other key to continue operations: ')
                    if e=='y' or e=='Y':
                        print('Thank You!!!')
                        break
                    else:
                        continue
                break
            else:
                i=i-1
                print('Incorrect PIN, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')
        break
        

