from Duration import Duration

class Event:
    """
    Represents an event in the museum.
    """

    def __init__(self, name, duration, location):
        """
        Initializes an Event object with provided attributes.

        Args:
            name (str): The name of the event.
            duration (Duration): The duration of the event.
            location (str): The location of the event.
        """
        self.name = name
        self.duration = duration
        self.location = location
