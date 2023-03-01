import streamlit as st
import time

import threading
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

URL = "https://www.unibet.fr/sport/football/europa-league/europa-league-matchs"
XPATH = "//*[@class='ui-mainview-block eventpath-wrapper']"
TIMEOUT = 20

st.title("Test Selenium")
st.markdown(
    "You should see some random Football match text below in about 21 seconds")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)
driver.get(URL)

try:
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((By.XPATH, XPATH,))
    )

except TimeoutException:
    st.warning("Timed out waiting for page to load")
    driver.quit()

time.sleep(10)
elements = driver.find_elements(By.XPATH, XPATH)
st.write([el.text for el in elements])
driver.quit()


def calc_num():
    i = 0
    while True:
        time.sleep(2)
        print('CALC_NUM', i)
        i += 1


def power_num():
    i = 1
    while True:
        time.sleep(5)
        print('POWER_NUM', i)
        i = i * 1.2


if __name__ == '__main__':
    print("__main__")

    is_calc_thread, is_power_thread = False, False
    print("Current Thread!")
    running_threads = enumerate(list(threading.enumerate()))

    for i, thread in running_threads:
        if "calc_num" in thread.name:
            print("Already interval exists")
            is_calc_thread = True
        print("Thread {}: {}".format(i, thread.name))

    print("Started Main")

    if not is_calc_thread:
        thread = threading.Thread(target=calc_num, name="calc_num")
        thread.start()

    if not is_power_thread:
        thread = threading.Thread(target=power_num)
        thread.start()

    print("Next Thread List")
    running_threads = enumerate(list(threading.enumerate()))
    for i, thread in running_threads:
        print("Thread {}: {}".format(i, thread.name))
