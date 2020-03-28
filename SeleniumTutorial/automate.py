from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element_by_id("tab-flight-tab-hp").click()

a =  input("Enter number")


#first text  box
driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")

#second text box
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")

driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("12/10/18")

driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("15/10/18")

driver.find_element_by_xpath('//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click()