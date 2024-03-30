class Duration:
    """
    Represents the duration of an event or exhibition.
    """

    def __init__(self, start_date, end_date):
        """
        Initializes a Duration object with provided attributes.

        Args:
            start_date (str): The start date of the duration.
            end_date (str): The end date of the duration.
        """
        self.start_date = start_date
        self.end_date = end_date
