from selenium import webdriver
import time
import json

driver = webdriver.Chrome()

url = 'https://www.leagueofgraphs.com/rankings/blue-vs-red/na'
c_list = []
c_dict = {}
driver.get(url)

def BlueRed(driver):
    
        table = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[2]/div/div/div/table')
        trs = table.find_elements_by_xpath('.//tr')
        
        for tr in trs:
            tds = tr.find_elements_by_xpath('.//td')
            if len(tds) == 0 :
                continue
            elif len(tds) == 1:
                continue

            name = tds[0].find_element_by_xpath('.//a/div/div[2]/span').text
            position = tds[0].find_element_by_xpath('.//a/div/div[2]/i').text
            Blue = tds[1].find_element_by_xpath('.//div[1]/progressbar/div/div[2]').text
            Red = tds[1].find_element_by_xpath('.//div[2]/progressbar/div/div[2]').text

            print('name:{} position:{} Blue: {} Red:{}'.format(name, position, Blue, Red))      
            # c_list.append([name, position, Blue, Red])
            c_dict[str(name)] = {'position':position, 'Blue':Blue, 'Red':Red}
        return c_dict
        
        
def toJson(c_dict):
    with open('BlueRed.json', 'w', encoding='utf-8') as file:
        json.dump(c_list, file, ensure_ascii=False, indent='\t')    

BlueRed(driver)

toJson(c_dict)


