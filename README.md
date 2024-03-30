# Louvre Museum Software Application

This repository contains the implementation of a software application for the Louvre Museum. The application is designed to manage artworks, exhibitions, visitors, and ticketing operations.

## Files

- **Artwork.py**: Defines the `Artwork` class representing artworks in the museum's collection.
- **Exhibition.py**: Defines the `Exhibition` class representing exhibitions in the museum.
- **PermanentExhibition.py**: Defines the `PermanentExhibition` class representing permanent exhibitions.
- **TemporaryExhibition.py**: Defines the `TemporaryExhibition` class representing temporary exhibitions.
- **Visitor.py**: Defines the `Visitor` class representing visitors to the museum.
- **Ticket.py**: Defines the `Ticket` class representing tickets for events or exhibitions.
- **Event.py**: Defines the `Event` class representing events in the museum.
- **Duration.py**: Defines the `Duration` class representing the duration of events or exhibitions.
- **VisitorCategory.py**: Defines the `VisitorCategory` class representing visitor categories.

## Test Cases

- **test_cases.py**: Contains unit test cases to validate the functionality of the implemented classes.
  
## Progress

### Step 1: Initial Setup
- Created separate files for each class based on the UML class diagram.
- Implemented class attributes and constructors.

### Step 2: Class Relationships
- Established relationships between classes as per the UML diagram.
- Implemented inheritance where necessary.
  
### Step 3: Documentation and Standards
- Added detailed documentation to each class and method following Python docstring conventions.
- Ensured adherence to PEP 8 coding standards for naming and formatting.
  
### Step 4: Test Cases
- Created test cases to validate the functionality of the implemented classes.
- Covered scenarios such as adding artwork, opening exhibitions, purchasing tickets, and displaying receipts.
  
## Usage

To use the classes in your project, simply import them into your Python scripts:

```python
from Artwork import Artwork
from Exhibition import Exhibition, PermanentExhibition, TemporaryExhibition
# Import other classes as needed
