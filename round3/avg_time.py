from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import datetime


driver = webdriver.Chrome()

def execute_function():
    start_time = datetime.datetime.now()
    driver.get('https://mathup.com/games/crossbit?mode=daily_challenge')
    driver.implicitly_wait(10)
    # time.sleep(5)
    wait = WebDriverWait(driver, 5)
    first_result = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"GamePostStart_eq-text__X4JCA")))
    end_time = datetime.datetime.now()
    time_taken= end_time-start_time
    return time_taken
   
total_time = datetime.timedelta(0)
n=10
for i in range(1,n): 
    time_taken = execute_function()
    print(f"Time take for {i} iteration is {time_taken}")
    total_time = total_time + time_taken
    
print(f"Avg Time take for {n} iteration are {total_time/n}")
