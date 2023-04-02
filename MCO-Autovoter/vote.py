from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def vote_on_planetminecraft(url):
    driver = webdriver.Chrome(executable_path='D:\Code\MCO-Autovoter\ChromeDriver')
    driver.get(url)

    mcname_input = driver.find_element_by_name('mcname')
    mcname_input.click()
    mcname_input.send_keys('Nii')

    submit_button = driver.find_element_by_xpath('//input[@data-r3var="vote"]')
    submit_button.click()

    time.sleep(3)
    driver.quit()

def vote_on_minecraft_server_list(url):
    driver = webdriver.Chrome(executable_path='D:\Code\MCO-Autovoter\ChromeDriver')
    driver.get(url)

    ignn_input = driver.find_element_by_name('ignn')
    ignn_input.click()
    ignn_input.send_keys('Nii')

    vote_button = driver.find_element_by_xpath('//input[@value="Click to Vote"]')
    vote_button.click()

    time.sleep(3)
    driver.quit()

websites = {
    "planetminecraft": "https://www.planetminecraft.com/server/minecraft-online-3375846/vote/",
    "minecraft_server_list": "https://minecraft-server-list.com/server/267113/vote/"
}

vote_on_planetminecraft(websites["planetminecraft"])
vote_on_minecraft_server_list(websites["minecraft_server_list"])
