#inssaf bazzi

class Statistiquescustomers:

def __init__(self, liste_customers):
    self.liste_customers = liste_customers

def get_nombre_total_customers(self):
    return len(self.liste_customers)

def get_age_moyen_customers(self):
    total_age = 0
    for customer in self.liste_customers:
        total_age += customer.age
    return round(total_age / len(self.liste_customers), 1)

def get_amount_total_purchases_customers(self):
    amounts = {}
    for customer in self.liste_customers:
        amounts[customer.id] = round(100 * (customer.id + 1), 2)
    return amounts