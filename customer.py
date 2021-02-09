class Customer:

    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
    def update_membership(self, new_membership_type):
        self.new_membership_type=new_membership_type

c= [Customer('James', 'bronze'), Customer('Greg', 'gold')]
c[0].update_membership('Silva')
print(c[0].new_membership_type)


