from enum import Enum

class Tags(str, Enum):
    sugarless = "sugarless" 
    keto = "keto"
    glutenFree = "gluten-free"
    vegan = "vegan"
    organic = "organic"

class CategoryType(str, Enum):
    daily = "daily"
    snack = "snack"
    drink = "drink"
    food = "food"
    poultry = "poultry"
    fish = "fish"
    meat = "meat"
    vegetable = "vegetable"
    nut = "nut"
    oil = "oil"
    vegetarian = "vegetarian"
    seafood = "seafood"
    condiment = "condiment"
    fat = "fat"