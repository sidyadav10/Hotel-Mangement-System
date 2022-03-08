from hotel_management_system import *

def main():
    a = Hotelmanage()

    while True:
        print("1. Enter customer data : ")
        print("2. Calculte room rent :")
        print("3. Calculate food purchase :")
        print("4. Show total cost :")
        print("5. Exit")

        try:
            b = int(input("Enter your choice : "))
            if b == 1:
                a.input_data()
            elif b == 2:
                a.roomrent()
            elif b == 3:
                a.foodpurchase() 
            elif b == 4:
                a.display() 
            elif b == 5:
                break
        except:
            print("Invalid entry plz enter valid...")            
    print("Thank you visit again.....")

main()                      