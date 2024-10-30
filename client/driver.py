from selenium import webdriver
from selenium.webdriver.common.by import By
from config.driver_config import DriverConfig

class Driver:

    def __init__(self):
        self.env = DriverConfig.driver_env
        self.driver_path = DriverConfig.driver_path
        self.driver = self.create_driver(self.env)

    @staticmethod
    def create_driver(driver_type):
        global driver
        if driver_type == "chrome":
            from selenium.webdriver.chrome.options import Options
            option = Options()
            option.add_argument("--headless")
            option.add_argument("--disable-gpu")
            option.add_argument("--no-sandbox")
            driver = webdriver.Chrome(options=option)
        return driver

    def get(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(3)

    def get_page(self):
        return self.driver.page_source

    def get_title(self):
        return self.driver.title

    def get_element_id(self, id):
        return self.driver.find_element(By.ID, id)

    def get_element_class(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

    def get_element_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def get_elements_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def close(self):
        self.driver.quit()