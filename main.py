from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

URL = "https://forms.gle/2uFrQakoyfS8S7GcA"

s=Service(r"C:/Development/chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get("https://www.zoopla.co.uk/to-rent/")

# Obtaining the Details of the Price, Address and Links
try:
# Handling Cookies Pop up
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="gdpr-consent-notice"]')))
    cookie_frame = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="save"]')))
    cookie_frame.click()
    location_search_el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-input-location"]')))
    location_search_el.send_keys("Cambridge")
    # Choose the maximum price per month select range
    price_range_select = Select(driver.find_element(By.XPATH, '//*[@id="rent_price_max_per_month"]'))
    price_range_select.select_by_value("500")
    search_btn = driver.find_element(By.ID, 'search-submit')
    search_btn.click()
    address = [x.get_attribute("innerText") for x in driver.find_elements(By.CSS_SELECTOR, 'a.e2uk8e20.css-1rzeb2c-StyledLink-Link-StyledLink.e33dvwd0 > p')]
    price = [x.get_attribute("innerText") for x in driver.find_elements(By.CSS_SELECTOR, 'p.css-1o565rw-Text.eczcs4p0')]
    links = [x.get_attribute("href") for x in driver.find_elements(By.CSS_SELECTOR, 'div.css-mww4lt-StyledContent.e2uk8e21 > a.e2uk8e20.css-1rzeb2c-StyledLink-Link-StyledLink.e33dvwd0')]
    print(links)
    print(price)
    print(address)
    driver.get(URL)
    # access and then load the elements first after each submit, through the loop, so the elements are loading again on the dom.
    for i in range(len(address)):
        driver.implicitly_wait(5)
        address_input = driver.find_element(By.XPATH,
                                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(address[i])
        price_input = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

        price_input.send_keys(price[i])
        links_input = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        links_input.send_keys(links[i])
        submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_btn.click()
        reset_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        reset_btn.click()
except TimeoutException:
    print("Cannot find Product")
finally:
    driver.quit()




