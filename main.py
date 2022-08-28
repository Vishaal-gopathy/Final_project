from getpass import getpass
from programmes import Adminfunctions,Userfunctions
class AdminActions(Adminfunctions):
    def execute(self,option):
        if option==1:
            print('►'*7,"Add Food",'◄'*7)
            Adminfunctions.addfood(self)
        if option==2:
            print('►'*7,"Edit Food",'◄'*7)
            Adminfunctions.editfood(self)
        if option==3:
            print('►'*7,"View Menu",'◄'*7)
            Adminfunctions.viewfood(self)
        if option==4:
            print('►'*7,"Remove Food",'◄'*7)
            Adminfunctions.removefood(self)

class UserActions(Userfunctions):
    def execute(self,choice):
        if choice=='a':
            print('►'*7,'Register Yourself','◄'*7)
            Userfunctions.register(self)
        if choice=='b':
            print('►'*7,'Log in','◄'*7)
            Userfunctions.login(self)
        if choice==1:
            print('►'*7,'Place New Order','◄'*7)
            Userfunctions.placeneworder(self)
        if choice==2:
            Userfunctions.orderhistory(self)
        if choice==3:
            print('►'*7,'Update Profile','◄'*7)
            Userfunctions.updateprofile(self)

if __name__=='__main__':
    NameOfAdmin='admin'
    Password='123'
    adminact=AdminActions()
    useract=UserActions()
    while True:
        print("VISHAAL'S CAFE ")
        print('≈'*45)
        print("CHOICES:\n\n1.Admin\t\t2.Customer")
        print('≈'*45)
        choice=int(input("Enter your choice :"))
        if choice==1:
            name=input('Enter Admin name :').lower().strip()
            key=getpass('Enter Password : ')
            while name==NameOfAdmin and key==Password:
                print('≈'*45)
                print(' Welcome Admin ')
                print('\n1.Add fooditem\n2.Edit Fooditem\n3.View Menu\n4.Remove Fooditem\n5.Exit Admin Portal')
                print('≈'*45)
                option=int(input("Enter your option :"))
                if option==5:
                    print('You are exiting Admin portal')
                    print('≈'*45)
                    break
                adminact.execute(option)
        elif choice==2:
            print('≈'*45)
            print("A==>Register\n\nB==>Log in")
            print('≈'*45)
            key=input("Enter your choice :").lower()
            if key=='a':
                useract.execute('a')
            elif key=='b':
                name=input("Enter your Full Name :")
                P_word=input("Enter your password :")
                for user in Userfunctions.Customerlist:
                    if user.Fullname==name and user.Password==P_word:
                        print(' Welcome {name}' )
                        break
                else:
                    print('invalid credentials')
                for user in Userfunctions.Customerlist:
                    while user.Fullname==name and user.Password==P_word:
                        print('≈'*45)
                        print('1.Place new Order\n2.View Order History\n3.Update Profile\n4.Exit User portal')
                        print('≈'*45)
                        option=int(input('Enter your choice :'))
                        if option==4:
                            print("You are exiting User portal\n")
                            break 
                        useract.execute(option)