from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)) is not None
        except TimeoutException:
            return False

    def is_url_contains(self, text):
        return text in self.driver.current_url

    def is_disabled(self, locator):
        element = self.find_element(locator)
        return element.get_attribute("disabled") is not None

    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    def get_current_url(self):
        return self.driver.current_url