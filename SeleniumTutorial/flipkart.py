from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")
numberList = []
n =  int(input("How many number do u want to send message:"))

for i in range(0,n):
	item = (input("Enter number"))
	numberList.append(item)

for i in numberList:
	driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys(i)

	driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()


