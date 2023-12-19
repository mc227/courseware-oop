'''

Let's create a class to manage invoices. Its constructor will take
an invoice number, the customer name, and the amount of money owed.

>>> invoice = Invoice(12, 'Mark Smith', 42.50)
>>> invoice.number
12
>>> invoice.customer
'Mark Smith'
>>> invoice.amount
42.5

And we'll keep track too of the total payments made. At first, this
will be zero.

>>> invoice.total_payments
0

Now, the customer may make payments in stages (rather than paying all
at once).  So let's create methods to add payments, check whether the
invoice is fully paid off, etc.

>>> invoice.add_payment(20)
>>> invoice.is_fully_paid()
False
>>> invoice.total_payments
20
>>> invoice.amount_due()
22.5

>>> invoice.add_payment(22.50)
>>> invoice.is_fully_paid()
True
>>> invoice.amount_due()
0.0

Sometimes, a customer will submit one large payment for several
invoices. And it may only partially cover one of them. Create a
CustomerAccount class to manage the nuances of this.

>>> customer_name = 'James Jones'
>>> account = CustomerAccount(customer_name)

Did you know Python class objects have a __name__ attribute?
>>> type(account).__name__
'CustomerAccount'
>>> account.name
'James Jones'

The add_invoice() method takes an instance of the Invoice class.

>>> account.add_invoice(Invoice(1, customer_name, 20.0))
>>> len(account.invoices)
1
>>> account.total_due()
20.0
>>> account.add_invoice(Invoice(2, customer_name, 25.0))
>>> len(account.invoices)
2
>>> account.total_due()
45.0
>>> account.add_invoice(Invoice(3, customer_name, 30.0))
>>> len(account.invoices)
3
>>> account.total_due()
75.0

>>> unpaid = account.unpaid_invoices()
>>> len(unpaid)
3
>>> type(unpaid[0]).__name__
'Invoice'
>>> unpaid[0].number
1
>>> unpaid[0].amount
20.0

>>> account.apply_payment(20)
>>> now_unpaid = account.unpaid_invoices()
>>> len(now_unpaid)
2
>>> now_unpaid[0].number
2
>>> account.total_due()
55.0

>>> account.apply_payment(10)
>>> account.total_due()
45.0
>>> len(account.unpaid_invoices())
2

>>> account.apply_payment(45)
>>> len(account.unpaid_invoices())
0

'''
# Write your code here:
class CustomerAccount:
    """
    Sometimes, a customer will submit one large 
    payment for several invoices. And it may 
    only partially cover one of them. Create 
    a CustomerAccount class to manage the 
    nuances of this.
    """
    def __init__(self, name):
        self.name = name
        self.invoices = []

    def add_invoice(self,invoice):
        """
        The add_invoice() method takes an instance of the Invoice class.
        """
        self.invoices.append(invoice)

    def total_due(self):
        """
        total due using list comprehension
        """
        return sum(invoice.amount_due() for invoice in self.invoices)

    def unpaid_invoices(self):
        """
        unpaid_invoices
        """
        items = []
        for invoice in self.invoices:
            if not invoice.is_fully_paid():
                items.append(invoice)
        return items

    def apply_payment(self, amount):
        """
        apply payment
        """
        for invoice in self.unpaid_invoices():
            due = invoice.amount_due()
            if due < amount:
                invoice.add_payment(due)
                amount -= due
            else:
                invoice.add_payment(amount)
                break
class Invoice:
    """
    Let's create a class to manage invoices. 
    Its constructor will take an invoice number, 
    the customer name, and the amount of money owed.
    """
    def __init__(self, number, customer, amount):
        """
        __init__
        """
        self.number = number
        self.customer = customer
        self.amount = amount
        self.total_payments = 0

    def add_payment(self,payment):
        """
        add_payment
        """
        self.total_payments += payment
    def is_fully_paid(self):
        """
        is fully paid?
        """
        return self.total_payments >= self.amount
    def amount_due(self):
        """
        amount due?
        """
        return self.amount - self.total_payments

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
