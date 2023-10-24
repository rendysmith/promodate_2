from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    url = 'https://www.bethowen.ru/catalogue'

    # Путь к исполняемому файлу Chrome WebDriver (chromedriver)
    driver_path = '/home/andy/Yandex.Disk/Python/WORK/Poker/chromedriver'

    # Specify the path to the chromedriver executable
    service = Service(executable_path=driver_path)

    chrome_options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--start-maximized")


    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # width, height = driver.get_window_size()
    # driver.set_window_size(int(width * 0.33), int(height * 0.33))

    #driver.execute_script("window.resizeTo(width * 0.33, height * 0.33)")

    # Устанавливаем масштаб окна
    #driver.set_window_size(int(width * 0.33), int(height * 0.33))
    #driver.implicitly_wait(10)
    # Открываем страницу Google
    driver.get(url)

    wait = WebDriverWait(driver, 20)  # 10 секунд - максимальное время ожидания

    # Ожидаем, пока элемент по CSS-селектору не станет видимым
    # element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[id='pagetitle']")))
    # print(element)

    while True:
        try:
            title = driver.find_element(By.CSS_SELECTOR, "h1[id='pagetitle']").text
            print(title)
            break
        except:
            print('Error!')
            driver.execute_script("window.stop();")
            time.sleep(3)


    urls = ['https://www.bethowen.ru/catalogue/dogs/korma/syxoi/korm-dlya-sobak-pro-dog-dlya-srednikh-porod-s-chuvstvitelnym-pishchevareniem-yagnenok-sukh-12kg/',
            'https://www.bethowen.ru/catalogue/dogs/korma/syxoi/korm-dlya-sobak-royal-canin-size-x-small-adult-dlya-miniatyurnykh-porod-ot-do-8-let/',
            'https://www.bethowen.ru/catalogue/dogs/korma/syxoi/korm-dlya-shchenkov-pro-dog-dlya-zdorovogo-rosta-i-energii-indeyka-sukh/?oid=516750']

    for url in urls:
        print('======================================================')
        print(url)
        driver.get(url)
        #city = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[class='getPopRegional']")))
        while True:
            wait = WebDriverWait(driver, 10)
            city_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='getPopRegional']"))).text
            print(f'city_text, >>>{city_text}<<<')
            if '' != city_text:
                break
            driver.refresh()
            time.sleep(5)

        # city_text = driver.find_element(By.CSS_SELECTOR, "span[class='getPopRegional']").text
        # print('city_text', city_text)

        name_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1[class='preview_text']"))).text
        print('name_text', name_text)

        # name_text = driver.find_element(By.CSS_SELECTOR, "h1[class='preview_text']").text
        # print('name_text', name_text)
        code_text = driver.find_element(By.CSS_SELECTOR, "div[class='tw-mr-4']").text
        print('code_text', code_text)

        packs = driver.find_elements(By.CSS_SELECTOR, "li[data-class='offer-tabs-choose']")

        for pack in packs:
            if "active" in pack.get_attribute("class"):
                resize = pack.text
                print('resize', resize)
                break

        time.sleep(5)

    # Закрываем браузер
    driver.quit()

if __name__ == "__main__":
    main()