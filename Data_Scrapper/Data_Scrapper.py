# Import Selenium libraries.
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import urllib.request
import requests
import pandas as pd
from dotenv import load_dotenv
import os

# We will be using these two control functions to ensure that selenium checks for the existance of these paths before interacting with them.
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_css(css):
    try:
        driver.find_element(By.CSS_SELECTOR, css)
    except NoSuchElementException:
        return False
    return True

# We will open the options for the chrome browser and disable flags to allow more time of automated software.
option = webdriver.ChromeOptions()

load_dotenv()

# We open some lists to store the relevant scrapped information.
INSTAGRAM_USER = os.getenv("elflamencomasnormal")  #elflamencoadormilao #misflamenquitosfamiliares #miflamenquitosonrojado #miflamencoatolondrado #miflamencomashermoso #eduardoelflamenco #miflamencomassorpresivo #elflamencoamedrantado #miflamencomasmolon #elflamencomoribundo #elflamencorepresivo #elflamencomastimidoentreellos #elflamencomasnormal #elflamencomasentrometido
INSTAGRAM_PASSWORD = os.getenv("@ingenierosdelIE")


images_count = 10
# Save instagram url.
usernames = [ 'costco', 'bestbuy', 'homedepot', 'unicef', 'who', 'wwf', 'amnesty', 'oxfaminternational', 'bloombergbusinessweek', 'nationalgeographic',
'reuters', 'apnews', 'usatoday', 'foxnews', 'cnbc', 'msnbc', 'bbcworldservice', 'huffpost', 'buzzfeed']

PATH = "/Users/beltran/Desktop/Data scrapping/chromedriver"
driver = webdriver.Chrome(PATH)
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Open instagram.
driver.get("https://www.instagram.com/")
driver.maximize_window()


# I will be using time sleep to walk throught the code and make everything visible.
time.sleep(3.5)
# Here we will start finding elements, I will generally do it by Xpath. We use .click() method to allow  clicking elements found.
onlyEssentialCookies = driver.find_element("xpath", "//button[contains(text(), 'Only allow essential cookies')]").click()

# Find username and password. 
time.sleep(4.5)
username = driver.find_element("css selector", "input[name='username']")
password = driver.find_element("css selector", "input[name='password']")

# Once found we clear the boxes to make sure we can send our password and username with no typos.
username.clear()
password.clear()

# Send info to relevant boxes.,
username.send_keys("elflamencomasnormal")
password.send_keys("@ingenierosdelIE")

# Login.
login = driver.find_element("css selector", "button[type='submit']").click()

# turn off notifications.
time.sleep(2.8) 
time.sleep(4.3)                 
nothow = driver.find_element("xpath", "//div[@class='_ac8f']").click()
time.sleep(3.2)
nothow2 = driver.find_element("xpath", "//button[contains(text(), 'Not Now')]").click()

# Find searchbox.
time.sleep(1.5)
searchbox1 = driver.find_element("css selector", "svg[aria-label='Search']").click()
time.sleep(2.22)
searchbox = driver.find_element("css selector", "input[placeholder='Search']")
searchbox.clear()

n = 0

influencersDict = {}
influencersDict['user_Name'] = []
influencersDict['followers'] = []
influencersDict['user_Description'] = []
influencersDict['post_Url'] = []
influencersDict['likes'] = []
influencersDict['post_Description'] = []
influencersDict['post_Location'] = []

while (n < len(usernames)):
    for i in usernames:
        time.sleep(2.3)
        # Search intagram user.
        searchbox.send_keys(i)
        time.sleep(2.8)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(1.6)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(1.8)
        usernames.remove(i)
        time.sleep(1.5)
        
        # We also want to check for the posts the influencer has in order to check if the value is lower than 15. In that case we will not scrap the user.
        if check_exists_by_xpath("//span[@class='_ac2a']") == True:
            pocosposts = driver.find_element(By.XPATH, "//span[@class='_ac2a']") #//span[@class='_ac2a']
            pocosposts = pocosposts.text
            pocosposts = pocosposts.replace(',', '')
            pocosposts = pocosposts.replace('.', '')
            pocosposts = int(pocosposts)
            print('\n''Numerodeposts:', pocosposts)
        else:
            pocosposts = 20
            print(pocosposts)
   
        if pocosposts > 15:
            if check_exists_by_css("h2") == True:
                # Find the Username of the instagram account
                user_Name_find = driver.find_element("css selector", "h2")
                user_Name = user_Name_find.text # Retrieve the text from username
                print('\n''UserName:', user_Name) # Save it and print it to console to check.
            else:
                user_Name = '' 
            for u in range(10):
                influencersDict['user_Name'].append(user_Name)

            if check_exists_by_xpath("//li[2]/a/span/span[@class='_ac2a']") == True:
                # Find the followers of the instagram account
                followers = driver.find_element(By.XPATH,"//li[2]/a/span/span[@class='_ac2a']")
                followers = followers.get_attribute("title")
                print('followers:', followers, '\n')
            else: 
                followers = ''
            for u in range(10):
                influencersDict['followers'].append(followers)

            if check_exists_by_xpath("//div[@class='_aa_c']") == True:
                # Find the Description of the instagram account
                user_Description_find = driver.find_element(By.XPATH, "//div[@class='_aa_c']")
                user_Description = user_Description_find.text
                print('Description:', user_Description, '\n')
            else:
                user_Description = '' 
            for u in range(10): 
                influencersDict['user_Description'].append(user_Description)

            # We click one of the images and use the next button later instead of scrolling (We want the information about the 10 last posts).
            time.sleep(2.1)
            if check_exists_by_xpath("//div[2]/a/div[1][@class='_aagu']") == True:
                image = driver.find_element(By.XPATH, "//div[2]/a/div[1][@class='_aagu']").click() 
                print('hols')
            else:
                print('hold')
                image = driver.find_element(By.XPATH, "//div[1][@class='_aagu']").click()
            
            time.sleep(0.9)
            while(images_count > 0):      
                if check_exists_by_xpath("//div[2]/a/div[1][@class='_aagu']") == True:
                    time.sleep(1)
                    images_count -= 1
                    # Find the post_url of the instagram post.
                    post_Url = driver.current_url
                    print('URL:', post_Url)
                    influencersDict['post_Url'].append(post_Url)

                    # Find the likes of the instagram post.
                    if check_exists_by_xpath("//span[@class='x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj']") == True:
                        likes_find = driver.find_element(By.XPATH, "//span[@class='x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj']")
                        likes = likes_find.text
                        print(likes)
                        print('likes:', likes)
                        influencersDict['likes'].append(likes)
                        print('lone')
                    else:
                        print ('hey')
                        likes = ''
                        influencersDict['likes'].append(likes)

                    # Find the desription of the instagram post.
                    if check_exists_by_xpath("//h1[@class='_aacl _aaco _aacu _aacx _aad7 _aade']") == True:
                        post_Description_Find = driver.find_element(By.XPATH, "//h1[@class='_aacl _aaco _aacu _aacx _aad7 _aade']")
                        post_Description = post_Description_Find.text
                        print('Post_Description:', post_Description)
                        influencersDict['post_Description'].append(post_Description)
                        print('lone')
                    else:
                        print ('hey')
                        post_Description = ''
                        influencersDict['post_Description'].append(post_Description)

                    if check_exists_by_xpath("//div[@class='_aaqm']") == True:
                    # Find the ubication of the instagram post.
                        ubi_find = driver.find_element(By.XPATH, "//div[@class='_aaqm']")
                        ubi = ubi_find.text
                        print('Ubication:', ubi, '\n')
                        influencersDict['post_Location'].append(ubi)
                        time.sleep(2)
                        print('lone')
                    else:
                        print ('hey')
                        ubi = ''
                        influencersDict['post_Location'].append(ubi)
                    time.sleep(1.88)
                    driver.find_element(By.XPATH, "//div[2][@class=' _aaqg _aaqh']").click()
                else:
                    images_count = 10
                    time.sleep(2.1)
                    driver.find_element("css selector", "svg[aria-label='Close']").click()
                    time.sleep(2.1)
                    searchbox1 = driver.find_element("css selector", "svg[aria-label='Search']").click()
                    time.sleep(1.8)
                    searchbox = driver.find_element("css selector", "input[placeholder='Search']")
                    searchbox.clear()

                    for u in range(10):
                        post_Url = ''
                        influencersDict['post_Url'].append(post_Url)

                        likes = ''
                        influencersDict['likes'].append(likes)
                        
                        post_Description = ''
                        influencersDict['post_Description'].append(post_Description)

                        ubi = ''
                        influencersDict['post_Location'].append(ubi)

            # Once we exit the loop all the data is added to an existing csv.
            df = pd.DataFrame(influencersDict)
            df.to_csv('influenceDataBrands.csv', mode='a', index=False, header=False)
            print(df)
            influencersDict = {}
            influencersDict['user_Name'] = []
            influencersDict['followers'] = []
            influencersDict['user_Description'] = []
            influencersDict['post_Url'] = []
            influencersDict['likes'] = []
            influencersDict['post_Description'] = []
            influencersDict['post_Location'] = []
            images_count = 10
            time.sleep(2.3)
            driver.find_element("css selector", "svg[aria-label='Close']").click()
            time.sleep(2.1)
            searchbox1 = driver.find_element("css selector", "svg[aria-label='Search']").click()
            time.sleep(2.4)
            searchbox = driver.find_element("css selector", "input[placeholder='Search']")
            searchbox.clear()

        else: #This is the case in which the scrapper did not even start scrapping the user (The path was not found) and therefore post_scrapping could not start. 
            for u in range(images_count):
                user_Name = ''
                influencersDict['user_Name'].append(user_Name)

                followers = ''
                influencersDict['followers'].append(followers)

                user_Description = ''
                influencersDict['user_Description'].append(user_Description)

                post_Url = ''
                influencersDict['post_Url'].append(post_Url)

                likes = ''
                influencersDict['likes'].append(likes)
                
                post_Description = ''
                influencersDict['post_Description'].append(post_Description)

                ubi = ''
                influencersDict['post_Location'].append(ubi)

            df = pd.DataFrame(influencersDict)
            df.to_csv('influenceDataBrands.csv', mode='a', index=False, header=False)
            influencersDict = {}
            influencersDict['user_Name'] = []
            influencersDict['followers'] = []
            influencersDict['user_Description'] = []
            influencersDict['post_Url'] = []
            influencersDict['likes'] = []
            influencersDict['post_Description'] = []
            influencersDict['post_Location'] = []

            # Fill the search box with the next name in the list. 
            print("clearing checkbox")
            time.sleep(1.92)
            driver.find_element("css selector", "svg[aria-label='Search']").click()
            time.sleep(1.8)
            searchbox1 = driver.find_element("css selector", "svg[aria-label='Search']").click()
            time.sleep(2.6)  
            searchbox = driver.find_element("css selector", "input[placeholder='Search']")    
            searchbox.clear() 

print(influencersDict)
df = pd.DataFrame(influencersDict)