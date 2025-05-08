from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

def execute_function():
    driver.get('https://mathup.com/games/crossbit?mode=championship')
    driver.implicitly_wait(10)
    time.sleep(5)
    wait = WebDriverWait(driver, 10)
    first_result = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"GamePostStart_eq-text__X4JCA")))
    startBtn = driver.find_elements(By.CLASS_NAME,"GamePostStart_btn__yoMra")
    startBtn.__getitem__(1).click()
    difficulty = driver.find_elements(By.CLASS_NAME,"GamePostStart_value__zH0b9")
    difficulty_text = difficulty.__getitem__(3)
    print(difficulty_text.get_attribute('innerText'))
   
for i in range(1,10): 
    execute_function()
