#https://www.youtube.com/watch?v=-zcjlXQgkmw
#from selenium import webdriver

from selenium.webdriver import Chrome

chromedriver = "C:\Testes\Drivers\chromedriver.exe"

driver = Chrome(chromedriver)
driver.maximize_window()

driver.get('https://www.python.org/')

driver.find_element_by_id('id-search-field').send_keys('Python')

driver.find_element_by_css_selector('#submit').click()

btn_txt = driver.find_element_by_id('submit').text

print(btn_txt)

driver.quit()