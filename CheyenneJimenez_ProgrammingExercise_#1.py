# Cinema Ticket Pre-Sale
TOTAL_TICKETS = 10
MAX_TICKETS_PER_BUYER = 4

# Each buyer may buy 1 to 4 tickets.

def get_ticket_request(tickets_left):
    "Ask user for a valid number of tickets."

    while True:
        try:
            tickets_requested = int(input('How many tickets would you like to buy?'))
            if tickets_requested < 1:
                print('Please enter at least 1 ticket.')
            elif tickets_requested > MAX_TICKETS_PER_BUYER:
                print('Each buyer can purchase up to 4 tickets.')
            elif tickets_requested > tickets_left:
                print(f'Only {tickets_left} ticket(s) are remaining')
            else:
                return tickets_requested
        except ValueError:
            print('Please enter a whole number.')


# This program sells up to 10 cinema tickets

def sell_tickets():
    "Sell tickets until all 10 tickets are sold."
    tickets_remaining = TOTAL_TICKETS
    total_buyers = 0

    print('Cinema Ticket Pre-Sale')
    print('There are 10 tickets available.')
    print('Each buyer can purchase up to 4 tickets.\n')

    while tickets_remaining > 0:
        print(f'Tickets left: {tickets_remaining}')
        tickets_requested = get_ticket_request(tickets_remaining)

        tickets_remaining -= tickets_requested # accumulator/update total remaining
        total_buyers += 1 # accumulator for buyers

        print(f'Purchased {tickets_requested} ticket(s). Tickets remaining: {tickets_remaining}\n')

    print('All tickets have been sold')
    print(f'Total number of ticket buyers: {total_buyers}')

sell_tickets()
