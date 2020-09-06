import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProblemPage:
    base_url = 'https://www.hackerrank.com/challenges/'
    driver = webdriver.Chrome(executable_path=r'C:\Selenium\drivers\chromedriver.exe')
    wait = WebDriverWait(driver, 10, 500)

    locator_box_auth = (By.XPATH, "//div[@class='auth-box']")
    locator_btn_cross = (By.XPATH, "//i[contains(@class,'close-icon')]")
    locator_text_all_samples = (By.XPATH, "//strong[starts-with(text(),'Sample Input')]")

    sample_test_data = []

    def __init__(self, addr: str) -> None:
        self.driver.get(self.base_url + addr + '/problem')

    def get_driver(self):
        return self.driver

    def get_sample_data(self):
        self.wait.until(EC.visibility_of_element_located(self.locator_box_auth))
        self.driver.find_element(*self.locator_btn_cross).click()
        ele_text_samples = self.driver.find_elements(*self.locator_text_all_samples)

        for e in ele_text_samples:
            ele_text_input, ele_text_output = e.find_elements_by_xpath("..//following::pre[position()<3]")
            self.sample_test_data.append([ele_text_input.text, ele_text_output.text])

        self.driver.quit()
        return self.sample_test_data
