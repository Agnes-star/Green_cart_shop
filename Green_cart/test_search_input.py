import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.search_input
    def test_verifying_search_input(self, driver):
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        search_element = driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']")
        search_element.click()
        search_element.send_keys("cucumber")
        cucumber_element = driver.find_element(By.XPATH, "(//div[@class='product'])[1]")
        assert cucumber_element.is_displayed()
