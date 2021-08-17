"""
main app for project 1
"""
import os
import tweepy
import requests
import flask
from spoonacular_parser import get_recipe, get_ingredients
from twitter_parser import get_tweet

APP = flask.Flask(__name__)

@APP.route("/")
def index():
    """main index function"""
    # initialize food list
    foods = ["ice cream", "rice", "cookies", "pasta", "pizza", "pie", "potato"]
    # get_tweet returns a tuple containing the search query and tweepy data
    try:
        random_tweet = get_tweet(foods)
    except tweepy.error.TweepError:
        print("Auth Error")
        return "Auth Error"
    except IndexError:
        print("No tweet found in the food list")
        return "No tweet found for an item in the food list"
    try:
        random_recipe = get_recipe(foods)
    except requests.exceptions.RequestException:
        print("Auth Error")
        return "Auth Error"
    except IndexError:
        print("No recipes found")
        return "No recipe found for an item in the food list"
    ingredients = get_ingredients(random_recipe)

    return flask.render_template(
        "index.html",
        original=random_tweet[0],
        food=random_recipe["title"],
        yields=random_recipe["servings"],
        ready=random_recipe["readyInMinutes"],
        sourceURL=random_recipe["sourceUrl"],
        imageURL=random_recipe["image"],
        ingredients=ingredients,
        numofingredients=len(ingredients),
        tweet=random_tweet[1],
    )


APP.run(port=int(os.getenv("PORT", "8080")), host=os.getenv("IP", "0.0.0.0"))
