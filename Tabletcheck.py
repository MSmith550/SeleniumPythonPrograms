import time
from selenium import webdriver
from selenium.webdriver.common.by import By as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
try:
    driver.get('https://www.bestbuy.com')
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'gh-search-input')))
    driver.find_element(By.ID, 'gh-search-input').click()
    driver.find_element(By.ID, 'gh-search-input').send_keys("tablets")
    driver.find_element(By.ID, 'gh-search-input').send_keys(Keys.ENTER)
    time.sleep(5)
    items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'sku-item')))
    for item in items:
        itemName = item.find_element(By.CLASS_NAME, 'sku-title')
        itemPriceStarting = item.find_element(By.CLASS_NAME, 'column-right')
        itemPrice = itemPriceStarting.find_element(By.TAG_NAME, 'span')
        print(itemName.accessible_name + " -- " + itemPrice.text)

finally:
    driver.close()
