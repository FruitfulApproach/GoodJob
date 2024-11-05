from selenium import webdriver
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


class AutoBrowser:
    def __new__(self):
        global auto_browser
        
        if auto_browser is None:
            auto_browser = super().__new__(AutoBrowser)
            
        return auto_browser
        
    def __init__(self):
        chromedriver_autoinstaller.install()
        # Check if the current version of chromedriver exists
        # and if it doesn't exist, download it automatically,
        # then add chromedriver to path               

        self._options = ChromeOptions('--disable-infobars')
        self._service = ChromeService('chromedriver.exe')
        self._driver = webdriver.Chrome(options=self._options)
        
    

auto_browser = None  