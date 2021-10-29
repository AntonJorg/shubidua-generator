from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# create browser service, installing if not cached
s=Service(ChromeDriverManager().install())

# instantiate chrome driver
driver = webdriver.Chrome(service=s)

driver.get("https://genius.com/artists/Shu-bi-dua")

songs_and_albums = driver.find_element(By.TAG_NAME, 'artist-songs-and-albums')

see_all_button = songs_and_albums.find_element(By.XPATH, "//*[contains(text(), 'Show all songs by')]")

driver.execute_script("arguments[0].click();", see_all_button)

sleep(5)