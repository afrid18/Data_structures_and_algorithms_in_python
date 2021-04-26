class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.

        The initial balance is zero.

        customer -> the name of the customer(e.g 'John Bowman')
        bank -> the name of the bank (e.g, 'California Savings')
        acnt -> the account identifier (e.g, '2353 3452 3453 3463')
        limit -> credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer"""
        return self._customer


    def get_bank(self):
        """Return the bank's name"""
        return self._bank

    def get_account(self):
        """Return the card identifying nuber (Typically stored as a string)"""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """
        charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

"""if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '2345 4563 2345 2456', 2500))
    wallet.append(CreditCard('John Bowman', "california Federal", '2353 7634 9876 4567', 3500))
    wallet.append(CreditCard('John Bowman', "california Finance", '2353 7564 9876 4567', 5000))


    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print()

"""


