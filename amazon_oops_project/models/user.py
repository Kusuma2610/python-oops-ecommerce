class User:
    def __init__(self,name,email):
        self.name=name
        self.__email=email
    def get_email(self):
        return self.__email
class PrimeUser(User):
    def __init__(self,name,email,membership):
        super().__init__(name,email)
        self.membership=membership
    def show_membership(self):
        print("prime membership:",self.membership)
        