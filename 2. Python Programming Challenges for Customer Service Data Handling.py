#Task 1: Customer Service Ticket Tracker

def open_ticket(tickets):
    while True:
        ticket = input("Enter Ticket ID (type 'quit' to stop adding tickets): ")

        if ticket.lower() == "quit":
            break

        if ticket in tickets:
            print("A ticket with the same ID already exists")

        customer = input("Enter customer name: ")
        issue = input("Enter the issue you're experiencing: ")
        status = input("Enter status: ").lower()

        tickets[ticket] = {"Customer": customer, "Issue": issue, "Status": status}
        print("Ticket has been opened")

def update_status(tickets, new_status):
    ticket = input("Enter ticket ID status you'd like to update")
    if ticket in tickets:
        tickets[ticket]["Status"] = new_status
        print(f"Status of {ticket} has been updated to {new_status}")
    else:
        print("The ticket was not found")



def display_tickets(tickets, filter_status=None):
    if filter_status is not None:
        filtered_tickets = {ticket_id: ticket_info for ticket_id, ticket_info in tickets.items() if ticket_info["Status"] == filter_status}
        for ticket_id, ticket_info in filtered_tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
    else:
        for ticket_id, ticket_info in tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}") 



service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


open_ticket(service_tickets)
update_status(service_tickets, "closed")
#Displays all tickets
display_tickets(service_tickets)
#Sorts tickets by status and displays them
display_tickets(service_tickets, filter_status="open")


