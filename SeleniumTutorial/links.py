from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME,"a")

print(len(links))

for link in links:
	print(link.text)



#clicking on the link

driver.find_element(By.LINK_TEXT,'REGISTER').click()