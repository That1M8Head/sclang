# Ticketing System
# An example of hypothetical SCLang code, but translated to Python

from time import sleep as delay

def welcome_message():
    print("Welcome to the Ticketing System!")

def check_ticket(ticket_id: int, ticket_owner: str):
    print(f"Ticket #{ticket_id} owned by {ticket_owner}")
    print("Please wait while we verify this ticket exists.")
    delay(5)
    print("Thank you!")
    return True

def print_ticket(ticket_id: int, ticket_owner: str):
    if not check_ticket(ticket_id, ticket_owner):
        print("Sorry, this ticket is invalid.")
        return
    ticket_display = [
        f"Ticket #{ticket_id} owned by {ticket_owner}",
        "-------------------------------------------",
        "Adult Ticket                         £10.00",
        "                                           ",
        "-------------------------------------------",
        "Authorised                                 ",
    ]
    print('\n'.join(ticket_display))

if __name__ == "__main__":
    welcome_message()
    print_ticket(123, "John Doe")
