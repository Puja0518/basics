
class Bank:

    def __init__(self, name, account_no, address, contact, email, balance, created_date):
        self.name = name
        self.account_no = account_no
        self.address = address
        self.contact = contact
        self.email = email
        self.balance = balance
        self.created_date = created_date

    def credit_amount(self, crd_amt):
        self.balance = self.balance + crd_amt

    def debit_amount(self, deb_amt):
        self.balance = self.balance - deb_amt

    def change_addr(self, new_addr):
        self.address = new_addr

customer1 = Bank("Saurav", 345672000025, "Barkakana", 9944363890, "saurav.saini@gmail.com", 5000, "21-08-2021")
customer2 = Bank("Prachi", 436270002121, "Ramgarh", 9073103633, "prachi.saini@gmail.com", 3000, "20-06-2021")
customer3 = Bank("Ritul", 345672000025, "Ranchi", 7261051818, "ritul.saini@gmail.com", 8000, "05-08-2021")

print(customer3.balance)
customer3.credit_amount(4000)
print(customer3.balance)

print(customer1.balance)
customer1.debit_amount(500)
print(customer1.balance)

print(customer2.address)
customer2.change_addr("Ranchi")
print(customer2.address)

