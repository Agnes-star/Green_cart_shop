import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.adding_to_cart
    def test_adding_3_vegetables_to_cart(self, driver):
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[1]").click()
        assert driver.find_element(By.XPATH, "//button[contains(text(),'✔ ADDED')]").text == "✔ ADDED"
        driver.find_element(By.XPATH, "(//a[@href='#'][normalize-space()='+'])[2]").click()
        driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[2]").click()
        assert driver.find_element(By.XPATH, "//button[contains(text(),'✔ ADDED')]").text == "✔ ADDED"
        driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='ADD TO CART'])[3]").click()
        assert driver.find_element(By.XPATH, "//button[contains(text(),'✔ ADDED')]").text == "✔ ADDED"

        driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()

        assert driver.find_element(By.XPATH, "(//span[@class='totAmt'])[1]") == 328