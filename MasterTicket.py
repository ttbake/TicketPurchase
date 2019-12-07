TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100


def calculate_price(num_of_tickets):
    return num_of_tickets * TICKET_PRICE + SERVICE_CHARGE


while tickets_remaining > 0:
    print("There are {} tickets remaining.".format(tickets_remaining))
    user_name = input("What is your name?    ")
    number_of_tickets = input("How many tickets would you like, {}?    ".format(user_name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again.    ".format(err))
        continue
    total_price = calculate_price(number_of_tickets)
    print("The total price of your {} tickets is {}.".format(number_of_tickets, total_price))
    proceed = input("Would you like to purchase the tickets? Y/N    ")
    if proceed.upper() == "Y":
        # TODO: Gather credit card information and process it.
        print("SOLD!")
        tickets_remaining -= number_of_tickets
    else:
        print("Thank you anyways, {}.".format(user_name))

print("Tickets have been sold out!")
