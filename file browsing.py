from selenium import webdriver    
import time
import os

try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    fname = browser.find_element_by_name('firstname')
    fname.send_keys('Me')
    lname = browser.find_element_by_name('lastname')
    lname.send_keys('Me')
    email = browser.find_element_by_name('email')
    email.send_keys('Me@gmail.com')
    element = browser.find_element_by_css_selector('input[type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt') 
    #file.txt должен лежать в той же директории, откуда запускается скрипт
    element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()