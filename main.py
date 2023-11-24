import time
import re
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def main():
    result = []
    driver = Driver(uc=True)
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    wait = WebDriverWait(driver, 500, ignored_exceptions)
    try:
        url = "https://moskva.beeline.ru/shop/catalog/telefony/smartfony/"
        driver.get(url=url)
        for page in range(1,32):
            time.sleep(20)
            cards = driver.find_elements(By.CLASS_NAME,"pVjzEa")
            for i in cards:
                price = i.find_element(By.CLASS_NAME,"Dg4IyP").text
                title = i.find_element(By.CLASS_NAME,"RnZwi8").text
                link = i.find_element(By.TAG_NAME,"a").get_attribute("href")
                time.sleep(1)
                result.append({
                    "Цена":price,
                    "Наименование":title,
                    "Ссылка":link
                })
            if driver.current_url =="https://moskva.beeline.ru/shop/catalog/telefony/smartfony/?s&k&i&p&=&7&2&0":
                with open("result.json", "a", encoding="utf-8") as file:
                    json.dump(result, file, indent=4, ensure_ascii=False)
            else:
                button = driver.find_element(By.XPATH, "//div[contains(@class,'MBF_k8')]/button[last()]")
                button.click()


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()