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

'''
# Write your code here:
class Invoice:
    """
    Invoice class to manage invoices.
    Its constructor will take an invoice number, customer name, and the amount of money they owed.
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




# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
