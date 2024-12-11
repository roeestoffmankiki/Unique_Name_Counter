import re  # For removing non-alphabetic characters

REGEX_PATTERN = r"[^a-zA-Z ]"

LAST_NAME_ERROR = "Last name must contain at least one alphabetic character."

FIRST_NAME_ERROR = "First name must contain at least one alphabetic character."


class Person:
    def __init__(self, first_name: str, last_name: str):
        """
        Initialize a Person object.
        Splits the first_name into first and middle names if applicable.

        Args:
            first_name (str): First name of the person, which may include middle names.
            last_name (str): Last name of the person.
        """
        # Use an external method to split first name into first and middle names
        self.first_name, self.middle_name = self.split_first_and_middle_names(first_name)
        self.last_name = self.normalize_name(last_name)


        # Validates the names are not empty
        if not self.first_name:
            raise ValueError(FIRST_NAME_ERROR)
        if not self.last_name:
            raise ValueError(LAST_NAME_ERROR)

    def split_first_and_middle_names(self, name:str):
        """
        Splits a name into first and middle names.
        Args:
            name (str): The combined first name and middle names.
        Returns:
            tuple: (first_name, middle_name)
        """
        parts = name.strip().split()
        first_name = self.normalize_name(parts[0] if parts else "")
        middle_name = {self.normalize_name(middle) for middle in parts[1:]} if len(parts) > 1 else set()
        return first_name, middle_name

    def normalize_name(self, name:str):
        """
        Normalize a name by converting to lowercase, stripping whitespace,
        and removing non-alphabetic characters.
        Args:
            name (str): Name to normalize.
        Returns:
            str: Normalized name.
        """
        if not name:
            return ""
        # Remove non-alphabetic characters and convert to lowercase
        name = re.sub(REGEX_PATTERN, "", name)
        return name.lower()

    def inverse_person_name(self):
        return Person(self.last_name, self.first_name)

    @staticmethod
    def person_create_full_name(full_name):
        """
        Static method to create a Person object from a full name.
        Args:
            full_name (str): The full name of the person.
        Returns:
            Person: A new Person object.
        """
        parts = full_name.strip().split()
        if len(parts) < 2:  # Ensure there are at least two parts (first and last name)
            raise ValueError("Bill name on card must include at least a first and last name.")

        last_name = parts[-1]  # Extract the last name
        first_name = " ".join(parts[:-1])  # Everything before the last name is treated as first and middle names

        return Person(first_name, last_name)

    def get_first_name(self): return self.first_name
    def get_middle_name(self): return self.middle_name
    def get_last_name(self): return self.last_name





