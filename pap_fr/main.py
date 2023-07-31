import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import codecs

def get_page_links(driver):
    links = driver.find_elements(By.XPATH, '//a[@class="item-thumb-link"]')
    return [link.get_attribute('href') for link in links]

def open_and_check_page(url):
    driver = webdriver.Edge()
    driver.get(url)
    file=codecs.open('all_urls.txt', 'a+')
    file.write(url +"\n")
    file.close()
    time.sleep(1)  # Wait for page to load
    element = driver.find_elements(By.XPATH, '//*[contains(text(),"calme")]')
    if element:
        file=codecs.open('calme.txt', 'a+')
        file.write(url +"\n")
        file.close()
    element = driver.find_elements(By.XPATH, '//*[contains(text(), "climatisation")]')
    if element:
        file=codecs.open('climatisation.txt', 'a+')
        file.write(url +"\n")
        file.close() 
    element = driver.find_elements(By.XPATH, '//*[contains(text(),"appartement")]')          
    if element:
        file=codecs.open('appartement.txt', 'a+')
        file.write(url +"\n")
        file.close()             
    driver.quit()
    return False

def scroll_to_page(driver):
    last_height = driver.execute_script("return document.body.scrollHeight") 
    n=1
    while True: 
            # scroll down 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
            # pause for download 
        time.sleep(3)
            # Calculate new and old height of sheet
        new_height = driver.execute_script("return document.body.scrollHeight") 
        if new_height == last_height: 
            print("End scrolling") 
            break 
        last_height = new_height
        print(str(n) + "...There are new contents, skrolling again")
        n +=1

def main():
    base_url = "https://www.pap.fr/annonce/locations-appartement-paris-75-g439-du-2-pieces-au-3-pieces-a-partir-de-50-m2" 
    driver = webdriver.Edge()
    time.sleep(1)
    driver.get(base_url)
    time.sleep(1)  # Wait for page to load
    scroll_to_page(driver)
    page_links = get_page_links(driver)
    for link in page_links:
        open_and_check_page(link)
    driver.quit()
    print("End parsing")

if __name__ == "__main__":
    main()
