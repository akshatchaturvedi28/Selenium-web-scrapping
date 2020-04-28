from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import urllib.request

import requests
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

#sDate = input()
#eDate = input()


startDate = driver.find_element(By.ID, "stDate").clear()
startDate = driver.find_element(By.ID, "stDate").send_keys('01/01/2014')


endDate = driver.find_element(By.ID, "endDate").clear()
endDate = driver.find_element(By.ID, "endDate").send_keys('28/04/2020')


searchByBox = driver.find_element(By.ID, "searchBy")
searchByBox = Select(searchByBox)
searchByBox.select_by_visible_text("Between dates")


stateBox = driver.find_element(By.ID, "stateId")
stateBox = Select(stateBox)
stateBox.select_by_visible_text("Rajasthan")

driver.implicitly_wait(30)


districtBox = driver.find_element(By.ID, "districtId")
districtBox = Select(districtBox)
districtBox.select_by_visible_text("Jaipur-I")


driver.find_element(By.ID, "searchImg").click()

#first = driver.get('http://cms.nic.in/ncdrcusersWeb/judgement/136281407041416356321231-12+Mo+Akbar+Vs+Reliance+Fresh.htm')

'''
driver.get('driver.find_element(By.XPATH, "//tr[@id='one'][10]/td[1]/a")')
with open('first.htm', 'w') as f:
    f.write(driver.page_source)
driver.close
'''
    
    

#print(driver.find_element(By.XPATH, "//tr[@id='one'][10]/td[1]/a").text)

'''
#Viewing individual page results
pages = driver.find_elements(By.XPATH, "//tr[@id='one']/td[1]/a")
for page in pages:
    print(page.click())
'''

    
'''
#Parsing over anchors
anchors = driver.find_elements(By.XPATH, "//td[@class='rhead']/a")
print(len(anchors))
'''


anchors = driver.find_elements(By.XPATH, "//td[@class='rhead']/a")
for anchor in anchors:
    print(len(anchors))


'''    
r = range(10)
for i in r:
    driver.find_element(By.XPATH, "//td[@class='rhead'][i]/a").click()
    
    for j in r:
        driver.find_element(By.XPATH, "//tr[@id='one'][j]/td[1]/a").click()
'''
