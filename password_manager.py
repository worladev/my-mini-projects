
class PasswordManager():
    old_passwords = []

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
    

pwd = PasswordManager()
pwd.set_password("kofi123")
print(pwd.old_passwords)

pwd.set_password("joHN@5")
print(pwd.old_passwords)

print(pwd.set_password("kofi123"))
print(pwd.old_passwords)

print(pwd.get_password())

print(pwd.is_correct("joHN@5"))
print(pwd.is_correct("kofi123"))