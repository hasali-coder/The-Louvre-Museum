from Duration import Duration

class Exhibition:
    """
    Represents an exhibition in the museum.
    """

    def __init__(self, name, duration, location):
        """
        Initializes an Exhibition object with provided attributes.

        Args:
            name (str): The name of the exhibition.
            duration (Duration): The duration of the exhibition.
            location (str): The location of the exhibition.
        """
        self.name = name
        self.duration = duration
        self.location = location
        self.artworks = []
