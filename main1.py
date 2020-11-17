from selenium import webdriver
import time
import json

driver = webdriver.Chrome()

url = 'https://www.leagueofgraphs.com/rankings/blue-vs-red/na'
c_dict = []
driver.get(url)

def BlueRed(driver):
    
        table = driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/div[2]/div/div/div/table')
        trs = table.find_elements_by_xpath('.//tr')
        cnt = 1
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
            # thumbnail = tds[0].find_element_by_xpath('.//a/div/div[1]').get_attribute('img')
            
            print('{}, name:{} position:{} Blue: {} Red:{} Thumbnail:{}'.format(cnt, name, position, Blue, Red, thumbnail))      
            # c_dict.append({'name':name, 'position':position, 'Blue':Blue, 'Red':Red})
            cnt += 1
        return c_dict
        
        
def toJson(c_dict):
    with open('BlueRed.json', 'w', encoding='utf-8') as file:
        json.dump(c_dict, file, ensure_ascii=False, indent='\t')    

BlueRed(driver)

toJson(c_dict)


