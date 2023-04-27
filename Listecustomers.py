#inssaf bazzi 

class Listecustomers:

    def __init__(self):
        self.liste = []

    def add_customer(self, Name, preName, age, adress, phone):
        customer = customer(Name, preName, age, adress, phone)
        self.liste.append(customer)

    def modify_customer(self, id, Name=None, preName=None, age=None, adress=None, phone=None):
        for customer in self.liste:
            if customer.id == id:
                if Name:
                    customer.set_Name(Name)
                if preName:
                    customer.set_preName(preName)
                if age:
                    customer.set_age(age)
                if adress:
                    customer.set_adresse(adress)
                if phone:
                    customer.set_telephone(phone)


       def delete_customer(self, id):
        for customer in self.liste:
            if customer.id == id:
                self.liste.remove(customer)
                return True
        return False

        def show_customer(self):
            for customer in self.liste:
                print(f"ID: {customer.id} | nom: {customer.nom} | Prénom: {customer.prenom} | age: {customer.age} | adresse: {customer.adresse} | téléphone: {customer.telephone}")

        def get_liste_customer(self):
            return self.liste