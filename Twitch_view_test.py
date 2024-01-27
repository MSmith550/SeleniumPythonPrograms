from selenium import webdriver
from selenium.webdriver.common.by import By as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get('https://www.twitch.tv/mojod/videos?filter=all&sort=time')
    wait = WebDriverWait(driver, 20)
    videos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="offline-channel-main-content"]/div[3]/div/div/div/div/div[2]/div/div[1]/div/article')))
    for video in videos:
        image = video.find_element(By.CSS_SELECTOR, 'article>div:nth-child(2) a img.tw-image')
        release_date = image.get_attribute('title')
        views = video.find_element(By.CSS_SELECTOR, 'article a>div>div:nth-child(3)>div')
        title = video.find_element(By.CSS_SELECTOR, 'a>h3')
        print(release_date + ' - ' + views.text + ' - ' + title.text)

finally:
    driver.close()
