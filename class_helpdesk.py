#This class is for the Help Desk Support Staff
class helpdesk:
    def __init__(self, staff_id, staff_username, staff_email, staff_password):
        self.staff_id = staff_id
        self.staff_username = staff_username
        self.staff_password = staff_password
        self.staff_email = staff_email

# Instance's of three help desk support staff
helpdesk_staff = {
    "help_desk_user1": {"staff_id": "1111","staff_username": "help_desk_user1", "password": "password1", "staff_email": "help_desk_user1@mywhitecliffe.com"},
    "help_desk_user2": {"staff_id": "2222","staff_username": "help_desk_user2", "password": "password1", "staff_email": "help_desk_user2@mywhitecliffe.com"},
    "help_desk_user3": {"staff_id": "3333","staff_username": "help_desk_user3", "password": "password1", "staff_email": "help_desk_user3@mywhitecliffe.com"}
}
