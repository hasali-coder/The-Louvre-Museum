class Artwork:
    """
    Represents an artwork in the museum's collection.
    """

    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        """
        Initializes an Artwork object with provided attributes.

        Args:
            title (str): The title of the artwork.
            artist (str): The artist of the artwork.
            date_of_creation (str): The date of creation of the artwork.
            historical_significance (str): The historical significance of the artwork.
            exhibition_location (str): The exhibition location of the artwork.
        """
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.exhibition_location = exhibition_location
