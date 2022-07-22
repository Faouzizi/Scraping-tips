url = 'https://fr.finance.yahoo.com/'

# Define options
chrome_options = Options()
# Change webdriver shape
chrome_options.add_argument("--window-size=1024,768")
# Setup the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# Go to the url page
driver.get(url)

# Click on button using text on the button
driver.find_element(By.XPATH, "//button[contains(., 'Refuser tout')]").click()

# Click on span using text on the span
driver.find_element(By.XPATH, "//span[contains(., 'Suivant')]").click()

# Click on li using text on the li
driver.find_element(By.XPATH, "//li[contains(., 'Ajouter Région')]").click()

# Click on label using text on the label
driver.find_element(By.XPATH, "//label[contains(., '%s')]" % country).click()

# Click on button containing 'fermer' on the title
driver.find_element(By.XPATH, "//button[contains(@title, 'Fermer')]").click()

# Find search bar using input tag and placeholder text
search_bar = driver.find_element(By.XPATH,
                                         """//input[contains(@placeholder, 'Filtres de recherche')]""")

#clearing the search bar 
search_bar.clear()

# Send a new text
search_bar.send_keys('Rendement de l’action')
