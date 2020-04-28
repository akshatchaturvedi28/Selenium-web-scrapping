from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request, urllib.error, urllib.parse

import os

os.chdir("C:/Users/aksha/desktop/webpage")

driver = webdriver.Chrome(executable_path='C:\Windows\System32\drivers\chromedriver.exe')

driver.get("http://cms.nic.in/ncdrcusersWeb/search.do?method=loadSearchPubLndc")


'''
links = driver.find_elements(By.TAG_NAME, "a")

print("Number of links" ,len(links))

for i in links:
    print(i.text)
'''


print('Enter Start Date as DD/MM/YYYY: ')
sDate = input()

print('\nEnter End Date as DD/MM/YYYY: ')
eDate = input()

print('\nEnter State: ')
stateValue = input()

print('\nEnter District: ')
districtValue = input()

startDate = driver.find_element(By.ID, "stDate").clear()
startDate = driver.find_element(By.ID, "stDate").send_keys(sDate)


endDate = driver.find_element(By.ID, "endDate").clear()
endDate = driver.find_element(By.ID, "endDate").send_keys(eDate)


searchByBox = driver.find_element(By.ID, "searchBy")
searchByBox = Select(searchByBox)
searchByBox.select_by_visible_text("Between dates")


stateBox = driver.find_element(By.ID, "stateId")
stateBox = Select(stateBox)
stateBox.select_by_visible_text(stateValue)

driver.implicitly_wait(30)


districtBox = driver.find_element(By.ID, "districtId")
districtBox = Select(districtBox)
districtBox.select_by_visible_text(districtValue)


driver.find_element(By.ID, "searchImg").click()

#first = driver.get('http://cms.nic.in/ncdrcusersWeb/judgement/136281407041416356321231-12+Mo+Akbar+Vs+Reliance+Fresh.htm')

'''
driver.get('driver.find_element(By.XPATH, "//tr[@id='one'][10]/td[1]/a")')
with open('first.htm', 'w') as f:
    f.write(driver.page_source)
driver.close
'''
    
    

#print(driver.find_element(By.XPATH, "//tr[@id='one'][10]/td[1]/a").text)


#Viewing individual page results
pages = driver.find_elements(By.XPATH, "//tr[@id='one']/td[1]/a")
for i in range (0, len(pages)):
    
    p = pages[i].text
    response = urllib.request.urlopen(pages[i].get_attribute("href"))
    webContent = response.read()

    f = open('webpage' + str(i+1) + '.html', 'wb')
    f.write(webContent)
    f.close
    
print('\nAll files of a page are downloaded successfully')

    

    
'''
#Parsing over anchors
anchors = driver.find_elements(By.XPATH, "//td[@class='rhead']/a")
print(len(anchors))
'''


'''
main_window = driver.current_window_handle
actions = ActionChains(driver)
find = driver.find_element(By.XPATH, "//td[@class='rhead'][4]/a")
find.send_keys(Keys.CONTROL + Keys.RETURN)
driver.find_element(By.XPATH, "//td[@class='rhead'][8]/a").send_keys(Keys.CONTROL + Keys.TAB)
'''



'''
main_window = driver.current_window_handle
anchors = driver.find_elements(By.XPATH, "//td[@class='rhead']/a")
for anchor in anchors:
    anchor.send_keys(Keys.CONTROL + 't')
    anchor.click()
    driver.switch_to_window(main_window)
'''

'''    
r = range(10)
for i in r:
    driver.find_element(By.XPATH, "//td[@class='rhead'][i]/a").click()
    
    for j in r:
        driver.find_element(By.XPATH, "//tr[@id='one'][j]/td[1]/a").click()
'''
