from selenium import webdriver

driver =  webdriver.Chrome()
# working with the radio button

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")


driver.find_element_by_id("RESULT_RadioButton-7_1").click()

status =  driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()
print(status)
