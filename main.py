from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import requests
import time


news_api_key = "57b3d49680ef46149e2f418004313e95"
USERNAME = "@telase_nik44695"
PASSWORD = "Python123@"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://twitter.com/i/flow/login?redirect_after_login=%2Fcompose%2Fpost")
time.sleep(5)
# username_input
username_input = driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
username_input.send_keys(USERNAME)
username_input.send_keys(Keys.ENTER)
time.sleep(2)
# password input
password_input = driver.find_element(By.NAME, value='password')
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

# getting news data
r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api_key}")
print(r.url)
news_dict = r.json()
articles = news_dict["articles"]

n = articles[1]
title = n.get('title')
print(title)
url = n.get('url')
print(url)

# posting a post
time.sleep(10)
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

pyautogui.click(530, 323)
pyautogui.keyDown('shift')
pyautogui.write("braking news", interval=0.1)
pyautogui.keyUp('shift')
pyautogui.press('enter')
pyautogui.write(title, interval=0.1)
pyautogui.press('enter')
pyautogui.write(url, interval=0.1)

post_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span')
post_button.click()



gggg