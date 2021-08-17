"""
functions to fetch data from spoonacular
"""
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests

dotenv_path = join(dirname(__file__), "tweepy.env")
load_dotenv(dotenv_path)
# spoonacular API access key here, check README for more info
spoonacular_key = os.getenv("SPOONACULAR_API")


def get_recipe(food_list):
    """turns recipe data"""
    rand = random.randint(0, 6)
    url = (
        "https://api.spoonacular.com/recipes/complexSearch?"
        f"query={food_list[rand]}&apiKey={spoonacular_key}"
    )
    response = requests.get(url)
    json_body = response.json()
    # randomly pick 1 of 10 results
    rand2 = random.randint(0, 9)
    # getting the recipe ID of a found food.
    rid = json_body["results"][rand2]["id"]
    url = f"https://api.spoonacular.com/recipes/{rid}/information?apiKey={spoonacular_key}"
    response = requests.get(url)
    json_body = response.json()

    return json_body


def get_ingredients(spoon_response):
    """get a list of ingredients"""
    ingredients = []

    for i in range(len(spoon_response["extendedIngredients"])):
        ingredients.append(spoon_response["extendedIngredients"][i]["original"])

    return ingredients
