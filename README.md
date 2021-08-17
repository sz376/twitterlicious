# hello web!

This program will search for tweets related to a random food item in a hardcoded list (currently hardcoded to "ice cream", "fried rice", "rasmalai", "tofu stew", "quesadilla", "tres leches", "sweet potato casserole") that is not a retweet, reply, or non-english and then displays it in a webpage.

### Dependencies

Tweepy v3.9.0  
Flask v1.1.2  
Jinja v2.11.2  
Requests v2.24.0 <br>
Spoonacular v3.0<br>
python-dotenv v0.14.0

### Usage

0. Sign up for the twitter developer portal at [https://developer.twitter.com](https://developer.twitter.com)
1. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
2. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
3. Sign up for the spoonacular api at [https://spoonacular.com/food-api](https://spoonacular.com/food-api)
4. Click on the "My Console" button and then the "Profile" tab to access your spoonacular api key.
5. Clone this repository by using git clone https://github.com/sz376/twitterlicious
6. In your local copy of this repository, create a new root-level file called tweepy.env
7. Add the following line in tweepy.env, and then save tweepy.env

```
CONSUMER_KEY='TODO'
CONSUMER_SECRET='TODO'
ACCESS_TOKEN='TODO'
ACCESS_TOKEN_SECRET='TODO'
SPOONACULAR_API='TODO'
```

8. Run the following in your terminal:
    sudo pip install tweepy
    (or) sudo pip3 install tweepy
    (or) pip install tweepy
    (or) pip3 install tweepy
9. Install flask using the same process as above ([sudo] pip[3] install flask)
10. Install python-dotenv using the same process as above ([sudo] pip[3] install python-dotenv)
11. Install spoonacular using the same process as above ([sudo] pip[3] install spoonacular)
12. Run `python proj1.py`

The script will run until aborted.

### Technical Issues
There were definately some growing pains in working with a new API. Initially I did not know how to use the tweepy API and had issues pulling actual tweets from tweepy objects. Luckedily the [tweepy documentation](http://docs.tweepy.org/) is very robust . I was able to search for whatever issue or data I wished to use and there were examples that made the learning process extremely easy. <br><br>
Another rather embarrassing error was trying to debug strange HTML errors concerning my for loops with HTML5 documentation. It took quite a while to remember that I should be looking at the [Jinja2 documentation](https://jinja.palletsprojects.com/en/2.11.x/) instead. <br><br>
Another hair-pulling issue was trying to debug a certain index out of range error while searching recipe data using Spoonacular. After a while I decided to take a break and see what was in the fridge. Opening it up, I realized that there was only one can of Coke left and then it hit me that I might have ran out of allocated requests. Sure enough, after checking my API account at Spoonacular, I saw that I was indeed out of requests. It goes to show that sometimes, taking a break is important in the workflow. <br>

### Additional Possible Features
A feature I would like to implement is the ability to search for recipes based on ingredients that a user has on hand. After looking at the Spoonacular documentation, there is definately possible with the current tools. Ingredients can be passed to a list and then passed through the request URL. An example shown on the documentation is:
```
GET https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2
```
A simple string manipulation should get the job done. <br><br>
Another feature I would like to implement is the ability to see the prices of local supermarkets for each ingredient provided by Spoonacular. Perhapes the Whisk API can provide a rough estimate for prices of grocery items. A quick look at the [documentation for Whisk](https://docs.whisk.com/api/retailers/search-store-items) shows that indeed it is possible to not only pull prices, but also local retailers.
