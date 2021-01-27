from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def web_driver(name, massage):

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

    driver.get('https://web.whatsapp.com/')

    landing = driver.find_element_by_xpath('//*[@id="app"]/div')
    spans = landing.find_elements_by_tag_name('span')

    while len(spans) <= 11:
        landing = driver.find_element_by_xpath('//*[@id="app"]/div')
        spans = landing.find_elements_by_tag_name('span')

        print('...')
        time.sleep(1)

    time.sleep(0.5)


    user = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    user.click()
    user.send_keys(name + Keys.ENTER)

    rite_massage = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    rite_massage.send_keys(massage + Keys.ENTER)

