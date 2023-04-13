# Import Selenium libraries.
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import urllib.request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# We open some lists to store the relevant scrapped information.
INSTAGRAM_USER = os.getenv("Your_ig_account")
INSTAGRAM_PASSWORD = os.getenv("Your_ig_password")

# We open some lists to store the relevant scrapped information.
post_list_url = []
likes_list = []
post_description_list = []
ubi_list = []

# Save Chrome path.
PATH = "Your_Path_To_Chrome"
driver = webdriver.Chrome(PATH)

# Open instagram.
driver.get("https://www.instagram.com/")


# I will be using time sleep to walk throught the code and make everything visible.
time.sleep(4)
# Here we will start finding elements, I will generally do it by Xpath. We use .click() method to allow  clicking elements found.
onlyEssentialCookies = driver.find_element("xpath", "//button[contains(text(), 'Only allow essential cookies')]").click()

# Find username and password.
time.sleep(4)
username = driver.find_element("css selector", "input[name='username']")
password = driver.find_element("css selector", "input[name='password']")

# Once found we clear the boxes to make sure we can send our password and username with no typos.
username.clear()
password.clear()

# Send info to relevant boxes.
username.send_keys("Your_ig_account")
password.send_keys("Your_ig_password")

# Login.
login = driver.find_element("css selector", "button[type='submit']").click()

# turn off notifications.
time.sleep(4)
time.sleep(4)
nothow = driver.find_element("xpath", "//button[contains(text(), 'Not now')]").click()
time.sleep(4)
nothow2 = driver.find_element("xpath", "//button[contains(text(), 'Not Now')]").click()

# Find searchbox.
time.sleep(5)
searchbox1 = driver.find_element("css selector", "svg[aria-label='Search']").click()
time.sleep(5)
searchbox = driver.find_element("css selector", "input[placeholder='Search']")
searchbox.clear()

# Search intagram user.
searchbox.send_keys("cristiano")
time.sleep(4)
searchbox.send_keys(Keys.ENTER)
time.sleep(4)
searchbox.send_keys(Keys.ENTER)
time.sleep(4)

# Find the Username of the instagram account
user_Name_find = driver.find_element(By.XPATH, "//h2")
user_Name = user_Name_find.text # Retrieve the text from username
print('\n''UserName:', user_Name) # Save it and print it to console to check.

# Find the followers of the instagram account
followers = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span")
print('followers:', followers.get_attribute("title"), '\n')

# Find the Description of the instagram account
user_Description_find = driver.find_element(By.XPATH, "//div[@class='_aa_c']")
user_Description = user_Description_find.text
print('Description:', user_Description, '\n')

# We click one of the images and use the next button later instead of scrolling (We want the information about the 10 last posts).
image = driver.find_element(By.XPATH, "//div[@class='_aabd _aa8k _aanf']").click()
time.sleep(4)

images_count = 1
#influerncersDict = {'Post_Url': ,'User_Name': ,'Followers': followers, 'Profile_Description': ,'Post_Description': ,'Hashtags': ,'Likes': ,'Comments': ,'Post_Location': }

# While loop to get the info from the first ten posts.
while(images_count < 11):
    driver.find_element("css selector", "svg[aria-label='Next']").click()

    # Find the post_url of the instagram post.
    post_Url = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a")
    print('URL:', post_Url.get_attribute("href"))
    post_list_url.append(post_Url.get_attribute("href"))

    # Find the likes of the instagram post.
    likes_find = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div/div/a/div/span")
    likes = likes_find.text
    print('likes:', likes)
    likes_list.append(likes)

    # Find the desription of the instagram post.
    post_Description_Find = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/h1")
    post_Description = post_Description_Find.text
    print('Post_Description:', post_Description)
    post_description_list.append(post_Description)

    # Find the ubication of the instagram post.
    ubi_find = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[2]/div[1]")
    ubi = ubi_find.text
    print('Ubication:', ubi, '\n')
    ubi_list.append(ubi)

    time.sleep(4)
    images_count += 1