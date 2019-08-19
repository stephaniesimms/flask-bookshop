"""Pricing calculator for bookstore."""

def get_total_cost(price, num_copies):
    """Calculate total cost, including tax.
    
        >>> get_total_cost(10, 3)
        33.0

    If you buy 5 of more books, you get a 5% discount: 

        >>> get_total_cost(10, 6)
        62.7
    """

    subtotal = price * num_copies

    # apply volume discount
    if num_copies >= 5:
        subtotal = subtotal * 0.95

    taxed_total = subtotal * 1.10

    return taxed_total


def format_usd(price):
    """Return a price, formatted in US dollars.
    
        >>> format_usd(10)
        '$10.00'

        >>> format_usd(10.222)
        '$10.22'
    """

    return "${:,.2f}".format(price)