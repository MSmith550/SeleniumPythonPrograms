from selenium import webdriver
from selenium.webdriver.common.by import By as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get('https://www.dumac.com/careers')
    wait = WebDriverWait(driver, 20)
    jobs = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="hs_cos_wrapper_widget_1644524336960"]/div/div')))
    for job in jobs:
        jobTitle = job.find_element(By.TAG_NAME, 'button')
        print(jobTitle.text)

finally:
    driver.close()
