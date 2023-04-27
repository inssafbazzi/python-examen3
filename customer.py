#inssaf bazzi
class customer:
   
    nb_customers = 0

    def __init__(self, Name, preName, age, adress, phone):
        self.Name = Name
        self.preName = preName
        self.age = age
        self.adress = adress
        self.phone = phone
        self.id = customer.nb_customers
        customer.nb_customers += 1

    def set_Name(self, Name):
        self.Name = Name

    def get_Name(self):
        return self.Name

    def set_preName(self, preName):
        self.preName = preName

    def get_preName(self):
        return self.preName

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_adress(self, adress):
        self.adress = adress

    def get_adress(self):
        return self.adress

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone