
class PasswordManager():
        # there should be a default password
        # old_password should be encapsulated
    def __init__(self, password):
        self.old_passwords = [password]

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return new_password
        else:
            return "Password already used. Try a new one"
    
    def get_password(self):
        return self.old_passwords[-1]
    

    def is_correct(self, check_password):
        if check_password == self.get_password():
            return True
        else:
            return False
    
#Test Cases
pwd = PasswordManager("user124")
print(f"\nPassword History: {pwd.old_passwords}")

pwd.set_password("worLA@")
print(f"\nPassword History: {pwd.old_passwords}")

print(pwd.set_password("worLA@"))
print(f"\nPassword History: {pwd.old_passwords}")

pwd.set_password("worlako25")
print(f"\nPassword History: {pwd.old_passwords}")

print(pwd.get_password())

print(pwd.is_correct("user124"))