import time
from selenium import webdriver

nums = open('p1.txt', 'r').read().splitlines()
login = nums[0]
password = nums[1]
print(login)
print(password)

driver = webdriver.Chrome(executable_path='C:/Users/ХХХ/Desktop/Учеба/Сафаров/Python/chromedriver.exe')
driver.get('http://vk.com')

input_login = driver.find_element_by_id('index_email')
input_login.send_keys(login)
input_pass = driver.find_element_by_id('index_pass')
input_pass.send_keys(password)

input_submit = driver.find_element_by_id('index_login_button')
input_submit.click()

#driver.close()
