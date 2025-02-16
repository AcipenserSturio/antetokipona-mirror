from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    "--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222',
]

for option in options:
    chrome_options.add_argument(option)

experimental = {
    "download.default_directory": '.',  # Set download directory
    "download.prompt_for_download": False,  # Disable download prompts
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,  # Allow safe downloads
}
chrome_options.add_experimental_option("prefs", experimental)

driver = webdriver.Chrome(options = chrome_options)

driver.get('https://antetokipona.infinityfreeapp.com/kule/kule.csv')
driver.implicitly_wait(10)
driver.get('https://antetokipona.infinityfreeapp.com/kule/kule.csv?i=1')

print(driver.page_source)
print(driver.get_cookies())

driver.implicitly_wait(60)
with open('./page.txt', 'w') as f:
    f.write(driver.page_source)

