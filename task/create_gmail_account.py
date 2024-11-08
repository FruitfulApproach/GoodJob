from core.auto_task_thread import AutoTaskThread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from unidecode import unidecode
import random

class CreateGmailAccount(AutoTaskThread):
    def __init__(self, driver, first_name, last_name, birthday, gender, password):
        super().__init__(driver)
        self._first_name = first_name
        self._last_name = last_name
        self._birthday = birthday
        self._gender = gender
        self._password = password
    
    @property
    def birthday(self):
        return self._birthday.toString("dd MM yyyy")
    
    @property
    def username(self):
        random_number = random.randint(1000, 9999)
        first_name_normal = unidecode(self._first_name).lower()
        last_name_normal = unidecode(self._last_name).lower()
        username = f"{first_name_normal}.{last_name_normal}{random_number}"
        return username
        
    def _run(self):
        driver = self.driver        
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        # Fill in name fields
        first_name = driver.find_element(By.NAME, "firstName")
        last_name = driver.find_element(By.NAME, "lastName")
        first_name.clear()
        first_name.send_keys(self._first_name)
        last_name.clear()
        last_name.send_keys(self._last_name)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Wait for birthday fields to be visible
        wait = WebDriverWait(driver, 20)
        day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

        # Fill in birthday
        birthday_elements = self.birthday.split()
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        month_dropdown.select_by_value(str(int(birthday_elements[1])))
        day_field = driver.find_element(By.ID, "day")
        day_field.clear()
        day_field.send_keys(birthday_elements[0])
        year_field = driver.find_element(By.ID, "year")
        year_field.clear()
        year_field.send_keys(birthday_elements[2])

        # Select gender
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        
        gender_value_map = {
            'Female' : '2',
            'Male': '1',
            'Rather not say' : '3',
            'Custom' : '4',
        }
        
        gender_dropdown.select_by_value(gender_value_map[self._gender])
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        
       # Create custom email
        time.sleep(2)
        if driver.find_elements(By.ID, "selectionc4") :
            create_own_option = wait.until(EC.element_to_be_clickable((By.ID,"selectionc4") ))
            create_own_option.click()
        
        wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
        username_field = driver.find_element(By.NAME, "Username")
        username_field.clear()
        username_field.send_keys(self.username)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()
        
        # Enter and confirm password
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        password_field.clear()
        password_field.send_keys(self._password)
        # Locate the parent div element with the ID "confirm-passwd"
        confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
         #Find the input field inside the parent div
        password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
        password_confirmation_field.clear()
        password_confirmation_field.send_keys(self._password)
        next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
        next_button.click()

        # Skip phone number and recovery email steps
        skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        for button in skip_buttons:
            button.click()

        # Agree to terms
        agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
        agree_button.click()

        self.status.emit(
            f"Your Gmail successfully created:\n{{\ngmail: {your_username}@gmail.com\npassword: {your_password}\n}}")
            
        
        