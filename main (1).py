#inssaf bazzi
# Python Standard Library 
import os 
import platform
import random
import shutil 

# Custom modules 

import customer
import Listecustomers
import Statistiquescustomers

class gérerInfoApp: 

    APP_NAME = "gérerInfoApp" 
   

    def __ini__ (self)

lc = Listecustomers()
lc.add_customer("inssaf", "bazzi", 23, "2 rue maurice ", "0155320011")
lc.add_customer("yan", "Mang", 27, "8 avenue des lila", "07553022")
lc.add_customer("noni", "tresor", 46, "10 av rein", "0755221144")


lc.modify_customer(2, "ani", "noula", 19, "8 avenue les roses", "065588444")

lc.delete_customer(1)

sc = Statistiquescustomers(lc.get_liste_customer())

nombre_total_clients = sc.get_nombre_total_customers()
print("Nombre total de clients : {nombre_total_clients}")

age_moyen_customers = sc.get_age_moyen_customers()
print("age moyen des clients : {age_moyen_customers}")

amount_total_purchases_customers = sc.get_amount_total_purchases_customers()
print("montant total des achats effectués par chaque client :")
for client_id, amounts in amount_total_purchases_customers.items():
print("Client {client_id} : {amounts}")

#pour quitéé app

    def quitter (self):  
        print ("merci pour utulise cette app")

