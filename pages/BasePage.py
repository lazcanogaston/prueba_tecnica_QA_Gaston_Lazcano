from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    #web driver methods

    def get_page(self, url):
        self.driver.get(url)
        
    def find_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(By.XPATH, locator)

    def actions_scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.actions.move_to_element(element).perform()

    def actions_scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element) 
    
    def get_page_title(self):
        return self.driver.title
    
    #web element methods
    
    def click(self, locator):
        self.find_element(locator).click()

    def js_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element) 
    
    def send_keys(self, locator, keys):
        self.find_element(locator).send_keys(keys)
    
    def get_attribute(self, locator, att):
        att_value = self.find_element(locator).get_attribute(att)
        return att_value

    #web driver wait 

    def wait_until_visible(self, locator):
        #element = self.find_element(locator)
        self.wait.until(EC.visibility_of(By.XPATH, locator))

    def wait_until_title_contains(self, title):
        self.wait.until(EC.title_contains(title))