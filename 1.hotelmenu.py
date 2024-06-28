# Welcome to Sandar resturant
# coke: Rs.50    
# momo: Rs.250   
# chowmin: Rs.150
# Enter your first item you want to order= momo
# Order of momo has been added.
# do you want to order anything else? (Yes/NO)yes
# Enter item for second order= coke
# Ordered item coke has been added.
# do you want to order anything else? (Yes/NO)no
# The total amount of items to pay is 250

menu= {
    "COKE": 50,
    "BUFF MOMO": 150,
    "HALF BUFF MOMO": 150/2,
    "VEG MOMO": 120,
    "HALF VEG MOMO": 120/2,
    "BUFF CHOWMIN": 150,
    "HALF BUFF CHOWMIN": 150/2,
    "VEG CHOWMIN": 120,
    "HALF VEG CHOWMIN": 120/2
}

# Greeting
print("Welcome, to the Sandar resturant")

# showing menu
for key, value in menu.items(): #items() method le key ra value loop ma access garxa
    print(f"{key}: Rs{value:.2f}")

order_total= 0
while True:
    a= input("Do you want to order something(Yes/No): ").lower()
    if a not in ["yes","no"]:
        print("please input valid input")
        continue
    if a == "yes":
        item_1= input("Enter first item for order: ").strip().upper()
        if item_1 in menu:
            order_total += menu[item_1] #menu vitra ko item user le order gareko price addd gareko
                                        #i.e suppose item1= coke then order_price= 0+50 = 50
            print(f"Ordered item {item_1} has been added.")
        else:
            print(f"Ordered item {item_1} is not available")
    else:
        print("thanks for visiting")
        exit()

    user_takes_order = True

    # for another item
    while user_takes_order:  #jaba samma user le order lerakhxa taba samma you loop chalerakhxa
        another_item = input("Do you want to order anything more(Yes/No): ").lower()
        if another_item == "yes":
            item_2= input("Enter another item for order: ").strip().upper()
            if item_2 in menu:
                order_total += menu[item_2]
                print(f"Ordered item {item_2} has been added.")
            else:
                print(f"Ordered item {item_2} is not available")
        else:
            print("Thanks for ordering.")
            break
        
    print(f"The total amount of items  to pay is ", order_total)


