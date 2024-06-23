class Customer:
    def __init__(self, name, address, premium):
        self.name = name
        self.address = address
        self.premium = premium
    def print_name(self):
        print(self.name)

myobj = Customer("John", "123 Street Rd", True)
myobj.print_name()


