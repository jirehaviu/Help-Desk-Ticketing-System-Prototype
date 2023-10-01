from class_helpdesk import helpdesk_staff

class Ticket:
    counter = 1 # Counter when a ticket is created
    open_tickets = [] 
    closed_tickets = []

    def __init__(self, staff_id, staff_username, staff_email,ticket_description, ticket_status, ticket_response ="Not Yet Provided"):
        self.ticket_id = Ticket.counter + 2000
        Ticket.counter += 1
        self.staff_id = staff_id
        self.staff_username = staff_username
        self.staff_email = staff_email
        self.ticket_description = ticket_description
        self.ticket_status = ticket_status
        self.ticket_response = ticket_response

        if ticket_status == "Open":
            Ticket.open_tickets.append(self)
        elif ticket_status == "Closed":
            Ticket.closed_tickets.append(self)

        # These parameters retrieves varibles from the class_ticket.py file
        self.staff_info = helpdesk_staff.get(staff_id) or helpdesk_staff.get(staff_username)

        if self.staff_info:
            self.staff_id = self.staff_info.get("staff_id")
            self.staff_username = self.staff_info.get("staff_username")
            self.staff_email = self.staff_info.get("staff_email")

    # This method allows the IT Department to resolve or generate a new password that is associated with a ticket
    def process_ticket_feedback(self, feedback):
        if "password change" in self.ticket_description.lower():
            self.ticket_response = feedback
            self.ticket_status = "Closed"
            new_password = self.staff_id[:2] + self.staff_username[:3]
            self.ticket_response = f"New password generated: {new_password}"
            Ticket.open_tickets.remove(self)
            Ticket.closed_tickets.append(self)
            print("Password changed and ticket closed!")
            return new_password
        else:
            self.ticket_response = feedback
            self.ticket_status = "Closed"
            Ticket.open_tickets.remove(self)
            Ticket.closed_tickets.append(self)

    # This method displays all tickets created
    def display_ticket_info(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Username: {self.staff_username}")
        print(f"Staff Email Address: {self.staff_email}")
        print(f"Description Of Issue: {self.ticket_description}")
        if self.ticket_response != "Not Yet Provided":
            print(f"Response: {self.ticket_response}")
        print(f"Ticket Status: {self.ticket_status}\n")

    # This method alters the ticket status from being open to closed and the ticket counter
    def close_ticket(self):
        if self.ticket_status == "Open":
            self.ticket_status = "Closed"
            Ticket.open_tickets.remove(self)
            Ticket.closed_tickets.append(self)
        else:
            print("Ticket is already closed.")

    # This method alters the ticket status and reopens a closed ticket
    def reopen_ticket(self):
        if self.ticket_status == "Closed":
            self.ticket_status = "Open"
            Ticket.closed_tickets.remove(self)
            Ticket.open_tickets.append(self)
        else:
            print("Ticket is not closed.")

    @staticmethod
    # Ticket statistics of whats currently summited,completed and open
    def show_statistics():
        print(f"Number of Tickets Submitted: {len(Ticket.open_tickets) + len(Ticket.closed_tickets)}")
        print(f"Number of Tickets Completed: {len(Ticket.closed_tickets)}")
        print(f"Number of Tickets Open: {len(Ticket.open_tickets)}")

    @staticmethod
    def print_tickets():
        for ticket in Ticket.open_tickets + Ticket.closed_tickets:
            print(f"Ticket ID: {ticket.ticket_id}")
            print(f"Status: {ticket.ticket_status}")
            print(f"Description: {ticket.ticket_description}\n")

# Instances of three created tickets
ticket2001 = Ticket("1111", "help_desk_user1", "help_desk_user1@mywhitecliffe.com", "Network connection failure", "Open")
ticket2002 = Ticket("2222", "help_desk_user2", "help_desk_user2@mywhitecliffe.com", "Hardware component faulty", "Closed")
ticket2003 = Ticket("3333", "help_desk_user3", "help_desk_user3@mywhitecliffe.com", "CRM software is unresponsive", "Open")


