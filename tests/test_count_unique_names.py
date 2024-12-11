import unittest
from count_unique_names import countUniqueNames

class TestCountUniqueNames(unittest.TestCase):
    def test_exact_match(self):
        """Test case where all names are exactly the same."""
        self.assertEqual(countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli"), 1)

    def test_nickname_match(self):
        """Test case where nicknames are used."""
        self.assertEqual(countUniqueNames("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli"), 1)

    def test_typo_in_last_name(self):
        """Test case with a typo in the last name."""
        self.assertEqual(countUniqueNames("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli"), 1)

    def test_middle_name_inclusion(self):
        """Test case with a middle name included."""
        self.assertEqual(countUniqueNames("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah"), 1)

    def test_different_individuals(self):
        """Test case with clearly different individuals."""
        self.assertEqual(countUniqueNames("Michele", "Egli", "Deborah", "Egli", "Michele Egli"), 2)

    def test_all_different_names(self):
        """Test case where all names are different."""
        self.assertEqual(countUniqueNames("Alice", "Smith", "Bob", "Johnson", "Charlie Brown"), 3)

    def test_typo_in_first_name(self):
        """Test case with a typo in the first name."""
        self.assertEqual(countUniqueNames("John", "Doe", "Jon", "Doe", "Johnny Doe"), 1)

    def test_case_insensitivity(self):
        """Test case to ensure matching is case-insensitive."""
        self.assertEqual(countUniqueNames("deborah", "egli", "Deborah", "Egli", "DEBORAH EGLI"), 1)

    def test_special_characters(self):
        """Test case with special characters in the names."""
        self.assertEqual(countUniqueNames("John*", "Doe", "John", "Doe", "John Doe"), 1)

    def test_empty_fields(self):
        """Test case with missing or empty fields."""
        with self.assertRaises(ValueError):
            countUniqueNames("", "Egli", "Deborah", "Egli", "Deborah Egli")

    def test_single_name_in_card(self):
        """Test case where the cardholder name contains only one name."""
        with self.assertRaises(ValueError):
            countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah")

    def test_middle_name_typo(self):
        """Test case with a typo in the middle name."""
        self.assertEqual(countUniqueNames("Deborah S", "Egli", "Deborah T", "Egli", "Deborah Egli"), 1)

    def test_closest_name_resolution(self):
        """Test case to ensure closest name is resolved correctly."""
        self.assertEqual(countUniqueNames("Jon", "Smith", "Johnny", "Smith", "John Smith"), 1)

    def test_edge_case_empty_list(self):
        """Test with empty list inputs for nicknames or CSV issues."""
        self.assertEqual(countUniqueNames("Jon", "Smith", "Mike", "Doe", "Alice Johnson"), 3)

    def test_p1_p2_p1p3_p2p3(self):
        """Test case where p1 != p2, but p1 = p3 and p2 = p3, resulting in 1 unique person. Ensures transitive."""
        self.assertEqual(
            countUniqueNames("Debbi", "Egli", "Debbie", "Egni", "Debbieaa Egni"),
            1
        )

    def test_provided_cases(self):
        """Test all the provided cases in the assignment."""
        self.assertEqual(countUniqueNames("Deborah", "Egli", "Deborah", "Egli", "Deborah Egli"), 1)
        self.assertEqual(countUniqueNames("Deborah", "Egli", "Debbie", "Egli", "Debbie Egli"), 1)
        self.assertEqual(countUniqueNames("Deborah", "Egni", "Deborah", "Egli", "Deborah Egli"), 1)
        self.assertEqual(countUniqueNames("Deborah S", "Egli", "Deborah", "Egli", "Egli Deborah"), 1)
        self.assertEqual(countUniqueNames("Michele", "Egli", "Deborah", "Egli", "Michele Egli"), 2)

    def test_multiple_nicknames_and_typos(self):
        """Test with multiple nicknames and typos across all fields."""
        self.assertEqual(
            countUniqueNames("Elizabeth", "Johnson", "Lizzy", "Johnsen", "Elisabeth Johnson"),
            1
        )

    def test_mismatched_middle_names(self):
        """Test case with mismatched middle names but matching first and last names."""
        self.assertEqual(
            countUniqueNames("John A", "Smith", "John B", "Smith", "John Smith"),
            1
        )

    def test_three_way_relationship(self):
        """Test where p1 != p2, but p1 = p3 and p2 = p3, resulting in 1 unique person."""
        self.assertEqual(
            countUniqueNames("Mike", "Johnson", "Michael", "Johnsen", "Mikey Johnson"),
            1
        )

    def test_multiple_middle_names(self):
        """Test case where middle names are long and varied but match."""
        self.assertEqual(
            countUniqueNames("Anna Maria", "Doe", "Anna M.", "Doe", "Anna Maria Doe"),
            2
        )

    def test_large_typo_tolerance(self):
        """Test case with extreme typos in the last name."""
        self.assertEqual(
            countUniqueNames("Robert", "Stevenson", "Robert", "Steevenson", "Bob Stevenson"),
            1
        )

    def test_all_fields_with_nicknames_and_typos(self):
        """Test case where all fields involve nicknames or typos."""
        self.assertEqual(
            countUniqueNames("Catherine", "Hernandez", "Cathy", "Hernandes", "Cathryn Hernandez"),
            2
        )

    def test_complex_name_relationships(self):
        """Test with multiple relationships and one unique individual."""
        self.assertEqual(
            countUniqueNames("Jonathan", "Doe", "Jon", "Doe", "Johnny Doe"),
            1
        )

    def test_edge_case_long_names(self):
        """Test case with excessively long names."""
        self.assertEqual(
            countUniqueNames(
                "Maximiliano Alexander",
                "Fernandez",
                "Max A.",
                "Fernandes",
                "Maximiliano Fernandez"
            ),
            1
        )


if __name__ == "__main__":
    unittest.main()