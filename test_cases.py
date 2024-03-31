import unittest
from Visitor import Visitor
from Ticket import Ticket
from Event import Event
from VisitorCategory import VisitorCategory

class TestMuseum(unittest.TestCase):

    def test_purchase_ticket(self):
        # Create visitor
        visitor = Visitor("John Doe", 30, "123456789")
        visitor_category = VisitorCategory("Adult")
        
        # Create event
        event = Event("Concert", "2024-05-15", "Outdoor Stage")
        
        # Purchase ticket
        ticket = Ticket(63, event, visitor_category, "2024-05-10", "Outdoor Stage")

        # Output visitor details
        print("Visitor Details:")
        print("Name of the Visitor:", visitor.name)
        print("Age:", visitor.age)
        print("Emirates ID:", visitor.ID)
        print("Visitor Category:", visitor_category.category)

        # Output event details
        print("\nEvent Details:")
        print("Event Name:", event.name)
        print("Event Date:", event.date)

        # Calculate total bill including VAT
        total_bill = ticket.price * 1.05
        print("\nTotal Bill (Inc VAT 5%):", total_bill)

if __name__ == '__main__':
    unittest.main()
