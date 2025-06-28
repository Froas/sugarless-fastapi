import random
from typing import List
def individual_serial(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "sugar": product["sugar"],
        "type": product["type"],
        "calories": product["calories"],
        "category": product["category"],
        "macros": product["macros"]
    }

def individual_serial_without_id(product) -> dict:
    return {
        "name": product["name"],
        "sugar": product["sugar"],
        "type": product["type"],
        "calories": product["calories"],
        "category": product["category"],
        "macros": product["macros"]
    }

def list_serial(products) -> list:
    return[individual_serial(product) for product in products]

def random_serial(products: List[dict]) -> dict:
    rand = random.randrange(0, len(products))
    return individual_serial_without_id(products[rand])