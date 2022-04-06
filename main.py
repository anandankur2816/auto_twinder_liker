from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from login_credentials import *
import time
timeout = time.time() + 60*4
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
s = Service("A:\Webservices ML\chromedriver (2).exe")
driver = webdriver.Chrome(service=s, options=chrome_options)


driver.get("http://www.tinder.com")

sleep(5)
#//*[@id="c849239686"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span
login_button = driver.find_element_by_xpath('//*[@id="c849239686"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_button.click()

sleep(2)
select_using_another_way_to_login = driver.find_element(By.XPATH, '//*[@id="c-879141390"]/div/div/div[1]/div/div/div[3]/span/button')
sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="c-879141390"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login.click()
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)
sleep(3)
driver.find_element(By.XPATH, '//*[@id="mount_0_0_Ru"]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]').click()
sleep(3)
driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
