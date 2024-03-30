class Visitor:
    """
    Represents a visitor to the museum.
    """

    def __init__(self, name, age, ID):
        """
        Initializes a Visitor object with provided attributes.

        Args:
            name (str): The name of the visitor.
            age (int): The age of the visitor.
            ID (str): The ID of the visitor.
        """
        self.name = name
        self.age = age
        self.ID = ID
        self.ticket = None
