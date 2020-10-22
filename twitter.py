# author somT-oss
# date: 22-10-2020

from time import sleep
from conf import EMAIL, PASSWORD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, url):
        driver = self.driver
        driver.get(url)
        sleep(3)
        username = driver.find_element_by_name("session[username_or_email]")
        password = driver.find_element_by_name("session[password]")
        sleep(3)

        username.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)
        sleep(3)

    def compose_tweet(self, tweet_url, tweet):
        driver = self.driver
        driver.get(tweet_url)
        sleep(3)
        tweet_box = driver.find_element_by_css_selector(
            "br[data-text='true']")

        tweet_box.send_keys(tweet)
        sleep(2)
        # incase your tweet is part of the trends you would want to add the two commented lines to your code

        # -------------------PART OF TREND TWEET------------------------

        # trending = driver.find_element_by_css_selector("span[dir='ltr']")
        # trending.click()
        # sleep(3)

        # -------------------------------------------------------------
        button = driver.find_element_by_css_selector(
            "div[data-testid='tweetButton']")
        button.click()


main_bot = TwitterBot()
main_bot.login("https://www.twitter.com/login")
main_bot.compose_tweet("https://twitter.com/compose/tweet",
                       "Yay! i used a twitter bot")
