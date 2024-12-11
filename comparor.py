from name_matcher import names_match_typo, find_closest_name


class Comparor:
    """
            Initializes the Comparor with a nickname handler.
            Args:
                nickname_handler (NicknameHandler): Handler to resolve nickname relationships.
            """

    def __init__(self, nickname_handler):
        """
        Initializes the Comparor with a nickname handler.
        Args:
            nickname_handler (NicknameHandler): Handler to resolve nickname relationships.
        """
        self.nickname_handler = nickname_handler
        self.all_names = nickname_handler.get_all_names()

    def is_same_person(self, p1, p2) -> bool:
        """
        Determines if two Person objects represent the same individual by comparing
        their first, middle, and last names using typo-tolerant matching and nickname resolution.

        Args:
            p1 (Person): The first Person object.
            p2 (Person): The second Person object.

        Returns:
            bool: True if the Person objects represent the same individual, False otherwise.
        """

        # Checks last name
        if not names_match_typo(p1.get_last_name(), p2.get_last_name()): return False

        # Checks middle names
        m1, m2 = p1.get_middle_name(), p2.get_middle_name()
        if not self.check_middle_names(m1, m2): return False

        first1, first2 = p1.get_first_name(), p2.get_first_name()
        if self.check_first_names(first1, first2):
            return True
        return False

    def check_middle_names(self, group1: set[str], group2: set[str]) -> bool:
        """
         Compares two sets of middle names to determine if they are compatible. Compatibility
         is defined as either having no middle names or having at least one middle name that matches
         directly or with typo tolerance.

         Args:
             group1 (set[str]): Middle names of the first person.
             group2 (set[str]): Middle names of the second person.

         Returns:
             bool: True if the middle names are compatible, False otherwise.
         """
        if not group1 or not group2:
            return True
        for name1 in group1:
            for name2 in group2:
                if name1 == name2 or names_match_typo(name1, name2):
                    return True
        return False

    def check_first_names(self, first1: str, first2: str) -> bool:
        """
        Compares two first names to determine if they match directly, with typo tolerance,
        or through nickname relationships.

        Args:
            first1 (str): First name of the first person.
            first2 (str): First name of the second person.

        Returns:
            bool: True if the first names match or are related, False otherwise.
        """
        if names_match_typo(first1, first2):
            return True
        if first1 not in self.all_names:
            first1 = find_closest_name(first1, self.all_names)
        if first2 not in self.all_names:
            first2 = find_closest_name(first2, self.all_names)
        if self.nickname_handler.are_related(first1, first2):
            return True
        return False






