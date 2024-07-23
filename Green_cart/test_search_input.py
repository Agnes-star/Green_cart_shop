import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.search_input
    def test_verifying_search_input_with_correct_product_name(self, driver):
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        search_element = driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']")
        search_element.click()
        search_element.send_keys("cucumber")
        cucumber_element = driver.find_element(By.XPATH, "(//div[@class='product'])[1]")
        assert cucumber_element.is_displayed()

    @pytest.mark.search_input
    def test_verifying_search_input_with_incorrect_product_name(self, driver):
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        search_element = driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']")
        search_element.click()
        search_element.send_keys("abcd")
        error_message = driver.find_element(By.XPATH, "(//h2[normalize-space()='Sorry, no products matched your "
                                                      "search!'])[1]").text

        assert error_message == "Sorry, no products matched your search!"
