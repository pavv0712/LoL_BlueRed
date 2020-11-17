from selenium import webdriver
import time
import json

driver = webdriver.Chrome()

url = 'https://kr.leagueoflegends.com/ko-kr/champions/'
driver.get(url)
slayer = []
fighter = []
mage = []
marksman = []
controller = []
tank = []

def SlayerChamp(driver):
    driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[1]/nav/div/div[2]/div[2]/ul/li[2]/button').click()
    time.sleep(3)
    div = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[2]/div[2]')
    aa = div.find_elements_by_xpath('.//a')

    for a in aa:
        name = a.get_attribute('href').split('/')[-2].capitalize()
        slayer.append(name)
        print('{}'.format(name))
    return slayer

def FighterChamp(driver):
    driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[1]/nav/div/div[2]/div[2]/ul/li[3]/button').click()
    time.sleep(3)
    div = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[2]/div[2]')
    aa = div.find_elements_by_xpath('.//a')

    for a in aa:
        name = a.get_attribute('href').split('/')[-2]
        fighter.append(name)
        print('{}'.format(name))
    return fighter

def MageChamp(driver):
    driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[1]/nav/div/div[2]/div[2]/ul/li[4]/button').click()
    time.sleep(3)
    div = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[2]/div[2]')
    aa = div.find_elements_by_xpath('.//a')

    for a in aa:
        name = a.get_attribute('href').split('/')[-2]
        mage.append(name)
        print('{}'.format(name))
    return mage

def MarksmanChamp(driver):
    driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[1]/nav/div/div[2]/div[2]/ul/li[5]/button').click()
    time.sleep(3)
    div = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[2]/div[2]')
    aa = div.find_elements_by_xpath('.//a')

    for a in aa:
        name = a.get_attribute('href').split('/')[-2]
        marksman.append(name)
        print('{}'.format(name))
    return marksman

def ControllerChamp(driver):
    driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[1]/nav/div/div[2]/div[2]/ul/li[6]/button').click()
    time.sleep(3)
    div = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[2]/div[2]')
    aa = div.find_elements_by_xpath('.//a')

    for a in aa:
        name = a.get_attribute('href').split('/')[-2]
        controller.append(name)
        print('{}'.format(name))
    return controller

def TankChamp(driver):
    driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[1]/nav/div/div[2]/div[2]/ul/li[7]/button').click()
    time.sleep(3)
    div = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[2]/section/div[2]/section[2]/div[2]')
    aa = div.find_elements_by_xpath('.//a')

    for a in aa:
        name = a.get_attribute('href').split('/')[-2]
        tank.append(name)
        print('{}'.format(name))
    return tank


def stoJson(slayer):
    with open('slayer.json', 'w', encoding='utf-8') as file:
        json.dump(slayer, file, ensure_ascii=False, indent='\t')

def ftoJson(fighter):
    with open('fighter.json', 'w', encoding='utf-8') as file:
        json.dump(fighter, file, ensure_ascii=False, indent='\t')

def mtoJson(mage):
    with open('mage.json', 'w', encoding='utf-8') as file:
        json.dump(mage, file, ensure_ascii=False, indent='\t')

def matoJson(marksman):
    with open('marksman.json', 'w', encoding='utf-8') as file:
        json.dump(marksman, file, ensure_ascii=False, indent='\t')

def ctoJson(controller):
    with open('controller.json', 'w', encoding='utf-8') as file:
        json.dump(controller, file, ensure_ascii=False, indent='\t')

def ttoJson(tank):
    with open('tank.json', 'w', encoding='utf-8') as file:
        json.dump(tank, file, ensure_ascii=False, indent='\t')   


SlayerChamp(driver)
stoJson(slayer) 

# FighterChamp(driver)
# ftoJson(fighter)

# MageChamp(driver)
# mtoJson(mage)

# MarksmanChamp(driver)
# matoJson(marksman)

# ControllerChamp(driver)
# ctoJson(controller)

# TankChamp(driver)
# ttoJson(tank)