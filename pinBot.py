import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True )


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

driver.get("https://www.pinterest.com/")
time.sleep(5)
login_button = driver.find_element(By.XPATH,"//div[contains(@class,'RCK Hsu')]")
time.sleep(2)
login_button.click()

time.sleep(6)
username = driver.find_element(By.ID,"email")
time.sleep(1)
password = driver.find_element(By.ID,"password")

login = driver.find_element(By.XPATH,"//button[@type='submit']")

username.send_keys("email")
password.send_keys("pass")


time.sleep(1)
login.click()

