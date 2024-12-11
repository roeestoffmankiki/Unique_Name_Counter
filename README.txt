Unique Name Counter

Overview
This project implements a Python program to count the number of unique individuals in a transaction based
on names provided in different contexts (billing address, shipping address, and cardholder name).
The program handles middle names, nicknames, and typos efficiently, ensuring modularity and accuracy.

Features:

Nickname Handling:
A custom-built nickname handler is used instead of a pre-made model to allow greater control and flexibility.
Supports multiple canonical names for a nickname, ensuring relationships are accurately captured.

Typo Handling:
A separate typo-handling module for clean modularity.
Implements a Damerau-Levenshtein Distance-based algorithm with a dynamic threshold to handle typos
proportionally to the length of the name.

Comparison Algorithm Flexibility:
The project uses a modular design, allowing for easy changes to the comparison algorithm.
A strategy pattern could be implemented in the future to dynamically switch between algorithms
based on the size of the dataset, accuracy needs, or complexity constraints.


Assumptions:

Minimum Name Requirements:
Every individual must have at least a first name and a last name.
The program raises an error if a required field is missing or invalid.

Cardholder Names:
Assumes that the cardholder name does not include a middle name.

Nickname Relationships:
If two nicknames share at least one common canonical name, they are treated as the same individual.

Typo Handling:
The typo handling uses Damerau-Levenshtein Distance to calculate the similarity between names.
A custom threshold (dynamic based on name length) determines if a typo is acceptable.

Middle Name Considerations:
Middle names are compared independently and treated as optional.
If middle names exist, they are matched either exactly or with typo tolerance.

Case Insensitivity:
All name comparisons are case-insensitive to ensure robust matching.

Special Characters:
Special characters and non-alphabetic symbols in names are stripped during normalization.

Dependencies
To install the required dependencies, run the following command:
pip install -r requirements.txt

Project Structure:

├── tests/                      # Directory containing test files
│   └── test_count_unique_names.py   # Unit tests for the countUniqueNames function
├── comparor.py                 # Handles name comparison logic
├── count_unique_names.py       # Contains the main countUniqueNames function
├── name_matcher.py             # Manages typo handling and similarity scoring
├── names.csv                   # CSV file containing nickname mappings
├── nickname_handler.py         # Handles nickname relationships and canonical mappings
├── person.py                   # Represents an individual and handles name normalization
├── requirements.txt            # Dependencies file
└── README.txt                  # Documentation for the project

to run unit tests:
1) Create a Virtual Environment
    python -m venv ${env_path}
    Replace ${env_path} with the path where you want to create the virtual environment.

2) Activate the Virtual Environment
    For Windows:
    ${env_path}\Scripts\activate

3) Navigate to the Root Project Directory Make sure you are in the directory
    containing the project files (Home_assignment/).

4) Install the Required Libraries Use the requirements.txt file to install dependencies:
    pip install -r requirements.txt

5) Run the Unit Tests Execute the following command to run the test suite:
    python -m unittest tests/test_count_unique_names.py





git config --global user.name "roeestoffmankiki"
git config --global user.email "roee.stoffman@mail.huji.ac.il"
