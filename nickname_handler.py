from collections import defaultdict

class NicknameHandler:
    def __init__(self, csv_path):
        """
        Initializes the NicknameHandler by loading and parsing the CSV file.
        Args:
            csv_path (str): Path to the nicknames CSV file.
        """
        self.canonical_to_nicknames = defaultdict(set)
        self.nickname_to_canonical = defaultdict(set)
        self.load_csv(csv_path)

    def load_csv(self, csv_path:str):
        """
        Loads the nicknames from a CSV file and creates bidirectional mappings.
        Args:
            csv_path (str): Path to the nicknames CSV file.
        """
        with open(csv_path, 'r') as file:
            for line in file:

                # Skip blank or comment lines
                if not line.strip() or line.startswith('#'):
                    continue

                # Split and clean names
                names = [name.strip().lower() for name in line.strip().split(',') if name.strip()]
                if not names:
                    continue  # Skip if the line results in no valid names

                canonical = names[0]  # First name as canonical
                nicknames = names[1:]

                # Map nicknames to canonical and vise versa
                for nickname in nicknames:
                    self.canonical_to_nicknames[canonical].add(nickname)
                    self.nickname_to_canonical[nickname].add(canonical)


    def get_canonical_name(self, name):
        """
        Returns the canonical name(s) for a given name (or the name itself if not found).
        Args:
            name (str): Name to be converted to its canonical form.
        Returns:
            set: Set of canonical names, or an empty set if no canonical mapping exists.
        """
        name = name.strip().lower()
        return self.nickname_to_canonical.get(name, set())

    def get_all_nicknames(self, canonical):
        """
        Returns all nicknames for a given canonical name.
        Args:
            canonical (str): Canonical name.
        Returns:
            set: Set of nicknames for the canonical name.
        """
        canonical = canonical.strip().lower()
        return self.canonical_to_nicknames.get(canonical, set())


    def are_related(self, name1, name2):
        """
        Checks if two names are related. A relationship exists if:
        - They are the same name (canonical or nickname).
        - They share a common canonical name.

        Args:
            name1 (str): The first name to check (canonical or nickname).
            name2 (str): The second name to check (canonical or nickname).

        Returns:
            bool: True if the names are related, False otherwise.
        """
        name1 = name1.strip().lower()
        name2 = name2.strip().lower()

        if name1 == name2: return True # not needed but good for readability

        # Checks if they are nicknames of one another
        if name1 in self.canonical_to_nicknames[name2] or name2 in self.canonical_to_nicknames[name1]:
            return True

        # Get canonical names for both names
        group1 = self.nickname_to_canonical[name1]
        group2 = self.nickname_to_canonical[name2]

        # Check if they share any common canonical name
        return not group1.isdisjoint(group2)

    def get_all_names(self):
        """
        Returns a set of all unique names (canonical and nicknames).
        Combines the keys of both canonical_to_nicknames and nickname_to_canonical.

        Returns:
            set: A set of all unique names.
        """
        # Merge the keys of both dictionaries to get all unique names
        return set(self.canonical_to_nicknames.keys()).union(self.nickname_to_canonical.keys())






