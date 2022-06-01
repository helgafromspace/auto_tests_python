from selenium import webdriver    
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
        
    input_num = browser.find_element_by_id('input_value')
    num = input_num.text
    func = calc(num)
    
    answer = browser.find_element_by_id('answer')
    answer.send_keys(func)
    
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