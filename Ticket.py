class Ticket:
    """
    Represents a ticket for an event or exhibition.
    """

    def __init__(self, price, event, visitor_category, purchased_on, location):
        """
        Initializes a Ticket object with provided attributes.

        Args:
            price (float): The price of the ticket.
            event (Event): The event associated with the ticket.
            visitor_category (VisitorCategory): The visitor category of the ticket.
            purchased_on (str): The date the ticket was purchased.
            location (str): The location of the ticket.
        """
        self.price = price
        self.event = event
        self.visitor_category = visitor_category
        self.purchased_on = purchased_on
        self.location = location
