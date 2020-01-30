import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


try:
        os.makedirs('./otter_download')
except FileExistsError:
        pass

def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)


options = Options()
options.add_argument("--headless")
options.add_argument("--enable-automation")
options.add_argument('--disable-extensions-file-access-check')
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--verbose')
options.add_experimental_option("prefs", {
        "download.default_directory": r"C:\Users\milic\Downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False,
        "profile.default_content_setting_values.notifications" : 2
})
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')


delay = 20  #seconds before timout



def otter_auto(file, chromept = r'C:\Users\milic\.bin\chromedriver.exe', email = 'alan.rutledge.firefly@gmail.com', password = '2JOPOreGOzp29', delay = 20):
        # initialize driver object and add the path_to_chrome_driver
        driver = webdriver.Chrome(options=options,
                                  executable_path=chromept)

        dow_dir = os.getcwd() + '\otter_download'
        enable_download_headless(driver, f'{dow_dir}')

        driver.implicitly_wait(delay)

        driver.get('https://otter.ai/login')
        time.sleep(2)

        element = driver.find_element_by_xpath('//*[@id="__next"]/div/nav/div/div[2]/button[1]')
        element.click()
        time.sleep(2)


        element = driver.find_element_by_xpath('//*[@id="__next"]/aside/div[1]/div/form/label[1]/div[1]/input')
        element.send_keys(email)

        # Doing the same for the password
        element = driver.find_element_by_xpath('//*[@id="__next"]/aside/div[1]/div/form/label[2]/div[1]/input')
        element.send_keys(password)

        # Then click the submit button
        element = driver.find_element_by_xpath('//*[@id="__next"]/aside/div[1]/div/form/button[3]')
        element.click()
        time.sleep(2)

        # Wait until button is clicakble
        element = WebDriverWait(driver, delay).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-dashboard/div[5]/div[1]/app-contextual-home/div/div/div[2]/div/div[1]/div/button/span')))
        element.click()
        time.sleep(2)


        #browse file
        element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/app-upload-audio-overlay/div/div[3]/div[1]/input')
        element.send_keys(file)
        time.sleep(2)


        #wait until upload is completed!
        WebDriverWait(driver, 300).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/app-upload-audio-overlay/div/div[2]/table/tbody/tr/td[4]/div/span')))
        time.sleep(2)

        #go to download page
        driver.get('https://otter.ai/my-notes')
        time.sleep(2)

        #wait until processing is done
       # element = driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div[5]/div[1]/app-my-conversation/div/div/div[2]/a/app-conversation-list-item/div/div[2]/div[3]/div[2]')
        #element.click()
        WebDriverWait(driver, 300).until(
                EC.invisibility_of_element_located((By.XPATH,
                                                  '/html/body/app-root/app-dashboard/div[5]/div[1]/app-my-conversation/div/div/div[2]/a[1]/app-conversation-list-item/div/div[2]/div[3]/div[2]/span')))
        time.sleep(2)
        #select file to download
        element = driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div[5]/div[1]/app-my-conversation/div/div/div[2]/a/app-conversation-list-item/div/div[2]/div[2]')
        #element = driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div[5]/div[1]/app-my-conversation/div/div/div[2]/a[1]/app-conversation-list-item/div/div[2]/div[2]/span')
        element.click()
        time.sleep(2)

        #click more options
        element = driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div[3]/app-head-bar/div/div[3]/div[6]/button')
        element.click()
        time.sleep(2)


        #click export text
        element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/button[2]')
        element.click()
        time.sleep(2)

        #click export as monologue
        element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/app-export-transcript-overlay/div/div[2]/div[6]/div/mat-slide-toggle/label/div/div/div[1]')
        element.click()
        time.sleep(2)

        #click continue
        element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/app-export-transcript-overlay/div/div[1]/button[2]')
        element.click()
        time.sleep(2)

        # go to download page
        driver.get('https://otter.ai/my-notes')
        time.sleep(2)

        #delete file from otter
        element = driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div[5]/div[1]/app-my-conversation/div/div/div[2]/a/app-conversation-list-item/div/div[3]')
        element.click()
        element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[2]')
        element.click()
        element = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/app-confirm-overlay/div/div[3]/button[2]')
        element.click()

        time.sleep(2)

        driver.quit()


if __name__ == "__main__":
        otter_auto()

