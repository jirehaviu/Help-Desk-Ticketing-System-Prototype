"""
Help-Desk Support Ticketing Software Prototype
Author: Jireh Tearea
ID:20230851
 
"""
import shutil
from class_ticket import Ticket
from class_helpdesk import helpdesk_staff
from class_admin import admin_staff
 
# This function aligns all texts to the center when running the terminal by importing the shutil module within python library
def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    return ' ' * padding + text

# These two functions will authenticate, if the user or admin is running this software to implement access control
def authenticate_help_desk_staff(username, password):
    if username in helpdesk_staff and helpdesk_staff[username]["password"] == password:
        return True
    else:
        return False

def authenticate_it_dept_staff(username, password):
    if username in admin_staff and admin_staff[username]["password"] == password:
        return True
    else:
        return False

def main():
    # Login selection screen
    print("\n")
    print(center_text("||          LOGIN          ||"))
    print("\n")
    
    while True:
        print("\n")
        print(center_text("Hi There, Select Your Department?"))
        print(center_text("1 - Help Desk Department"))
        print(center_text("2 - IT Department"))
        print(center_text("3 - Neither"))
        option = int(input(center_text("Input your option: ")))

        if option == 1: # Help-Desk Login screen, help desk user must input their username and password for vaildation 
            print("\n")
            print(center_text("||          Help Desk Login          ||"))
            print("\n")
            print(center_text("Please input your Username and Password"))
            username = input(center_text("Username: "))
            password = input(center_text("Password: "))

            if authenticate_help_desk_staff(username, password):
                print("\n")
                
                while True:
                    # Help Desk option selection screen
                    print(center_text(f"||          Welcome, {username}         ||\n"))
                    print(center_text("1 - Create Ticket"))
                    print(center_text("2 - View Tickets"))
                    print(center_text("3 - Respond to Ticket"))
                    print(center_text("4 - Logout"))
                    help_desk_option = int(input(center_text("Input your option: ")))
                    if help_desk_option == 1:
                        # This option allows the help desk staff to create a new internal support ticket 
                        print("\n")
                        print("||         Create A New Ticket         ||")
                        print("Please provide the following ticket information")
                        staff_id = input("Staff ID: ")
                        staff_username = input("Staff Username: ")
                        staff_email = input("Staff Email Address: ")
                        ticket_description = input("Description of the issue: ")
                        ticket = Ticket(staff_id,staff_username,staff_email,ticket_description,"Open")
                        print("Ticket Submitted Successfully")
                        print(f"Your Ticket ID Number is {ticket.ticket_id}")
                    elif help_desk_option == 2:
                        # This option generates all internal support tickets
                        print("\n")
                        print("||          Ticket Information         ||")
                        print("\n")
                        for ticket in Ticket.open_tickets + Ticket.closed_tickets:
                            ticket.display_ticket_info()
                    elif help_desk_option == 3:
                        # This option allows the help desk support staff to issue a response
                        print("\n")
                        ticket_token = int(input(center_text("Enter Ticket ID Number: ")))
                        for ticket in Ticket.open_tickets:
                            if ticket.ticket_id == ticket_token:
                                reply = input(center_text("Enter Reply: "))
                                ticket.provide_feedback(reply)
                                break
                        else:
                            # Error message, incorrect ticket id number
                            print("\n")
                            print(center_text("Invalid Ticket ID"))
                    elif help_desk_option == 4:
                        break
                    else:
                        # Error Message, incorrect option selection
                        print("\n")
                        print(center_text("Invalid option. Please try again."))

            else:
                # Error message, incorrect username or password
                print("\n") 
                print(center_text("Invalid username or password. Please try again."))

        elif option == 2: # IT Department Login screen, admin staff must input their username and password for vaildation
            print("\n")
            print(center_text("||         IT Department Login          ||"))
            print("\n")
            username = input(center_text("Username: "))
            password = input(center_text("Password: "))

            if authenticate_it_dept_staff(username, password):
                print("\n")
                while True:
                    # IT Department option selection screen
                    print(center_text(f"||          Welcome, {username}!          ||"))
                    print(center_text("1 - View Tickets"))
                    print(center_text("2 - Resolve Ticket"))
                    print(center_text("3 - Change Admin Password"))
                    print(center_text("4 - Ticket Statistics"))
                    print(center_text("5 - Reopen Ticket"))
                    print(center_text("6 - Logout"))
                    it_dept_option = int(input(center_text("Input your option: ")))

                    if it_dept_option == 1:
                        # This option previews, brief information on all tickets for the IT Department to solve or have already been solved
                        print("\n")
                        Ticket.print_tickets()
                    elif it_dept_option == 2:
                        # This option allows the IT Department to resolve any tickets that have been summitted from the help desk staff
                        print("\n")
                        ticket_id = int(input("Enter Ticket ID Number: "))
                        for ticket in Ticket.open_tickets:
                            if ticket.ticket_id == ticket_id:
                                reply = input("Enter Reply: ")
                                new_password = ticket.process_ticket_feedback(reply)
                                if new_password:
                                      print(f"New password generated: {new_password}")
                                break
                        else:
                            print("Invalid Ticket Token")
                    elif it_dept_option == 3:
                        # This option allows the admin to manually change their password or another admin staff member
                        print("||          Admin Password Change*          ||")
                        admin_username = input("Enter Admin Username: ")
                        new_password = input("Enter new password: ")
                        if admin_username in admin_staff:
                            admin_staff[admin_username]["password"] = new_password
                        else:
                            print(f"No IT Department staff found with the ID {admin_username}.")
                    elif it_dept_option == 4:
                        # This option displays all current ticket stats that have been created
                        print("\n")
                        print("||          Ticket Statistics*          ||")
                        Ticket.show_statistics()
                    elif it_dept_option == 5:
                        # This option allows admin to reopen a certain
                        print("\n")
                        ticket_id = int(input("Enter Ticket ID Number: "))
                        for ticket in Ticket.closed_tickets:
                            if ticket.ticket_id == ticket_id:
                                ticket.reopen_ticket()
                                print(f"Ticket {ticket_id} has been reopened.")
                                break
                        else:
                            print("Invalid Ticket ID")
                    elif it_dept_option == 6:
                        break
                    else:
                        # Error Message, incorrect option selection
                        print("\n")
                        print(center_text("Invalid option. Please try again."))

            else:
                # Error message, incorrect username or password
                print("\n")
                print(center_text("Invalid username or password. Please try again."))

        elif option == 3:
            print("\n")
            print(center_text("Closing Software"))
            break
        else:
            # Error Message, incorrect option selection
            print("\n")
            print(center_text("Invalid option. Please try again."))

if __name__ == "__main__":
    main()
