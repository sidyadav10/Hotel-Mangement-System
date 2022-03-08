# cutumer module
class Hotelmanage:
    def __init__(self,rt ='',s= 0,p=0,r=0,t=0,a=1000,name = '',address = "",cindate= "",coutdate = "",rno = 1):
        print(f"++++++++WELCOME TO DEEP VALLEY HOTEL+++++++++++")
        self.rt = rt
        self.r = r
        self.t =t
        self.p =p
        self.s =s 
        self.a =a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def input_data(self):
        self.name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.cindate = input("Enter cindate: ")
        self.coutdate = input("Enter your coutdate: ") 
        print(f"Your room number is {self.rno} ")

    def roomrent(self):
        print("We Have the following rooms for you")
        print("1.  Class A ---> 4000")
        print("2.  Class B ---> 3500")
        print("3.  Class C ---> 3000")
        print("4.  Class D ---> 2500")
        try:
            x = int(input("Enter the number to choose a class: "))
            y = int(input("For how many days you want to stay: "))
            if x == 1:
                print("You have choose class A")
                self.s = 4000 * y
            elif x == 2:
                print("You have choose class B")
                self.s = 3500 * y
            elif x == 3:
                print("You have choose class C")
                self.s = 3000 * y
            elif x == 4:
                print('You have choose class D')
                self.s = 2500 * y
            else:
                print("Choose a room plz")
            print(f"Your room rent is {self.s}")
        except:
            print("Invalid input plz enter number...")
    
    def foodpurchase(self):
        print("+++++++Resturant Menu++++++")
        print("1. Dessert ==>100","2. Drinks ==>50","3. Breakfast ==>90","4. Lunch ==>110","5. Dinner ==> 200","6. Exit")
        while True:
            try:
                f = int(input("Enter to order: "))
                if f == 1:
                    d = int(input("Enter the Qty: "))
                    self.r =self.r + 100 * d
                elif f == 2:
                    d = int(input("Enter the qty: "))
                    self.r =self.r + 50 * d
                elif f == 3:
                    d = int(input("Enter the qty: "))    
                    self.r = self.r + 90 * d
                elif f == 4:
                    d = int(input("Enter the qty: "))    
                    self.r = self.r + 110 * d
                elif f == 5:
                    d = int(input("Enter the qty: "))    
                    self.r = self.r +200 * d
                elif f == 6:
                    break
            except:
                print("Invalid entry plz enter valid entry....")
            print(f"Total food cost {self.r}")

    def display(self):
        print("++++ Hotel Bill ++++++")
        print("Customer Details : ")
        print(f"Customer name :{self.name}")
        print(f"Customer address :{self.address}")
        print(f"Customer check in date :s{self.cindate} ")
        print(f"Customer check out date :{self.coutdate}")
        print(f"Your room number :{self.rno}")
        print(f"Your room rent :{self.s} ")
        print(f"Your food bill :{self.r}")

        self.rt = self.s + self.t + self.p + self.r

        print(f"Your subtotal purchased is :{self.rt}")
        print(f"Additional service charge is :{self.a}")
        print(f"Your Grand total purchase is :{self.rt + self.a}")
        self.rno += 1


