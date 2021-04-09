from selenium import webdriver


class Browser:
    chromedriver = "C:\Testes\Drivers\chromedriver.exe"
    driver = webdriver.Chrome( chromedriver)
    driver.maximize_window()