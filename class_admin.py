# This class is for the administration staff in the IT department
class admin:
    def __init__(self, admin_username, admin_password):
        self.admin_username = admin_username
        self.admin_password = admin_password

    # This method changes the password for admins ONLY. Help desk staff doesnt have copntroll access.
    def change_password(self, new_password):
        self.admin_password = new_password
        print(f"Password for {self.admin_username} has been changed successfully.")

# Instance's of three administration staff in the IT Department
admin_staff = {
    "admin1": {"password" : "password1"},
    "admin2": {"password" : "password2"},
    "admin3": {"password" : "password1"}
}
