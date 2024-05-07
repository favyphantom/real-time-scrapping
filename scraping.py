from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_price_patelbros(search_query, _location):
    # Initialize the WebDriver (example with Chrome)
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        driver.get("https://shop.patelbros.com/search?item=" + search_query)

        # Wait for the location selection element to become clickable
        wait = WebDriverWait(driver, 30)
        # Assuming there are multiple locations, find the one you want (e.g., Chicago)
        # This example looks for the div containing "Chicago" and clicks the associated selection button
        locations = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mtopbot5")))
        find_location = False
        for location in locations:
            if _location.upper() in location.text:
                find_location = True
                select_button = location.find_element(By.XPATH, "./ancestor::li//a[contains(@class,'location-selected-button')]")
                select_button.click()
                break

        if not find_location:
            driver.quit()

        confirm_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".popup-price-list")))  # Update with actual ID or selector

        # Confirm
        confirm_element.click()

        # Now navigate or search as needed with the location set
        search_box = driver.find_element(By.NAME, 'searchBar')  # Update with actual name or selector
        search_box.send_keys(search_query + "\n")  # Simulate typing the search query and hitting Enter

        # Scrape the prices or data you need
        # This is just an example; you'll need to adjust it based on the website's structure
        prices = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mbot6")))
        results = []
        for price in prices:
          text = price.text
          if text != '':
            results.append(text)

        return results

    finally:
        driver.quit()


def get_price_petsmart(search_query):
    # Initialize the WebDriver (example with Chrome)
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        driver.get("https://www.petsmart.com/search/?q=" + search_query)

        # Wait for the location selection element to become clickable
        wait = WebDriverWait(driver, 10)
        # Assuming there are multiple locations, find the one you want (e.g., Chicago)
        # This example looks for the div containing "Chicago" and clicks the associated selection button
        prices = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-price")))
        results = []
        for price in prices:
          text = price.text

          if text != '':
              results.append(text)
        
        return results
    
    finally:
        driver.quit()


def get_price_target(search_query):
    # Initialize the WebDriver (example with Chrome)
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        driver.get(f"https://www.target.com/s?searchTerm=${search_query}&tref=typeahead%7Cterm%7C{search_query}%7C%7C%7Chistory")

        # Wait for the location selection element to become clickable
        wait = WebDriverWait(driver, 10)
        # Assuming there are multiple locations, find the one you want (e.g., Chicago)
        # This example looks for the div containing "Chicago" and clicks the associated selection button
        prices = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[data-test='current-price']")))
        results = []
        for price in prices:
          text = price.text

          if text != '':
              results.append(text)
        
        return results
    
    finally:
        driver.quit()


def get_price_meijer(search_query):
    # Initialize the WebDriver (example with Chrome)
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        driver.get(f"https://www.meijer.com/shopping/search.html?text=${search_query}")

        # Wait for the location selection element to become clickable
        wait = WebDriverWait(driver, 10)
        # Assuming there are multiple locations, find the one you want (e.g., Chicago)
        # This example looks for the div containing "Chicago" and clicks the associated selection button
        prices = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-tile__regular-price")))
        results = []
        for price in prices:
          text = price.text

          if text != '':
              results.append(text)
        
        return results
    
    finally:
        driver.quit()


def get_price_costco(search_query):
    # Initialize the WebDriver (example with Chrome)
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        driver.get(f"https://www.costco.com/CatalogSearch?dept=All&keyword=${search_query}")

        # Wait for the location selection element to become clickable
        wait = WebDriverWait(driver, 10)
        # Assuming there are multiple locations, find the one you want (e.g., Chicago)
        # This example looks for the div containing "Chicago" and clicks the associated selection button
        prices = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price")))
        results = []
        for price in prices:
          text = price.text

          if text != '':
              results.append(text)
        
        return results
    
    finally:
        driver.quit()


def get_price_walmart(search_query):
    # Initialize the WebDriver (example with Chrome)
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        driver.get(f"https://www.walmart.com/search?q=${search_query}")

        # Wait for the location selection element to become clickable
        wait = WebDriverWait(driver, 10)
        # Assuming there are multiple locations, find the one you want (e.g., Chicago)
        # This example looks for the div containing "Chicago" and clicks the associated selection button
        prices = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".w_iUH7")))
        results = []
        for price in prices:
          text = price.text

          if text != '':
              results.append(text)
        
        return results
    
    finally:
        driver.quit()
