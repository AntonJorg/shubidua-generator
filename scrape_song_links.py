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

html = driver.find_element(By.TAG_NAME, "html")

cookie_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookie_button.click()

songs_and_albums = driver.find_element(By.TAG_NAME, 'artist-songs-and-albums')

see_all_button = songs_and_albums.find_element(By.XPATH, "//*[contains(text(), 'Show all songs by')]")
see_all_button.click()

sleep(2)

modal_window = driver.find_element(By.CLASS_NAME, "modal_window")
input_field = modal_window.find_element(By.TAG_NAME, "input")

scroll_container = modal_window.find_element(By.XPATH, "//div[@ng-if='$scrollable_data_ctrl.models.length']")

prev_num_elements = -1
while True:
    scroll_list_elements = modal_window.find_elements(By.TAG_NAME, "transclude-injecting-local-scope")
    curr_num_elements = len(scroll_list_elements)
    print("Number of scroll list elements:", curr_num_elements)

    #input_field.send_keys(Keys.PAGE_DOWN)

    driver.execute_script("arguments[0].scrollIntoView(true);", scroll_list_elements[-1])
    sleep(2)

    if curr_num_elements == prev_num_elements:
        break

    prev_num_elements = curr_num_elements

links = [el.find_element(By.TAG_NAME, "a").get_attribute("href") for el in scroll_list_elements]
links = [link + "\n" for link in links if link.startswith("https://genius.com/Shu-bi-dua-")]

f = open("song_links.txt", "w")
f.writelines(links)
f.close()
