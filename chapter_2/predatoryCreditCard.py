from creditCard import CreditCard

class predatoryCreditCard(CreditCard):
    """An extension to the creditCard class, that compounds interest and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.
        The initial balance is zero.

        Customer    the name of the customer (e.g, 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the account identifier (e.g., '3452 6342 4623 2463')
        limit       credit limit (measured in dollers)
        apr         annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """


        super().__init__(customer, bank, acnt, limit)
        self._apr = apr



    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.


        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """

        success = super().charge(price)
        if not success:
            self._balance += 5
        return success


    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


# A little change never mind
