from wsgiref.types import InputStream

from comparor import Comparor
from nickname_handler import NicknameHandler
from person import Person

CSV_PATH = r"names.csv"

INVALID_INPUT = "All fields should be filled"


def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    """
    Counts the number of unique names across billing, shipping, and cardholder names.

    Args:
        billFirstName (str): First name from the billing address.
        billLastName (str): Last name from the billing address.
        shipFirstName (str): First name from the shipping address.
        shipLastName (str): Last name from the shipping address.
        billNameOnCard (str): Full name as it appears on the credit card.

    Returns:
        int: The number of unique names.
    """

    if not billFirstName or not billLastName or not shipFirstName or not shipLastName or not billNameOnCard:
        raise ValueError(INVALID_INPUT)

    bill_person = Person(billFirstName, billLastName)
    ship_person = Person(shipFirstName, shipLastName)
    card_person = Person.person_create_full_name(billNameOnCard)
    inverted_card_person = card_person.inverse_person_name()


    nickname_handler = NicknameHandler(CSV_PATH)
    comparor = Comparor(nickname_handler)

    counter = 3

    p1p2 = comparor.is_same_person(bill_person, ship_person)
    p1p3 = (comparor.is_same_person(bill_person, card_person) or
            comparor.is_same_person(bill_person, inverted_card_person))
    p2p3 = (comparor.is_same_person(ship_person, card_person) or
            comparor.is_same_person(ship_person, inverted_card_person))

    if p1p2:
        counter -= 1
        if p1p3 or p2p3:
            counter -= 1
    else:
        if p1p3 or p2p3:
            counter -= 1
        if p1p3 and p2p3:
            counter -= 1

    return counter

