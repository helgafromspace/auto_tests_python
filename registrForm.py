from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    input_fname = browser.find_element_by_xpath('//label[contains(text(),"First name*")]/following-sibling::input')
    input_fname.send_keys("Мой")
    input_lname = browser.find_element_by_xpath('//label[contains(text(),"Last name*")]/following-sibling::input')
    input_lname.send_keys("Мой")
    input_email = browser.find_element_by_xpath('//label[contains(text(),"Email*")]/following-sibling::input')
    input_email.send_keys("Мой")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
