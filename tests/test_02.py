from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    text = message.text

    driver.quit()

def test_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    driver.implicitly_wait(0.5)

    check_button = driver.find_element(by=By.ID, value="my-check-2")
    check_button.click()
    driver.save_screenshot("screenshot.png")

    driver.quit()

