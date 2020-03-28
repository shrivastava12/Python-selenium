from selenium import webdriver

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

drp = Select(driver.find_element_by_id("RESULT_RadioButton-9"))

#select by visible text
drp.select_by_visible_text('Morning')

#select by index

drp.select_by_index(2)

#select by value
drp.select_by_value(1)

#capture all the option
all = drp.options

for i in all:
	print(i.text)

#count number of option
drp.options
print(len(drp.options))