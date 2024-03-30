import unittest
from Artwork import Artwork
from Exhibition import Exhibition, PermanentExhibition, TemporaryExhibition
from Visitor import Visitor
from Ticket import Ticket
from Event import Event
from Duration import Duration
from VisitorCategory import VisitorCategory

class TestMuseum(unittest.TestCase):

    def test_add_artwork(self):
        artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503–1506", "Iconic portrait", "Permanent Gallery")
        self.assertEqual(artwork.title, "Mona Lisa")

    def test_open_exhibition(self):
        duration = Duration("2024-04-01", "2024-06-30")
        exhibition = TemporaryExhibition("Impressionist Art", duration, "Exhibition Hall")
        self.assertEqual(exhibition.name, "Impressionist Art")

    def test_purchase_ticket(self):
        event = Event("Concert", Duration("2024-05-15", "2024-05-15"), "Outdoor Stage")
        visitor_category = VisitorCategory("Adult")
        ticket = Ticket(100, event, visitor_category, "2024-05-10", "Outdoor Stage")
        self.assertEqual(ticket.price, 100)

    def test_display_receipt(self):
        visitor = Visitor("John Doe", 30, "123456789")
        event = Event("Concert", Duration("2024-05-15", "2024-05-15"), "Outdoor Stage")
        visitor_category = VisitorCategory("Adult")
        ticket = Ticket(100, event, visitor_category, "2024-05-10", "Outdoor Stage")
        visitor.ticket = ticket
        receipt = f"Name: {visitor.name}\nEvent: {ticket.event.name}\nPrice: {ticket.price}\nLocation: {ticket.location}"
        self.assertEqual(receipt, "Name: John Doe\nEvent: Concert\nPrice: 100\nLocation: Outdoor Stage")

if __name__ == '__main__':
    unittest.main()
