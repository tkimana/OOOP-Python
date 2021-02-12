class User:
    def log(self):
        print(self)


class Customer(User):

    def log(self):
        print("I'm a customer")

    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
    def update_membership(self, new_membership_type):
        self.new_membership_type=new_membership_type


    # Create a property
    @property
    def name(self):
        return self._name


    # Setter
    @name.setter
    def name(self, name):
        self._name = name

   # To delete
    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        print('Print String')
        return self.name + " " + self.membership_type
    
    def print_all_customers(customers):
        for customer in c:
            print(customer)


# Check if the atributes are similar 
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:

          return True

        return False


c= [Customer('James', 'bronze'), Customer('Greg', 'gold')]
Customer.print_all_customers(c)
print(c[0].name)


