from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

time.sleep(30)
qtd = 0

while qtd < (27 + 13):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys('te amo muito, vida!')
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
    qtd += 1

driver.close()