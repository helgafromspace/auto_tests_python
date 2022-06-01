from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    
    button =  browser.find_element(By.ID, "book")
    button.click()
    
    input_num = browser.find_element(By.ID,"input_value")
    num = input_num.text
    func = calc(num)
    
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(func)
    
    button = browser.find_element(By.ID,"solve")
    button.click()
    
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()