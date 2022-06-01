from selenium import webdriver    
import time
import math
from selenium.webdriver.support.ui import Select

try:
    browser=webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    num1 = browser.find_element_by_id('input_value')
    x = int(num1.text)
    y = math.log(abs(12*math.sin(x)))
    input_result = browser.find_element_by_id('answer')
    input_result.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()