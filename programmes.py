from allvariables import Adminvariables,Uservariables

class Adminfunctions:

    Menu=[]
    Foodid=101
    def addfood(self):
        FoodID=self.Foodid
        self.Foodid+=1
        print("Food ID =",FoodID)
        Name=input('Enter Food name :')
        Quantity=int(input('Quantity :'))
        Price=float(input('Price :Rs.'))
        Discount=int(input('Discount :'))
        Stock=int(input('Stock :'))
        food_obj=Adminvariables(FoodID,Name,Quantity,Price,Discount,Stock)
        self.Menu.append(food_obj)
        
        print("Food item added succesfully !!\n")
        
        print('▒'*50)
    
    def editfood(self):
        FoodID=int(input("Enter ID of the food you want to edit :"))
        for food in self.Menu:
            if food.FoodID==FoodID:
                Name=input('Enter Food name :')
                Quantity=int(input('Quantity :'))
                Price=float(input('Price :Rs.'))
                Discount=int(input('Discount :'))
                Stock=int(input('Stock :'))

                food.set_Name(Name)
                food.set_Quantity(Quantity)
                food.set_Price(Price)
                food.set_Discount(Discount)
                food.set_Stock(Stock)

                print('Food item edited sucessfully!!!\n')
                print('edited food item :',food)
                break
        else:
            print("Invalid ID")
        print('▒'*50)

    def viewfood(self):
        print("MENU")
        for food in Adminfunctions.Menu:
            print(food)
        print("End of Menu")
        print('▒'*50)

    def removefood(self):
        FoodId=int(input("Enter ID of the food you want to delete :"))
        for food in self.Menu:
            if food.FoodID==FoodId:
                print('Item removed successfully!!')
                self.Menu.remove(food)
                break
        else:
            print('Invalid ID')

        print('▒'*50) 

class Userfunctions:
    Customerlist=[]
    Orderslist=[]

    def register(self):
        Fullname=input("Enter your Full Name :")
        Phonenumber=int(input("Enter your Phonenumber :"))
        Email=input("Enter your mail :")
        Address=input("Enter your Address :")
        Password=input("Enter your password :")
        customer_obj=Uservariables(Fullname,Phonenumber,Email,Address,Password)
        self.Customerlist.append(customer_obj)
        print('Your account has been registered succesfully!!\n')
    
              
                    
    def placeneworder(self):
        Adminfunctions.viewfood(self) 

        order=input("Enter the IDs of the food you want to order with comma in between :")
        order=order.split(',')
        order[:]=[int(i) for i in order]
        print(order)
        IDlist=[i.FoodID for i in Adminfunctions.Menu]
        if(all(x in IDlist for x in order)):
            for i in order:
                for food in Adminfunctions.Menu:
                    if food.FoodID==i and food.Stock==0:
                        print(f'Sorry,{food.FoodID}.{food.Name}is out of stock.')
                        break
                    elif food.FoodID==i and food.Stock>0:
                        print(food)
                        print('1.Place the order\n2.Edit the Order\n') 
                        choice=int(input("Enter your response :"))     
                        if choice==1:
                            Fullname=input("Enter your Name to confirm the order :")
                            Password=input("Enter password to place the order :")
                            for user in self.Customerlist:
                                if user.Fullname==Fullname and user.Password==Password:
                                    self.Orderslist.append([Fullname,order])
                                    food.Stock-=1
                                    print("order Placed successfully!!")
                                    break
                            else:
                                print('Invalid Credentials')
                        elif choice==2:
                            self.placeneworder()
        else:
            print('Id you entered is not in Menu')        
        
    def orderhistory(self):
        Fullname=input("Enter your Name to view your order history :")
        print('►'*7,'Order History','◄'*7)
        namelist=[i[0] for i in self.Orderslist]
        if Fullname in namelist:
            for term in self.Orderslist:
                if term[0]==Fullname:
                    print(term[1])
        else:
            print('No orders in given name')
        
    def updateprofile(self):
        name=input("Enter your Full Name :")
        P_word=input("Enter your password :")
        for user in self.Customerlist:
            if user.Fullname==name and user.Password==P_word:
                Phonenumber=int(input("Enter your new Phonenumber :"))
                Email=input("Enter your new  mail :")
                Address=input("Enter your new Address :")
                Password=input("Enter your new password :")

                user.set_Phonenumber(Phonenumber)
                user.set_Email(Email)
                user.set_Address(Address)
                user.set_Password(Password)
                print('Profile updated Successfully')
                break
        else:
            print('Invalid Credentials')