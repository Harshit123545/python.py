def book_train_ticket(num_tickets):
    base_ticket_price = 100  # Assuming a base ticket price of $100

    if num_tickets>=6:
        print("max of 6 tickets can be booked at a time")
        return

    total_price = base_ticket_price * num_tickets

    # Apply discount based on the number of tickets
    if num_tickets == 2:
        discount = 0.03  # 3% discount for 1 ticket
        discounted_price = total_price - (total_price * discount)
        print(f"Congratulations! You've got a 3% discount. Total price: {discounted_price:.2f}")
    elif num_tickets == 3:
        discount = 0.05 # 5% discount for 3 tickets
        discounted_price = total_price - (total_price * discount)
        print(f"Congratulations! You've got a 5 % discount. Total price: {discounted_price:.2f}")
    elif num_tickets >=4:
         discount =  0.06
         discounted_price = total_price - (total_price * discount)
         print(f"Congratulations! You've got a 6 % discount. Total price: {discounted_price:.2f}")     
    else:
        print(f"Total price without discount:{total_price:.2f}")

# Get the number of tickets from the user
try:
    num_tickets = int(input("Enter the number of train tickets to book: "))
    book_train_ticket(num_tickets)
except ValueError:
    print("Please enter a valid number.")
