from rapidfuzz import process, fuzz

import textdistance

# Constants
MATCH_NAME = 0
SIMILARITY_SCORE = 1
TYPO_FRACTION = 0.3

def names_match_typo(name1, name2):
    """
    Checks if two single-word names are close enough based on Damerau-Levenshtein distance.
    Args:
        name1 (str): First name.
        name2 (str): Second name.
    Returns:
        bool: True if names are close enough, False otherwise.
    """

    if not name1 and not name2: return True

    # Calculate Damerau-Levenshtein distance
    distance = textdistance.damerau_levenshtein(name1, name2)

    # Check if distance is within the threshold
    return distance <= get_threshold(name1, name2)


def get_threshold(name1, name2):
    """
    Calculates the dynamic typo tolerance threshold based on the average length of two names.
    The threshold is a fraction of the average length, ensuring longer names tolerate more typos.

    Args:
        name1 (str): First name to calculate the threshold for.
        name2 (str): Second name to calculate the threshold for.

    Returns:
        int: The dynamic typo tolerance threshold.
    """
    # Clean and get the lengths of both names
    name1_len = len(name1.strip())
    name2_len = len(name2.strip())

    # Calculate the threshold using the average length
    average_length = (name1_len + name2_len) // 2
    threshold = max(1, int(average_length * TYPO_FRACTION))

    return threshold

def find_closest_name(target_name:str, name_list):
    """
    Finds the closest name to the target name from a list using RapidFuzz's process.extractOne.
    Args:
        target_name (str): The target name to compare.
        name_list (set): A list of names to search.
    Returns:
        str: The closest name to the target name if within the typo tolerance threshold;
         otherwise, the target name itself.
    """
    result = process.extractOne(target_name, name_list)
    if not result: return target_name

    # Extract the best match
    result = result[MATCH_NAME]

    # Verify that the closest name matches within the typo tolerance
    if not names_match_typo(result, target_name):
        return target_name

    return result


# def damerau_levenshtein_scorer(a:str, b:str) -> float :
#     """
#     Converts the Damerau-Levenshtein distance into a similarity score.
#     Args:
#         a (str): First string.
#         b (str): Second string.
#     Returns:
#         float: Similarity score (0.0 to 100.0).
#     """
#     max_len = max(len(a), len(b))
#     if max_len == 0:
#         return 100.0  # Both strings are empty, consider them identical.
#
#     # Calculate normalized similarity score
#     distance = textdistance.damerau_levenshtein(a, b)
#     similarity = 100.0 * (1 - distance / max_len)
#     return similarity

